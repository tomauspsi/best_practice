# Comportamento di Claude (CLAUDE.md, AGENTS.md): guida semplice

Tema 1, versione 1, del 25 ottobre 2026. Da rivedere quando esce un nuovo modello Claude (ad esempio Opus 5.6) o il 18 dicembre 2026.
Le prove e le fonti, per gli agenti, stanno in `ricerche/comportamento.md`. Questo file è per te.

Per chi usa Claude Code, la chat dell'app e, se serve, Cursor o Codex. Ogni passo ha un esempio.

1. **Un CLAUDE.md è il foglio di istruzioni di Claude Code.** Mettilo nella cartella del progetto, ad esempio `D:\Workspace\best_practice\CLAUDE.md`, e mandalo su GitHub: così lo leggono anche le attività nel cloud.
2. **Scrivi poco e preciso.** Meno di 200 righe. «Scrivi in italiano» va bene; «lavora bene» non serve. Per ogni riga chiediti: se la tolgo, Claude sbaglia? Se no, cancellala.
3. **Metti solo ciò che Claude non può capire da solo.** Comandi da lanciare, nomi dei branch, regole del tuo stile. Non incollare manuali.
4. **Una regola, una casa.** Non scrivere la stessa regola in due file: se si contraddicono, Claude ne segue una a caso.
5. **Le regole che non si possono rompere non vanno nel CLAUDE.md.** Sono richieste, non blocchi. Per un blocco vero serve un «hook» o un permesso nelle impostazioni (Claude può aiutarti a scriverlo).
6. **Procedure lunghe in una «skill».** Una skill si apre solo quando serve. Il CLAUDE.md resta corto.
7. **La chat dell'app non legge il CLAUDE.md.** Per la chat usa le Istruzioni del Project; per il resto vedi `guida_memoria.md`.
8. **Se usi anche Cursor o Codex:** crea `AGENTS.md` con le regole comuni e scrivi dentro `CLAUDE.md` la riga `@AGENTS.md`. Evita `CLAUDE.local.md` se non cambi l'impostazione, perché fa smettere Claude di leggere `AGENTS.md`.
9. **Non farlo scrivere tutto a un'intelligenza artificiale e fidarti.** Uno studio ha trovato che i file generati in automatico non migliorano i risultati e costano di più. Rileggi e taglia.
10. **I file di istruzioni di altri sono come programmi di altri.** Prima di aprire con Claude un repo scaricato, guarda i suoi file di istruzioni.
11. **Quando esce un modello nuovo** (ad esempio Opus 5.6) rileggi le istruzioni e togli quelle diventate inutili; in Claude Code lancia `/doctor prompt-audit`.
12. **Errore comune:** mettere regole solo in `C:\Users\Tommi\.claude\CLAUDE.md` e aspettarsi che le attività nel cloud le seguano: lì non arrivano.
