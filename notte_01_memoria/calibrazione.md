# Calibrazione fonti, notte 01 (v2, 2026-10-19)

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

## Distribuzione dei Tier (registro v2, calcolata con `csv.DictReader`)
- 61 righe: T1 29 · T2 19 · T3 13.
- Esiti: ok 40, ok parziale 3, snippet 6, 403 5, bloccato dallo strumento 3, redirect 2, 404 1, vuoto 1.
- Metodo: fetch 55, snippet 6.
Comando: `python3 -I -c "import csv,collections; r=list(csv.DictReader(open('notte_01_memoria/registro_fonti.csv'))); print(collections.Counter(x['tier'] for x in r))"`

## Soglie
- **Reddit (100 voti e 30 commenti):** inapplicabile, perché il sito è bloccato dallo strumento e i mirror non mostrano i voti in modo affidabile. Lasciala invariata; tutto Reddit resta T3 finché non c'è accesso diretto.
- **GitHub (≥ 1.000 stelle e ultimo commit leggibile entro 6 mesi):** applicabile solo con `commits/main`. Per modelcontextprotocol/servers la data è leggibile (2026-10-19). Per mem0 e basic-memory si legge solo una release senza anno ("25 Sep", "25 Aug"): li ho tenuti in T2 con `nota_tier` "anno dedotto". Proposta: considerare "data senza anno" sufficiente solo se è anche la release marcata "Latest".
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
- Questa run (v2): 33 letture di pagina (WebFetch, offset inclusi), 4 ricerche web, 0 sottoagenti. Durata misurata con `TZ=Europe/Rome date`: 11:10-11:20.
- Il consumo in dollari non è visibile all'agente: confrontare il saldo prima e dopo (saldo prima di questa run: 54 USD).

## Modifiche proposte al prompt
1. Il prompt v1 nomina `precedenti/` ma la cartella era assente; ora è sul branch `claude/correzione-notte-01`. Indicare il branch sorgente.
2. Il prompt v1 consente fino a 5 sottoagenti, il prompt di correzione ne vieta l'uso. Allineare le due versioni (0 sottoagenti è la scelta più economica).
3. Ammettere esplicitamente l'esito "snippet" per le fonti 403, con declassamento automatico a [Inferenza].
4. Per GitHub indicare la pagina `commits/main/<path>` come fonte della data dell'ultimo commit.
