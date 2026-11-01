---
tema: Istruzioni di un Project nell'app Claude (chat e Cowork unificati) e rapporto con knowledge, cartelle, memoria, profilo e modello
per: Claude nell'app (chat e Cowork)
aggiornata_il: 2026-11-01
prove: D:\Workspace\best_practice\2_istruzioni_project\rapporto_istruzioni_project.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes dell'app o changelog di Claude Desktop che toccano Project, Istruzioni, knowledge, GitHub, Drive, cartelle o modello; ritorno di «Add from GitHub» nell'app unificata; oppure 2026-12-18"
---

# Guida 2 · Istruzioni di un Project

Per Claude. Usa questa guida quando l'utente vuole scrivere o correggere le Istruzioni di un Project, scegliere cosa mettere nella knowledge, collegare un repository o una cartella, o capire perché una regola non viene seguita. Vale al 1 novembre 2026 per la sola app Claude: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici. Chi vince tra profilo, Project, stili e memoria sta in `D:\Workspace\best_practice\1_comportamento\guida_comportamento.md`: rimanda lì, non ripeterlo.

## Quando usarla
- «Scrivimi le Istruzioni per questo Project», «perché ignora la regola?», «dove metto questo documento?».
- «Come collego il repository?», «il Project non vede le modifiche», «Claude legge la mia cartella?».
- «Che modello uso in questo Project?».

