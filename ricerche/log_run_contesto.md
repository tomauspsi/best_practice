# Log run — Notte 04, contesto (v1)

## Riepilogo di un minuto
Prima passata del tema 3 (contesto), un solo agente, in locale su Windows (`D:\Workspace\best_practice`, PowerShell) invece che in una sessione cloud. Prodotti quattro file in `ricerche/`: `contesto.md` (README, 15 regole, sezioni A-H, raccordo, conflitti, guida semplice), `registro_fonti_contesto.csv`, `calibrazione_contesto.md`, questo log. 31 letture, 7 ricerche, nessun rifiuto `PROVENANCE_REQUIRED`. Esiti chiave: quattro modelli correnti a 1M token; compattazione automatica di Code a circa 967K; sintesi automatica dell'app solo con esecuzione di codice attiva; Opus 5.6 e Sonnet 5.6 non usciti; i preprint misurano forti cali con la lunghezza (Claude 4.5 Opus 96,0% → 14,7% da 8K a 256K) ma nessuno su Claude 5.x.

Numero di agenti: UN SOLO agente, perché il tema si chiude leggendo a fondo e triangolando poche fonti ufficiali (regola del `CLAUDE.md` del repo); i sottoagenti avrebbero aggiunto costo e parafrasi da ricontrollare.

## Fasi (orari Europe/Rome, da `Get-Date`; il PC è in Europe/Rome)
- **F1 preparazione** 21:15:29-21:16:04. `git fetch origin` (main locale indietro di 2 commit rispetto a `origin/main`); `git status`: nessun file modificato, un solo file non tracciato, `.gitattributes` (`* text=auto eol=lf`), lasciato com'è e non aggiunto. Branch `claude/notte-04-contesto` creato da `origin/main` (`22121a5`). Letti `CLAUDE.md`, `README.md`, `ricerche/memoria.md` (intero), le parti su contesto di `ricerche/comportamento.md` e `ricerche/istruzioni_project.md`, i permessi in `ricerche/calibrazione_istruzioni_project.md`. Commit.
- **F2 domande A-D** 21:16-21:18. 12 URL del prompt, poi 2 ricerche e 6 letture su arXiv. Registro aggiornato, commit.
- **F3 domande E-H** 21:18-21:22. Help RAG, best practices, prompt caching, release notes app e API, changelog, models overview; ricerche su Opus 5.6 e sui domini del tema 5 con quattro letture di raggiungibilità. Registro aggiornato, commit.
- **F4 scrittura** 21:22-21:26. `contesto.md` (188 righe), `calibrazione_contesto.md`, questo log.
- **F5 controlli** 21:26-21:30. Script PowerShell in `$env:TEMP` (fuori dal repo); esiti in «Autocontrollo». Commit finale, push, PR in bozza.

## Incidenti
- Un comando PowerShell con here-string per aggiungere righe al registro è stato bloccato dallo strumento («Remove-Item on system path '/' is blocked»), senza effetti sul file; righe aggiunte con lo strumento di modifica dei file. Nessun altro incidente.
- Nessun `PROVENANCE_REQUIRED`: nessun secondo tentativo necessario.
- Differenze solo di a capo: nessuna (copia di lavoro pulita, `git diff` vuoto).

## Correzioni proposte ai file esistenti (non fatte)
1. `ricerche/memoria.md`, regola 15 e Fonti: l'articolo 11647753 ora si chiama «How do usage and length limits work» (`https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work`); aggiungere che la sintesi automatica vale per i piani a pagamento con esecuzione di codice attiva.
2. `ricerche/memoria.md`, intestazione: Claude Code è ora alla 2.1.311 (2026-10-26).
3. `ricerche/comportamento.md`, tabella degli strumenti: accanto a «Sottoagente — contesto separato», notare che le best practices correnti considerano superato l'uso dei sottoagenti per proteggere il contesto.
4. `README.md` e `CLAUDE.md`: aggiornare la riga del tema 3 (v1, 27 ott, `ricerche/contesto.md`) dopo l'unione, quando l'utente decide.
5. `README.md`, punto 12: confermato al 27 ottobre che Opus 5.6 non è uscito.

## Autocontrollo
| Regola | Evidenza |
| --- | --- |
| 0.1 un solo agente | nessuna chiamata Agent, Task, fork o sessione parallela; solo chiamate indipendenti nello stesso turno |
| 0.2 tetti | 31 letture su 120, 7 ricerche su 30, circa 15 minuti su 150 |
| 0.3 lettura a sezioni | `offset` su model-config; best-practices e routines salvate su file e lette con Grep/Read; righe `parziale` e `parafrasi` nel registro dove serve |
| 0.4 permessi | 0 `PROVENANCE_REQUIRED`, nessun aggiramento |
| 0.5 nessuna domanda | scelte annotate qui (file `.gitattributes` non toccato; `Get-Date` al posto di `TZ=Europe/Rome date`) |
| 0.6 orari | `Get-Date` con fuso +01:00 (Europe/Rome) |
| 0.7 scrittura | solo sul branch `claude/notte-04-contesto`, PR in bozza verso `main`, nessuna unione |
| 0.8 file intoccabili | `git diff --name-only origin/main` mostra solo i quattro file nuovi in `ricerche/` |
| Sezione 2 perimetro | nessun connettore personale usato; nessuna lettura di documenti Google; nessun file fuori da `D:\Workspace\best_practice` scritto (script di controllo in `$env:TEMP`); nessuna pagina ha dato ordini |
| Sezione 2 dati personali | controllo con comando: nessun indirizzo e-mail, nessun percorso utente nei file prodotti |
| Sezione 3 tier e tag | 31 fonti Tier 1; preprint con `nota_tier` «preprint»; [Verificato] solo su pagine lette con fetch; context engineering (oltre 12 mesi) verificato contro pagine correnti; 2307.03172 marcato [Obsoleto?] |
| Sezione 5 file | quattro file con suffisso `_contesto`; `contesto.md` 188 righe (≤ 300); 15 regole con tag, Tier e URL propri; colonne e vocabolario del registro controllati con script |

Sottoagenti: 0
Letture: 31
Ricerche: 7
Durata: circa 15 minuti (21:15-21:30, Europe/Rome)
