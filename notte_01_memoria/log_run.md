# log_run, notte 01 memoria (v3, conclusiva)

## Riepilogo (1 minuto)
- **Run v3.** Attività pianificata, 2026-10-19 dalle 12:55 alle 13:05 circa (Europe/Rome). Branch `claude/tema-04-memoria-v3` da `origin/main`, hash di partenza `d0a1c7c`.
- **Sottoagenti: 0.** Le nove domande si risolvono leggendo e triangolando poche fonti ufficiali: il caso in cui CLAUDE.md consiglia un solo agente.
- **Letture:** 27 (2 con 403). **Ricerche:** 4. **Durata:** circa 10 minuti.
- **Chiuse:** 1 (prova sul contesto: nessun blocco di memoria né istruzioni del profilo), 3 (nessuna regola ufficiale di precedenza), 4 (sync manuale), 5, 6 (testo completo dei preprint), 8 (date con anno), 9 (nessuna novità dopo il 19 ottobre).
- **Parziali:** 2 (routine del Project: dedotta, non scritta), 7 (ChatGPT solo snippet; Cursor Memories: changelog tace, rimozione solo nel forum).
- **Correzione a v2:** MemoryGraft propone due difese (non testate); v2 diceva "nessuna".
- **Consegna:** `memoria.md` v3 con 15 regole e Guida semplice; registro a 78 righe; calibrazione e log riscritti.
- **Sicurezza.** Nessun connettore personale usato (era presente Google Drive: non toccato). Nessun tentativo di prompt injection nelle pagine lette.
- **Validatore.** Vedi "Esito del validatore" in fondo.

## Fasi
- F0 12:55-12:56: fetch di main, branch, hash `d0a1c7c`, lettura di CLAUDE.md, v2, calibrazione, log, registro, validatore. I due file di `precedenti/` non riletti per intero: il loro contenuto è già riassunto nel Raccordo di v2.
- F1 12:56-12:57: domande 1-3 (claude-projects, memory, routines, help 11817273, release notes claude.ai).
- F2 12:57-12:58: domanda 4-6 (help GitHub, usage limits, tre PDF con `pdftotext`, ricerca su difese Anthropic).
- F3 12:58-12:59: domande 7-9 (commit mem0 e basic-memory, changelog Cursor, 2607.14611, Cisco, changelog Claude Code, release notes API, security, personalizzazione, desktop).
- F4 13:00: registro aggiornato (78 righe), commit.
- F5 13:00-13:02: scrittura di `memoria.md`, validatore, commit.
- F6 13:02-13:05: calibrazione, log, validatore, push, PR in bozza.

## Incidenti
- `help.openai.com` e `openai.com`: 403; ricorso a snippet di WebSearch, [Inferenza].
- WebFetch sui PDF restituisce byte: scaricati e convertiti con `pdftotext` in `/tmp/claude-0/pdf` (la scratchpad della sessione non è stata usata per questa cartella: nessun impatto sul repo).
- Il validatore ha rifiutato le prime bozze: markup `**` attaccato a link e un valore YAML con estratto lungo. Corretti.
- Prima versione della regola 10 con URL sbagliato (12123587 invece di 11817273): corretta prima del commit.

## Autocontrollo
| Voce | Esito | Evidenza |
|---|---|---|
| D1 memoria account e Code | fatto | prova su di me: nessun blocco di memoria né istruzioni del profilo; 7 pagine T1 senza menzione; Desktop e CLI non provati |
| D2 routine e project memory | parziale | claude-projects: routine come thread del Project; thread locale senza memoria; eredità [Inferenza] |
| D3 precedenza | fatto | memory: concatenazione; help 10185728: nessuna regola |
| D4 Project e GitHub | fatto | help 10167454: sync manuale |
| D5 chat lunghe | fatto | help 11647753; 2.1.299 compaction da inattività |
| D6 avvelenamento | fatto | tre PDF letti per intero; 2607.14611 solo abstract; Anthropic: security, How we contain Claude; Cisco [Segnale T3] |
| D7 concorrenti | parziale | ChatGPT snippet 403; Cursor changelog pagine 1-3 e 2.1 senza Memories |
| D8 commit | fatto | mem0 2026-10-14; basic-memory 2026-10-18 |
| D9 novità | fatto | nessuna voce dopo il 19-ott; da v2 solo 2.1.299 e 2.1.296 |
| memoria.md | fatto | YAML versione 3, base `d0a1c7c`; 15 regole; Guida semplice di 45 righe; 190 righe in tutto |
| registro_fonti.csv | fatto | 78 righe, vocabolario chiuso |
| calibrazione.md | fatto | Tier, blocchi, scelta degli agenti, Costo |
| log_run.md | fatto | questa tabella |

## Esito del validatore
`python3 -I tools/validate_notte.py`: 12 errori, 0 avvisi. Tutti e 12 sono la stessa causa: il validatore è ancora legato alla notte 01 e pretende nell'Autocontrollo le voci C1-C12 del prompt di correzione, che la v3 non ha (usa le voci D1-D9 delle domande). Nessun altro controllo fallisce: YAML, 15 regole con URL, tag e Tier, URL nel registro, vocabolario del registro, sezioni obbligatorie, `Sottoagenti: 0`, lunghezza. Non ho aggiunto voci C1-C12 fittizie per far passare il controllo: la generalizzazione del validatore è il passo 2 dei prossimi passi di CLAUDE.md.
