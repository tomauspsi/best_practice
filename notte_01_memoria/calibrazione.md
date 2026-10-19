# Calibrazione fonti — notte 01 (2026-10-19)

## Cosa ha funzionato
- **Tier 1 Anthropic**: code.claude.com, platform.claude.com, support.claude.com, github.com/anthropics (pagina HTML delle issue): tutti leggibili. Le pagine docs non riportano data di pubblicazione; le date affidabili stanno solo nei changelog e nelle release notes.
- Pagine grandi (changelog ~1 MB, release notes 127k, prompt caching 160k caratteri): WebFetch ne restituisce una parte; serve `offset`. Non tutte lette.
- news.ycombinator.com, dev.to, huggingface.co, simonwillison.net, ai.google.dev, learn.microsoft.com (solo home), docs.aws.amazon.com, forum.cursor.com (indice): ok.

## Cosa è stato bloccato
| Dominio | Esito | Trattamento |
|---|---|---|
| reddit.com, old.reddit.com | rifiutato dallo strumento | non aggirato; nessun dato Reddit |
| stackoverflow.com | rifiutato dallo strumento | non aggirato |
| medium.com | 403 | solo snippet di ricerca (declassato) |
| openai.com, help.openai.com (FAQ) | 403 | solo snippet di ricerca |
| api.github.com | 403 | pagina HTML di GitHub (senza data commit) |
| discord.com | ok ma vuoto | non indicizzabile, confermato |
| platform.openai.com | redirect 301 | non seguito |
- arXiv: l'URL di ricerca provato dava 404 (errore mio, non blocco); i preprint sono arrivati da snippet.
- Il connettore GitHub MCP non era disponibile per i repo di terzi.

## Distribuzione dei Tier (52 URL nel registro)
T1: 30 · T2: 11 · T3: 11 (alcuni T1 letti solo da snippet). Il peso reale delle affermazioni è quasi tutto T1.

## Soglie
- **Reddit (100 voti, 30 commenti):** non verificabile, il sito è inaccessibile con questi strumenti. Per ora irrilevante.
- **GitHub (1.000 stelle + attività negli ultimi 6 mesi):** la parte "attività" non si misura (data ultimo commit non visibile, API 403). Rischio di soglia troppo larga: mem0 (67k stelle) e basic-memory (4,3k) passano su sole stelle. Proposta: richiedere stelle ≥ 1.000 **e** una data di ultimo commit leggibile, altrimenti T3.
- Issue chiuse su github.com/anthropics: utili come T1 per i bug, ma "chiusa" non prova che il fix funzioni; marcare lo stato come non riverificato.

## Elenco proposto per la notte 02 (istruzioni di comportamento, AGENTS.md)
code.claude.com/docs (memory, sub-agents, hooks, settings, skills), agents.md (sito dello standard), github.com/openai/agents.md, cursor.com/docs/context/rules, docs.github.com (istruzioni Copilot), platform.claude.com/docs prompting best practices, github.com/anthropics (skills, claude-code), arxiv.org, simonwillison.net. Aggiungere un controllo preliminare di raggiungibilità di agents.md.

## Modifiche proposte a questo prompt
1. Indicare se `precedenti/` esiste: in questa run il repo era vuoto e il confronto è saltato.
2. Chiarire se vale il branch `claude/notte-01-memoria` o quello assegnato dalla sessione (qui usato quello assegnato: `claude/determined-hamilton-m6vkag`).
3. Consentire un modello fisso per i sottoagenti e fissare "estratto ≤ 15 parole verbatim": gli agenti hanno restituito parafrasi (segnalate "parafrasi").
4. Aggiungere una regola per le pagine troncate: obbligo di rileggere con `offset` quelle citate come fonte unica.
5. Il vincolo "ogni URL citato compare nel registro con esito ok" collide con i preprint letti solo da snippet: ammettere esito "snippet" con declassamento.
6. Il fuso orario del sandbox è UTC: l'orario Rome va calcolato con `TZ=Europe/Rome`.
