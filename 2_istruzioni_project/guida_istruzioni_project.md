---
tema: Istruzioni di un Project dell'app Claude (chat e Cowork) e rapporto con knowledge, memoria e profilo
per: Claude (chat, Cowork, Code) quando aiuta l'utente su questo tema
aggiornata_il: 2026-10-27
prove: D:\Workspace\best_practice\2_istruzioni_project\rapporto_istruzioni_project.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes dell'app o dei Project; oppure 2026-12-18"
---

# Guida 2 · Istruzioni di un Project

Per Claude. Usa questa guida quando l'utente vuole scrivere o correggere le Istruzioni di un Project, decidere cosa mettere nella knowledge, o capire perché una regola non viene seguita. Vale al 27 ottobre 2026: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici.

## Quando usarla
- «Scrivimi le istruzioni per questo Project», «perché ignora la regola?», «dove metto questo documento?».
- Quando l'utente vuole che una regola valga in tutte le chat di un lavoro.

## Cosa è vero oggi
- Le Istruzioni valgono per tutte le chat di quel Project e per nessun'altra. Il nome e la descrizione del Project Claude non li vede.
- Istruzioni = come comportarsi; knowledge = materiale da consultare. Vicino al limite la knowledge passa in modalità di ricerca (RAG) da sola.
- Nessuna pagina ufficiale dice chi vince tra Istruzioni del Project, istruzioni del profilo, memoria e stili.
- Una prova dell'utente (25 ottobre, una sola) ha mostrato che una regola salvata solo nella memoria non è stata seguita; la stessa nelle Istruzioni sì.
- Nessun limite ufficiale di lunghezza per i Project dell'app; 16.000 caratteri valgono solo per i Projects di Claude Code.
- Documenti collegati: un documento Google si aggiorna da solo (Project privati), ma Claude non lo scrive se non gli viene chiesto. Un repository GitHub si aggiorna solo con il comando di sincronizzazione; nella nuova esperienza unificata di chat e Cowork «aggiungi da GitHub» non è supportato, quindi i file si caricano a mano.
- Le Istruzioni di un Project dell'app non arrivano a Claude Code.
- Haiku 5.5 con molte regole tende a saltare passi: per ricerche e controlli serve un modello più forte.

## Regole da applicare
1. Nelle Istruzioni va ciò che deve valere sempre; nei documenti fatti, elenchi e dati; nella memoria solo preferenze e decisioni.
2. Una regola, una casa: se sta già nel profilo, non ripeterla nel Project. Se due fonti si sovrappongono, scrivi nelle Istruzioni quale vince.
3. Scrivi come a un collega nuovo: chiaro, con il motivo, dicendo cosa fare e non solo cosa evitare.
4. Niente «SEMPRE» o «ASSOLUTAMENTE» ripetuti: i modelli recenti esagerano.
5. Parti corto e aggiungi una regola solo dopo un errore visto.
6. Di' cosa fare se manca qualcosa: «dimmi cosa manca e fermati, senza indovinare».
7. Se servono esempi, 3-5 e diversi tra loro.
8. Chiudi con «le regole di questo Project valgono per tutta la conversazione»: aiuta i modelli piccoli.
9. Dopo ogni modifica, e a ogni modello nuovo, prova con 5-6 domande vere e 2-3 trabocchetti.

Schema di Istruzioni da proporre (adattalo, resta sotto le 25 righe):
```text
Scopo: <una frase: a cosa serve questo Project>.
Fonti: i fatti stanno nei documenti del Project; se un dato manca, di' cosa manca e fermati.
Se due fonti si contraddicono, vale <fonte>; dillo.
Come lavori: <2-4 passi, ognuno con il motivo>.
Prima di dire «fatto»: <controllo concreto>.
Chiedi il mio via libera prima di: <azioni irreversibili o fuori ambito>.
Formato: <lingua, lunghezza, forma>.
Le regole di questo Project valgono per tutta la conversazione.
```

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato di cose da fare, una per riga, con un esempio. Indica sempre dove cliccare nell'app e, per i file, il percorso Windows completo. Se proponi delle Istruzioni, dalle in un blocco pronto da incollare.

Elenco tipo, da adattare al caso:
1. Apri il Project nell'app e clicca il pulsante delle Istruzioni del Project.
2. Incolla lo schema che ti propongo e completa le parti tra `< >`.
3. Togli dalle Istruzioni ciò che è già nelle istruzioni del profilo.
4. Sposta elenchi, tabelle e dati in un documento della knowledge, con un nome chiaro.
5. Apri una chat nuova nel Project e fai 5 domande vere e 2 a trabocchetto.
6. Se una regola non viene seguita, riscrivila più chiara con il motivo, invece di aggiungerne un'altra.

## Cosa non sappiamo
- In quale pannello stia esattamente l'icona di sincronizzazione di GitHub: la pagina ufficiale non lo dice.
- Se le Istruzioni rientrino nel RAG quando la knowledge è grande.
- Chi vince tra profilo, Project, memoria e stili.

## Prove
Regole numerate, conflitti tra pagine ufficiali, studi sull'aderenza: `D:\Workspace\best_practice\2_istruzioni_project\rapporto_istruzioni_project.md`.
