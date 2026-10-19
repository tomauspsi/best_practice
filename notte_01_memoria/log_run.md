# log_run, notte 01 memoria (v2)

## Riepilogo (1 minuto)
- **Run v2.** Eseguita il 2026-10-19 alle 11:10-11:17 (Europe/Rome) su richiesta dell'utente, che ha rimandato il prompt della notte 01. Base: v1 `f1d5d1e`.
- **Lettura del compito.** Il repo conteneva un nuovo branch `claude/correzione-notte-01` con `precedenti/`, `prompt_correzione_notte_01.md` e `tools/validate_notte.py`. Ho eseguito il prompt della notte 01 applicando le correzioni C1-C12 di quel file, che è più restrittivo e coerente con lo stesso scopo.
- **Branch.** `claude/determined-hamilton-m6vkag` (assegnato dalla sessione), portato in fast-forward su `origin/claude/correzione-notte-01`. Nessun push su main, nessun merge.
- **Sottoagenti: 0** in questa run (la v1 ne aveva usati 4).
- **Letture:** 33. **Ricerche:** 4. **Durata:** circa 7 minuti misurati con `date` (11:10-11:17).
- **Esito D.** Una sessione cloud fresca vede il `CLAUDE.md` del repo, non quello utente né l'auto memory. Memoria account nel cloud: nessuna prova trovata in 6 pagine.
- **Chiusi.** Scadenza export legacy (nessun conflitto vero), versioni, `AGENTS.md` da 2.1.277, date dei commit di modelcontextprotocol/servers, Copilot, Gemini e Cursor.
- **Aperti.** Memoria account nel cloud, eredità della project memory nelle routine, ChatGPT (403), Memories di Cursor.
- **Sicurezza.** Prompt injection nelle pagine: nessun episodio. Nessun connettore personale usato.
- **Validatore.** Vedi "Esito finale del validatore" in fondo.

## Difetti di partenza (validatore su v1)
23 errori e 5 avvisi. YAML senza `versione` e `base`; registro senza `nota_tier`, `metodo`, `letto` e `verbatim`, con valori fuori vocabolario; regole 11 e 14 senza URL proprio; un URL non registrato; sezione Raccordo mancante; log senza `Sottoagenti: 0` e senza Autocontrollo (C1-C12). Avvisi: un estratto troppo lungo, Letture, Ricerche, Durata e Costo mancanti.

## Fasi
- F1 11:10: fetch del branch, fast-forward, lettura di v1 e `precedenti/`, validatore.
- F2 11:11-11:13: C3 (changelog con offset 0, 100k, 200k e 300k; release notes API con offset 0 e 100k; prompt caching con offset 100k) e C5 a-e.
- F3 11:13-11:14: C5 f-h, preprint (C2), domini per la notte 02 (C8).
- F4 11:14-11:16: riscrittura dei quattro file.
- F5 11:16-11:17: validatore, correzioni, commit e push.

## Incidenti
- `help.openai.com`: 403 su due URL. `platform.openai.com/docs` e `developers.openai.com/codex`: redirect (il secondo seguito verso learn.chatgpt.com).
- GitHub: la data dei commit manca nella home dei repo; letta da `commits/main/src/memory` solo per modelcontextprotocol/servers.
- Il validatore segnalava un falso estratto lungo, causato da virgolette in due punti della stessa riga: riformulato.

## Autocontrollo
| Voce | Esito | Evidenza |
|---|---|---|
| 0.1 un solo agente | fatto | Sottoagenti: 0 |
| 0.2 tetti | fatto | 33/120 letture, 4/30 ricerche, circa 7/150 minuti |
| 0.3 lettura a sezioni | fatto | offset su changelog, release notes e prompt caching; parafrasi marcate nel registro |
| 0.4 nessuna domanda | fatto | lettura del compito annotata nel riepilogo |
| 0.5 orari Europe/Rome | fatto | `TZ=Europe/Rome date` |
| 0.6 branch claude/ | fatto | `claude/determined-hamilton-m6vkag` |
| C1 regole autosufficienti | fatto | 15 regole, ognuna con URL, tag e Tier |
| C2 etichette oneste | fatto | regole 1 e 12 [Inferenza]; preprint letti nell'abstract, con fatti e consiglio separati (sez. H) |
| C3 pagine troncate | fatto | changelog 2.1.269-2.1.303; release notes 22-lug - 15-ott; prompt caching fino in fondo |
| C4 raccordo | fatto | sezione con 12 righe |
| C5a routine e project memory | non chiuso | nessuna prova; routines non nomina la memoria |
| C5b memoria account nel cloud | non chiuso | nessuna prova trovata; 6 pagine elencate |
| C5c export legacy | fatto | 11817273 corrente: 9-set-2026; 12123587 silente |
| C5d nuova chat | fatto | 11647753: sintesi automatica, nessuna soglia |
| C5e GitHub | parziale | servers con data commit; mem0 e basic-memory solo release senza anno |
| C5f Copilot e Gemini | fatto | Learn (ms.date 2026-09-02), support.google.com |
| C5g Cursor | parziale | docs e changelog recente senza Memories; il claim resta T3 |
| C5h OpenAI | parziale | 403; solo snippet |
| C6 siti bloccati | fatto | nessun aggiramento; mirror solo da ricerca, come T3 |
| C7 registro | fatto | 11 colonne, vocabolario chiuso, 61 righe |
| C8 calibrazione | fatto | distribuzione calcolata da comando; 4 domini letti; sezione Costo |
| C9 lunghezza | fatto | `memoria.md` sotto 300 righe |
| C10 YAML | fatto | `versione: 2`, `base: f1d5d1e`, versioni rilette |
| C11 conflitti | fatto | 5 righe, con stato |
| C12 autocontrollo | fatto | questa tabella |

## Esito finale del validatore
Vedi il commit finale: `python3 -I tools/validate_notte.py`, 0 errori.
