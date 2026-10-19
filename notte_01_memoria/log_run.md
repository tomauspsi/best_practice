# log_run — notte 01 memoria

## Riepilogo (1 minuto)
- Run eseguita il 2026-10-19 in modo interattivo dalla sessione cloud, non alle 03:30 programmate; orari Europe/Rome da `date`.
- Prodotti: `memoria.md`, `registro_fonti.csv`, `calibrazione.md`, `log_run.md`.
- Repo vuoto all'avvio: `precedenti/` assente, quindi nessun confronto con i report del 18 ottobre.
- Branch: `claude/determined-hamilton-m6vkag` (assegnato dalla sessione) al posto di `claude/notte-01-memoria`. Push riuscito al primo tentativo.
- 4 sottoagenti (B, C+D, F+G, H+I) su modello `sonnet`; A+E fatti da me.
- Bloccati dallo strumento: reddit.com, old.reddit.com, stackoverflow.com. Medium e openai.com 403. Nessun aggiramento.
- Prompt injection nelle pagine: nessun episodio. Il filtro del harness ha segnalato due report dei sottoagenti per un testo simile a istruzioni su `settings.json`: erano citazioni delle docs, nessuna azione intrapresa.
- Esito decisivo (domanda D): la sessione cloud fresca vede il `CLAUDE.md` del repo, non `C:\Users\Tommi\.claude\CLAUDE.md` né l'auto memory locale; memoria chat dell'account → Claude Code cloud non documentata.
- Aperti: vedi "Cosa non è stato verificato" in `memoria.md`.
- Proxy di costo: ~55 letture di pagina e ~8 ricerche web in totale (limite 200); 4 sottoagenti (limite 5); il consumo in dollari non è visibile.

## Fasi
- FASE 0 03:16 — ambiente: strumenti WebSearch/WebFetch caricati; branch creato; commit di prova e push ok.
- FASE 1 03:17 — sonda raggiungibilità: mia (code/support/platform.claude.com, reddit, HN, discord, simonwillison, GitHub issues, arxiv) + agente F+G (~17 domini). Esiti nel CSV.
- FASE 2 03:17–03:19 — ricerca: 4 sottoagenti in background; letture sue: B 5, C+D 13, F+G 15, H+I 7 (+ ricerche). Mie: ~10 fetch + 4 ricerche. Verifica diretta della pagina Dreams e delle tabelle cloud/Projects.
- FASE 3 — triangolazione: conflitti in `memoria.md`; due fonti non indipendenti (blog su Auto Dream) contate come una.
- FASE 4 — scrittura dei 4 file.
- FASE 5 — controllo: righe di `memoria.md` ≤ 300; nessun dato personale; URL del registro con esito (ok, parziale, snippet, bloccato) e non tutti "ok" (vedi proposta di modifica al prompt).

## Incidenti
- `precedenti/` mancante. · URL arXiv di ricerca 404 (errore mio). · API GitHub 403 e MCP GitHub non autorizzato per repo terzi. · Pagine lunghe lette solo in parte. · Refuso nel nome del tool `memory_20250818` nella prima bozza, corretto prima del commit.
- Estratti dei sottoagenti spesso parafrasi, non verbatim: segnalato nelle tabelle.