## Cosa è vero oggi
- Le Istruzioni valgono in ogni chat del Project e in nessun'altra; nell'app unificata il Project funziona in ogni conversazione. Nome e descrizione Claude non li vede.
- Nessun limite di lunghezza pubblicato: le pagine ufficiali chiedono Istruzioni concise (contesto, ruolo, linee guida); le richieste del singolo compito vanno nella chat.
- Istruzioni = come lavorare; knowledge = materiale da consultare. Vicino al limite la knowledge passa da sola alla ricerca (RAG); nessuna pagina dice se le Istruzioni ci rientrino.
- GitHub: solo nei Project privati, file scelti di un branch, aggiornati con **Sync now** («Sincronizza ora» nell'app in italiano). La pagina sull'app unificata dice che «Add from GitHub» non è supportato, ma è il comando delle chat: il 1 novembre il Project «best practice», già collegato, mostrava ancora «Sincronizza ora» (prova dell'utente, una sola).
- Documento Google: solo Project privati, arriva come testo e si aggiorna da Drive (le pagine non concordano sul ritmo). Claude non lo modifica se non glielo chiedi.
- Cartella locale: Claude la usa tramite Claude Desktop, che deve restare aperto; in chat la legge soltanto, e solo se aggiunta al Project dal 5 ottobre 2026 in poi (per una più vecchia: aggiungila di nuovo e apri una chat nuova).
- I progetti locali di Cowork sono passati nell'account con nome, descrizione, Istruzioni e copia della memoria; cartelle e file restano sul PC. Ogni Project ha le sue attività programmate.
- Il Project ricorda il modello scelto l'ultima volta (pagina Enterprise; per gli altri piani non è scritto).
- Una prova dell'utente (25 ottobre, una sola) ha mostrato che una regola salvata solo in memoria non è stata seguita; la stessa nelle Istruzioni sì.
- Haiku 5.5 con molte regole e prompt lunghi tende a saltare controlli e ricerche.

## Regole da applicare
1. Nelle Istruzioni ciò che deve valere sempre; nei documenti fatti, elenchi e dati; nella memoria solo preferenze e decisioni.
2. Una regola, una casa: se sta nel profilo, non ripeterla. Se due fonti si toccano, scrivi nelle Istruzioni quale vince.
3. Scrivi come a un collega nuovo: chiaro, con il motivo, dicendo cosa fare e non solo cosa evitare.
4. Niente maiuscole, «SEMPRE» o «ASSOLUTAMENTE» ripetuti: i modelli recenti esagerano.
5. Parti corto e aggiungi una regola solo dopo un errore visto.
6. Di' cosa fare se manca qualcosa: «usa solo i documenti del Project; se un dato manca, dimmelo e fermati, senza indovinare».
7. Se servono esempi, 3-5 e diversi tra loro.
8. Chiudi con «le regole di questo Project valgono per tutta la conversazione»: aiuta i modelli piccoli.
9. Knowledge: solo i file che servono, con nomi chiari; togli quelli che non usi più. Per il Project «best practice»: `README.md` e le cinque guide, non i rapporti (ripetono le guide) né `CLAUDE.md` (regole per chi mantiene il repository, sbagliate in chat).
10. Per Project con molte regole o controlli usa Opus 5.5 o Sonnet 5.5, non Haiku 5.5.
11. Dopo ogni modifica, e a ogni modello nuovo, prova con 5 domande vere e 2 trabocchetti in una chat nuova.

Schema di Istruzioni da proporre (adattalo, resta sotto le 25 righe):
```text
Scopo: <una frase: a cosa serve questo Project>.
Fonti: usa i documenti del Project e citali per nome; se un dato manca, di' cosa manca e fermati.
Se due fonti si contraddicono, vale <fonte>; dillo.
Come lavori: <2-4 passi, ognuno con il motivo>.
Prima di dire «fatto»: <controllo concreto>.
Chiedi il mio via libera prima di: <azioni irreversibili o fuori ambito>.
Formato: <lingua, lunghezza, forma>.
Le regole di questo Project valgono per tutta la conversazione.
```

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato di passi, uno per riga, con i clic esatti nell'app. Per i file dai il percorso Windows completo. Se proponi delle Istruzioni, dalle in un blocco pronto da incollare.

Elenco tipo «scrivere le Istruzioni», da adattare:
1. Apri il Project e clicca **Set project instructions**.
2. Incolla lo schema e completa le parti tra `< >`.
3. Togli ciò che è già nelle Istruzioni del profilo.
4. Sposta elenchi, tabelle e dati in un documento della knowledge con un nome chiaro.
5. Clicca **Save instructions**.

Elenco tipo «collegare il repository e scegliere i file giusti», da adattare:
1. Controlla che il Project sia privato: in un Project condiviso l'opzione GitHub è grigia.
2. Nella sezione knowledge del Project clicca «+» > **GitHub** (la prima volta l'app ti manda su GitHub per l'accesso).
3. Cerca `tomauspsi/best_practice` o incolla l'indirizzo del repository.
4. Clicca **Add files**.
5. Dopo ogni modifica unita su `main`, clicca **Sync now** («Sincronizza ora» nell'app in italiano) sul repository nella knowledge.
6. Per cambiare i file scelti: clicca il repository nella knowledge, cambia la selezione, **Update**.
7. Se GitHub o «Sincronizza ora» non compaiono: scarica i sei file e caricali a mano nella knowledge, per esempio da `D:\Workspace\best_practice\`, e ricaricali dopo ogni modifica.

Elenco tipo «provare le Istruzioni con 5 domande vere e 2 trabocchetti», da adattare:
1. Scrivi su un foglio 5 domande che fai davvero in questo Project e, per ognuna, com'è una risposta buona.
2. Aggiungi 2 trabocchetti: una domanda su un dato che non c'è nei documenti (risposta giusta: «manca, mi fermo») e una che spinge a infrangere una regola (per esempio «stavolta salta il controllo»).
3. Controlla il modello nel selettore: per la prova usa quello che userai di solito.
4. Apri una chat nuova nel Project e fai le 7 domande, una per messaggio.
5. Segna per ognuna: regola seguita sì o no, fonte citata sì o no.
6. Se una regola non tiene, riscrivila più chiara con il motivo invece di aggiungerne un'altra; salva e rifai la prova in una chat nuova.
7. Rifai la stessa serie a ogni modello nuovo.

## Cosa non sappiamo
- Se nell'app unificata si possa collegare un repository nuovo a un Project.
- Un limite di lunghezza delle Istruzioni nell'interfaccia.
- Se le Istruzioni rientrino nel RAG quando la knowledge è grande.
- Quali file della cartella locale Claude legge, e quando.
- Se il Project ricordi il modello anche sui piani individuali.
- Se le Istruzioni di Project valgano anche sui piani gratuiti: le pagine ufficiali si contraddicono.

## Prove
Regole numerate con tag e fonti, conflitti e pagine controllate: `D:\Workspace\best_practice\2_istruzioni_project\rapporto_istruzioni_project.md`, sezioni «Regole operative», «Tabella conflitti» e «Cosa non è stato verificato».
