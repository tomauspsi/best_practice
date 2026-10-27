---
tema: comportamento di Claude Code e degli altri agenti con i file di istruzioni (CLAUDE.md, AGENTS.md, rules, skill, hook)
per: Claude (chat, Cowork, Code) quando aiuta l'utente su questo tema
aggiornata_il: 2026-10-27
prove: D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes di Claude Code su CLAUDE.md, AGENTS.md, rules o hook; oppure 2026-12-18"
---

# Guida 1 · Comportamento: CLAUDE.md e AGENTS.md

Per Claude. Usa questa guida quando l'utente vuole scrivere, correggere o capire un `CLAUDE.md`, un `AGENTS.md`, le regole di un repo o i file di istruzioni di un altro strumento. Vale al 27 ottobre 2026: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici.

## Quando usarla
- «Cosa metto nel CLAUDE.md?», «perché Claude non segue questa regola?», «uso anche Cursor o Codex: che file serve?».
- Prima di aprire con un agente un repo scaricato da altri.
- Dopo l'uscita di un modello nuovo.

## Cosa è vero oggi
- Claude Code legge `CLAUDE.md` (e `.claude/CLAUDE.md`, `CLAUDE.local.md`, `.claude/rules/`). Legge `AGENTS.md` solo se non trova nessun `CLAUDE.md`, e un `CLAUDE.local.md` conta come `CLAUDE.md`.
- I file trovati si sommano, nessuno prevale: con due regole opposte Claude può seguirne una a caso.
- Un `CLAUDE.md` è contesto, non un vincolo: per un divieto vero servono hook o permessi.
- La chat dell'app e Cowork non leggono `CLAUDE.md`: per loro valgono le Istruzioni del Project (guida 2).
- Un `CLAUDE.md` solo sul PC (`C:\Users\<utente>\.claude\CLAUDE.md`) non arriva alle sessioni e alle attività nel cloud: lì arriva solo il repo.
- Un solo studio (preprint) ha misurato i file di contesto: né quelli generati da un'IA né quelli scritti a mano migliorano i risultati in generale, e costano in media oltre il 20% in più.
- Su Windows si usa la riga `@AGENTS.md` dentro `CLAUDE.md`, non un collegamento simbolico: lì il collegamento chiede privilegi di amministratore e git può scaricarlo come un file di una riga.

## Regole da applicare
1. Scrivi istruzioni verificabili e concrete («lancia `npm test` prima del commit», non «testa bene»): Claude le segue meglio.
2. Meno di 200 righe per `CLAUDE.md`; per ogni riga il test è: «se la tolgo, Claude sbaglia?». Le righe in più fanno ignorare quelle utili.
3. Metti solo ciò che Claude non ricava dal codice: i comandi esatti di test e controllo, i punti in cui il codice inganna, le decisioni che non stanno nel repo, ciò che hai già corretto due volte. Non descrivere architettura e cartelle: Claude legge il repo da solo.
4. Una regola, una casa: mai la stessa regola in due file, perché le copie divergono.
5. Divieti e azioni da fare sempre: hook `PreToolUse` o permessi, non testo.
6. Procedure lunghe in una skill (si carica solo quando serve); regole per una cartella in `.claude/rules/` con `paths`.
7. Con più strumenti sullo stesso repo: `AGENTS.md` con le regole comuni e, dentro `CLAUDE.md`, la riga `@AGENTS.md`; niente `CLAUDE.local.md` senza l'impostazione `claude-md-and-agents-md`.
8. Scrivi in positivo e con il motivo; niente maiuscole urlate né «MUST» diffusi: i modelli recenti li prendono troppo alla lettera. Se una riga viene ignorata, non aggiungere «IMPORTANT»: accorcia il file o trasforma la regola in un hook.
9. A ogni modello nuovo rileggi le istruzioni e togli quelle superate; in Code c'è `/doctor prompt-audit`.
10. I file di istruzioni di altri sono codice non fidato: vanno letti prima di aprirli con un agente.

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato di cose da fare, una per riga, ognuna con un esempio concreto e, se serve, il percorso Windows completo del file. Prima la risposta, poi al massimo un consiglio. Se manca un dato (quale repo, quale strumento), chiedilo in una riga invece di indovinare.

Elenco tipo, da adattare al caso:
1. Apri il file `D:\Workspace\<progetto>\CLAUDE.md` (crealo se manca, nella cartella del progetto).
2. Scrivi solo: i comandi esatti per controllare il lavoro, i punti in cui il codice trae in inganno, le decisioni che non stanno nei file, le cose che hai dovuto correggere due volte. Togli spiegazioni, manuali e descrizioni delle cartelle.
3. Rileggi ogni riga chiedendoti se, togliendola, Claude sbaglierebbe; se no, cancellala.
4. Se una regola deve valere per forza, chiedi a Claude un hook: il testo da solo non basta.
5. Se usi anche Cursor o Codex, sposta le regole comuni in `AGENTS.md` e lascia in `CLAUDE.md` la riga `@AGENTS.md`.
6. Manda il file su GitHub: solo così lo leggono anche le attività nel cloud.
7. Quando esce un modello nuovo, ripeti il passo 3.

## Cosa non sappiamo
- Se Claude, davanti a due istruzioni opposte, ne scelga una a caso o le concili: due pagine ufficiali dicono cose diverse.
- Nessuna misura sui modelli 5.x dell'effetto di un `CLAUDE.md` lungo o corto.
- Gli studi sulla sicurezza dei file di regole sono letti solo come abstract.

## Prove
Regole numerate, tabelle per strumento (Codex, Copilot, Cursor, Gemini CLI, VS Code) e fonti: `D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md`.
