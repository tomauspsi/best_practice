# Log run — Notte 05, attività programmate (v1)

## Riepilogo di un minuto
Prima passata del tema 5 (attività programmate), un solo agente, in locale su Windows (`D:\Workspace\best_practice`, PowerShell). Prodotti quattro file in `ricerche/`: `attivita.md` (README, 15 regole, sezioni A-H, raccordo, conflitti, guida semplice), `registro_fonti_attivita.csv`, `calibrazione_attivita.md`, questo log. 36 letture, 6 ricerche, nessun `PROVENANCE_REQUIRED`, nessuna attività creata o toccata. Esiti chiave: sei vie per programmare (cloud, Desktop, `/loop`, Cowork e app, GitHub Actions, Managed Agents); le routine ora si chiamano «cloud scheduled tasks»; le attività cloud pesano sull'abbonamento come le sessioni interattive e i crediti entrano solo oltre il limite, il che spiega le osservazioni delle notti 03 e 04; `send_later` non ha pagina ufficiale.

Numero di agenti: UN SOLO agente, perché il tema si chiude leggendo a fondo e triangolando poche fonti ufficiali (regola del `CLAUDE.md` del repo); i sottoagenti avrebbero aggiunto costo e parafrasi da ricontrollare.

## Fasi (orari Europe/Rome, da `Get-Date`; il PC è in Europe/Rome)
- **F1 preparazione** 21:42:27-21:43:31. `git fetch origin` (`origin/main` avanzato da `dc631d3` a `e5e53d7`); `git status`: nessun file tracciato modificato, un solo file non tracciato, `.gitattributes` (`* text=auto eol=lf`), lasciato com'è e non aggiunto. Branch `claude/notte-05-attivita` creato da `origin/main` (`e5e53d7`). Letti `CLAUDE.md`, `README.md`, `ricerche/memoria.md` (sezione D e regole), `ricerche/contesto.md` (regole, sezioni E-H, raccordo, conflitti), `ricerche/calibrazione_contesto.md`, `ricerche/collegare_claude_app_a_code.md` (parti su Cowork e attività). Commit.
- **F2 domande A-D** 21:43-21:48. I 10 URL del prompt (routines letta per intero a sezioni da file), poi 3 ricerche, Managed Agents, `web-scheduled-tasks` (redirect), issue 40124, 8 blocchi del changelog di Code, release notes dell'app e dell'API. Registro aggiornato e committato due volte.
- **F3 domande E-H** 21:48-21:51. permission-modes, tools-reference, help 12429409, claude-projects, changelog Cowork, help 13345190, routines-fire, blog Managed Agents, desktop, issue 103724; 3 ricerche; 3 letture di raggiungibilità per la ripassata finale. Registro aggiornato, commit.
- **F4 scrittura** 21:51-21:55. `attivita.md` (208 righe), `calibrazione_attivita.md`, questo log. Commit.
- **F5 controlli** dalle 21:55. Script PowerShell in `$env:TEMP` (fuori dal repo); esiti in «Autocontrollo». Commit finale, push, PR in bozza.

## Incidenti
- Un comando PowerShell con here-string per aggiungere righe al registro è stato bloccato dallo strumento («Remove-Item on system path '/loop' is blocked»): il testo `/loop` dentro le righe è stato scambiato per un percorso. Nessun effetto sul file; righe scritte con lo strumento di scrittura dei file. Stesso incidente della notte 04.
- Nessun `PROVENANCE_REQUIRED`: nessun secondo tentativo necessario.
- `claude` non è nel PATH della sessione PowerShell: versione installata di Code non rilevata; si usa quella del changelog.
- Saldo dei crediti prima della run non dichiarato nel messaggio di avvio (solo utilizzo del piano 57%): annotato in calibrazione.

