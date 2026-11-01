---
tema: contesto di Claude nell'app (chat e Cowork unificati, Project): finestra, cosa la riempie, degrado, sintesi automatica, chat lunghe
versione: 2
base: c9cc04b
verificato_il: 2026-11-01
aggiornato_il: 2026-11-01 (run 3: perimetro ridotto alla sola app; tolti Claude Code e API; ogni fatto riletto sulla pagina del giorno)
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes dell'app o changelog di Claude Desktop che toccano contesto, sintesi automatica, connettori, effort o limiti; oppure 2026-12-18"
versioni_rilevate:
  modelli_app: "Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5: 1M in chat; in Cowork Haiku 5.5 500K (help 8606394)"
  app_claude: "senza numero di versione; release notes dell'app: ultima voce 2026-10-21 (Duet); app unificata chat e Cowork: 2026-09-16"
  claude_desktop: "v4.4212.0 del 2026-10-29 (changelog di Cowork, letti 200.000 di 245.508 caratteri)"
  opus_5_6: "non uscito al 2026-11-01 (release notes dell'app)"
---

# Contesto di Claude nell'app: stato al 1 novembre 2026 (v2)

v2 sostituisce v1 (27 ottobre), che copriva anche Claude Code e l'API. La storia sta nei commit. Le pagine di support.claude.com arrivano dallo strumento come riassunto: qui sono parafrasi, senza virgolette, salvo i nomi di menu e pulsanti. Fatti vicini già verificati altrove: Istruzioni del profilo, stili e skill in `D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md`; Istruzioni del Project in `D:\Workspace\best_practice\2_istruzioni_project\rapporto_istruzioni_project.md`; memoria tra chat in `D:\Workspace\best_practice\4_memoria\rapporto_memoria.md`; attività programmate e costi in `D:\Workspace\best_practice\5_attivita\rapporto_attivita.md`.

## Risposta breve
- Il contesto è tutto ciò che Claude ha davanti quando risponde. Nell'app i quattro modelli correnti hanno 1M token; in Cowork Haiku 5.5 ne ha 500K.
- Più contesto non vuol dire risposte migliori: con più token calano accuratezza e richiamo («context rot»).
- Una chat lunga consuma più limite d'uso a ogni domanda; quella che fa scattare la sintesi automatica ancora di più.
- La sintesi automatica c'è solo sui piani a pagamento con esecuzione di codice attiva; la cronologia resta; nessuna soglia pubblicata.
- Le mosse che rendono di più, tutte nell'app: una chat per argomento, Project con Istruzioni brevi e solo i file utili, connettori spenti o «On demand», effort più basso per la routine, Settings > Usage per controllare.

