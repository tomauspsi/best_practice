---
tema: personalizzazione nell'app Claude (Istruzioni del profilo, stili, skill, plugin, connettori, autonomia)
per: Claude nell'app (chat e Cowork)
aggiornata_il: 2026-11-01
prove: D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes dell'app o changelog di Claude Desktop che toccano stili, skill, plugin, connettori, permessi o Istruzioni; ritorno online della pagina d'aiuto sugli stili; oppure 2026-12-18"
---

# Guida 1 · Personalizzazione nell'app

Per Claude. Usa questa guida quando l'utente vuole decidere dove mettere una regola, scrivere o correggere una skill, riordinare le Istruzioni del profilo, gestire connettori e permessi, o capire perché Claude non segue una preferenza. Vale al 1 novembre 2026 per la sola app Claude: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici. I principi di scrittura delle istruzioni stanno in `D:\Workspace\best_practice\2_istruzioni_project\guida_istruzioni_project.md`. CLAUDE.md, hook e skill di Claude Code esistono solo in Claude Code: se l'utente ne chiede, dillo in una riga.

## Quando usarla
- «Dove metto questa regola?», «la mia skill non parte», «parte quando non deve», «Claude ignora le mie istruzioni».
- «Posso fidarmi di questa skill o di questo plugin?», «come impedisco a Claude di mandare mail da solo?».
- «Che fine hanno fatto gli stili?».

## Cosa è vero oggi
- Dove va cosa:

| Leva | Dove si imposta | Chi la legge | Quando |
|---|---|---|---|
| Istruzioni del profilo | Settings > Your Claude > «Instructions for Claude» | Claude in ogni conversazione e attività programmata | Sempre |
| Stile | Menu degli stili, in uscita (vedi sotto) | Claude, nella conversazione con lo stile scelto | A ogni messaggio |
| Istruzioni del Project | Pulsante delle Istruzioni nel Project | Claude nelle chat di quel Project | Sempre, solo lì |
| Skill | Customize > Skills | Claude: all'inizio solo nome e descrizione, il resto quando serve | Quando la richiesta somiglia alla descrizione, o con «/» |
| Connettore | Customize > Connectors; per chat «+» > «Connectors» | Claude, quando gli serve un dato o un'azione nel servizio | Se acceso nella chat |

- Le «Global instructions» di Cowork sono confluite nelle Istruzioni del profilo: vanno ricontrollate. Nessun limite di lunghezza pubblicato.
- Stili: risultano in migrazione verso le skill (stili personalizzati come skill spente, Concise, Explanatory e Formal tolti), ma la pagina che lo diceva oggi risponde 404 e il system prompt di Sonnet 5.5 nomina ancora gli stili. Stato incerto.
- Una skill è una cartella con `SKILL.md`: `name` in minuscole e trattini, uguale alla cartella; `description` che dice cosa fa e quando usarla; poi le istruzioni. Si carica come ZIP della cartella. Serve **Code execution and file creation** acceso.
- La descrizione è l'unica parte che Claude legge prima di decidere. Limite: 200 caratteri per una pagina d'aiuto, 1.024 per le altre fonti ufficiali.
- Una skill spenta non è disponibile. Le skill e i plugin di terzi non li controlla Anthropic: istruzioni e script girano nella conversazione.
- Permessi per strumento: **Always allow**, **Needs approval**, **Blocked**. Autonomia nella casella del messaggio: **Manually approve**, **Automatically approve** (predefinita), **Skip all approvals**.
- Nessuna pagina dice chi vince tra profilo, Project, stile, memoria e skill.

