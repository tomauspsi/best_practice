---
tema: Istruzioni di un Project nell'app Claude (chat e Cowork unificati) e rapporto con knowledge, cartelle, memoria, profilo e modello
versione: 2
base: ae830f3
verificato_il: 2026-11-01
aggiornato_il: 2026-11-01 (run 5: perimetro ridotto alla sola app; tolti i Projects di Claude Code; ogni fatto riletto sulla pagina del giorno)
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes dell'app o changelog di Claude Desktop che toccano Project, Istruzioni, knowledge, GitHub, Drive, cartelle o modello; ritorno di «Add from GitHub» tra le funzioni supportate dell'app unificata; oppure 2026-12-18"
versioni_rilevate:
  modelli_app: "Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 (release notes dell'app: Opus 5.5 2026-09-22, Sonnet 5.5 2026-09-28, Haiku 5.5 2026-10-07)"
  app_claude: "release notes dell'app: ultima voce 2026-10-21 (Duet); app unificata chat e Cowork dal 2026-09-16, rilascio graduale; nessuna voce su Project dopo quella data"
  claude_desktop: "v4.4212.0 del 2026-10-29 (changelog di Claude Desktop, letto con grep)"
  opus_5_6: "non uscito al 2026-11-01 (release notes dell'app)"
---

# Istruzioni di un Project nell'app Claude: stato al 1 novembre 2026 (v2)

v2 sostituisce v1 (26-27 ottobre), che copriva anche i Projects di Claude Code. La storia sta nei commit. Le pagine di support.claude.com arrivano dallo strumento come riassunto: qui sono parafrasi, senza virgolette, salvo i nomi di menu e pulsanti. Fatti vicini già verificati altrove, non ripetuti: precedenza tra profilo, Project, stili, memoria e skill in `D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md`; contesto, RAG e limiti dei file in `D:\Workspace\best_practice\3_contesto\rapporto_contesto.md`; memoria di Project in `D:\Workspace\best_practice\4_memoria\rapporto_memoria.md`; attività programmate in `D:\Workspace\best_practice\5_attivita\rapporto_attivita.md`. Tag: [Verificato] [Inferenza] [Obsoleto/Conflitto] [Segnale T3]; [Segnale] interno per le prove dell'utente.

## Risposta breve
- Le Istruzioni di un Project valgono in ogni chat di quel Project e in nessun'altra; nell'app unificata i Project funzionano in ogni conversazione. Nome e descrizione Claude non li vede.
- Nessuna pagina pubblica un limite di lunghezza: la pagina sui limiti chiede Istruzioni concise, con contesto, linee guida e ruolo; le richieste del singolo compito vanno nella chat.
- Knowledge: solo i file che servono. Il RAG parte da solo vicino al limite; nessuna pagina dice se le Istruzioni ci rientrino.
- GitHub: nei Project privati si aggiungono file scelti di un repository e si aggiornano con **Sync now**. La pagina sull'app unificata dice che «Add from GitHub» non è supportato; nessuna pagina dice se un Project già collegato continui a sincronizzarsi.
- Cartella locale: Claude la raggiunge tramite Claude Desktop, che deve restare aperto; in chat l'accesso è in sola lettura e vale per le cartelle aggiunte dal 5 ottobre 2026 in poi.
- Il Project ricorda il modello scelto l'ultima volta (pagina d'aiuto Enterprise); Haiku 5.5 non è adatto a Istruzioni lunghe con molte regole.
- Opus 5.6: non uscito al 1 novembre. Rivalutare tutto quando esce.