## Regole operative
1. Spiega la finestra per modello: in chat 1M per Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Haiku 5.5; 500K per Fable 5, Opus 4.8, 4.7, 4.6 e Sonnet 4.6; 200K per gli altri. In Cowork 1M per la maggior parte dei modelli correnti, Haiku 5.5 500K, Opus 4.6, Sonnet 4.6 e Haiku 4.5 200K. Una parte della finestra è sempre riservata alla risposta. [Verificato] · T1 · <https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
2. Di' cosa entra nel contesto solo nei limiti di ciò che le pagine dicono: le Istruzioni del profilo valgono in tutte le conversazioni; le Istruzioni del Project nelle chat del Project; la knowledge del Project entra intera finché sta nella finestra, poi con il RAG solo la parte pertinente; le skill entrano quando servono (progressive disclosure, richiedono l'esecuzione di codice); strumenti e connettori pesano molto; le chat passate entrano solo quando Claude le cerca, con una chiamata visibile. Nessuna pagina dice se memoria, stili e descrizioni delle skill siano sempre presenti. [Verificato] le singole voci · [Inferenza] il quadro d'insieme · T1 · <https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features>; <https://support.claude.com/en/articles/12512176-what-are-skills>; <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>; <https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans>
3. Non riempire il contesto solo perché c'è spazio: «As token count grows, accuracy and recall degrade»; conta scegliere cosa mettere quanto lo spazio. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/context-windows>
4. Spiega il costo delle chat lunghe: a ogni turno il modello riceve tutta la cronologia più il messaggio nuovo; nell'app le conversazioni più lunghe e complesse usano più limite, e quelle che fanno scattare la sintesi automatica ancora di più. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/context-windows>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
5. Sulla sintesi automatica non promettere più di quanto c'è: solo piani a pagamento con esecuzione di codice attiva; vicino al limite Claude riassume i messaggi vecchi; la cronologia completa resta e Claude può riferirvisi; il segnale è «organizing its thoughts»; casi rari (primo messaggio enorme, errori) arrivano comunque al limite. Nessuna soglia generale; in Cowork Sonnet 5 compatta a 500K. [Verificato] · T1 · <https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
6. Apri una chat nuova per un lavoro non collegato e quando una chat lunga si avvicina al limite d'uso; nell'app unificata non si può ramificare una conversazione da un punto precedente, quindi il filo si porta a mano con poche righe su dove eri. Nessuna pagina ufficiale dell'app descrive un «documento di passaggio». [Verificato] le prime due parti · [Inferenza] le righe di passaggio · T1 · <https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>; <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>
7. Nei Project lascia lavorare il RAG: parte da solo quando la knowledge si avvicina al limite, porta la capacità fino a 10 volte, non si attiva a mano, torna all'elaborazione in contesto se la knowledge scende; si riconosce da un indicatore e dallo strumento di ricerca nella knowledge. Piani Pro, Max, Ultra, Team, Enterprise. [Verificato] · T1 · <https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects>
8. Tieni brevi le Istruzioni del Project (contesto generale, linee guida, ruolo di Claude; le istruzioni di un compito vanno nella chat) e togli ogni tanto i file del Project che non usi più. [Verificato] · T1 · <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
9. Usa il Project per i documenti che richiami spesso: i documenti caricati vanno in cache e pesano meno quando li riusi; la cache scade dopo un periodo di inattività e il primo messaggio dopo una pausa lunga conta di nuovo tutto. [Verificato] · T1 · <https://support.claude.com/en/articles/9797557-usage-limit-best-practices>
10. Scegli tra allegato e knowledge: in chat fino a 20 file da 500 MB ciascuno, PDF fino a 1.000 pagine (grafici e immagini letti fino a 100 pagine); nel Project file da 30 MB, numero illimitato, solo testo estratto salvo i PDF multimodali, pensati come riferimento per più chat. [Verificato] · T1 · <https://support.claude.com/en/articles/8241126-upload-files-to-claude>
11. Spegni i connettori che non servono dal menu della chat («+» > «Connectors», interruttore); con 10 o più connettori passa «Tool access» da «Auto» (predefinito) a «On demand» per lasciare più spazio alla conversazione. Nessuna pagina dà il peso in token di un connettore. [Verificato] · T1 · <https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
12. Per la ricerca web chiedi a Claude di non cercare quando non servono notizie aggiornate: nell'app unificata non c'è un interruttore dedicato e Claude cerca quando lo ritiene utile; la ricerca approfondita si apre con «+» > «Research» o `/deep-research`. [Verificato] · T1 · <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
13. Abbassa l'effort per i compiti di routine: si cambia dal nome del modello accanto al pulsante di invio > «Effort» (low, medium, high, xhigh da Opus 4.7, max); l'effort alto usa più token e porta prima al limite; ogni modifica vale dalla risposta seguente. Su Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1 e Opus 5 il ragionamento non si spegne. [Verificato] · T1 · <https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
14. Metti in conto il lavoro agentico: tutto conta sui limiti del piano; si possono avere più attività insieme e per lavori complessi Claude coordina più sottoagenti; le attività con più passi (codice, file, connettori, browser) consumano più di una domanda; raggruppa il lavoro collegato in una sola attività e controlla Settings > Usage. Nessuna pagina dice se il consumo cresca in proporzione al numero di attività. [Verificato] · T1 · <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>; <https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork>
15. Metti i documenti lunghi in alto e la domanda in fondo: le domande alla fine migliorano la risposta fino al 30% nei test, soprattutto con più documenti; con testi lunghi chiedi prima le citazioni pertinenti. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>

