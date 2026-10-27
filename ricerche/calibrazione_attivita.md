# Calibrazione — Notte 05, attività programmate (v1)

Run del 2026-10-27, dalle 21:42 (Europe/Rome), locale su Windows (`D:\Workspace\best_practice`, PowerShell), un solo agente.

## Cosa ha funzionato
- Gli URL esatti nel prompt: tutte le 10 letture iniziali riuscite al primo tentativo, lette in gruppi di tre o quattro in parallelo.
- Le pagine lunghe salvate su file (routines 49 KB, cloud-environments 64.8 KB, tools-reference 85.8 KB, claude-projects 61.4 KB) si leggono bene con Grep sui titoli e Read a sezioni.
- Il changelog di Code (1.124.089 caratteri) si filtra a blocchi di 100.000 con `offset` e un prompt di parole chiave: 8 letture coprono da 2.1.312 (27-ott) a 2.1.144 (19-mag), oltre i 90 giorni chiesti.
- Le ricerche con `allowed_domains` ufficiali hanno portato al changelog di Cowork e alla issue su `send_later`, due fonti che i soli URL del prompt non davano.

## Cosa è stato bloccato
| Dominio | Esito | Trattamento |
| --- | --- | --- |
| nessuno | nessun 403, 404 o rifiuto dello strumento | — |
| code.claude.com/docs/en/web-scheduled-tasks | redirect alla pagina routines | registrato come `redirect`, contenuto già letto |
| support.claude.com | pagine restituite come riassunto (niente testo verbatim) | `verbatim` = parafrasi nel registro; nel README nessuna virgoletta da queste pagine |
| PowerShell con testo `/loop` dentro un here-string | bloccato dallo strumento (scambiato per un percorso da cancellare) | righe aggiunte al registro con lo strumento di scrittura dei file |
| Reddit, Stack Overflow, openai.com, dev.to, mindstudio.ai, betterstack.com | comparsi nei risultati, non letti | scartati: per il tema bastavano le fonti T1; i blog sono T3 |

## Esito dei permessi
- **`PROVENANCE_REQUIRED`: 0.** Nessuna lettura rifiutata, quindi nessun secondo tentativo.
- Come nella notte 04: run locale, domini pre-approvati in `D:\Workspace\best_practice\.claude\settings.json`, modalità permessi della sessione dell'utente. Due sole prove locali, entrambe pulite; nel cloud restano i 4 rifiuti della notte 03 [Inferenza].
- Collegamento utile: il changelog 2.1.304 (19-ott) corregge le sessioni Cowork programmate che aspettavano cinque minuti per ogni approvazione di URL di WebFetch che nessuno dava. È lo stesso meccanismo del `PROVENANCE_REQUIRED` nel cloud [Inferenza].

## Distribuzione dei Tier (calcolata dal registro)
Comando (PowerShell, dalla cartella del repo):
```powershell
$r = Import-Csv ricerche\registro_fonti_attivita.csv; $r | Group-Object tier | ForEach-Object { "tier $($_.Name): $($_.Count)" }; $r | Group-Object esito | ForEach-Object { "esito $($_.Name): $($_.Count)" }
```
Risultato: 36 righe; tier 1: 34; tier 2: 0; tier 3: 2. Esiti: ok 18, ok parziale 17, redirect 1. Domini: code.claude.com 22, support.claude.com 7, platform.claude.com 3, claude.com 2, github.com 2.
Scelta annotata: le due issue su github.com/anthropics hanno il dominio di Tier 1 ma sono segnalazioni di utenti senza risposta né correzione, quindi sono registrate come Tier 3.

## Proposte per la ripassata finale (in ordine di priorità)
| Priorità | Tema | Pagine da rileggere | Verifica di raggiungibilità |
| --- | --- | --- | --- |
| 1 | 4 memoria (v3 del 19-ott, il più vecchio) | [memory](https://code.claude.com/docs/en/memory), cloud-environments (tabella «What carries over»), claude-projects, help 11817273, release notes dell'app | ok: titolo «How Claude remembers your project», auto memory ancora a 200 righe o 25 KB |
| 2 | 3 contesto | [context-window](https://code.claude.com/docs/en/context-window), model-config, costs, prompt-caching, compaction dell'API | ok: tabella di cosa sopravvive alla compattazione invariata (cita v2.1.304) |
| 3 | 2 istruzioni di un Project | [help 9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), help 10185728, claude-projects (16.000 caratteri) | ok: «aggiornata oltre una settimana fa» |
| 4 | 1 comportamento | memory (sezione `AGENTS.md`), best-practices, skills | — |
| 5 | 5 attività (questo) | routines, desktop-scheduled-tasks, changelog Cowork, help 13854387 | — (letti oggi) |
Da correggere nella ripassata, non qui: la riga di memoria.md su `/clear` nel cloud (vedi `attivita.md`, raccordo).

## Proposte di modifica a questo prompt
1. Punto 1.4: aggiungere `https://code.claude.com/docs/en/permission-modes`, `https://code.claude.com/docs/en/tools-reference`, `https://platform.claude.com/docs/en/managed-agents/scheduled-deployments` e `https://claude.com/docs/cowork/changelog`: sono quattro delle fonti più usate e oggi si trovano solo cercando.
2. Domanda F: chiedere il changelog di Code per intervallo di versioni (per esempio «da 2.1.230 in su») invece che «90 giorni»: rende esplicito quante letture con `offset` servono (qui 7 per 90 giorni).
3. Domanda D: aggiungere «dove si attivano le notifiche push di un'attività cloud», con l'avvertenza che può non esserci una pagina (qui: nessuna prova trovata).
4. Regola 0.3: per le pagine di support.claude.com, che lo strumento restituisce come riassunto, dire subito di segnarle «parafrasi» e di non citarle tra virgolette.
5. Sezione 3: precisare che una issue utente su github.com/anthropics vale come Tier 3 (o Tier 2 se chiusa con fix), non come Tier 1.

## Costo
- Letture di pagina: 36 (nessuna rifiutata; 8 sono blocchi del changelog di Code). Ricerche web: 6. Sottoagenti: 0.
- Durata: circa 15 minuti (21:42-21:57, Europe/Rome).
- Il consumo in dollari non è visibile all'agente: confrontare il saldo dei crediti prima e dopo e anche l'utilizzo del piano (valori prima della run: quelli dichiarati dall'utente nel messaggio di avvio). Messaggio di avvio: utilizzo del piano 57%; saldo dei crediti non dichiarato (l'ultimo noto, del 27 ottobre, è 23 USD).
