---
tema: memoria tra una chat e l'altra nell'app Claude (chat e Cowork unificati, Project)
versione: 4
base: 93dad62
verificato_il: 2026-11-01
aggiornato_il: 2026-11-01 (run 1: perimetro ridotto alla sola app; tolte le parti su Claude Code, API e altri prodotti; ogni fatto riletto sulla pagina del giorno)
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes o changelog di Claude Desktop che toccano memoria, Project, cartelle o permessi; oppure 2026-12-18"
versioni_rilevate:
  app_claude: "senza numero di versione; release notes dell'app: ultima voce 2026-10-21 (Duet); memoria: ultima voce 2026-08-25; app unificata chat e Cowork: 2026-09-16"
  claude_desktop: "v4.4212.0 del 2026-10-29 (changelog di Cowork letto il 1-nov per i primi 100.000 caratteri, voci dal 2026-09-17)"
  modelli: "Opus 5.5 (2026-09-22), Sonnet 5.5 (2026-09-28), Haiku 5.5 (2026-10-07), Fable 5.1 (2026-09-01), dalle release notes dell'app"
---

# Memoria nell'app Claude: stato al 1 novembre 2026 (v4)

v4 sostituisce v3 (27 ottobre), che copriva anche Claude Code, l'API e altri prodotti. La storia sta nei commit. Le pagine di support.claude.com arrivano dallo strumento come riassunto: qui sono parafrasi, senza virgolette, salvo i nomi di menu e pulsanti. Tutte le pagine d'aiuto lette mostrano solo «Updated yesterday» o simili, senza data.

## Risposta breve
- Nell'app ci sono quattro cose che durano tra le chat: memoria dell'account, memoria di ogni Project, ricerca nelle chat passate (piani a pagamento), e ciò che l'utente scrive in Istruzioni e knowledge. Le attività di Cowork eseguite solo sul computer hanno una memoria a parte.
- Claude scrive in memoria durante la chat; «ricorda che…» salva subito; la modifica vale dalla conversazione successiva.
- Dentro un Project, una chat nuova vede sempre Istruzioni e knowledge; la memoria del Project e dell'account quando pertinente; le chat precedenti solo se Claude le cerca.
- La memoria è un promemoria: ciò che deve valere sempre va nelle Istruzioni. Nessuna pagina dichiara una precedenza.
- Claude può scrivere un documento (Google, cartella locale) solo con un connettore o una cartella collegata e, per quanto risulta, quando glielo si chiede.

