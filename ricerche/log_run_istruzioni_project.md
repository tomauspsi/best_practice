# log_run, notte 03 istruzioni di un Project (v1)

## Riepilogo (1 minuto)
- Attività pianificata, 2026-10-26, circa 23:01-23:17 (Europe/Rome). Branch `claude/notte-03-istruzioni-project` da `main` (`a39fbc2`).
- Un solo agente, perché si leggono a fondo e si triangolano poche fonti ufficiali (regola del `CLAUDE.md`).
- Sottoagenti: 0. Letture: 35. Ricerche: 8. Durata: circa 16 minuti.
- Chiuse: A, B, C, D, F (guide di Haiku 5.5 e Sonnet 5.5 lette), G, H. E in parte: quattro preprint, solo abstract o riassunto, nessuna misura sulle Istruzioni di un Project né su Claude 5.5.
- Risultato principale: nessun limite ufficiale per i Project classici, nessuna precedenza dichiarata (ricontrollata su cinque pagine), nessuna prova che le Istruzioni di un Project di chat arrivino a una sessione Code. Opus 5.6 e Sonnet 5.6 non risultano usciti.
- Nessun connettore personale usato (erano agganciati; non toccati i documenti Google). Nessun tentativo di prompt injection nelle pagine lette.
- Consegna: `istruzioni_project.md` (15 regole), registro (35 righe), calibrazione, questo log.

## Fasi
- F1 23:01-23:03: repo già presente in `/home/claude/best_practice`, branch creato da `origin/main`, lettura di `CLAUDE.md` (dal contesto), prompt, `comportamento.md`, `istruzioni_per_progetti.md`, `calibrazione_comportamento.md`, parti di `memoria.md`.
- F2 23:03-23:09: A, B, C, D (support, Academy, claude-projects, prompting, context engineering, RAG, memoria, GitHub, Drive, Cowork).
- F3 23:09-23:12: E, F, G, H (arXiv, guide dei modelli, release notes).
- F4 23:12-23:13: scrittura README e registro. Letture di raggiungibilità per il tema 3.
- F5 23:14-23:17: controllo con script (fuori dal repo), calibrazione, log, commit, push e PR.
- Nota sugli orari: le fasi hanno durato meno di quanto il prompt ammetteva (tetto 150 minuti); la profondità è limitata dai riassunti dello strumento, non dal tempo.

## Incidenti
- **PROVENANCE_REQUIRED sulle prime quattro letture** (support 9519177, support 10185728, code `claude-projects`, Academy), nonostante gli URL fossero nel prompt e i domini pre-approvati. Secondo tentativo riuscito per tutte e quattro. Dettaglio in [calibrazione_istruzioni_project.md](calibrazione_istruzioni_project.md). Le regole `allow` del repo non hanno quindi risolto il problema delle prime richieste.
- La pagina `9519177` non tratta Drive né GitHub né «Sync now» come diceva il prompt: letti `10166901` e `10167454`.
- `release-notes/overview` della piattaforma: letti 100.000 caratteri su 104.366.
- Le chiamate WebFetch rispondono con riassunti di un modello piccolo: i virgolettati sono quelli visti.

## Correzioni proposte ai file esistenti (non fatte)
1. `CLAUDE.md`, sezione «Scoperte»: le regole `allow` in `.claude/settings.json` NON evitano il PROVENANCE_REQUIRED sulle prime letture di una sessione cloud (4 su 4 nella notte 03); un secondo tentativo ha funzionato. Aggiungere `academy.claude.com` all'elenco dei domini.
2. `ricerche/memoria.md`: aggiungere che la memoria creata in un Project può comparire anche nelle chat fuori Project se la memoria è attiva (pagina 11817273, letta il 26 ottobre).
3. `ricerche/istruzioni_per_progetti.md`: la frase sui Cowork project «non sincronizzato né condivisibile» è in conflitto con il Help Center (`14116274`, condivisione Team/Enterprise); il report parla di «Cowork projects» come cartelle locali.
4. `ricerche/comportamento.md`, sezione «Cosa non è stato verificato»: le guide di Sonnet 5.5 e Haiku 5.5 sono ora lette (vedi `istruzioni_project.md`, F).
5. `CLAUDE.md`, Prossimi passi 4: la notte 03 è fatta; resta da programmare il tema 3 (contesto) con i domini in `calibrazione_istruzioni_project.md`.

## Autocontrollo
| Regola | Esito | Evidenza |
|---|---|---|
| 0.1 un solo agente | ok | Sottoagenti: 0; nessun Agent/Task chiamato |
| 0.2 tetti | ok | 35 letture su 120, 8 ricerche su 30, circa 16 minuti su 150 |
| 0.3 letture a sezioni, ≤15 parole | ok parziale | `claude-projects` con grep; i riassunti dello strumento sono marcati «parafrasi» nel registro; preprint solo abstract |
| 0.4 nessuna domanda | ok | nessuna domanda fatta |
| 0.5 orari con `TZ=Europe/Rome date` | ok | 23:01, 23:11, 23:13, 23:14 |
| 0.6 scrittura su branch `claude/...`, PR in bozza | ok | branch `claude/notte-03-istruzioni-project`; PR in bozza verso `main` |
| 0.7 file esistenti non modificati | ok | solo quattro file nuovi in `ricerche/` |
| 2 perimetro | ok | nessun connettore; nessun dato personale (controllo con grep); 4 blocchi non aggirati, ritentati una volta |
| 3 tier e tag | ok | solo Tier 1; nessun [Segnale T3]; [Verificato] solo su pagine lette con fetch; il [Segnale] interno è dichiarato come tale |
| 5 file e formato | ok | `istruzioni_project.md` 190 righe (≤300); 15 regole, ciascuna con tag, Tier e URL propri; 27 URL citati tutti nel registro; vocabolario del registro rispettato; script di controllo fuori dal repo |
| 5.3 distribuzione Tier da comando | ok | calcolata con `collections.Counter` |
| 5.1 sezioni nell'ordine | ok | Risposta breve, Regole, Stato dell'arte (A–H), Raccordo, Conflitti, Non verificato, Fonti per Tier, Guida semplice (14 voci, entro 40 righe) |
| Domande non chiuse | parziale | limite di lunghezza delle Istruzioni nei Project classici (non dichiarato); RAG e Istruzioni; eredità dei Project di chat in Code/Cowork; testo intero dei preprint |