## Regole operative
1. Scrivi nelle Istruzioni del Project ciò che deve valere in ogni chat del Project: si impostano con **Set project instructions** e **Save instructions** e valgono per tutte le chat del Project; nell'app unificata i Project funzionano in ogni conversazione. [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>; <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>
2. Non affidare nulla al nome o alla descrizione del Project: Claude non li vede. Ciò che serve va nelle Istruzioni o nella knowledge. [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>; <https://academy.claude.com/courses/claude-101/introduction-to-projects>
3. Istruzioni = come Claude lavora (contesto, ruolo, linee guida, tono, processo); knowledge = materiale da consultare; le richieste del singolo compito vanno nella chat. Fatti che cambiano, schemi ed elenchi lunghi stanno nei documenti. [Verificato] · T1 · <https://academy.claude.com/courses/claude-101/introduction-to-projects>; <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
4. Tieni le Istruzioni concise: nessuna pagina dell'app pubblica un limite di lunghezza, e la pagina sui limiti chiede di tenerle brevi e centrate sull'essenziale. [Verificato] per il silenzio e il consiglio · T1 · <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>
5. Non cercare una precedenza ufficiale tra Istruzioni del Project, profilo, stili e memoria: nessuna pagina la fissa. Una regola, una casa; se due fonti si toccano, scrivi nelle Istruzioni quale vince. Dettagli in `D:\Workspace\best_practice\1_comportamento\rapporto_comportamento.md`. [Verificato] per il silenzio · [Inferenza] per il consiglio · T1 · <https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features>
6. Una regola che deve valere sempre va nelle Istruzioni, non solo nella memoria. [Segnale] interno: prova dell'utente del 25 ottobre (Haiku 5.5, chat dell'app), una regola salvata solo in memoria non seguita, la stessa nelle Istruzioni sì; una sola prova. Le Istruzioni valgono in ogni chat del Project [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
7. Scrivi come a un collega nuovo e brillante: esplicito, con il motivo, dicendo cosa fare invece di cosa evitare; test: se una persona con poco contesto sarebbe confusa, lo sarà anche Claude. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>
8. Niente «CRITICAL» o maiuscole diffuse: i modelli recenti rispondono di più al system prompt e possono esagerare; attenua il linguaggio aggressivo. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>
9. Se servono esempi, 3-5, diversi tra loro; pochi esempi canonici invece di un elenco di casi limite. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>; <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
10. Parti da Istruzioni minime e aggiungi solo dopo un errore osservato; «minimale» non vuol dire «corto». Post del 2025-09-29 (oltre 12 mesi), concorde con la pagina di prompting corrente. [Verificato] come consiglio · T1 · <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
11. Di' cosa fare se manca qualcosa (un file, un dato): permetti esplicitamente di dire che manca, chiedi di basarsi solo sui documenti del Project e di non indovinare. La tecnica è ufficiale per ridurre le invenzioni; applicarla alle Istruzioni di un Project è nostra. [Verificato] per la tecnica · [Inferenza] per il Project · T1 · <https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations>
12. Per un repository GitHub: solo in un Project privato, «+» nella sezione knowledge > **GitHub** > repository > file e cartelle > **Add files**; per cambiare i file, seleziona il repository nella knowledge > file > **Update**; dopo ogni modifica al repository, **Sync now**. Si leggono solo nomi e contenuti dei file di un branch, e devono stare nella finestra di contesto: scegli pochi file. [Verificato] · T1 · <https://claude.com/docs/connectors/github.md>; <https://support.claude.com/en/articles/10167454-using-the-github-integration>
13. Con Istruzioni lunghe o molte regole non affidarti a Haiku 5.5: con prompt lunghi a effort basso salta ricerche e controlli o si ferma prima; per l'aderenza Anthropic suggerisce la frase «le regole valgono per tutta la conversazione» ed effort `high`. Il Project ricorda il modello scelto l'ultima volta. [Verificato] per la pagina · [Inferenza] per l'app · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5>; <https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization>
14. Nell'app unificata tratta il Project come contenitore unico: funziona in ogni conversazione; i progetti locali di Cowork passano nell'account con nome, descrizione, Istruzioni e una copia della memoria, mentre cartelle e file restano sul computer; una cartella locale fa da contesto solo con Claude Desktop aperto; ogni Project ha le sue attività programmate. [Verificato] · T1 · <https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork>; <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>
15. A ogni nuovo modello rileggi le Istruzioni, togli ciò che serviva ai modelli vecchi e rifai le tue prove: le guide di Sonnet 5.5 e Opus 5.5 chiedono di ritarare sulle proprie prove invece di riportare le impostazioni vecchie e di ritestare le mitigazioni. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5>; <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5>

## Stato dell'arte

### A. Cosa sono e come funzionano (domanda 4, prima parte)
- Creare: claude.ai/projects o barra laterale > **+ New Project**, nome e descrizione. Istruzioni: **Set project instructions** > testo > **Save instructions**; valgono in tutte le chat del Project. Nessun limite di lunghezza nella pagina. [Verificato] T1 · [help 9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Nome e descrizione: visibili all'utente, non a Claude (parafrasi); Academy dice lo stesso della descrizione. [Verificato] T1 · help 9519177; [Academy](https://academy.claude.com/courses/claude-101/introduction-to-projects)
- Lunghezza: nessun limite in help 9519177, 11647753, 14116274, 10185728, Academy; help 11647753 consiglia Istruzioni concise con contesto generale, linee guida e ruolo di Claude, e di lasciare alla chat le richieste del compito. Una ricerca web ha trovato solo cifre di terzi, discordi (non tenute). Non provato nell'interfaccia. [Verificato] T1 per il silenzio · [help 11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- Chat: si spostano in un Project dal menu accanto al nome della chat > «Add to project». Archiviare non cambia knowledge né condivisione; si elimina solo dopo averlo tolto dall'archivio. [Verificato] T1 · help 9519177
- Nell'app unificata i Project tengono insieme file, Istruzioni e contesto e funzionano in ogni conversazione. [Verificato] T1 · [help 16761823](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- Versione nuova dei Project (una conversazione con thread paralleli): oggi solo per alcuni utenti di Claude Code; chat e Cowork restano sulla versione classica per ora. Fuori perimetro. [Verificato] T1 · [help 9517075](https://support.claude.com/en/articles/9517075-what-are-projects)
- Segnale dal changelog di Claude Desktop: v1.26832.0 del 2026-08-06 ha corretto chat avviate in un Project che non ricevevano Istruzioni e link di contesto. Se una regola del Project sembra ignorata, aggiornare l'app è il primo controllo. [Verificato] T1 per la voce · [Inferenza] per il consiglio · [changelog](https://claude.com/docs/cowork/changelog.md)

### B. Knowledge: cosa caricare e perché (domanda 2)
- La knowledge vale in tutte le chat del Project; il contesto non passa tra le chat se non sta nella knowledge. [Verificato] T1 · help 9519177; Academy
- RAG: parte da solo quando la knowledge si avvicina al limite della finestra, porta la capacità fino a 10 volte, si riconosce da un indicatore e dallo strumento di ricerca nella knowledge; piani Pro, Max, Ultra, Team, Enterprise. Consigli: nomi di file descrittivi, documenti collegati nello stesso Project, citare i file per nome. La pagina non dice se le Istruzioni rientrino nel RAG. [Verificato] T1 · [help 11473015](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
- Le Istruzioni sono un campo a parte rispetto alla knowledge (pulsante e salvataggio propri). [Verificato] T1 · help 9519177. Che restino sempre in contesto è [Inferenza]: nessuna prova trovata (pagine controllate: help 11473015, 9519177, 9517075, 11647753, Academy).
- Pulizia: togliere ogni tanto i file del Project che non si usano più. [Verificato] T1 · help 11647753. Limiti di file e capacità: `D:\Workspace\best_practice\3_contesto\rapporto_contesto.md`, sezione «D. Cosa caricare e dove».
- Perché, per il Project «best practice», selezionare solo `README.md` e le cinque guide: la guida GitHub chiede di partire da pochi file centrali al compito e di restare nei limiti di token; le guide riassumono i rapporti, quindi i rapporti duplicherebbero ogni regola e, se il RAG si attiva, aumenterebbero i pezzi recuperati in concorrenza; `CLAUDE.md` contiene istruzioni per gli agenti che mantengono il repository (rami, PR, tetti), che in una chat dell'app sarebbero regole sbagliate. [Verificato] per il consiglio sui file · [Inferenza] per il resto · T1 · [GitHub, claude.com](https://claude.com/docs/connectors/github.md)

### C. GitHub e Google Drive nel Project (domanda 1)
- Aggiungere: solo Project privati (in un Project condiviso l'opzione è grigia, «Only accessible from private projects»); «+» nella sezione knowledge > **GitHub** > repository > file e cartelle > **Add files**. Cambiare i file: repository nella knowledge > selezione > **Update** (la pagina del Help Center lo chiama ancora icona **Configure files**). Aggiornare: **Sync now** sul repository (icona **Sync** nel Help Center). Disponibile su tutti i piani, Free compreso. [Verificato] T1 · [GitHub, claude.com](https://claude.com/docs/connectors/github.md); [help 10167454](https://support.claude.com/en/articles/10167454-using-the-github-integration)
- Cosa arriva: nomi e contenuti dei file di un branch; niente cronologia, PR, issue, metadati. Più repository insieme, purché stiano nella finestra. Se si perde l'accesso, l'anteprima sparisce, la cronologia resta. [Verificato] T1 · stesse pagine
- App unificata: tra i limiti attuali «Add from GitHub» non è supportato (parafrasi). [Verificato] T1 · help 16761823 (riletta il 2026-11-01). «Add from GitHub» è il nome dell'opzione nelle chat; nel Project l'opzione si chiama **GitHub**. Se il limite tocchi anche la knowledge di un Project già collegato, e se l'icona Sync resti: nessuna prova trovata (pagine controllate: help 16761823, 10167454, 9519177, 14116274, GitHub su claude.com, changelog di Claude Desktop, release notes dell'app; una ricerca web). [Inferenza] il limite riguarda almeno il comando delle chat.
- Se **Sync now** manca: scaricare da GitHub i file scelti e caricarli a mano nella knowledge, ricaricandoli dopo ogni modifica; oppure un documento Google (vedi sotto). [Inferenza] su fatti [Verificato] delle stesse pagine.
- Documento Google: solo Project privati; nella knowledge **Add files** (help 10166901: sezione Files > «+») > **Google Drive** > file o URL. Arriva come testo (Docs in Markdown senza immagini, Sheets in CSV, Slides in testo), esportazione fino a circa 10 MB. [Verificato] T1 · [Drive, claude.com](https://claude.com/docs/connectors/google/drive.md); [help 10166901](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- Aggiornamento del documento Google: help 10166901 dice che resta sincronizzato con la versione più recente; la pagina claude.com dice che si aggiorna periodicamente quando si apre il Project. Vedi conflitti. Prova dell'utente del 25-ott: una chat nuova ha visto la modifica dopo circa sei minuti; Claude non aggiorna il documento senza richiesta. [Segnale] interno, una prova

### D. Il Project nell'app unificata (domande 3 e 4, seconda parte)
- Il Project unificato contiene Istruzioni, attività programmate, contesto e memoria; come contesto si aggiungono una cartella locale, un Project di chat collegato o un URL. Creazione da **Projects** > **+**: **Start from scratch**, **Import from project** (copia file e Istruzioni da un Project di chat), **Use an existing folder**. [Verificato] T1 · [help 14116274](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- Spostamento nell'account: Claude Desktop sposta da solo i progetti nati da una cartella locale; passano nome, descrizione, Istruzioni (con i link di Drive) e una copia della memoria se accesa; restano sul computer cartelle, file e sessioni precedenti; se il progetto era collegato a un Project di chat, descrizione e Istruzioni vanno lì. Pro, Max e Ultra in Claude Desktop; Team ed Enterprise con «Chat and Cowork unified» acceso. [Verificato] T1 · help 14116274; help 16761823
- Cartella locale: Claude legge e scrive solo nelle cartelle collegate, le raggiunge quando un compito ne ha bisogno, tramite Claude Desktop, che deve restare aperto (se si chiude o il computer dorme la sessione può finire). [Verificato] T1 · [help 13345190](https://support.claude.com/en/articles/13345190-get-started-with-cowork); help 16761823
- In chat: accesso in sola lettura alle cartelle aggiunte a un Project dopo la v2.19675.1 del 2026-10-05; per una cartella aggiunta prima, aggiungerla di nuovo e aprire una chat nuova. [Verificato] T1 · [changelog](https://claude.com/docs/cowork/changelog.md)
- Cosa legge Claude della cartella e quando: nessuna pagina elenca i file letti né dice che li rilegga a ogni conversazione (pagine controllate: help 14116274, 13345190, 16761823, guida Cowork). La guida Cowork dice che Claude legge file fino a 50 MB e che i file trascinati nel Project si copiano nella prima cartella. [Verificato] T1 · [guida Cowork](https://claude.com/docs/cowork/guide/projects.md)
- Attività programmate: ogni Project ha le sue; le attività in background di un Project usano cartelle, Istruzioni e memoria del Project (guida Cowork, per Dispatch). Help 13854387 non nomina i Project. Il resto in `D:\Workspace\best_practice\5_attivita\rapporto_attivita.md`, sezione «Project». [Verificato] T1 · help 14116274; guida Cowork; [help 13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)

### E. Prove e studi
| Fonte | Cosa dimostra | Cosa non dimostra | Tag |
|---|---|---|---|
| [arXiv 2608.02639](https://arxiv.org/abs/2608.02639) (preprint, 2026-07-31) | Con 1-20 istruzioni impilate l'aderenza scende da circa 96% a 20% (Sonnet 4.6 e altri); il calo viene da conflitti a coppie | Non Claude 5.5; compiti sintetici | [Verificato] sull'abstract, il 2026-10-26; non riletto |
| [arXiv 2607.19257](https://arxiv.org/abs/2607.19257v1) (preprint, 2026-07-21) | Da 10 a 160 regole l'aderenza cala; nessun vantaggio affidabile del Markdown | Modelli non nominati | [Verificato] sull'abstract, il 2026-10-26; non riletto |
- [Inferenza] i due preprint sostengono, in modo indiretto, poche regole per Project; nessuno misura le Istruzioni di un Project.
- Istruzioni in negativo: nessuna misura trovata di «non fare X» contro «fai Y»; resta un consiglio di Anthropic. [Inferenza]
- [Segnale] interno, non fonte: il 25 ottobre l'utente ha visto (chat dell'app, Haiku 5.5) una regola di formato salvata solo in memoria non applicata, la stessa nelle Istruzioni sì. Una sola prova.

### F. Modelli e Project (domanda 7)
- Il Project tiene il proprio modello: i Project nuovi partono dal modello predefinito, quelli esistenti tengono il modello che ogni utente ha scelto l'ultima volta lì; il modello si cambia in qualsiasi conversazione. La pagina è per le organizzazioni Enterprise; per gli altri piani nessuna pagina lo dice. [Verificato] T1 · [help 15330088](https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization) · [Inferenza] per i piani individuali
- Il selettore del modello è dove era prima dell'unificazione. Un'attività programmata impostata a mano ha un campo facoltativo per il modello. [Verificato] T1 · help 16761823; help 13854387
- Haiku 5.5: a effort `low` con prompt lunghi salta ricerche, si ferma prima o salta controlli; `high` per seguire le istruzioni con rigore; la frase «The rules in this system prompt hold for the whole conversation» ha aumentato l'aderenza nei test di Anthropic. [Verificato] T1 · [Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)
- Sonnet 5.5: per il lavoro lungo più difficile è meglio un Opus; tende ad aggiungere ciò che non è chiesto e a costruire quando si volevano idee (blocco «When the user asks for ideas... stop»). [Verificato] T1 · [Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- Opus 5.5: risponde bene a istruzioni che nominano i comportamenti precisi da evitare; nelle chat, istruzioni del tipo «pensa con attenzione» si possono togliere. [Verificato] T1 · [Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- Quando evitare Haiku 5.5 nel Project: Istruzioni con molti passi o controlli, risposte che dipendono da ricerche, regole da tenere anche se l'utente insiste. [Inferenza] sulle pagine sopra. Finestra di Haiku 5.5 in Cowork: `D:\Workspace\best_practice\3_contesto\rapporto_contesto.md`.

### G. Piani e condivisione (domanda 6)
- Project per tutti, Free fino a cinque; RAG sui piani a pagamento; condivisione («Can view», «Can edit») su Team ed Enterprise, salvo blocco dell'amministratore. [Verificato] T1 · help 9519177; help 9517075
- GitHub e Drive nella knowledge: solo Project privati. [Verificato] T1 · GitHub e Drive su claude.com
- Istruzioni di Project e piani: help 10185728 dice, nella sezione di scelta, «solo piani a pagamento», mentre help 9519177 descrive **Set project instructions** senza limiti di piano. Riletto oggi: la contraddizione resta. Per l'utente (piano a pagamento) non cambia nulla. [Obsoleto/Conflitto]

### H. Modello di Istruzioni (generico, ≤ 25 righe)
Ogni voce rimanda alle regole sopra; sono tutte [Inferenza] (raccomandazione), costruite su fatti [Verificato].
```text
Scopo: <una frase: per che cosa serve questo Project>.                      (regole 1, 2)
Fonti: i fatti stanno nei documenti del Project; usa quelli e citali per
nome. Se un dato manca o un file non si apre, di' che cosa manca e
fermati, senza indovinare.                                                   (3, 11)
Se due fonti si contraddicono, vale <fonte A>; dillo.                        (5)
Come lavori:
- <passo 1, con il motivo>
- <passo 2, con il motivo>
Prima di dire «fatto»: <controllo concreto>.
Chiedi il mio via libera prima di: <azioni irreversibili o fuori ambito>.
Formato delle risposte: <lingua, lunghezza, forma concreta>.                (7)
Le regole di questo Project valgono per tutta la conversazione.             (13)
<2-3 esempi diversi in tag, solo se servono>                                (9)
```
- Nelle Istruzioni: scopo, ordine delle fonti, flussi, regole con motivo, cosa fare se manca qualcosa, formato, limiti d'azione. (regole 3, 7, 11)
- Nei documenti: schemi, convenzioni, elenchi lunghi, dati. (regola 3)
- Nella memoria: preferenze emerse e decisioni, non regole che devono valere sempre. (regola 6)
- Nel profilo: lingua e tono validi ovunque; non ripeterli nel Project. (regola 5)
- Dopo ogni modifica e a ogni nuovo modello: 5 domande vere e 2 trabocchetti in una chat nuova. (regola 15)

## Raccordo con v1
| Punto di v1 | Stato oggi |
|---|---|
| Regole 1-10, 13, 15; sezioni A, B, C, E, F, H | Tenute e rilette sulle pagine del giorno; preprint non riletti (vedi E) |
| 16.000 caratteri nei Projects di Claude Code | Tolto: fuori perimetro (solo una nota in «Cosa non è stato verificato») |
| «Le Istruzioni di un Project dell'app non arrivano a Claude Code» | Tolto: fuori perimetro |
| Regola 11 con l'esempio dei Projects di Code | Riscritta con la pagina ufficiale sulle invenzioni; il Project è [Inferenza] |
| Regola 12 (Sync, «Configure files») | Aggiornata: Project privati, **Add files**, **Update**, **Sync now** (pagina claude.com) |
| Regola 14 e sezione D (Code e Cowork separati) | Riscritte per l'app unificata |
| Conflitto «Cowork project: dove vive» | Risolto (vedi conflitti) |
| Sezione «Projects e Claude Code» | Tolta |

## Tabella conflitti
| Tema | Fonte A | Fonte B | Stato |
|---|---|---|---|
| Istruzioni di Project e piani | help 9519177 (T1, senza data): Istruzioni senza limiti di piano; Project anche Free | help 10185728 (T1, senza data): Istruzioni di Project «solo piani a pagamento» | Non risolto, riletto il 2026-11-01: incoerenza interna di 10185728; più probabile 9519177 [Inferenza]; si chiude solo con una prova su un account Free |
| Dove vive un Project di Cowork | guida Cowork su claude.com (T1, senza data): solo sul computer, non sincronizzato né condiviso | help 14116274 e 16761823 (T1, aggiornate di recente): i progetti locali passano nell'account, condivisione su Team ed Enterprise | Risolto per l'app unificata a favore delle pagine d'aiuto: la guida descrive Cowork prima dell'unificazione; cartelle e file restano comunque sul computer. Coerente con `D:\Workspace\best_practice\4_memoria\rapporto_memoria.md` e `D:\Workspace\best_practice\5_attivita\rapporto_attivita.md` |
| GitHub nell'app unificata | help 16761823 (T1, aggiornata ieri): «Add from GitHub» non supportato | GitHub su claude.com (T1, senza data): aggiunta e **Sync now** nella knowledge del Project, senza eccezioni | Non risolto: forse il limite riguarda solo il comando delle chat [Inferenza]; si chiude guardando l'interfaccia del Project dell'utente |
| Aggiornamento del documento Google | help 10166901 (T1): resta sincronizzato con la versione più recente; commenti e suggerimenti visibili | Drive su claude.com (T1): si aggiorna periodicamente quando si apre il Project; Claude non legge commenti né suggerimenti (detto per i file letti dal connettore) | Non risolto: la pagina claude.com sembra più recente e precisa [Inferenza] |

## Cosa non è stato verificato
- Se un Project con un repository già collegato continui a sincronizzarsi nell'app unificata e se l'icona Sync resti (pagine controllate: help 16761823, 10167454, 9519177, 14116274, GitHub su claude.com, changelog di Claude Desktop, release notes dell'app).
- Limite di lunghezza delle Istruzioni nell'interfaccia: nessuna pagina lo pubblica; non provato. (Il tetto di 16.000 caratteri riguarda solo i Projects di Claude Code.)
- Se le Istruzioni rientrino nel RAG o restino sempre in contesto: help 11473015 tace.
- Quali file della cartella locale Claude legge e quando; se li rilegga a ogni conversazione.
- Se il Project ricordi il modello anche sui piani individuali: la sola pagina che lo dice è per Enterprise.
- Se le attività programmate di un Project leggano le Istruzioni del Project: lo dice la guida Cowork per le attività in background (Dispatch); help 13854387 tace.
- Preprint: non riletti in questa run (abstract letti il 2026-10-26).
- Changelog di Claude Desktop (245.784 caratteri): letto con grep su «project», «GitHub», «instructions», «model», non per intero.
- Reddit, forum e blog di terzi: non interrogati; le cifre di terzi sulla lunghezza delle Istruzioni non sono state tenute.

## Fonti per Tier
**Tier 1 (lette il 2026-11-01).** support.claude.com: [9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) · [9517075](https://support.claude.com/en/articles/9517075-what-are-projects) · [11473015](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) · [10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) · [14116274](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) · [16761823](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) · [10167454](https://support.claude.com/en/articles/10167454-using-the-github-integration) · [10166901](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors) · [11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) · [13345190](https://support.claude.com/en/articles/13345190-get-started-with-cowork) · [13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) · [15330088](https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization) · [12138966](https://support.claude.com/en/articles/12138966-release-notes). claude.com: [GitHub](https://claude.com/docs/connectors/github.md) · [Google Drive](https://claude.com/docs/connectors/google/drive.md) · [guida Cowork, projects](https://claude.com/docs/cowork/guide/projects.md) · [changelog di Claude Desktop](https://claude.com/docs/cowork/changelog.md). academy.claude.com: [introduction to projects](https://academy.claude.com/courses/claude-101/introduction-to-projects). platform.claude.com: [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) · [Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) · [Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) · [Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5). anthropic.com: [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29). arXiv (preprint, letti il 2026-10-26): [2608.02639](https://arxiv.org/abs/2608.02639) · [2607.19257](https://arxiv.org/abs/2607.19257v1).
**Tier 2.** Nessuna fonte usata.
**Tier 3.** Nessuna fonte usata; guide di terzi con cifre sulla lunghezza delle Istruzioni viste nei risultati di ricerca e scartate.

## Guida
Le istruzioni d'uso per Claude e i passi per l'utente stanno in `D:\Workspace\best_practice\2_istruzioni_project\guida_istruzioni_project.md`.