## Regole operative
1. Usa un Project per separare la memoria: ogni Project ha la sua, usa anche quella dell'account e mai quella di altri Project; la memoria del Project può comparire fuori; spegni «Use account memory» (sezione Memory della pagina del Project) per isolarlo. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>; <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
2. Per ritrovare una chat passata chiedi di cercarla: la ricerca c'è solo sui piani a pagamento (Pro, Max, Ultra, Team, Enterprise), dentro un Project cerca solo nelle chat di quel Project, non copre le vecchie attività di Cowork; interruttore «Search and reference chats» in Settings > Your Claude, oppure, nell'app per Windows dell'utente, Impostazioni > Memoria > «Ricerca e consultazione delle chat». [Verificato] per la pagina; [Inferenza] per la schermata · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>; <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>
3. Metti nelle Istruzioni (profilo o Project) le regole che devono valere sempre, non solo in memoria. [Segnale] interno: prova dell'utente del 25 ottobre, una regola solo in memoria non seguita, la stessa nelle Istruzioni sì; una sola prova. Le Istruzioni del Project valgono per tutte le chat del Project [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
4. Per far ricordare subito una cosa scrivi «ricorda che…»: nella memoria nuova Claude salva per argomenti durante la chat e su richiesta salva subito; ricordare, cambiare o dimenticare in chat vale dalla conversazione successiva; nella memoria legacy la sintesi si aggiorna entro 24 ore. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
5. Gestisci la memoria da Impostazioni > Memoria, come nell'app per Windows dell'utente: «Genera memoria dalle chat» per accenderla o spegnerla, sezioni «Tu» e «Argomenti» per leggerla, casella in fondo per correggerla, «Esporta» per una copia. Nel layout nuovo delle pagine d'aiuto lo stesso sta in Settings > Your Claude, con «Manage» accanto a «Your memory». Per una chat sola, «+» > «Memory» prima del primo messaggio. [Verificato] per le pagine · [Inferenza] per la schermata, una sola osservazione · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context> (vedi tabella conflitti)
6. Non usare la memoria per dati sensibili: cancellare una chat non cancella le memorie nate da lì; i temi sensibili restano fuori finché non si accende «Include sensitive topics in memory»; numeri di documenti, conti, precedenti penali e stato migratorio non si salvano mai; «Reset memory» cancella tutto, anche le memorie dei Project, senza ritorno. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
7. Metti nella knowledge ciò che deve passare da una chat all'altra del Project: la knowledge vale in tutte le chat del Project, mentre il contesto delle altre chat non è condiviso se non lo si aggiunge alla knowledge; vicino al limite, sui piani a pagamento, passa in modalità RAG. [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
8. Aggiorna a mano la knowledge che viene da GitHub («Sync now» o icona Sync); un documento Google aggiunto da Drive, possibile solo nei Project privati, resta sincronizzato con la versione su Drive. [Verificato] · T1 · <https://support.claude.com/en/articles/10167454-using-the-github-integration>; <https://support.claude.com/en/articles/10166901-use-google-workspace-connectors>
9. Per un documento-memoria scritto da Claude usa i connettori Google nominando Google in modo esplicito: Claude crea e modifica documenti, fogli e presentazioni in un riquadro accanto alla chat (web su Chrome o Claude Desktop con il browser integrato) e salva file su Drive; la pagina non descrive scritture fatte da sole, senza richiesta. [Verificato] sulle capacità · [Inferenza] sull'assenza di scritture autonome · T1 · <https://support.claude.com/en/articles/10166901-use-google-workspace-connectors>
10. Controlla i permessi di scrittura: nella casella di testo la modalità è «Auto» (predefinita su Pro, Max, Ultra e Team) o «Manual» (predefinita su Enterprise), più «Skip all approvals»; per ogni strumento di un connettore valgono «Always allow», «Needs approval» o «Blocked» (Customize > Connectors > connettore > «Tool permissions»); la pagina sui connettori colloca questa impostazione tra i poteri dell'owner di Team ed Enterprise. [Verificato] · T1 · <https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork>; <https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities>
11. Una cartella locale serve da archivio scritto, non da memoria automatica: Claude legge e scrive solo nelle cartelle collegate, solo con Claude Desktop aperto, e chiede prima di cancellare file in modo definitivo; nessuna pagina dice che rilegga i file da solo a ogni conversazione. [Verificato] sull'accesso · [Inferenza] sulla lettura automatica · T1 · <https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork>; <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>
12. Non contare sulla memoria delle attività di Cowork eseguite solo sul computer: resta con quelle attività, e le sessioni locali non usano la memoria delle chat. [Verificato] · T1 · <https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude>; <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
13. Scrivi nel prompt di un'attività programmata, o nelle Istruzioni del Project, ciò che deve sapere: un'attività creata nel Project gira con il contesto del Project, le Istruzioni del profilo valgono anche nelle attività, ma nessuna pagina nomina la memoria del Project. [Verificato] su contesto e Istruzioni · [Inferenza] sulla memoria · T1 · <https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context>; <https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork>
14. Non cercare una precedenza ufficiale tra memoria, Istruzioni del profilo, Istruzioni del Project, stili e knowledge: la pagina sulla personalizzazione dice che le funzioni si usano da sole o insieme e non fissa un ordine; tieni ogni informazione in una sola casa. [Verificato] l'assenza · [Inferenza] la regola · T1 · <https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features>
15. Non far salvare in memoria testo preso da pagine esterne senza rileggerlo: secondo un preprint, una sola scrittura avversaria influenza a lungo un agente e le difese contro la prompt injection non coprono l'avvelenamento della memoria. [Inferenza] · T1 (preprint, agenti non Claude) · <https://arxiv.org/abs/2606.04329>

## Stato dell'arte

