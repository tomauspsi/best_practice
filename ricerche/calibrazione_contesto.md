# Calibrazione — Notte 04, contesto (v1)

Run del 2026-10-27, 21:15-21:27 circa (Europe/Rome), locale su Windows (`D:\Workspace\best_practice`, PowerShell), un solo agente.

## Cosa ha funzionato
- Gli URL esatti nel prompt: tutte le 12 letture iniziali riuscite al primo tentativo.
- Le pagine di code.claude.com e platform.claude.com rispondono in Markdown pulito: tabelle e numeri arrivano intatti, quasi sempre con estratti verbatim.
- Due ricerche mirate su arXiv hanno dato i preprint giusti (2510.05381, 2602.07962, 2605.28079); il testo HTML di 2602.07962 è stato letto per intero, figure escluse.
- Le pagine più lunghe di 100.000 caratteri (model-config) si leggono con `offset`; quelle oltre 50 KB vengono salvate su file e lette a sezioni con Grep e Read (best-practices, routines).

## Cosa è stato bloccato
| Dominio | Esito | Trattamento |
| --- | --- | --- |
| nessuno | nessun blocco, nessun 403 o 404 | — |
| Reddit, Stack Overflow, openai.com | non interrogati: per il tema 3 bastavano le fonti ufficiali | — |
| claude.ai/public/artifacts, claudeissues.com, blog terzi | comparsi nei risultati di ricerca, non letti | scartati: Tier 3 o contenuto generato da utenti |

## Esito dei permessi
- **`PROVENANCE_REQUIRED`: 0.** Nessuna lettura rifiutata, quindi nessun secondo tentativo necessario.
- Differenza dalla notte 03 (4 rifiuti sulle prime letture parallele di una sessione cloud): questa run gira in locale, con i domini pre-approvati in `D:\Workspace\best_practice\.claude\settings.json` e la modalità permessi della sessione dell'utente. Una sola prova: non dice se il rimedio funzioni anche nel cloud [Inferenza].
- La prima lettura è partita in un gruppo di quattro in parallelo, come nella notte 03, senza rifiuti.

## Distribuzione dei Tier (calcolata dal registro)
Comando (PowerShell, dalla cartella del repo):
```powershell
$r = Import-Csv ricerche\registro_fonti_contesto.csv; $r | Group-Object tier | ForEach-Object { "tier $($_.Name): $($_.Count)" }
```
Risultato: 31 righe; tier 1: 31; tier 2: 0; tier 3: 0. Esiti: ok 25, ok parziale 6. Domini: code.claude.com 11, platform.claude.com 7, support.claude.com 6, arxiv.org 6, www.anthropic.com 1.

## Domini per la notte successiva (tema 5, programmazione delle attività)
Trovati con due ricerche; ciascuno con una lettura di raggiungibilità.
| Pagina | Esito |
| --- | --- |
| [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) | ok, intera: `/loop`, promemoria una tantum, `CronCreate`/`CronList`/`CronDelete`, scadenza a 7 giorni, tabella cloud / Desktop / sessione |
| [desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) | ok, intera: attività locali di Desktop, recupero delle run perse, permessi |
| [routines](https://code.claude.com/docs/en/routines) | ok, solo anteprima (49 KB salvati su file): le routine ora si chiamano «cloud scheduled tasks», research preview |
| [help 13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) | ok, parziale: attività ricorrenti in Cowork, aggiornata questa settimana |
| `send_later` | nessuna pagina ufficiale trovata con una ricerca dedicata: solo un plugin di terzi lo nomina [Segnale T3]. Da cercare di nuovo nella notte 05 (strumenti di Cowork o della nuova esperienza unificata) |

## Proposte di modifica a questo prompt
1. Punto 0.6: per le run locali su Windows scrivere «`TZ=Europe/Rome date` oppure `Get-Date` se il PC è già in Europe/Rome», così la regola è eseguibile su entrambe le piattaforme.
2. Punto 1.4: aggiungere `https://code.claude.com/docs/en/best-practices` e `https://code.claude.com/docs/en/prompt-caching` agli URL da leggere per primi: sono due delle pagine più utili per le domande C ed E.
3. Domanda A: separare «cosa riempie il contesto nell'app» come domanda a sé, con l'indicazione che potrebbe non esistere una pagina ufficiale (è uscita «nessuna prova trovata»).
4. Domanda B: chiedere esplicitamente il testo completo almeno di un preprint per gruppo (lunghezza, posizione, istruzioni); in questa run il testo intero c'è solo per LOCA-bench.
5. Per il tema 5: includere nel prompt gli URL esatti della tabella sopra e la domanda «esiste `send_later` come strumento ufficiale?».

## Costo
- Letture di pagina: 31 (nessuna rifiutata). Ricerche web: 7. Sottoagenti: 0.
- Durata: circa 12 minuti (21:15-21:27, Europe/Rome).
- Il consumo in dollari non è visibile all'agente: confrontare il saldo dei crediti prima e dopo (saldo prima di questa run: 23 USD, dichiarato dall'utente il 27 ottobre) e anche l'utilizzo del piano (prima della run: 53%, dichiarato dall'utente il 27 ottobre).
- Nota: la run gira in una sessione locale del desktop, non come attività cloud: il confronto con la notte 03 va letto con questa differenza.
