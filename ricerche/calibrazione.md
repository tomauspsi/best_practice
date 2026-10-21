# Calibrazione fonti, notte 01 (v3, 2026-10-19)

## Cosa ha funzionato
- **Tier 1 Anthropic** (code.claude.com, platform.claude.com, support.claude.com, github.com/anthropics): tutto leggibile. Le pagine docs non hanno date; le date affidabili stanno nei changelog e nelle release notes.
- **Pagine lunghe.** Si leggono a blocchi di 100.000 caratteri con `offset`. Il changelog di Claude Code (1.113.891 caratteri) contiene le versioni da 2.1.269 a 2.1.303 nei primi 400.000.
- **Tier 1 di altri vendor.** learn.microsoft.com (con `ms.date` nei metadati), support.google.com e arxiv.org/abs: leggibili.
- **Docs di altri vendor:** cursor.com/docs, docs.github.com, learn.chatgpt.com (Codex, dopo un redirect 308 da developers.openai.com) e agents.md: leggibili.
- **GitHub HTML:** stelle leggibili. La data dell'ultimo commit si legge dalla pagina `commits/main/<path>`; la pagina `releases` mostra giorno e mese senza anno per l'anno corrente.

## Cosa è stato bloccato
| Dominio | Esito | Trattamento |
|---|---|---|
| reddit.com, old.reddit.com | bloccato dallo strumento | non aggirato; mirror reddit.sentinel-team.org solo da ricerca normale, come T3 |
| stackoverflow.com | bloccato dallo strumento | non aggirato |
| help.openai.com (entrambi gli URL), openai.com | 403 | snippet di WebSearch, usati come [Inferenza] |
| medium.com | 403 | non usato |
| api.github.com | 403 | pagina HTML di GitHub |
| platform.openai.com/docs | redirect 301 verso developers.openai.com | non seguito (non tratta ChatGPT) |
| discord.com | vuoto | confermato non indicizzabile |
| help.openai.com/.../8590148-memory-faq, openai.com/index/memory-and-new-controls-for-chatgpt | 403 anche nella v3 | snippet di WebSearch, [Inferenza]; non aggirato |

## Distribuzione dei Tier (registro v3, calcolata con `csv.DictReader`)
- 78 righe: T1 38 · T2 26 · T3 14.
- Esiti: ok 54, ok parziale 4, snippet 7, 403 6, bloccato dallo strumento 3, redirect 2, 404 1, vuoto 1.
- Metodo: fetch 71, snippet 7.
Comando: `python3 -I -c "import csv,collections; r=list(csv.DictReader(open('ricerche/registro_fonti.csv'))); print(collections.Counter(x['tier'] for x in r))"`

## Nuove osservazioni della v3
- **PDF di arXiv.** WebFetch restituisce i byte del PDF, non il testo; il file viene salvato in locale. Si converte con `pdftotext -layout` (presente nell'ambiente) in una cartella a parte e si legge il testo: così i preprint sono letti per intero. L'abstract da solo (v2) aveva portato a un errore: MemoryGraft propone difese.
- **WebFetch su pagine molto lunghe.** Oltre ~50 KB la risposta è salvata su file: usare `grep` sul file invece di rileggere.
- **Cursor.** Il changelog è paginato (`/changelog/page/N`, cinque voci a pagina); la rimozione delle Memories è nelle release 2.1.x del nov-2025, oltre le prime tre pagine. La pagina `/changelog/2-1` esiste e non cita le Memories.
- **GitHub `commits/main`.** Mostra la data con anno (es. "Oct 14, 2026"): è la fonte per la soglia dei 6 mesi, meglio della pagina `releases`.
- **Prova sul contesto.** Una sessione cloud avviata da routine mostra nel contesto: `CLAUDE.md` del repo, e-mail dell'account, skill e connettori dell'account; non mostra blocchi di memoria né istruzioni del profilo.

## Soglie
- **Reddit (100 voti e 30 commenti):** inapplicabile, perché il sito è bloccato dallo strumento e i mirror non mostrano i voti in modo affidabile. Lasciala invariata; tutto Reddit resta T3 finché non c'è accesso diretto.
- **GitHub (≥ 1.000 stelle e ultimo commit leggibile entro 6 mesi):** applicabile solo con `commits/main`. Per modelcontextprotocol/servers la data è leggibile (2026-10-19). Per mem0 (2026-10-14) e basic-memory (2026-10-18) la v3 ha letto `commits/main` con l'anno: soglia rispettata, T2 senza riserve.
- **Issue chiuse su github.com/anthropics:** T1 come esistenza del bug, non come prova del fix.

## Domini per la notte 02 (istruzioni di comportamento, AGENTS.md), una lettura ciascuno
| Dominio | Esito | Cosa offre |
|---|---|---|
| [agents.md](https://agents.md/) | ok | standard; "The closest AGENTS.md to the edited file wins" |
| [docs.github.com](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) | ok | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `AGENTS.md` |
| [cursor.com/docs](https://cursor.com/docs/context/rules) | ok | `.cursor/rules`, `AGENTS.md` in root e sottocartelle |
| [learn.chatgpt.com](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | ok (dopo un redirect 308) | Codex: `AGENTS.override.md`, limite di 32 KiB |
Da aggiungere: code.claude.com/docs (memory, sub-agents, hooks, skills, best-practices), platform.claude.com prompting best practices, github.com/anthropics/skills.

## Costo
- Questa run (v3): 27 letture di pagina (WebFetch, offset inclusi; 2 risposte 403), 4 ricerche web, 0 sottoagenti. Durata misurata con `TZ=Europe/Rome date`: 12:55-13:05 circa.
- Agenti: nessuno. Le nove domande si sono risolte leggendo e triangolando poche fonti ufficiali, il caso in cui CLAUDE.md consiglia un solo agente; i tre sottoagenti consentiti avrebbero restituito parafrasi da ricontrollare (come in v1) e moltiplicato i token.
- Il consumo in dollari non è visibile all'agente: l'utente confronta il saldo prima e dopo (saldo prima di questa run: da indicare dall'utente; dopo la v2: 52 USD).

## Modifiche proposte al prompt
1. Il prompt v1 nomina `precedenti/` ma la cartella era assente; ora è sul branch `claude/correzione-notte-01`. Indicare il branch sorgente.
2. Il prompt v1 consente fino a 5 sottoagenti, il prompt di correzione ne vieta l'uso. Allineare le due versioni (0 sottoagenti è la scelta più economica).
3. Ammettere esplicitamente l'esito "snippet" per le fonti 403, con declassamento automatico a [Inferenza].
4. Per GitHub indicare la pagina `commits/main/<path>` come fonte della data dell'ultimo commit.