### A. Memoria dell'account e dei Project
- Due esperienze convivono: quella nuova, per argomenti salvati durante la chat, e quella legacy, con una sintesi quotidiana più una sintesi per Project. [Verificato] T1 · help 11817273
- Dal 25 agosto 2026 la memoria vale in chat e in Cowork nel cloud; gli argomenti stanno sotto Topics e si modificano o cancellano. [Verificato] T1 · [release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Percorsi della memoria nuova: Settings > Your Claude > «Manage» accanto a «Your memory» (leggere, modificare, «Delete»); «Memory from chats» (accesa o spenta); «Include sensitive topics in memory». Percorsi vecchi: Settings > Memory > «Generate memory from chats»; legacy: Settings > Capabilities. [Verificato] T1 · help 11817273
- Schermata dell'app Claude per Windows dell'utente, 1 novembre 2026: Impostazioni ha una voce «Memoria» tra le Preferenze, con «Ricerca e consultazione delle chat», «Genera memoria dalle chat», «Includi argomenti sensibili nella memoria», «Importa memoria da altri provider AI» («Avvia importazione»), «Esporta memoria» («Esporta», archivio .zip di file Markdown), le sezioni «Tu» e «Argomenti» e una casella per chiedere modifiche. Corrisponde al percorso «vecchio» delle pagine d'aiuto (Settings > Memory). Nella stessa schermata non c'è una voce Your Claude. [Inferenza] una sola osservazione
- Pausa: Claude tiene la memoria ma non la usa né ne crea; le chat della pausa non si aggiungono dopo. [Verificato] T1 · help 11817273
- Memoria spenta per una chat: «+» > «Memory» prima del primo messaggio, non si cambia dopo; vale anche nei Project; la chat resta nella cronologia e nella ricerca. [Verificato] T1 · help 11817273
- Cowork: nel cloud Claude parte da ciò che ricorda delle chat e ciò che emerge in un'attività torna alla chat; la scelta si fa all'avvio dell'attività. [Verificato] T1 · [help 13345190](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- Spostando i Project locali di Cowork sull'account, passa una copia della memoria se la memoria è accesa; cartelle e file restano sul computer. [Verificato] T1 · [help 14116274](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- Conservazione: con una retention personalizzata (Enterprise) il periodo vale anche per la memoria, salvo quella dei Project, che si cancella con il Project. [Verificato] T1 · help 11817273

### B. Cosa vede una chat nuova dentro un Project
| Fonte | La vede sempre? | Per cosa conviene | Prova |
|---|---|---|---|
| Istruzioni del Project | Sì, in ogni chat e attività del Project | Regole | help 9519177; Academy |
| Istruzioni del profilo | Sì, in ogni conversazione e attività | Preferenze generali | help 10185728; Academy |
| Knowledge del Project | Sì, in ogni chat (RAG vicino al limite) | Fatti e documenti | help 9519177 |
| Memoria del Project e dell'account | Quando pertinente; non garantita | Dettagli minori | help 11817273; [Segnale] interno del 25-ott |
| Chat precedenti del Project | Solo se Claude le cerca (piani a pagamento) | Riprendere un filo | help 11817273 |
| Cartella locale del Project | Accessibile, con Claude Desktop aperto; lettura automatica non documentata | File di lavoro | help 13345190; Academy |

### C. Scrivere un documento-memoria
- Connettori Google: creazione e modifica dal vivo di documenti, fogli e presentazioni; caricamento e salvataggio su Drive (serve «Create and edit files» attivo). Per Gmail e per condividere, spostare o cestinare su Drive serve l'approvazione, di default; la pagina dice anche che ogni azione per conto dell'utente richiede approvazione esplicita. Claude rilegge il documento prima di ogni modifica. [Verificato] T1 · help 10166901
- Notion: nessuna pagina letta in questa run. Nessuna prova trovata.
- Artifact e documenti dell'app (Docs, Slides, Design): si salvano nella scheda «Artifacts», raggiungibile da ogni conversazione; si modificano chiedendo a Claude o a mano («Edit with Claude»); possono tenere dati tra le sessioni. La pagina non dice se Claude modifichi un artifact da un'altra chat né se lo legga nelle chat successive. [Verificato] T1 · [help 17153992](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- Cartella collegata: Claude legge e scrive solo lì; i file creati compaiono accanto alla conversazione; serve Claude Desktop aperto. Le «Folder instructions» di una cartella si gestiscono nel pannello Customize di Claude Desktop e Claude le può aggiornare da solo durante la sessione. [Verificato] T1 · help 13345190; help 16761823; [guida Cowork](https://claude.com/resources/guides/claude-cowork-product-guide/getting-started)
- Permessi: tabella di help 13345190. In «Manual» gli strumenti «Always allow» passano e gli altri chiedono; in «Auto» passano gli strumenti di sola lettura e per scrittura e cancellazione decide Claude, con un controllo di sicurezza; in «Skip all approvals» passa tutto tranne «Blocked». Su Team ed Enterprise l'organizzazione può imporre l'approvazione per ogni scrittura. [Verificato] T1 · help 13345190
- Un'istruzione del Project che chieda di aggiornare un documento in ogni chat: nessuna pagina ne parla. [Inferenza] le Istruzioni arrivano a ogni chat, ma ogni scrittura passa dai permessi del connettore e nulla garantisce che Claude la faccia senza richiesta.

### D. Cartella locale e attività programmate
- Cartella: il Project di Cowork contiene Istruzioni, attività programmate, contesto (cartella locale, Project di chat collegato o URL) e memoria; ogni conversazione del Project ha accesso alle cartelle di contesto. La guida Cowork dice che Claude non vede file finché non si collega una cartella. [Verificato] T1 · help 14116274; Academy; guida Cowork
- Le attività che usano file o app del computer richiedono Claude Desktop aperto; un'attività programmata che chiede file locali gira solo in locale. [Verificato] T1 · help 16761823; [help 13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- Attività programmate: ogni esecuzione è una sessione Cowork a sé; usano connettori, skill, plugin e i file salvati nell'account; nel Project girano con il contesto del Project. Nessuna pagina dice se leggano o scrivano la memoria del Project, o se aggiornino un documento senza che il prompt lo chieda. Il resto sta in `D:\Workspace\best_practice\5_attivita\rapporto_attivita.md`. [Verificato] T1 · help 13854387; Academy

### E. Import ed export
- Import (tutti i piani, web e Claude Desktop): Settings > Your Claude > «Start import» (nell'app per Windows dell'utente: Impostazioni > Memoria > «Avvia importazione»), incolla il testo esportato dall'altro assistente, «Add to memory»; la memoria aggiornata compare poco dopo, con «See what Claude learned about you» per controllare (legacy: fino a 24 ore). Funzione sperimentale: Claude può non incorporare tutto, e tiene soprattutto temi di lavoro. [Verificato] T1 · [help 12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)
- Export: Settings > Your Claude > «Manage» accanto a «Your memory» (nell'app per Windows dell'utente: Impostazioni > Memoria > «Esporta», che scarica un archivio .zip di file Markdown [Inferenza], formato non descritto dalle pagine), oppure chiedere in chat di trascrivere le memorie parola per parola e salvarle in un file. Le memorie sono incluse anche nell'esportazione della cronologia. [Verificato] T1 · help 12123587; help 11817273

### F. Piani, incognito, chat condivise
- Memoria accesa di default su Free, Pro, Max e Ultra (web, Desktop, mobile). Su Team ed Enterprise l'owner la abilita in Organization settings > Capabilities, ma ogni membro decide per sé; l'owner non vede le memorie altrui; spegnerla per l'organizzazione cancella subito tutte le memorie. Non disponibile con accordi HIPAA o del settore pubblico. [Verificato] T1 · help 11817273
- Incognito (tutti i piani, icona a forma di fantasma in una chat nuova fuori Project): niente memoria, niente cronologia, niente ricerca. Su Team ed Enterprise restano almeno 30 giorni e finiscono nelle esportazioni. Nell'app unificata le chat in incognito aprono l'esperienza precedente. [Verificato] T1 · help 11817273; help 16761823
- Chat condivise: l'istantanea contiene i messaggi fino alla condivisione e gli artifact, non i file allegati; si gestiscono in Settings > Privacy > «Manage» accanto a «Shared chats». La pagina non parla di memoria. [Verificato] T1 · [help 10593882](https://support.claude.com/en/articles/10593882)

### G. Rischio: avvelenamento della memoria
- [2606.04329](https://arxiv.org/abs/2606.04329) (preprint, v2 del 18-giu-2026, abstract riletto il 1-nov): quattro canali di scrittura in memoria, nove vulnerabilità, sei classi di attacco, benchmark MPBench; una sola scrittura avversaria può influenzare a lungo il comportamento; le difese esistenti contro la prompt injection non coprono questi attacchi. Agenti studiati diversi da Claude. [Verificato] sull'abstract
- La pagina sulla memoria dice solo che Anthropic applica salvaguardie e valutazioni alla memoria, senza dettagli. [Verificato] T1 · help 11817273

### H. Novità recenti
- Release notes dell'app, ultima voce 2026-10-21: nessuna voce sulla memoria dopo il 25 agosto. [Verificato] T1 · release notes
- Changelog di Claude Desktop (sezione «Cowork», v4.29.0 del 2026-10-27): corretto il caso in cui la memoria non si poteva mettere in pausa con Cowork spento; le impostazioni della memoria passano in Settings > General. [Verificato] T1 · [changelog](https://claude.com/docs/cowork/changelog)
- Altre voci sulla memoria nel changelog (import da Claude per le installazioni «3P», di terze parti) non riguardano un account personale. [Inferenza] T1 · changelog

## Tabella conflitti
| Tema | Fonte A | Fonte B | Stato |
|---|---|---|---|
| Dove stanno le impostazioni della memoria | help 11817273, 12123587: Settings > Your Claude nel layout nuovo, Settings > Memory in quello vecchio (T1) | changelog v4.29.0, 2026-10-27: Settings > General (T1) | Chiuso in parte: nell'app per Windows dell'utente, il 1 novembre, è Impostazioni > Memoria, cioè il layout vecchio [Inferenza, una schermata]; il percorso dipende dal layout dell'account |
| Dove vive un Project di Cowork | guida «Organize work with projects»: solo sul computer, non sincronizzato (T1) | help 14116274: con l'app unificata i Project locali passano sull'account (T1) | Risolto a favore di help 14116274 per l'app unificata [Inferenza]: la guida descrive Cowork prima dell'unificazione |
| Chi imposta «Always allow», «Needs approval», «Blocked» | help 11176164: l'owner di Team ed Enterprise, per tutta l'organizzazione (T1) | help 13345190: tabella valida per tutti, senza piani (T1) | Aperto: per Pro e Max nessuna pagina lo dice in modo esplicito |
| Approvazione delle modifiche a un documento Google | help 10166901: ogni azione richiede approvazione esplicita (T1) | stessa pagina: per documenti, fogli e presentazioni non descrive un passo di approvazione (T1) | Aperto |
| Memoria che nasce dall'esperienza | memoria nuova: argomenti durante la chat (T1) | memoria legacy: sintesi ogni 24 ore (T1) | Coerente: dipende dall'account; si capisce dal menu (Your Claude o Capabilities) |

## Cosa non è stato verificato
- Dopo quanto tempo, in minuti, una chat nuova veda una memoria appena scritta: la pagina dice solo «dalla conversazione successiva». Si prova dicendo «ricorda che…» e aprendo subito una chat nuova.
- Se le attività programmate di un Project leggano o scrivano la memoria del Project (help 13854387, 14116274 e Academy non lo dicono).
- Se un'istruzione del Project basti perché Claude aggiorni un documento in ogni chat senza richiesta: nessuna prova; si prova con un Project di test e un documento Google.
- Se Claude rilegga da solo i file della cartella locale a ogni conversazione (pagine controllate: help 14116274, 13345190, 16761823, guida Cowork, guida «Organize work with projects», Academy).
- Notion come documento-memoria: nessuna pagina letta.
- Se Claude modifichi un artifact da un'altra chat o lo legga nelle chat successive (help 17153992 tace).
- Memoria e chat condivise (help 10593882 tace).
- Se Impostazioni > Memoria valga per tutti gli account o solo per quello dell'utente; quando l'account passerà al layout Your Claude.
- Dove stiano le Istruzioni del profilo nel layout dell'utente: per le pagine d'aiuto, nel layout vecchio, Settings > Account; non verificato sulla schermata.
- La prova del 25 ottobre non è stata ripetuta.
- Il changelog di Claude Desktop è stato letto solo per i primi 100.000 caratteri (voci dal 2026-09-17 al 2026-10-29).

## Fonti per Tier
**Tier 1.** support.claude.com: [11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) · [16761823](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) · [14116274](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) · [13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) · [13345190](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) · [11176164](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) · [13730515](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access) · [10166901](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors) · [10167454](https://support.claude.com/en/articles/10167454-using-the-github-integration) · [12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude) · [17153992](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) · [10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) · [10593882](https://support.claude.com/en/articles/10593882) · [12138966](https://support.claude.com/en/articles/12138966-release-notes). claude.com: [changelog di Cowork](https://claude.com/docs/cowork/changelog) · [Organize work with projects](https://claude.com/docs/cowork/guide/projects) · [guida Cowork](https://claude.com/resources/guides/claude-cowork-product-guide/getting-started). academy.claude.com: [Standing context](https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context). arXiv (preprint): [2606.04329](https://arxiv.org/abs/2606.04329).
**Tier 2.** Nessuna fonte usata.
**Tier 3.** Nessuna fonte usata. Guide di terzi viste nei risultati di ricerca (per esempio che Claude salvi un `memory.md` nella cartella del Project, o che le attività programmate girino solo con Claude Desktop aperto) non sono state tenute: contraddette o non confermate dalle pagine T1.

## Guida
Le istruzioni d'uso per Claude e i passi per l'utente stanno in `D:\Workspace\best_practice\4_memoria\guida_memoria.md`.
