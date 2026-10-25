# Calibrazione fonti, notte 02 (comportamento, v1, 2026-10-25)

## Cosa ha funzionato
- **Tier 1 Anthropic** (code.claude.com, platform.claude.com, anthropic.com, claude.com blog): leggibili. Le pagine docs non hanno date; il blog ha la data in pagina (2026-06-18), il post di engineering 2025-09-29.
- **Pagine lunghe.** `memory`, `hooks-guide` e `migration guide` vengono salvate su file oltre ~50 KB: si leggono con `grep`. `skills`, `sub-agents` e `changelog` arrivano a blocchi di 100.000 caratteri.
- **Altri vendor.** agents.md, docs.github.com, cursor.com/docs, learn.chatgpt.com, github.com/google-gemini (pagina `blob/main/docs/...`) e code.visualstudio.com: leggibili.
- **arXiv.** `abs` e `pdf` rispondono con un riassunto dello strumento; il testo del PDF non è stato convertito con `pdftotext` in questa notte, quindi i risultati dei preprint sono [Verificato] sul riassunto, non sul testo intero.
- **Fonte di sicurezza.** Un blog di fornitore (Pillar) è l'unica descrizione letta del Rules File Backdoor: resta [Segnale T3].

## Cosa è stato bloccato
| Dominio | Esito | Trattamento |
|---|---|---|
| support.claude.com (due articoli sui Project) | bloccato dallo strumento (PROVENANCE_REQUIRED: permesso non risposto in tempo) | non aggirato; riprovare con gli URL nel prompt |
| claude.com/blog/using-claude-projects | 404 (indirizzo ipotizzato) | scartato |
| Reddit, Stack Overflow, help.openai.com | non interrogati | non tema di questa notte |

## Distribuzione dei Tier (registro, calcolata con un comando)
- 29 righe: T1 24 · T2 4 · T3 1.
- Esiti: ok 23, ok parziale 3, bloccato dallo strumento 2, 404 1.
- Metodo: fetch 29, snippet 0.
Comando: `python3 -I -c "import csv,collections; r=list(csv.DictReader(open('ricerche/registro_fonti_comportamento.csv'))); print(collections.Counter(x['tier'] for x in r), collections.Counter(x['esito'] for x in r))"`

## Domini per la notte 03 (istruzioni di un Project), una lettura ciascuno
| Dominio | Esito di raggiungibilità |
|---|---|
| [code.claude.com/docs/en/claude-projects](https://code.claude.com/docs/en/claude-projects) | ok (beta Pro e Max, 59 KB) |
| [support.claude.com 9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) | bloccato oggi (permesso); letto il 19 ottobre |
| [support.claude.com 10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) | bloccato oggi (permesso); letto il 19 ottobre |
| [platform.claude.com prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | ok |
| claude.com/blog | l'indirizzo ipotizzato dà 404: trovare gli articoli sui Project con una ricerca, non per tentativi |

## Modifiche proposte al prompt
1. Elencare nel prompt gli URL che servono (soprattutto support.claude.com): lo strumento chiede il permesso per indirizzi non comparsi nella conversazione e nelle run non presidiate la richiesta scade.
2. Chiedere la conversione con `pdftotext` per i preprint di cui si cita un numero, come nella notte 01.
3. Le domande A–I sono tante per 150 minuti solo a parole: la run è durata circa un quarto d'ora. Si può chiedere più profondità (testi interi dei preprint, Sonnet 5.5 e Haiku 5.5, Windows e link simbolici).
4. Per le pagine con `grep` indicare nel registro `parziale` (fatto qui).

## Costo
- Letture di pagina (WebFetch): 29 (25 di ricerca, 4 di raggiungibilità per la notte 03; di queste 2 bloccate e 1 con 404). Ricerche web: 8. Sottoagenti: 0. Durata: circa 16 minuti (22:52-23:08, Europe/Rome).
- Saldo prima di questa run, dichiarato dall'utente: 26 USD.
- Il consumo in dollari non è visibile all'agente: confrontare il saldo prima e dopo (ultimo saldo noto: 40 USD dopo la v3 del 19 ottobre; il saldo prima di questa run lo riporta l'utente).