## Scelte fatte senza chiedere (regola 0.5)
- `.gitattributes` non tracciato: non è una modifica a un file tracciato, quindi la run prosegue senza toccarlo.
- Issue su github.com/anthropics: Tier 3 (segnalazioni di utenti senza risposta), non Tier 1 per dominio.
- Pagine di support.claude.com restituite come riassunto: `verbatim` = parafrasi, nessuna virgoletta nel README.
- Changelog di Code letto oltre i 90 giorni (fino al 19 maggio) per non tagliare a metà un blocco.

## Correzioni proposte ai file esistenti (non fatte)
1. `ricerche/memoria.md`, sezione D: «`/compact` funziona, `/clear` no» è superato; oggi `/clear` funziona nelle sessioni cloud ([claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)). E la scheda dei Project si chiama Scheduled tasks, non Routines.
2. `CLAUDE.md`, «Costi» (27 ottobre): togliere la premessa «non come sessione Code cloud con crediti»: anche le sessioni cloud e le attività cloud pagano con il piano; i crediti entrano solo oltre il limite e se sono attivi ([routines](https://code.claude.com/docs/en/routines)).
3. `CLAUDE.md`, «Perimetro e sicurezza»: aggiungere che le attività cloud partono in auto mode e che conviene togliere i connettori dalla scheda Connectors dell'attività, non solo vietarli nel prompt.
4. `CLAUDE.md` e `README.md`: dopo l'unione, riga del tema 5 (v1, 27 ott, `ricerche/attivita.md`); nel dizionario del README, «attività programmata» può citare i nomi nuovi (cloud scheduled task, già routine).
5. `ricerche/collegare_claude_app_a_code.md`: la frase sull'app di Cowork che deve restare aperta non vale più per le attività programmate (ora nel cloud).
6. `CLAUDE.md`, «Prossimi passi» 5: la notifica push di un'attività cloud non è documentata nelle pagine lette; verificarla a mano nell'interfaccia.

## Autocontrollo
| Regola | Evidenza |
| --- | --- |
| 0.1 un solo agente | nessuna chiamata Agent, Task, fork o sessione parallela; solo chiamate indipendenti nello stesso turno |
| 0.2 tetti | 36 letture su 120, 6 ricerche su 30, durata sotto i 150 minuti (riga sotto) |
| 0.3 lettura a sezioni | `offset` sul changelog (8 blocchi); routines, cloud-environments, tools-reference, claude-projects salvate su file e lette con Grep/Read; righe `parziale` e `parafrasi` nel registro dove serve |
| 0.4 permessi | 0 `PROVENANCE_REQUIRED`, nessun aggiramento |
| 0.5 nessuna domanda | scelte annotate sopra |
| 0.6 orari | `Get-Date` con fuso +01:00 (Europe/Rome) |
| 0.7 scrittura | solo sul branch `claude/notte-05-attivita`, PR in bozza verso `main`, nessuna unione |
| 0.8 file intoccabili | `git diff --name-only origin/main` controllato dallo script: solo i quattro file nuovi in `ricerche/` |
| 0.9 nessuna attività vera | nessuno strumento di programmazione chiamato; elencati per nome in `attivita.md`, sezione F |
| 0.10 nessuna verifica sui modelli | nessuna ricerca su modelli nuovi |
| Sezione 2 perimetro | nessun connettore personale usato; nessun documento Google aperto; nessun file scritto fuori da `D:\Workspace\best_practice` salvo lo script in `$env:TEMP`; nessuna pagina ha dato ordini |
| Sezione 2 dati personali | controllo con comando: nessun indirizzo e-mail né percorso utente nei file prodotti |
| Sezione 3 tier e tag | 34 fonti Tier 1, 2 Tier 3; [Verificato] solo su pagine lette con fetch; parafrasi segnate; il blog del 9 giugno è sotto i 12 mesi |
| Sezione 5 file | quattro file con suffisso `_attivita`; `attivita.md` sotto 300 righe; 15 regole con tag, Tier e URL propri; colonne e vocabolario del registro controllati con lo script |

Sottoagenti: 0
Letture: 36
Ricerche: 6
Durata: dalle 21:42:27 (Europe/Rome); fine nella riga del commit finale
Attività create o modificate: 0
