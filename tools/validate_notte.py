#!/usr/bin/env python3
"""Validatore della consegna "notte 01 - memoria".

Uso (dalla radice del repo):  python3 -I tools/validate_notte.py [cartella]
Esce con codice 1 se ci sono ERRORI. Gli AVVISI non bloccano ma vanno spiegati in log_run.md.
"""
import csv
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "ricerche")
errors, warns = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def norm(url):
    url = url.strip().rstrip(".,;:)>\"'")
    url = url.split("#")[0]
    return url.rstrip("/").lower()


def finish():
    for w in warns:
        print("AVVISO:", w)
    for e in errors:
        print("ERRORE:", e)
    print(f"\nRiepilogo: {len(errors)} errori, {len(warns)} avvisi")
    sys.exit(1 if errors else 0)


names = ("memoria.md", "registro_fonti.csv", "calibrazione.md", "log_run.md")
paths = {n: root / n for n in names}
for n, p in paths.items():
    if not p.is_file():
        err(f"manca il file {p}")
if errors:
    finish()

# ---------------------------------------------------------------- memoria.md
text = paths["memoria.md"].read_text(encoding="utf-8")
lines = text.splitlines()
if len(lines) > 300:
    err(f"memoria.md ha {len(lines)} righe (massimo 300)")

fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not fm:
    err("memoria.md: intestazione YAML mancante")
else:
    keys = set(re.findall(r"^([A-Za-z_]+):", fm.group(1), re.M))
    for k in ("tema", "verificato_il", "rivalutare_se", "versioni_rilevate", "versione", "base"):
        if k not in keys:
            err(f"memoria.md: chiave YAML mancante: {k}")

# regole operative
rules, in_rules = [], False
for ln in lines:
    if ln.startswith("## "):
        in_rules = "REGOLE OPERATIVE" in ln.upper()
        continue
    if in_rules and re.match(r"^\d+\.\s", ln):
        rules.append(ln)
if not rules:
    err("memoria.md: sezione REGOLE OPERATIVE PER AGENTI vuota o assente")
if len(rules) > 15:
    err(f"memoria.md: {len(rules)} regole operative (massimo 15)")

TAGS = r"\[(Verificato|Inferenza|Obsoleto/Conflitto|Segnale T3)\]"
URL_RE = r"https?://[^\s<>\]\"]+"

# ---------------------------------------------------------------- registro
registry = {}
with paths["registro_fonti.csv"].open(encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    cols = reader.fieldnames or []
    need = ["url", "dominio", "tier", "nota_tier", "data_fonte", "esito", "metodo",
            "letto", "verbatim", "alternativa_usata", "note"]
    missing = [c for c in need if c not in cols]
    if missing:
        err("registro_fonti.csv: colonne mancanti: " + ", ".join(missing))
    OK_ESITO = {"ok", "ok parziale", "snippet", "403", "404", "robots", "bloccato dallo strumento",
                "paywall", "timeout", "solo-js", "redirect", "vuoto"}
    vocab = {
        "tier": {"1", "2", "3"},
        "esito": OK_ESITO,
        "metodo": {"fetch", "snippet"},
        "letto": {"intero", "parziale", "no"},
        "verbatim": {"si", "parafrasi", "na"},
    }
    bad = {k: [] for k in vocab}  # colonna -> [(riga, valore)]
    dup = []
    for i, row in enumerate(reader, start=2):
        u = norm(row.get("url", "") or "")
        if not u:
            err(f"registro riga {i}: url vuoto")
            continue
        if u in registry:
            dup.append(i)
        registry[u] = row
        for col, allowed in vocab.items():
            if col in cols and row.get(col) not in allowed:
                bad[col].append((i, row.get(col)))
    for col, items in bad.items():
        if items:
            esempi = ", ".join(f"riga {i}: '{v}'" for i, v in items[:3])
            err(f"registro, colonna {col}: {len(items)} righe fuori vocabolario ({esempi})")
    if dup:
        warn(f"registro: {len(dup)} url duplicati (righe {dup[:5]})")

# regole: tag, tier, url propri, e [Verificato] solo con lettura reale
for n, r in enumerate(rules, start=1):
    tag = re.search(TAGS, r)
    if not tag:
        err(f"regola {n}: tag mancante")
    if not re.search(r"\bT[123]\b", r):
        err(f"regola {n}: Tier (T1/T2/T3) mancante")
    urls = re.findall(URL_RE, r)
    if not urls:
        err(f"regola {n}: nessun URL proprio (vietato 'stesso URL della regola X')")
    if tag and tag.group(1) == "Verificato" and "metodo" in (cols or []):
        for u in urls:
            row = registry.get(norm(u))
            if row is None:
                err(f"regola {n}: [Verificato] ma {u} non e' nel registro")
            elif not (str(row.get("esito", "")).startswith("ok") and row.get("metodo") == "fetch"):
                err(f"regola {n}: [Verificato] ma {u} non e' stato letto con fetch (esito={row.get('esito')}, metodo={row.get('metodo')})")

# ogni URL citato in memoria.md deve stare nel registro
cited = {norm(u) for u in re.findall(URL_RE, text)}
absent = sorted(u for u in cited if u not in registry)
if absent:
    err(f"{len(absent)} URL di memoria.md non sono nel registro, ad esempio: " + "; ".join(absent[:5]))

# estratti lunghi (euristica)
for m in re.finditer(r'"([^"\n]{20,600})"', text):
    if len(m.group(1).split()) > 15:
        warn("estratto tra virgolette oltre 15 parole: " + m.group(1)[:60] + "...")

# dati personali
if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text) or re.search(
        r"(?i)tommaso|manari|busana|matilde di canossa|albo a\b", text):
    err("memoria.md: possibile dato personale (email, nome, indirizzo)")

# sezioni obbligatorie
for h in ("Risposta breve", "REGOLE OPERATIVE", "Raccordo con i report", "Tabella conflitti",
          "Cosa non è stato verificato", "Fonti per Tier"):
    if not re.search(r"^## .*" + re.escape(h), text, re.M | re.I):
        err(f"memoria.md: sezione mancante: {h}")

# ---------------------------------------------------------------- log e calibrazione
log = paths["log_run.md"].read_text(encoding="utf-8")
if not re.search(r"(?i)sottoagenti\s*:\s*0\b", log):
    err("log_run.md: manca la riga 'Sottoagenti: 0'")
for k in ("Letture", "Ricerche", "Durata"):
    if not re.search(rf"(?i){k}\s*:\s*\S+", log):
        warn(f"log_run.md: manca '{k}: ...'")
if not re.search(r"(?im)^#+\s*Autocontrollo", log):
    err("log_run.md: manca la sezione Autocontrollo")
for c in [f"C{i}" for i in range(1, 13)]:
    if not re.search(rf"\b{c}\b", log):
        err(f"log_run.md: Autocontrollo senza la voce {c}")
cal = paths["calibrazione.md"].read_text(encoding="utf-8")
if not re.search(r"(?i)notte 02", cal):
    warn("calibrazione.md: manca l'elenco per la notte 02")
if not re.search(r"(?i)costo", cal):
    warn("calibrazione.md: manca la sezione Costo")

# ---------------------------------------------------------------- git
try:
    br = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                        capture_output=True, text=True, check=True).stdout.strip()
    if br in ("main", "master"):
        err(f"sei sul branch {br}: lavora su un branch claude/...")
    elif not br.startswith("claude/"):
        warn(f"il branch '{br}' non ha il prefisso claude/")
except Exception:
    warn("impossibile leggere il branch git")

finish()