## Stato dell'arte

### A. Che cos'è e cosa lo riempie
- **Definizione.** Tutto il testo a cui il modello può riferirsi nel generare, risposta compresa: una «working memory», diversa dai dati di addestramento. Nell'API conta ogni cosa della richiesta: prompt di sistema, messaggi, risultati di strumenti, immagini, documenti, definizioni degli strumenti, ragionamento. [Verificato] T1 · [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows). Che l'app funzioni allo stesso modo sotto la superficie è [Inferenza].
- **Finestre nell'app.** Vedi regola 1 e tabella F. Sulle pagine di support non compare il piano Free. [Verificato] T1 · help 8606394
- **Cosa la riempie nell'app (domanda 1).** Nessuna pagina elenca tutto. Pezzi verificati:
  - Istruzioni del profilo: valgono in tutte le conversazioni (help 10185728). Istruzioni del Project: solo nel Project.
  - Knowledge del Project: in contesto finché ci sta, poi RAG (help 11473015); nella pagina sugli allegati il contenuto totale del Project deve stare nella finestra (help 8241126; vedi conflitti).
  - Skill: progressive disclosure, Claude carica solo ciò che serve al compito; richiedono l'esecuzione di codice (help 12512176). Che le descrizioni stiano sempre nel contesto lo dice solo la documentazione per sviluppatori: [Inferenza] per l'app.
  - Strumenti e connettori: «token-intensive» (help 8606394, 11647753); «On demand» lascia più spazio (help 11176164).
  - Ricerca nelle chat passate: parte solo su richiesta e compare come chiamata di strumento (help 11817273).
  - Memoria: la pagina non dice se entri sempre o solo quando serve; si spegne per una chat da «+» > «Memory» prima del primo messaggio; la chat in incognito non la usa né la salva (help 11817273).
  - Stili: nessuna pagina d'aiuto trovata che ne parli rispetto al contesto.
  [Verificato] le singole voci · T1
- **Indicatore del contesto.** In Claude Desktop v2.42304.0 (2026-10-15) c'è una scheda «Context» nel pannello laterale della sessione; l'anello sotto il campo dei messaggi mostra l'uso del piano. [Verificato] T1 · [changelog di Cowork](https://claude.com/docs/cowork/changelog). Che sia visibile in ogni conversazione dell'app unificata è [Inferenza] non verificata.

