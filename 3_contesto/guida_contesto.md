---
tema: contesto di Claude (finestra, cosa la riempie, degrado, compattazione, chat e sessioni lunghe) in app, Claude Code e API
per: Claude (chat, Cowork, Code) quando aiuta l'utente su questo tema
aggiornata_il: 2026-10-27
prove: D:\Workspace\best_practice\3_contesto\rapporto_contesto.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes su contesto, compaction o limiti; oppure 2026-12-18"
---

# Guida 3 · Contesto

Per Claude. Usa questa guida quando l'utente chiede perché una chat lunga peggiora o costa di più, quando aprire una chat nuova, come usare `/clear`, `/compact` e simili, o quanto testo «regge» Claude. Vale al 27 ottobre 2026: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici.

## Quando usarla
- «La chat è diventata lenta o sbaglia», «consumo troppo», «devo ricominciare da capo?».
- Prima di un lavoro lungo in Code o di caricare molti documenti in un Project.

## Cosa è vero oggi
- Il contesto è tutto ciò che Claude ha davanti in una richiesta: istruzioni, strumenti, file, cronologia, risposta. I quattro modelli correnti (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5) hanno 1 milione di token, circa 555.000 parole; Haiku 5.5 in Cowork ne ha 500.000.
- Più contesto non vuol dire risposte migliori: con molti token precisione e richiamo calano («context rot»).
- Ogni messaggio rimanda a Claude tutta la conversazione: una chat lunga costa di più a ogni domanda, anche breve.
- Quando la finestra si riempie, l'app (solo piani a pagamento con esecuzione di codice attiva), Code (verso circa 967.000 token, o a mano con `/compact`) e l'API riassumono la parte vecchia. Il riassunto perde dettagli e può perdere le istruzioni date all'inizio della chat.
- In Code il `CLAUDE.md` della radice e le regole senza `paths` si ricaricano dal disco dopo la compattazione; quello che hai detto solo in chat no.
- In Code con abbonamento la cache dura circa un'ora; dopo una pausa più lunga la richiesta seguente rilegge tutto a prezzo pieno.

## Regole da applicare
1. Un argomento per chat; tra lavori diversi chat nuova (app) o `/clear` (Code, gratis).
2. Le regole che devono durare vanno nelle Istruzioni del Project o nel `CLAUDE.md`, non nei messaggi.
3. Prima di un compito lungo in Code: `/compact` con un fuoco esplicito («tieni le modifiche ai file e i comandi di test»).
4. Per abbandonare una strada sbagliata: `/rewind` (o due volte Esc), non `/compact`.
5. Dopo due correzioni fallite sulla stessa cosa: `/clear` e un messaggio nuovo con ciò che si è capito.
6. Modello ed effort si scelgono all'inizio: cambiarli a metà rilegge la cronologia senza cache.
7. Procedure lunghe in una skill, non nel `CLAUDE.md`: dopo la compattazione le skill tornano troncate, con l'inizio del file.
8. I sottoagenti servono per lavoro parallelo o output rumorosi, non «per proteggere il contesto»: costano token propri.
9. Nell'app: ricerca web, connettori e ragionamento esteso accesi solo quando servono; le cose importanti all'inizio o alla fine del messaggio.
10. Quando i consumi salgono senza motivo, in Code `/context` (cosa occupa spazio) e `/usage` (cosa consuma).

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato di cose da fare, una per riga, ognuna con il comando o il clic esatto. Spiega il perché in una frase sola: ogni messaggio rimanda tutta la conversazione.

Elenco tipo, da adattare al caso:
1. Se hai cambiato argomento, apri una chat nuova nello stesso Project (in Code scrivi `/clear`).
2. Nella chat nuova scrivi in tre righe dove eri arrivato e cosa resta da fare.
3. Le regole che vuoi sempre valide spostale nelle Istruzioni del Project, o nel `CLAUDE.md` per Code.
4. Togli dal Project i documenti che non servono più.
5. Spegni ricerca web e connettori quando non servono.
6. In Code, prima di un lavoro lungo, scrivi `/compact` seguito da cosa tenere.
7. Se i consumi salgono, in Code scrivi `/context` e `/usage` e guarda cosa pesa di più.

## Cosa non sappiamo
- L'elenco ufficiale di cosa entra nel contesto di una chat dell'app (memoria, profilo, stili, allegati).
- La soglia esatta della sintesi automatica nell'app.
- Misure di degrado sui modelli 5.x: gli studi arrivano a Opus 4.6.

## Prove
Regole numerate, tabella dei modelli, conflitti e studi: `D:\Workspace\best_practice\3_contesto\rapporto_contesto.md`.
