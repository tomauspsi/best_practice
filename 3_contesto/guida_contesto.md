---
tema: contesto di Claude nell'app (finestra, cosa la riempie, degrado, sintesi automatica, chat lunghe)
per: Claude nell'app (chat e Cowork)
aggiornata_il: 2026-11-01
prove: D:\Workspace\best_practice\3_contesto\rapporto_contesto.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes dell'app o changelog di Claude Desktop che toccano contesto, sintesi automatica, connettori, effort o limiti; oppure 2026-12-18"
---

# Guida 3 · Contesto

Per Claude. Usa questa guida quando l'utente chiede perché una chat lunga peggiora o consuma di più, quando aprire una chat nuova, o come tenere leggero ciò che Claude ha davanti. Vale al 1 novembre 2026 per la sola app Claude: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici. Claude Code ha comandi suoi per il contesto: se l'utente ne chiede, dillo in una riga.

## Quando usarla
- «La chat è diventata lenta o sbaglia», «consumo troppo», «devo ricominciare da capo?», «meglio allegare o mettere nel Project?».
- Prima di caricare molti documenti in un Project o di un lavoro lungo in Cowork.
- Memoria tra chat: `D:\Workspace\best_practice\4_memoria\guida_memoria.md`. Istruzioni del Project: `D:\Workspace\best_practice\2_istruzioni_project\guida_istruzioni_project.md`.

## Cosa è vero oggi
- **Che cos'è:** tutto ciò che Claude ha davanti quando risponde: istruzioni, file, strumenti, cronologia della chat e la risposta stessa.
- **Quanto spazio:** in chat 1 milione di token per Fable 5.1, Opus 5.5, Sonnet 5.5 e Haiku 5.5; in Cowork Haiku 5.5 ne ha 500.000. Una parte è sempre riservata alla risposta.
- **Più non è meglio:** con più token calano precisione e richiamo («context rot»). Gli studi lo misurano fino a Claude 4.5, non sui modelli 5.x.
- **Costo:** a ogni domanda Claude rilegge tutta la conversazione, quindi una chat lunga consuma più limite d'uso anche per una domanda breve.
- **Sintesi automatica:** solo sui piani a pagamento con esecuzione di codice attiva. Vicino al limite Claude riassume i messaggi vecchi; la cronologia resta consultabile; compare «organizing its thoughts». Consuma più limite. Nessuna soglia pubblicata, salvo Sonnet 5 in Cowork (500.000 token).
- **Cosa entra, per quanto dicono le pagine:** le Istruzioni del profilo in ogni conversazione; le Istruzioni del Project nelle chat del Project; la knowledge del Project intera finché ci sta, poi solo la parte pertinente (RAG); le skill quando servono; strumenti e connettori, che pesano molto; le chat passate solo quando Claude le cerca. Per memoria e stili nessuna pagina lo dice.
- **Project con molti file:** il RAG parte da solo vicino al limite, porta fino a 10 volte la capacità e non si regola. I documenti del Project vanno in cache: dopo una pausa lunga il primo messaggio li conta di nuovo per intero.
- **Allegati o Project:** in chat fino a 20 file da 500 MB, PDF fino a 1.000 pagine (grafici letti fino a 100); nel Project file da 30 MB, solo testo salvo i PDF multimodali, validi per tutte le chat del Project.
- **Ramificare una chat** da un punto precedente non si può nell'app unificata.
- **Lavoro in parallelo:** si possono avere più attività insieme e Claude può usare sottoagenti; tutto conta sui limiti del piano e le attività con più passi consumano di più. Quanto in più, nessuna pagina lo dice.

## Regole da applicare
1. Un argomento per chat: per un lavoro non collegato, o quando una chat lunga si avvicina al limite, proponi una chat nuova nello stesso Project.
2. Nella chat nuova bastano tre righe su dove si era arrivati, cosa è deciso e cosa resta da fare; le regole che valgono sempre vanno nelle Istruzioni del Project, non nei messaggi.
3. Istruzioni del Project brevi: contesto generale, linee guida, ruolo di Claude. Le istruzioni del singolo compito stanno nella chat.
4. Togli dal Project i file che non servono più; usa il Project per i documenti che servono in più chat e l'allegato per quelli di una chat sola.
5. Connettori spenti quando non servono; con 10 o più connettori, «Tool access» su «On demand».
6. Se non servono notizie aggiornate, chiedi a Claude di non cercare sul web: nell'app unificata non c'è un interruttore.
7. Effort più basso per i compiti di routine; sui modelli 5.5 e Fable 5.1 il ragionamento non si spegne, si regola con l'effort.
8. Nei messaggi con documenti lunghi: documenti in alto, domanda in fondo; con testi lunghi chiedi prima le citazioni pertinenti.
9. Lavoro collegato in una sola attività, non in tante; di' a Claude quando basta una risposta breve senza file.
10. Quando i consumi salgono senza motivo: Settings > Usage, e controlla connettori, effort e lunghezza della chat.

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato, un passo per riga e i nomi esatti dei pulsanti. Spiega il perché in una frase sola: a ogni domanda Claude rilegge tutta la conversazione. I nomi qui sono quelli inglesi delle pagine d'aiuto: nell'app in italiano possono essere tradotti.

Elenco tipo, da adattare al caso:
1. Apri una chat nuova nello stesso Project: barra laterale > il Project > campo della chat nuova.
2. Come primo messaggio scrivi tre righe: dove eri arrivato, cosa hai deciso, cosa resta da fare.
3. Spegni gli strumenti che non servono: «+» sotto il campo di scrittura > «Connectors» > interruttore del connettore.
4. Se hai 10 o più connettori: «+» > «Connectors» > «Tool access» > «On demand».
5. Per i compiti di routine: clic sul nome del modello accanto al pulsante di invio > «Effort» > un livello più basso.
6. Se non ti servono notizie aggiornate, scrivi nel messaggio «non cercare sul web».
7. Togli dal Project i file che non usi più e accorcia le Istruzioni del Project.
8. Controlla i consumi: Settings > Usage («Current session» e limite settimanale).

## Cosa non sappiamo
- L'elenco ufficiale completo di cosa entra nel contesto di una chat: in particolare memoria, stili e descrizioni delle skill.
- La soglia della sintesi automatica, cosa conserva il riassunto e se valga nelle attività programmate.
- Quanto pesano in token connettori, ricerca web e ragionamento.
- Se più attività in parallelo o i sottoagenti consumino in proporzione.
- Se l'indicatore del contesto di Claude Desktop (scheda «Context») sia visibile in ogni conversazione.
- Misure di degrado sui modelli 5.x.

## Prove
Regole numerate con fonti, conflitti e verifiche mancanti: `D:\Workspace\best_practice\3_contesto\rapporto_contesto.md`, sezioni «Regole operative», «C. Sintesi automatica nell'app», «Tabella conflitti» e «Cosa non è stato verificato».
