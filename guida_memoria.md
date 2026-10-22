# Memoria di Claude: guida semplice

Valida al 19 ottobre 2026. Da rivedere quando esce un nuovo modello di Claude o quando le novità ufficiali toccano la memoria.  
Le prove, le fonti e il dettaglio tecnico, per gli agenti, stanno in `ricerche`. Questo file è per te.

## In una frase

Non esiste una memoria unica di Claude. Esistono più "quaderni" separati, e ogni strumento legge solo i suoi. Un file che vuoi far leggere a tutti deve stare in un posto che tutti sanno raggiungere, e va richiamato, non copiato.

## I quaderni che esistono davvero

| Quaderno | Cosa contiene | Chi lo scrive | Dove vive | Chi lo legge |
|---|---|---|---|---|
| Memoria della chat | Le tue preferenze e i fatti emersi parlando | Claude, mentre chatti | Nel tuo account claude.ai, uno per ogni Project più uno generale | Le chat dell'app (e Cowork, quando lavora nel cloud) |
| Cerca nelle chat passate | Richiama conversazioni vecchie su richiesta | Nessuno: cerca nelle chat | Account | Le chat, ma mai da un Project a un altro |
| Istruzioni del profilo | Come vuoi che Claude si comporti sempre | Tu | Impostazioni di claude.ai | Tutte le chat dell'app |
| Istruzioni di un Project | Come comportarsi solo in quel lavoro | Tu | Il Project | Le chat di quel Project |
| Conoscenza di un Project | File che carichi o che colleghi (da GitHub o Drive) | Tu | Il Project | Le chat di quel Project |
| `CLAUDE.md` | Le regole di un progetto di codice o di ricerca | Tu | Una cartella del PC, o il repo su GitHub | Claude Code |
| Memoria automatica di Code | Appunti che Claude Code scrive da solo | Claude Code | `C:\Users\Tommi\.claude\projects\` sul tuo PC | Claude Code sul PC |
| Memoria di un Project di Code | Appunti del lavoro di un Project di Claude Code (ancora in prova) | Claude Code | Nel Project, nel cloud | I thread cloud di quel Project |

La memoria della chat è poca per scelta: Claude non salva da solo i temi sensibili (salute, religione, politica) e non salva mai documenti d'identità o conti. La vedi e la modifichi in Impostazioni > Memoria.

## Cosa NON si parlano

- La memoria della chat non arriva a Claude Code. Nessuna pagina ufficiale dice il contrario, e una prova fatta da dentro una sessione cloud non ha mostrato nulla del tuo account.
- La memoria automatica di Code resta sul tuo PC: il cloud e le routine non la vedono.
- `C:\Users\Tommi\.claude\CLAUDE.md` lo legge solo Code sul tuo PC. Una routine nel cloud parte da una copia pulita del repo e vede solo ciò che sta nel repo.
- La chat dell'app non legge i tuoi `CLAUDE.md`.

Quindi sì: ogni strumento è in gran parte un silo. Di comune c'è una sola cosa: i file che tu metti nel posto giusto.

## Un documento Google per la memoria della chat: ha senso?

Sì. È la strada più pratica se vuoi una memoria tra le chat di un Project senza usare Code e senza copia e incolla.

Cosa dicono le pagine ufficiali:
- **La chat può modificare un documento Google già esistente.** Si incolla il link del documento in chat e Claude lo modifica dal vivo in un pannello accanto alla conversazione. Servono i connettori Docs, Sheets e Slides attivi. Funziona su Claude sul web (in Chrome) e su Claude Desktop con il browser integrato attivo.
- **I permessi sono i tuoi.** Claude può aprire e cambiare solo i file a cui accede il tuo account Google. Non devi condividere il file con nessuno: se resta privato, lo vedete solo tu e Claude, mentre lavori.
- **Un Project lo legge.** Un documento Google aggiunto alla conoscenza di un Project si rilegge da Drive ogni tanto, quando apri il Project. Funziona solo nei Project privati, non in quelli condivisi.
- **Claude può anche creare file nuovi su Drive.** Se chiedi "un Google doc" per nome, lo crea come documento Google; se chiedi un documento generico, lo crea come file locale.

Come usarlo:
1. Crea un documento Google privato, per esempio `passaggio`.
2. Aggiungilo alla conoscenza di un Project privato.
3. A fine lavoro, in chat, scrivi: «aggiorna il documento passaggio con le decisioni di oggi», incollando il link.
4. Nella chat successiva dello stesso Project, il documento è già lì.

Limiti:
- **Non è automatico.** Claude lo aggiorna solo quando glielo chiedi, in quella chat.
- **Il Project lo rilegge ogni tanto,** non subito.
- **Va richiamato.** Meglio scrivere nelle istruzioni del Project: «all'inizio leggi il documento passaggio».
- **Questo punto va provato da te.** Le pagine ufficiali non sono del tutto concordi su un dettaglio (se la modifica dal pannello sia "in prova" o no), e non l'ho potuto provare. La prova è in fondo, in "Cosa non sappiamo ancora".
- **Attenzione alle attività programmate.** Partono con tutti i connettori del tuo account e, secondo la guida ufficiale, usano anche gli strumenti di scrittura senza chiedere. Se Drive è collegato, una routine potrebbe modificare i tuoi documenti. Il divieto va scritto in ogni prompt, oppure si toglie il connettore dall'attività.
- **Dati personali:** il documento è tuo e privato, ma sta su Google. Tieni dentro solo ciò che accetti di avere lì.

Due posti, due scopi, nessun testo in doppia copia:
- **Documento Google:** memoria per le chat di un Project.
- **Repo `D:\Workspace\best_practice`:** regole e ricerche per gli agenti, cioè Claude Code. Ha la storia delle modifiche e lo leggono anche le routine nel cloud.

## La chat può scrivere nei file del repo?

No. Il collegamento tra la chat (o un Project) e un repo GitHub è solo di lettura: Claude legge i nomi e il contenuto dei file, non vede cronologia, pull request né issue. Per modificare file e aprire pull request serve Claude Code.

Conseguenza pratica, se non vuoi usare Code né fare copia e incolla:
- La memoria tra le chat di uno stesso Project esiste già, e si aggiorna da sola: è la memoria del Project. Parti da lì, e aggiungi un documento Google solo se ti serve più controllo.
- Un file nel repo collegato al Project serve solo se qualcuno lo aggiorna: tu, oppure Claude Code.
- Un documento Google su Drive, invece, la chat lo può anche modificare (vedi la sezione sopra). Per la memoria della chat è la strada più comoda.

Una prova semplice, in un Project privato: scrivi «Ricorda per questo Project: rispondi sempre in italiano e parti dalla conclusione». Poi apri una chat nuova nello stesso Project e guarda se la regola viene seguita, e se compare la voce in Impostazioni > Memoria.

## Dove mettere cosa

| Cosa | Dove | Chi lo vede |
|---|---|---|
| Regole di un progetto | `CLAUDE.md` nella cartella del progetto, poi sul repo | Code sul PC, Code nel cloud, routine |
| Regole su un tipo di file o una sottocartella | File separati in `.claude\rules\` del repo | Come sopra, solo quando servono |
| Le tue preferenze personali, solo per Code | `C:\Users\Tommi\.claude\CLAUDE.md` | Code sul PC |
| Come vuoi che Claude si comporti in ogni chat | Istruzioni del profilo in claude.ai | Le chat dell'app |
| Come comportarsi in un lavoro di chat | Istruzioni del Project | Le chat di quel Project |
| Conoscenza valida per qualsiasi strumento | Un file neutro nel repo, per esempio `D:\Workspace\best_practice\ricerche\memoria.md` | Tutti, se richiamato |
| Memoria tra le chat di un Project, sotto il tuo controllo | Un documento Google privato, collegato al Project | Le chat di quel Project |
| Cosa deve sapere una routine | Nel prompt della routine e nel repo | La routine |
| Stato di un lavoro tra una sessione e l'altra | Un file di appunti nel repo, aggiornato a fine lavoro | La sessione successiva |

## Una sola casa per ogni informazione

Se la stessa regola sta in tre posti, prima o poi una sola viene corretta. Claude Code, con due regole opposte, ne segue una a caso. Perciò: la regola vive in un posto, gli altri la richiamano.

## `CLAUDE.md` o `AGENTS.md`?

- `CLAUDE.md` lo legge Claude Code.
- `AGENTS.md` è un foglio di istruzioni letto da molti strumenti (Cursor, Codex, Copilot). Serve solo se usi più di uno strumento sullo stesso repo.
- Se esiste solo `AGENTS.md`, Claude Code lo legge. Se esistono tutti e due, legge solo `CLAUDE.md`: scrivi allora dentro `CLAUDE.md` la riga `@AGENTS.md`, che significa "includi qui quel file". La regola vive in `AGENTS.md`, e `CLAUDE.md` la richiama.

## I tre `CLAUDE.md`

- Nel repo su GitHub, per esempio `D:\Workspace\best_practice\CLAUDE.md` dopo il push: lo legge Code sul PC, Code nel cloud e le routine.
- Dentro la cartella di un progetto: è lo stesso file finché non lo mandi su GitHub. Se resta solo sul PC, il cloud non lo vede.
- Nella cartella utente, `C:\Users\Tommi\.claude\CLAUDE.md`: solo Code sul tuo PC, in tutti i progetti.

Tienili brevi: più sono lunghi, meno Claude li segue. Ciò che vale solo per una cartella va in un file a parte.

## Cose da ricordare

- La memoria è un promemoria, non un divieto. Per vietare qualcosa a Claude Code servono gli "hook", cioè controlli automatici.
- Non far scrivere in memoria testo preso da pagine web senza rileggerlo: dei testi avvelenati possono finire nella memoria di un agente. Le ricerche lo mostrano su altri modelli, non su Claude, ma il rischio vale per qualsiasi agente.
- Dati sensibili: non metterli nella memoria della chat né nei file del repo. Cancellare una chat non cancella le memorie che ne sono derivate.
- Le chat molto lunghe peggiorano: Claude riassume i messaggi vecchi e perde dettagli. Meglio aprire una chat nuova dentro lo stesso Project e passargli un breve riassunto del punto a cui eri arrivato.
- Un Project della chat collegato a GitHub non si aggiorna da solo: premi "Sync now" dopo ogni modifica. E il collegamento è solo di lettura.

## Cosa non sappiamo ancora

- Se una routine creata da un Project legga la memoria di quel Project: le guide dicono che parte come un thread del Project, ma non lo scrivono.
- Se la modifica di un documento Google dalla chat funzioni davvero nel tuo caso: le pagine ufficiali la descrivono, ma una di esse la chiama "in prova" e un'altra no. Prova: crea un documento privato `passaggio` con tre righe, aggiungilo a un Project privato, incolla il link in chat e scrivi «aggiungi in fondo questa decisione: usiamo il metodo X». Guarda se la modifica compare nel pannello. Poi apri una chat nuova nello stesso Project e chiedi «cosa c'è scritto in passaggio?».
- Come funziona la memoria di ChatGPT in dettaglio: le pagine ufficiali non erano leggibili.
- Se Cursor abbia davvero tolto la sua funzione Memories: lo dice solo un forum.

## Per cominciare, in ordine

1. Tieni il testo vero nel repo, in file brevi e neutri.
2. Metti nel `CLAUDE.md` del repo le regole per gli agenti, e richiama i file lunghi invece di copiarli.
3. Nel Project della chat, scrivi poche istruzioni di comportamento e lascia lavorare la memoria del Project.
4. Se ti serve più controllo, aggiungi al Project un documento Google privato come memoria, e chiedi a Claude di aggiornarlo a fine lavoro. Per i file di riferimento che non cambiano, puoi invece collegare il repo (sola lettura) e premere "Sync now" a ogni novità.
5. Controlla ogni tanto cosa ha salvato Claude da solo, in Impostazioni > Memoria e nella cartella `C:\Users\Tommi\.claude\projects\`, e cancella ciò che è sbagliato o vecchio.

## Dove controllare

- [Memoria e ricerca nelle chat](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- [Come Claude Code ricorda un progetto](https://code.claude.com/docs/en/memory)
- [Cosa vede una sessione cloud](https://code.claude.com/docs/en/cloud-environments)
- [Connettori Google](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Project di chat](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