### B. Degrado
- **Cosa dice Anthropic.** «As token count grows, accuracy and recall degrade»: context rot. [Verificato] T1 · context windows. Spiegazione: ogni token consuma un «attention budget» e il transformer crea «n² pairwise relationships for n tokens»; i modelli hanno visto meno sequenze lunghe in addestramento. Post del 2025-09-29, oltre 12 mesi, coerente con la pagina corrente. [Verificato] T1 · [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Misure (due preprint, Tier 1 con nota «preprint»; nessuno misura i modelli 5.x né l'app).**
  - LOCA-bench, agenti con contesto che cresce: da 8K a 256K Claude-4.5-Opus 96,0% → 14,7%, GPT-5.2-Medium 72,0% → 21,3%, Gemini-3-Flash 64,0% → 17,3%; il distacco si apre verso 32K. A 128K la chiamata programmatica degli strumenti è la tecnica più costante (Claude 34,0 → 40,0); pulizia e compaction danno guadagni piccoli. 15 compiti, dipende dallo scaffold. [2602.07962](https://arxiv.org/html/2602.07962) (2026-02-08)
  - «Lost in the Middle»: risultati migliori con l'informazione all'inizio o alla fine, peggiori nel mezzo. Modelli del 2023: [Obsoleto?] per i modelli correnti, ma coerente con il consiglio corrente di Anthropic sulla posizione (regola 15). [2307.03172](https://arxiv.org/abs/2307.03172)
- **Distinzione.** Misurato: calo con la lunghezza, fino a Claude 4.5. Non misurato: Claude 5.x, l'app, la sintesi automatica. Il consiglio «scegli cosa mettere» è di Anthropic; il legame con i numeri dei preprint è [Inferenza].

### C. Sintesi automatica nell'app (domanda 2)
- **Condizioni e comportamento.** Regola 5. [Verificato] T1 · help 8606394 (aggiornata questa settimana), help 11647753
- **Soglia.** Nessuna soglia generale pubblicata; l'unico numero è Sonnet 5 in Cowork, che compatta a 500K. [Verificato] T1 · help 8606394
- **Cosa conserva.** La cronologia completa resta e Claude vi può fare riferimento; la pagina non dice cosa entra nel riassunto né se le Istruzioni date all'inizio sopravvivano. [Verificato] l'assenza · T1
- **Segnale visibile.** «organizing its thoughts». [Verificato] T1 · help 8606394, 11647753
- **App unificata e attività.** La pagina sull'app unificata non parla di sintesi né di finestra (help 16761823); la pagina di Cowork dice che le attività lunghe non si fermano per limiti di contesto, senza spiegare come (help 13345190). Il changelog di Claude Desktop, letto per 200.000 di 245.508 caratteri, non ha voci su compattazione o `/compact` per Cowork. Che la sintesi valga anche nelle attività è [Inferenza] da help 8606394 (soglia di Sonnet 5 in Cowork).
- **Consumo.** Le chat che fanno scattare la sintesi usano più limite. [Verificato] T1 · help 8606394, 11647753

### D. Cosa caricare e dove (domande 3, 4, 7)
- **Connettori.** «Tool access» si trova in «+» (o «/») > «Connectors» > «Tool access»: «Auto» predefinito, «On demand» consigliato con 10 o più connettori per dare «more room» alla conversazione; per la maggior parte degli utenti «Auto» va bene. Disconnessione completa da Customize > Connectors. Peso in token: non dichiarato. [Verificato] T1 · help 11176164
- **Ricerca web.** Nessun interruttore nell'app unificata; Claude cerca quando lo ritiene utile; per evitarlo, chiederlo. [Verificato] T1 · help 16761823, 11647753
- **Modello, effort, ragionamento.** Dal nome del modello accanto al pulsante di invio: modello («More models» per gli altri), «Effort», interruttore «Thinking» o «Extended» dove esiste. Modelli con effort: Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1, Opus 5, Sonnet 5, Fable 5, Opus 4.7, Opus 4.6, Sonnet 4.6. Ogni modello segna un «Default». Effort più alto: risposte più approfondite e più lente, più token. La pagina non parla di Cowork; il changelog di Claude Desktop v2.9939.2 (2026-09-24) aggiunge l'interruttore del ragionamento esteso accanto all'effort in Cowork, e v2.16120.0 (2026-09-29) dice che l'effort Max vale solo per la sessione corrente. [Verificato] T1 · help 8664678; changelog di Cowork
- **Allegati o knowledge.** Regola 10. Conviene l'allegato per un documento usato in una sola chat, anche grande o con grafici; la knowledge per ciò che serve in più chat, sapendo che va in cache e che oltre la finestra lavora il RAG. [Inferenza] sulla scelta · T1 · help 8241126, 11473015, 9797557
- **Project in generale.** Raccolgono file, Istruzioni e contesto; funzionano in ogni conversazione dell'app unificata. [Verificato] T1 · help 16761823

### E. Chat lunghe e lavoro in parallelo (domande 5, 6)
- **Consigli ufficiali dell'app.** Usare i Project (RAG); Istruzioni del Project brevi; togliere i file inutili; spegnere il ragionamento esteso quando non serve; abbassare l'effort per la routine; spegnere gli strumenti che non servono e chiedere di non cercare sul web; vicino al limite d'uso in una chat lunga, aprirne una nuova; al limite di lunghezza, chat nuova o Project. [Verificato] T1 · help 11647753
- **Altri consigli ufficiali.** Pianificare la conversazione e raggruppare le domande collegate in un messaggio; rivedere il prompt prima di inviarlo; usare chat search e memoria invece di ripetere. [Verificato] T1 · help 9797557. Cowork: raggruppare il lavoro collegato in una sola attività; conversazione nuova per lavori non collegati, così non si porta dietro contesto superfluo; dire quando basta una risposta rapida senza file. [Verificato] T1 · help 13345190
- **Parallelo.** Più attività insieme; sottoagenti coordinati per lavori complessi; tutto conta sui limiti del piano; durante il rollout la misura può differire tra account con e senza la nuova esperienza. Proporzionalità del consumo: nessuna prova trovata. [Verificato] T1 · help 16761823, 13345190
- **Ricominciare senza perdere il filo.** Ramificare da un punto precedente non è disponibile nell'app unificata. [Verificato] T1 · help 16761823. Nessuna pagina dell'app descrive un documento di passaggio: resta [Segnale T3] di comunità. Vicini ufficiali: note strutturate fuori dalla finestra da riportare quando servono (context engineering, 2025) e file di stato perché una sessione nuova si rimetta in pari in fretta (context windows, per agenti). Le tre righe su dove eri sono quindi [Inferenza] coerente con queste pagine. Il changelog di Claude Desktop cita un pulsante «Edit» sull'ultimo messaggio e «Restart conversation from here» in Chat, in una sezione per installazioni con gateway: versione non certa, [Inferenza] che valga per tutti.
- **Dove guardare i consumi.** Settings > Usage: sessione corrente di cinque ore, limite settimanale, orario di reset; da v3.6556.1 (2026-10-22) anche i token in cache. [Verificato] T1 · help 11647753, 9797557; changelog di Cowork

### F. Modelli nell'app
| Modello | Chat | Cowork |
| --- | --- | --- |
| Fable 5.1 | 1M | 1M |
| Opus 5.5 | 1M | 1M |
| Sonnet 5.5 | 1M | 1M |
| Haiku 5.5 | 1M | 500K |
Fonte: help 8606394. [Verificato] T1. Opus 5.6 non compare nelle release notes dell'app al 1 novembre (ultima voce 2026-10-21). [Verificato] T1 · [release notes](https://support.claude.com/en/articles/12138966-release-notes)

### G. Modello di pratica (generico, [Inferenza] su ogni voce)
1. Un Project per lavoro; Istruzioni brevi; solo i file che servono (D, E).
2. Un argomento per chat; quando cambi argomento o la chat è lunga, chat nuova nello stesso Project con tre righe su dove eri (B, E).
3. Esecuzione di codice attiva se vuoi la sintesi automatica, sapendo che il riassunto perde dettagli e consuma di più (C).
4. Connettori spenti quando non servono, «On demand» con 10 o più; niente ricerca web se non servono dati aggiornati (D).
5. Effort più basso per la routine, scelto all'inizio (D).
6. Documenti in alto, domanda in fondo (B, regola 15).
7. Settings > Usage quando i consumi salgono senza motivo (E).
8. A ogni modello nuovo, rileggere help 8606394 e help 8664678 (F).

## Raccordo con v1
| Punto | Stato al 1-nov |
| --- | --- |
| Regole 1-9, 12, 13 di v1 (Claude Code e API) | Tolte: fuori perimetro |
| Regola 10 (sintesi automatica) | Ancora vero; ora regola 5, con la soglia di Sonnet 5 in Cowork |
| Regola 11 (RAG) | Ancora vero; ora regola 7, con indicatore e ritorno all'elaborazione in contesto |
| Regola 14 (LOCA-bench) | Numeri riletti e uguali; spostata in B |
| Regola 15 (context awareness) | Tolta: voce dell'API |
| Preprint 2510.05381, 2507.11538, 2605.28079 | Tolti: al massimo due preprint |
| Documento di passaggio | Ancora [Segnale T3]; in più: ramificazione non disponibile nell'app unificata |

## Tabella conflitti
| Tema | Fonte A (data, Tier) | Fonte B (data, Tier) | Stato |
| --- | --- | --- | --- |
| Come l'app gestisce la finestra piena | context windows: le interfacce come claude.ai possono gestirla «first in, first out» (corrente, T1, nota a piè di pagina) | help 8606394: sintesi dei messaggi vecchi, cronologia conservata (aggiornata questa settimana, T1) | Risolto a favore di help 8606394 per i piani a pagamento con esecuzione di codice; senza esecuzione di codice il comportamento non è descritto |
| Capacità della knowledge di un Project | help 8241126: il contenuto totale deve stare nella finestra (2026-07-23, T1) | help 11473015: con il RAG fino a 10 volte (corrente, T1) | Non risolto: forse la pagina sugli allegati non è aggiornata o vale senza RAG |
| Sintesi automatica e limite d'uso | snippet di ricerca del 27-ott: non conta sul limite (T1 non letto) | help 8606394 e 11647753 lette: usa più limite (corrente, T1) | Risolto a favore delle pagine lette |
| Finestra di Haiku 5.5 | chat: 1M (T1) | Cowork: 500K (T1) | Risolto: dipende dalla superficie |
| Istruzioni del Project sui piani gratuiti | help 10185728: Project anche gratis, fino a cinque (T1) | stessa pagina: Istruzioni del Project solo a pagamento (T1) | Non risolto: incoerenza interna della pagina |

## Cosa non è stato verificato
- Elenco completo di cosa entra nel contesto di una chat dell'app: se memoria, stili e descrizioni delle skill siano sempre presenti. Pagine controllate: help 8606394, 11647753, 10185728, 12512176, 11817273, 16761823.
- Soglia della sintesi automatica (salvo Sonnet 5 in Cowork), contenuto del riassunto, comportamento senza esecuzione di codice; se valga nelle attività programmate. Pagine controllate: help 8606394, 11647753, 16761823, 13345190, changelog di Cowork (200.000 di 245.508 caratteri).
- Peso in token di connettori, ricerca web e ragionamento; se il consumo di attività parallele e sottoagenti cresca in proporzione.
- Se la scheda «Context» di Claude Desktop sia visibile in ogni conversazione dell'app unificata.
- Pagina d'aiuto sugli stili dell'app rispetto al contesto: nessuna trovata con una ricerca.
- Finestra del piano Free.
- La pagina di claude.com sui gateway di Claude Desktop, che descrive la compattazione delle sessioni Cowork, è stata vista solo come estratto di ricerca, non letta; riguarda installazioni con gateway.

## Fonti per Tier
**Tier 1.** support.claude.com: [8606394](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans) · [11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) · [11473015](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) · [11176164](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) · [16761823](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) · [13345190](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) · [8664678](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings) · [8241126](https://support.claude.com/en/articles/8241126-upload-files-to-claude) · [12512176](https://support.claude.com/en/articles/12512176-what-are-skills) · [9797557](https://support.claude.com/en/articles/9797557-usage-limit-best-practices) · [11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) · [10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) · [12138966](https://support.claude.com/en/articles/12138966-release-notes). claude.com: [changelog di Cowork](https://claude.com/docs/cowork/changelog). platform.claude.com: [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) · [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). anthropic.com: [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). arXiv (preprint): [2602.07962](https://arxiv.org/html/2602.07962) · [2307.03172](https://arxiv.org/abs/2307.03172)
**Tier 2.** Nessuna fonte usata.
**Tier 3.** Nessuna fonte letta; il documento di passaggio resta [Segnale T3] senza fonte citata.

## Guida
Le istruzioni d'uso per Claude e i passi per l'utente stanno in `D:\Workspace\best_practice\3_contesto\guida_contesto.md`.
