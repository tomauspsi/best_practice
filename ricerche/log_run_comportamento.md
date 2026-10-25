# log_run, notte 02 comportamento (v1)

## Riepilogo (1 minuto)
- Attività pianificata, 2026-10-25, circa 22:52-23:08 (Europe/Rome). Branch `claude/notte-02-comportamento` da `main` (`a2d1a0c`).
- Un solo agente, perché si leggono a fondo e si triangolano poche fonti ufficiali per vendor (regola del `CLAUDE.md`).
- Sottoagenti: 0. Letture: 29. Ricerche: 8. Durata: circa 16 minuti.
- Chiuse: A (tabella sette strumenti), B, C, D (senza le guide di Sonnet 5.5 e Haiku 5.5), E (due preprint, solo riassunto o abstract), F, G (tranne Windows e link simbolici), H (Opus 5.6 non trovato), I.
- Nessun connettore personale usato (erano agganciati; non toccati i documenti Google). Nessun tentativo di prompt injection nelle pagine lette.
- Consegna: `comportamento.md` (15 regole), registro (29 righe), calibrazione, questo log.

## Fasi
- F1 22:52-22:53: repo già presente, branch creato, lettura di CLAUDE.md, prompt, memoria.md, calibrazione, registro e log precedenti.
- F2: letture A, B, C (agents.md, Copilot, Cursor, Codex, memory, best-practices, hooks-guide, skills, sub-agents, features-overview, Gemini CLI, VS Code).
- F3: D, E, F, H, I (prompting, Opus 5.5, preprint, security, changelog, blog Anthropic, Pillar).
- F4-F5: scrittura dei quattro file, controllo con script fuori dal repo, commit e PR.
- Nota: durante la run ho comunicato «27 letture, 9 ricerche»; il conteggio finale dal registro è 25 + 4 letture e 8 ricerche.

## Incidenti
- Due letture di support.claude.com rifiutate con PROVENANCE_REQUIRED (permesso non risposto): non aggirate.
- `claude.com/blog/using-claude-projects` (indirizzo ipotizzato): 404.
- Le chiamate WebFetch rispondono con riassunti di un modello piccolo: i virgolettati nel README sono solo quelli visti nel testo ricevuto (memory, best-practices, features-overview, migration guide con grep).

## Correzioni proposte ai file esistenti (non fatte)
1. `ricerche/memoria.md`, regola 6 e `CLAUDE.md`: aggiungere che un `CLAUDE.local.md` conta come `CLAUDE.md` e spegne la lettura di `AGENTS.md` (pagina memory, 2026-10-25), e l'impostazione `claude-md-and-agents-md`.
2. `CLAUDE.md` del repo: «`@AGENTS.md` dentro `CLAUDE.md`» è corretto; si può aggiungere `/config` → Project instructions come alternativa.
3. `ricerche/memoria.md`: la riga «changelog… nessuna versione più nuova» è superata (oggi 2.1.310 del 2026-10-23).

## Autocontrollo
| Regola | Esito | Evidenza |
|---|---|---|
| 0.1 un solo agente | ok | Sottoagenti: 0; nessun Agent/Task chiamato |
| 0.2 tetti | ok | 29 letture su 120, 8 ricerche su 30, circa 16 minuti su 150 |
| 0.3 letture a sezioni, ≤15 parole | ok parziale | verbatim brevi; per pagine con riassunto dello strumento «parafrasi» nel registro; i preprint non sono letti per intero (vedi calibrazione) |
| 0.4 nessuna domanda | ok | nessuna domanda fatta |
| 0.5 orari con `TZ=Europe/Rome date` | ok | 22:52 e 23:06 |
| 0.6 scrittura su branch `claude/...`, PR in bozza | ok | branch `claude/notte-02-comportamento`; PR in bozza verso `main` |
| 0.7 file esistenti non modificati | ok | solo quattro file nuovi in `ricerche/` |
| 2 perimetro | ok | nessun connettore; nessun dato personale; due blocchi non aggirati |
| 3 tier e tag | ok | un [Segnale T3] (Pillar); [Verificato] solo su pagine lette con fetch |
| 5 file e formato | ok | `comportamento.md` 157 righe, 15 regole con tag, Tier e URL; ogni URL citato nel registro; vocabolario rispettato; script di controllo fuori dal repo |
| 5.3 distribuzione Tier da comando | ok | calcolata con `collections.Counter` |
| Domande non chiuse | parziale | Sonnet 5.5 e Haiku 5.5, Windows e link simbolici, testo intero dei preprint |