## Regole da applicare
1. Una regola, una casa. Sempre valida → profilo; per un lavoro → Project; per un compito che ritorna → skill. Mai la stessa regola in due posti: diverge.
2. Una regola che deve valere sempre non va in una skill né solo in memoria: la skill parte solo quando la richiesta corrisponde.
3. Non costruire nulla di nuovo sugli stili. Tono e formato per un compito → skill; tono e formato ovunque → profilo.
4. Descrizione della skill: cosa fa + «Usare quando...» con le parole che l'utente scrive davvero + «Non usarla quando...» per i casi vicini. Terza persona, sotto 200 caratteri.
5. Corpo della skill corto (sotto 500 righe), solo ciò che Claude non sa, file collegati direttamente da `SKILL.md`, niente password né date che invecchiano.
6. Prima di accendere una skill o un plugin di terzi, leggi con l'utente `SKILL.md` e i file: cerca invii verso siti esterni, script, richieste di dati.
7. Connettori: accesi solo nelle chat che li usano; con 10 o più, «Tool access» su «On demand». Strumenti che scrivono, inviano o cancellano: «Needs approval» o «Blocked».
8. Modalità manuale con file, account o siti delicati, con un plugin nuovo, con azioni difficili da annullare.
9. Se Claude non segue una regola: spostala nella casa giusta; riscrivila con il motivo e dicendo cosa fare; togli maiuscole e «CRITICAL»; se è un'azione, usa i permessi; prova in una chat nuova.
10. Se due fonti si toccano, scrivi nelle Istruzioni del Project quale vince.

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato di passi, uno per riga, con i clic esatti nell'app. Per i file dai il percorso Windows completo. Se proponi una descrizione o delle Istruzioni, dalle in un blocco pronto da incollare.

Elenco tipo «scrivere una skill che parte da sola», da adattare:
1. Scrivi in una frase il compito e com'è un risultato buono: diventa la descrizione.
2. Crea la cartella, per esempio `C:\Users\<utente>\Desktop\riassunto-verbale\`, e dentro il file `SKILL.md`.
3. In cima a `SKILL.md` metti l'intestazione:
```text
---
name: riassunto-verbale
description: Riassume verbali di riunione in decisioni, compiti e scadenze. Usare quando l'utente incolla o allega un verbale. Non usarla per email o articoli.
---
```
4. Sotto scrivi i passi, ognuno con il motivo, e un esempio di risultato.
5. Comprimi la cartella (tasto destro > Comprimi in > Cartella compressa): nello ZIP deve esserci la cartella, non i file sciolti.
6. Nell'app apri Customize > Skills > «+» > «+ Create skill» > «Upload a skill» e scegli lo ZIP.
7. Accendila con **Turn on**. Controlla che in Settings > Capabilities sia acceso **Code execution and file creation**.
8. In una chat nuova manda 3 richieste che devono farla partire e 2 simili che non devono; guarda nel ragionamento se l'ha caricata.
9. Se non parte, aggiungi alla descrizione le parole usate nelle richieste; se parte a sproposito, rafforza il «Non usarla quando...». Ricarica e riprova.
10. Per sceglierla a mano, scrivi «/» nella casella del messaggio e selezionala.

Elenco tipo «riordinare le Istruzioni del profilo», da adattare:
1. Apri Settings > Your Claude (layout vecchio: Settings > Account) e copia «Instructions for Claude» in un file, per esempio `C:\Users\<utente>\Desktop\istruzioni_profilo.txt`.
2. Controlla che ci siano le vecchie «Global instructions» di Cowork e togli i doppioni.
3. Segna ogni riga: vale ovunque (resta), vale per un lavoro (va nelle Istruzioni del Project), vale per un compito (va in una skill).
4. Sposta le righe segnate nel Project o nella skill e cancellale dal profilo.
5. Riscrivi ciò che resta in frasi brevi, con il motivo e dicendo cosa fare: lingua, tono, formato, quando chiedere conferma.
6. Togli maiuscole, «SEMPRE» e «MAI» ripetuti.
7. Salva e apri una chat nuova; fai 3 domande normali e 1 a trabocchetto per vedere se le regole tengono.
8. Per le azioni da non fare da sole (inviare, cancellare) non basta il testo: Customize > Connectors > il connettore > **Tool permissions** > «Needs approval» o «Blocked».

## Cosa non sappiamo
- Stato reale della migrazione degli stili sull'account dell'utente: la pagina d'aiuto è irraggiungibile.
- Limite di lunghezza delle Istruzioni del profilo; limite dello ZIP e numero massimo di skill.
- Se l'app accetti il caricamento di un file `.skill` oltre allo ZIP: lo nomina solo il changelog per i fornitori cloud.
- Lunghezza vera della descrizione (200 o 1.024 caratteri).
- Un ordine di precedenza tra profilo, Project, stile, memoria e skill.
- Cosa dicono su preferenze e skill i system prompt di Opus 5.5, Haiku 5.5 e Fable 5.1.

## Prove
Regole numerate con tag e fonti, conflitti e pagine controllate: `D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md`, sezioni «Regole operative», «Conflitti» e «Cosa non è stato verificato».
