---
tema: istruzioni di un Project di Claude (chat dell'app) e rapporto con conoscenza, memoria, profilo, CLAUDE.md
versione: 1
base: a39fbc2
verificato_il: 2026-10-26
rivalutare_se: "nuovo modello Claude, per esempio Opus 5.6; release notes dell'app o dei Project che toccano Istruzioni, memoria, connettori; oppure 2026-12-18"
versioni_rilevate:
  modelli: "claude-fable-5-1, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5 (pagina models overview, senza date). Lanci dalle release notes dell'app: Opus 5.5 il 2026-09-22, Sonnet 5.5 il 2026-09-28, Haiku 5.5 il 2026-10-07. Opus 5.6 e Sonnet 5.6 non compaiono"
  projects: "due versioni: classica (chat e Cowork, la maggior parte degli utenti) e beta in Claude Code (Pro e Max, non Team né Enterprise); entrambe descritte nelle pagine ufficiali del 2026-10-26"
  ultime_voci: "release notes dell'app: 2026-10-21 (Claude Duet); release notes della piattaforma: 2026-10-23. Nessuna voce su Project o memoria dopo il 2026-08-25"
---

# Istruzioni di un Project: stato al 26 ottobre 2026 (v1)

Prima passata del tema 2, da `main` (`a39fbc2`). Non rifà i temi chiusi: [comportamento.md](comportamento.md) (CLAUDE.md, AGENTS.md) e [memoria.md](memoria.md). Tag: [Verificato] [Inferenza] [Obsoleto/Conflitto] [Segnale T3]. Quasi tutte le pagine ufficiali non hanno data (solo «Updated this week»): la data è quella della lettura, salvo dove indicato. Le letture passano da uno strumento che restituisce riassunti: i virgolettati sono quelli visti nel testo ricevuto.

## Risposta breve
- Le Istruzioni di un Project valgono per tutte le chat di quel Project e solo per quelle. Il nome e la descrizione del Project non arrivano a Claude.
- Per i Project classici nessuna pagina ufficiale dichiara un limite di lunghezza. Il tetto di 16.000 caratteri esiste solo nei Projects beta di Claude Code.
- Nessuna pagina ufficiale dice quale fonte vince tra Istruzioni del Project, istruzioni del profilo, memoria e stili: ricontrollato oggi su cinque pagine, nessuna precedenza.
- Le fonti ufficiali sul come scriverle sono scarse: la guida pratica è quella di prompting generale (chiare, motivate, in positivo, esempi diversi, enfasi rara).
- Più regole, aderenza minore: due preprint recenti misurano il calo (solo abstract letti, modelli 4.6 o senza nome), non su Claude 5.5.
- Haiku 5.5 con prompt lunghi tende a saltare passi o fermarsi presto (pagina ufficiale): per compiti con molte regole o controlli serve un modello più forte.
- Opus 5.6 e Sonnet 5.6: non risultano usciti al 26 ottobre. Rivalutare tutto quando escono.

## REGOLE OPERATIVE PER AGENTI
1. Scrivi nelle Istruzioni del Project ciò che deve valere in ogni chat del Project: si applicano a tutte le chat del Project e a nessuna fuori. [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
2. Non affidare nulla al nome o alla descrizione del Project: Claude non li vede. Ogni informazione necessaria va nelle Istruzioni o nella knowledge. [Verificato] · T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
3. Istruzioni = come Claude si comporta; knowledge = materiale a cui attinge. Fatti che cambiano e schemi lunghi vanno nei documenti, non nelle Istruzioni. [Verificato] per la divisione · T1 · <https://academy.claude.com/courses/claude-101/introduction-to-projects>
4. Sui Project classici non c'è un limite ufficiale di lunghezza; 16.000 caratteri valgono solo per i Projects beta di Claude Code. Tieni comunque le Istruzioni brevi: il numero è un'inferenza dal calo di aderenza misurato e dai consigli sul minimo. [Verificato] per i limiti; [Inferenza] per la brevità · T1 · <https://code.claude.com/docs/en/claude-projects>
5. Nessuna precedenza ufficiale tra Istruzioni del Project, profilo, stili e memoria: non scrivere la stessa regola in due posti e non creare regole opposte. Se due fonti si sovrappongono, di' nelle Istruzioni quale vince. [Verificato] per il silenzio; [Inferenza] per il consiglio · T1 · <https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features>
6. Una regola che deve valere sempre va nelle Istruzioni (o in `CLAUDE.md` per Code), non solo nella memoria. [Segnale] interno del progetto (prova dell'utente del 25 ottobre con Haiku 5.5, una sola prova) coerente con le docs: le memorie di Project sono note che Claude consulta. [Inferenza] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
7. Scrivi come a un collega nuovo: esplicito, specifico, con il motivo; di' cosa fare invece di cosa evitare. Test: se una persona con poco contesto sarebbe confusa, lo sarà anche Claude. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>
8. Niente «CRITICAL» o «MUST» diffusi: i modelli recenti reagiscono troppo al system prompt; attenua il linguaggio e rimuovi l'eccesso di regole. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>
9. Se servono esempi, 3-5, diversi tra loro, in tag coerenti; meglio pochi esempi canonici che un elenco di casi limite. [Verificato] · T1 · <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
10. Parti da Istruzioni minime e aggiungi solo dopo un errore osservato; «minimale» non vuol dire «corto». Il post è del 2025-09-29 (oltre 12 mesi) ma concorda con la pagina di prompting corrente. [Verificato] come consiglio · T1 · <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
11. Di' cosa fare se manca qualcosa (un file, un dato, un accesso): dire che cosa manca e fermarsi, senza sostituire né indovinare. L'esempio ufficiale è per i Projects di Code; per le chat dell'app è un trasferimento. [Verificato] come esempio; [Inferenza] per il trasferimento · T1 · <https://code.claude.com/docs/en/claude-projects>
12. Per Project con GitHub, premi «Sync now» dopo ogni modifica: si sincronizzano solo nomi e contenuti dei file di un branch, e devono stare nella finestra di contesto. Un documento Google aggiunto da Drive si aggiorna da solo, ma solo nei Project privati e solo come testo. [Verificato] · T1 · <https://support.claude.com/en/articles/10167454-using-the-github-integration>
13. Con prompt lunghi o molte regole non affidarti a Haiku 5.5: salta passi o si ferma prima; per l'aderenza Anthropic suggerisce una frase («le regole valgono per tutta la conversazione») e effort alto, impostazioni che l'app non sempre espone. [Verificato] per la pagina; [Inferenza] per l'app · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5>
14. Sessioni di Code e Cowork non ereditano da sole i Project di chat: un Project di Code manda le Istruzioni a ogni thread (anche locale) ma la memoria solo ai thread cloud; un Cowork project vive sul computer e può collegare un Project di chat per la sua knowledge. Nessuna pagina dice che le Istruzioni di un Project di chat arrivino a una sessione Code. [Verificato] · T1 · <https://claude.com/docs/cowork/guide/projects.md>
15. A ogni nuovo modello rileggi le Istruzioni, togli ciò che serviva ai modelli vecchi e rifai le tue prove (Opus 5.5: «rifai le mitigazioni»; Sonnet 5.5: nuova serie di eval). Opus 5.6 e Sonnet 5.6 non sono usciti. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5>

## Stato dell'arte

### A. Cosa sono e come funzionano
- Dove: pulsante «Set project instructions» nella pagina principale del Project; valgono per tutte le chat del Project. La pagina non dà limiti di lunghezza né esempi. [Verificato] T1 · [create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Nome e descrizione: Claude non ci ha accesso. Il corso Academy dice lo stesso della descrizione (parafrasi). [Verificato] T1 · stessa pagina; [Academy](https://academy.claude.com/courses/claude-101/introduction-to-projects)
- Piani: Project per tutti, Free compresi (massimo cinque); RAG sui piani a pagamento (Pro, Max, Team, Enterprise); condivisione («Can view», «Can edit») su Team ed Enterprise, con interruttore dell'amministratore. [Verificato] T1 · create and manage projects; [RAG](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) (2026-09-10)
- Knowledge: usata in ogni chat del Project; il contesto non passa da una chat all'altra se non è nella knowledge. Vicino al limite di contesto scatta il RAG (fino a 10x di capacità, non regolabile); la pagina RAG non dice se le Istruzioni ci rientrino. File con nomi descrittivi, citati per nome. [Verificato] T1 · RAG; create and manage projects
- Versioni: la classica (chat e Cowork) resta com'è; la beta in Claude Code (una conversazione che coordina thread cloud, Pro e Max) ha memoria di Project e Istruzioni fino a 16.000 caratteri. I progetti spostati nella beta mantengono Istruzioni, file, cronologia. [Verificato] T1 · [what are projects](https://support.claude.com/en/articles/9517075-what-are-projects) · [claude-projects](https://code.claude.com/docs/en/claude-projects) · [projects redesigned](https://claude.com/resources/articles/projects-redesigned) (2026-09-17)
- Drive: un documento Google si aggiunge da Files > «+» > Drive, si sincronizza con la versione più recente, solo nei Project privati, solo testo (immagini ignorate, commenti visibili). [Verificato] T1 · [Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- GitHub: «+» > GitHub, selezione di file e cartelle; «Sync now» riporta l'ultima versione; si sincronizzano solo file (nomi e contenuti) di un branch, niente cronologia né PR; devono stare nel contesto. [Verificato] T1 · [GitHub integration](https://support.claude.com/en/articles/10167454-using-the-github-integration)
- Nota: la pagina 9519177 non tratta Drive né GitHub né «Sync now», contrariamente a quanto indicava il prompt di questa notte: stanno nelle due pagine sopra.

### B. Istruzioni, conoscenza, memoria, profilo, stili
| Cosa | Dove vale | Fonte |
|---|---|---|
| Istruzioni del profilo («Instructions for Claude», Settings > Your Claude) | Tutte le conversazioni | [personalization](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) |
| Istruzioni del Project | Solo le chat di quel Project | personalization; create and manage projects |
| Knowledge del Project | Materiale consultato in ogni chat del Project | create and manage projects |
| Memoria | Una per Project; il Project usa la sua più quella delle chat fuori Project, mai quella di altri Project | [memoria](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) |
| Skill | Comportamenti caricati su richiesta | personalization |
| Stili | Non trattati dalla pagina di personalizzazione; il system prompt pubblicato di Sonnet 5.5 dice che lo stile di scrittura si imposta con la funzione stili | [system prompt Sonnet 5.5](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-5-5) |
- Precedenza: la pagina di personalizzazione dice che le funzioni si usano «independently or in combination», senza risolvere i conflitti; Academy dice che le Istruzioni «work alongside» preferenze e stili; la pagina sulla memoria non nomina Istruzioni né profilo; il system prompt di Sonnet 5.5 non parla di Project né di precedenza. Nessuna precedenza dichiarata. [Verificato] T1 per il silenzio
- Memoria e Istruzioni: la memoria creata in un Project resta in quel Project e può comparire anche nelle chat fuori Project se la memoria è attiva; «Use account memory» isola il Project; la pagina non dice se l'interruttore tocchi le Istruzioni. Novità rispetto a [memoria.md](memoria.md): la frase sulla memoria di Project che compare fuori dai Project. [Verificato] T1 · pagina memoria
- Incoerenza ufficiale: la pagina di personalizzazione dice sia «Project per tutti» sia, nella sezione di scelta, che le Istruzioni di Project sono «solo per i piani a pagamento». Vedi tabella conflitti. [Obsoleto/Conflitto]
- Il system prompt pubblicato dice che tono, formato e funzioni personali vanno nelle preferenze dell'utente. [Verificato] T1 · system prompt Sonnet 5.5 (versioni del 2026-10-07 e del 2026-09-28, testo uguale per questo punto)

### C. Scrivere buone istruzioni
Cosa dimostra la fonte e cosa è un consiglio: le fonti ufficiali non misurano le Istruzioni di un Project; sono consigli di Anthropic, validi per i system prompt in generale.
- Chiarezza: «Think of Claude as a brilliant but new employee»; il test del collega con poco contesto. Consiglio. [Verificato] T1 · [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Positivo, non negativo; motivo della regola («Claude can generalize from the explanation»); l'esempio ufficiale sostituisce «NEVER use ellipses» con la spiegazione della lettura vocale. Consiglio. [Verificato] T1 · stessa pagina
- Enfasi: i modelli recenti rispondono di più al system prompt e possono «overtrigger»; «soften any aggressive language»; «If in doubt, use [tool]» sovra-attiva. Consiglio con osservazione di Anthropic. [Verificato] T1 · stessa pagina
- Esempi: «Include 3–5 examples for best results», vari; tag XML coerenti per dividere le parti; un ruolo in una frase. Consiglio. [Verificato] T1 · stessa pagina
- Documenti lunghi in alto e domanda in fondo: fino al 30% in più nei test della pagina. Misura di Anthropic, per contesti lunghi in un prompt, non per le Istruzioni. [Verificato] T1 · stessa pagina
- Altezza giusta: «The right altitude is the Goldilocks zone»; sezioni distinte con tag XML o intestazioni Markdown; il minimo che descrive il comportamento, non necessariamente corto; si parte da un prompt minimo e si aggiunge dopo i fallimenti; esempi canonici invece di casi limite. Consigli del 2025-09-29 (oltre 12 mesi), concordi con la pagina corrente. [Verificato] come consiglio, T1 · [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Contesto lungo: «context rot», il recupero cala con i token nella finestra; descritto come risultato di studi citati, non misurato su Claude 5.5. [Verificato] T1 · stesso post
- Academy: istruzioni specifiche; elenco di quattro voci nell'articolo (contesto, processo, tono e stile, requisiti), cinque nel video (tono, competenza, stile di risposta, esiti, contesto). Esempi: «Use a professional but conversational tone»; un flusso di riassunto di trascrizioni. Parafrasi. [Verificato] T1 · [Academy](https://academy.claude.com/courses/claude-101/introduction-to-projects)
- Per i Projects beta di Code, la guida ufficiale elenca cinque voci: a che serve il Project; dove avviene il lavoro (repository, branch); come un thread controlla il lavoro prima di dire «fatto»; cosa fare se manca qualcosa; cosa chiede il tuo via libera. [Verificato] T1 · [claude-projects](https://code.claude.com/docs/en/claude-projects)
- «Outdated instructions are worse than none»: detto per CLAUDE.md (pagina del 2026-04-15), applicabile per analogia. [Verificato] T1; [Inferenza] per l'analogia · [Give Claude context](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts)

### D. Project e Claude Code / Cowork
- Projects beta in Code: le Istruzioni (fino a 16.000 caratteri) vanno a ogni nuovo thread e alla conversazione; la memoria (`MEMORY.md`) la leggono i thread cloud, non quelli locali; i thread cloud leggono il `CLAUDE.md` dei repository ma non le loro skill, `.mcp.json` o `settings.json`. Regole su un repository vanno nel suo `CLAUDE.md`, note sul Project nella memoria. [Verificato] T1 · [claude-projects](https://code.claude.com/docs/en/claude-projects) (letta con grep e sezioni, vedi non verificato)
- Un thread locale «starts with the project's instructions, but not with its memory files loaded». [Verificato] T1 · stessa pagina
- Cowork project (guida): vive sul computer, non è sincronizzato né condiviso; ha descrizione, cartelle, Istruzioni, link, memoria; si può «linkare» un Project di chat perché le sessioni Cowork attingano alla sua knowledge. Nessuna frase dice se le Istruzioni del Project collegato vengano lette. [Verificato] T1 · [Cowork guide](https://claude.com/docs/cowork/guide/projects.md)
- Cowork project (Help Center): importare un Project di chat ne copia file e Istruzioni in un Cowork project (è un trasferimento, non un collegamento); condivisione Team ed Enterprise; progetti locali spostati nell'account. [Verificato] T1 · [Cowork projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) · conflitto con la guida: vedi tabella.
- Chat e Cowork unificate dal 2026-09-16 (rollout graduale): «Projects work in every conversation», le Istruzioni globali di Cowork sono confluite in «Instructions for Claude». [Verificato] T1 · [one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) · release notes
- Sessione Code cloud fresca: vede solo il repository; per i fatti già verificati rimando a [memoria.md](memoria.md). Nessuna prova trovata che le Istruzioni di un Project di chat arrivino a Code.

### E. Prove e studi
| Fonte | Cosa dimostra | Cosa non dimostra | Tag |
|---|---|---|---|
| [arXiv 2608.02639](https://arxiv.org/abs/2608.02639) (preprint, 2026-07-31) | Benchmark con 24 istruzioni verificabili, impilate da 1 a 20: l'aderenza scende da circa 96% a 20% con Sonnet 4.6, GPT-5-mini, Gemini 2.5 Flash; il calo viene da conflitti a coppie; riscrivere il prompt («compilazione») dà fino a circa 11 punti ai modelli deboli, nulla ai forti | Non Claude 5.5; compiti sintetici; abstract soltanto | [Verificato] sull'abstract |
| [arXiv 2607.19257](https://arxiv.org/abs/2607.19257v1) (preprint, 2026-07-21) | Cinque modelli senza nome: da 10 a 160 regole l'aderenza cala, le risposte perfette sono zero da 80 regole; nessun vantaggio affidabile del Markdown; oltre 64k-128k token il recupero cala | Modelli non nominati: non si sa se ci siano modelli Claude | [Verificato] sull'abstract |
| [arXiv 2604.09443](https://arxiv.org/html/2604.09443v2) (preprint, 2026-04-13) | ManyIH: con fino a 12 livelli di priorità i modelli di punta sono intorno al 40%; Opus 4.6 51,3% e Sonnet 4.6 39,1% sul codice; il formato della priorità conta | Non è il caso Project/profilo; modelli 4.6 | [Verificato] sul riassunto dello strumento |
| [arXiv 2404.13208](https://arxiv.org/abs/2404.13208) (OpenAI, 2024) | Un modello può imparare a dare priorità alle istruzioni di livello più alto | Nessuna misura su Claude né sui Project | [Verificato] sull'abstract |
- Già in [comportamento.md](comportamento.md) (non riletti qui): 2602.11988 (file di contesto non migliorano il successo, costo +20%) e 2507.11538 (IFScale). Citati solo per rimando.
- Istruzioni in negativo: nessuna prova trovata di una misura su «non fare X» contro «fai Y»; pagine controllate: best practices, context engineering, i tre arXiv sopra (solo abstract). Il consiglio «dì cosa fare» di Anthropic resta un consiglio. [Inferenza]
- Effetto di un cambio di modello: le guide ufficiali dicono di rifare i test (Sonnet 5.5: «Run a fresh sweep against your own evals»); nessuna misura pubblica sui Project. [Verificato] T1 · [Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- [Segnale] interno, non fonte: il 25 ottobre l'utente ha provato (chat dell'app, Haiku 5.5) che una regola di formato salvata solo nella memoria del Project non è stata applicata subito dopo, mentre la stessa nelle Istruzioni sì. Una sola prova; descritta in `CLAUDE.md`.
- Per un'interpretazione: [Inferenza] i due preprint sostengono, in modo indiretto, di tenere poche regole per Project; nessuno misura le Istruzioni di un Project.

### F. Un modello piccolo e uno forte
- Haiku 5.5: «In long agent prompts, the model is more likely to skip a search, stop early»; con un prompt lungo a effort `low` a volte si ferma e restituisce il compito; da `low` a `medium` le fermate si dimezzano e i token in uscita più che raddoppiano. Per le chat, una frase come «The rules in this system prompt hold for the whole conversation» ha aumentato l'aderenza nei test di Anthropic; per l'aderenza massima, effort `high`. La pagina non confronta Haiku con Opus. [Verificato] T1 · [Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)
- Sonnet 5.5: tende ad aggiungere test, documenti e file non richiesti e a iniziare a costruire quando si volevano solo idee; blocchi consigliati: «Limit scope», «Ideas before action». I prompt per Sonnet 5 dovrebbero funzionare senza modifiche. [Verificato] T1 · Sonnet 5.5
- Opus 5.5: risponde a istruzioni specifiche e a divieti con nome più che a consigli generici; aggiunte lunghe al system prompt vanno in coda dalla prima richiesta; per le istruzioni da chat «consider removing them». [Verificato] T1 · [Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- Posizionamento: Opus 5.5 «per la maggior parte dei carichi», Sonnet 5.5 miglior equilibrio tra velocità e intelligenza, Haiku 5.5 alto volume e bassa latenza; Fable 5.1 per ragionamento e lavoro lungo. [Verificato] T1 · [models](https://platform.claude.com/docs/en/about-claude/models/overview)
- Nuovi modelli: Opus 5.6 e Sonnet 5.6 non compaiono nella pagina dei modelli, nelle release notes dell'app (ultima voce 2026-10-21), né nella parte letta di quelle della piattaforma (ultima voce 2026-10-23); una ricerca web non ha trovato un rilascio. Nessuna prova trovata. [Verificato] T1 · [release notes dell'app](https://support.claude.com/en/articles/12138966-release-notes) · [release notes della piattaforma](https://platform.claude.com/docs/en/release-notes/overview)
- Come rivalutare: rileggi le Istruzioni, togli ciò che serviva ai modelli vecchi, rifai una piccola serie di domande reali e casi trappola, prima e dopo. [Inferenza] sulle guide di Opus 5.5 e Sonnet 5.5

### G. Raccordo
Vedi la sezione seguente.

### H. Modello di Istruzioni (generico, ≤ 25 righe)
Ogni voce rimanda alle regole sopra; sono tutte [Inferenza] (raccomandazione), costruite su fatti [Verificato] citati.
```text
Scopo: <una frase: per che cosa serve questo Project>.                      (regole 1, 2)
Fonti: i fatti stanno nei documenti del Project; se un dato manca o un
file non si apre, di' che cosa manca e fermati, senza indovinare.            (3, 11)
Se due fonti si contraddicono, vale <fonte A>; dillo.                        (5)
Come lavori:
- <passo 1, con il motivo>
- <passo 2, con il motivo>
Prima di dire «fatto»: <controllo concreto>.                                (11)
Chiedi il mio via libera prima di: <azioni irreversibili o fuori ambito>.
Formato delle risposte: <lingua, lunghezza, forma concreta>.                (7)
Le regole di questo Project valgono per tutta la conversazione.             (13)
<2-3 esempi diversi in tag, solo se servono>                                (9)
```
- Nelle Istruzioni: scopo, ordine delle fonti, flussi, regole decisionali con motivo, comportamento se manca qualcosa, formato, limiti d'azione. (regole 3, 7, 11)
- Nei documenti: schemi, colonne, convenzioni, elenchi lunghi, dati. (regola 3)
- Nella memoria: preferenze emerse e decisioni, non regole che devono valere sempre. (regola 6)
- Nel profilo: lingua e tono validi ovunque; non ripeterli nel Project. (regola 5)
- Dopo ogni modifica: una piccola serie di prove, e a ogni nuovo modello. (regola 15)

## Raccordo con i report precedenti
| Punto | Report | Stato oggi |
|---|---|---|
| Istruzioni = comportamento, knowledge = materiale | [istruzioni_per_progetti.md](istruzioni_per_progetti.md) | Ancora vero (Academy, create and manage projects) |
| Nessun limite ufficiale per i Project classici; 16.000 caratteri solo nella beta | istruzioni_per_progetti.md; [memoria.md](memoria.md) | Ancora vero, riletto (claude-projects, create and manage projects) |
| Nome e descrizione non visibili a Claude | istruzioni_per_progetti.md | Ancora vero (9519177) |
| Nessuna precedenza ufficiale tra profilo, Project, memoria | istruzioni_per_progetti.md; memoria.md | Ancora vero, ricontrollato su cinque pagine |
| Pagina di personalizzazione incoerente sui piani a pagamento | istruzioni_per_progetti.md | Ancora vero (10185728) |
| Enfasi attenuata, esempi 3-5, positivo con motivo | istruzioni_per_progetti.md | Ancora vero (pagina di prompting corrente) |
| Consiglio 400-700 parole | istruzioni_per_progetti.md | Resta [Inferenza]: nessuna fonte ufficiale; non riverificabile |
| Cowork project «non sincronizzato né condivisibile» | istruzioni_per_progetti.md | Contraddetto in parte: il Help Center parla di condivisione Team/Enterprise (vedi conflitti) |
| Project con GitHub: «Sync now» | memoria.md | Ancora vero (10167454); aggiunto: solo un branch, solo file |
| Memoria per Project, mai quella di altri Project | memoria.md | Ancora vero; nuovo: la memoria di Project può comparire fuori dai Project |
| Haiku 5.5 e Sonnet 5.5: guide non lette | [comportamento.md](comportamento.md) | Ora lette (F) |
| Reddit (snapshot di aggregatore), Hacker News, blog, esempio «piante e bonsai» | istruzioni_per_progetti.md | Non riverificati: fonti di Tier 3 o inaccessibili; l'esempio privato non è stato ripreso |

## Tabella conflitti
| Tema | Fonte A | Fonte B | Stato |
|---|---|---|---|
| Istruzioni di Project e piani | Create and manage projects (T1, senza data): Project per tutti, Free compresi | Personalization features (T1, senza data): nella sezione di scelta, Istruzioni di Project «solo piani a pagamento» | Non risolto: provare nell'interfaccia dell'account |
| Cowork project: dove vive | Guida Cowork su claude.com (T1, senza data): sul computer, non sincronizzato né condiviso | Help Center Cowork projects (T1, senza data): condivisione Team/Enterprise, progetti locali spostati nell'account | Non risolto: pagine non datate; la guida può precedere |
| Classico e beta | What are projects (T1): i Project di chat restano come oggi | Projects redesigned (T1, 2026-09-17): i Project esistenti saranno aggiornati con l'estensione del rollout | Conciliabile: dipende dal rollout dell'account; verificare quale versione si ha |
| Enfasi | Prompting best practices (T1): attenuare il linguaggio aggressivo | `Claude Code best-practices` (T1, letto nella notte 02): «IMPORTANT» su una riga | Conciliabile (vedi [comportamento.md](comportamento.md)) |

## Cosa non è stato verificato
- Il limite di lunghezza delle Istruzioni nei Project classici: nessuna pagina lo dichiara; non provato nell'interfaccia.
- Se le Istruzioni di un Project rientrano nel RAG o restano sempre in contesto: la pagina RAG tace.
- Se una sessione Code o Cowork legge le Istruzioni di un Project di chat collegato: nessuna pagina lo dice.
- I preprint: solo abstract o riassunto dello strumento; 2604.09443 letto come riassunto; i modelli sono 4.6 o non nominati, non 5.5.
- La pagina `claude-projects` (60 KB) è stata letta con grep e sezioni, non per intero; la pagina `release-notes/overview` della piattaforma, per i primi 100.000 caratteri su 104.366; la pagina di prompting, per un solo blocco.
- Reddit, Stack Overflow, Hacker News, blog di terzi: non interrogati. Nessun testo reale di Istruzioni di un Project è stato letto da una fonte ufficiale (solo l'esempio di Code).
- Nessuna misura pubblica dell'effetto di un cambio di modello sulle Istruzioni di un Project.

## Fonti per Tier
**Tier 1.** support.claude.com: [9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) · [10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) · [9517075](https://support.claude.com/en/articles/9517075-what-are-projects) · [11473015](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) · [11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) · [10167454](https://support.claude.com/en/articles/10167454-using-the-github-integration) · [10166901](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors) · [14116274](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) · [16761823](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) · [14553240](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts) · [12138966](https://support.claude.com/en/articles/12138966-release-notes). code.claude.com: [claude-projects](https://code.claude.com/docs/en/claude-projects). claude.com e academy: [Cowork guide](https://claude.com/docs/cowork/guide/projects.md) · [projects redesigned](https://claude.com/resources/articles/projects-redesigned) · [Academy](https://academy.claude.com/courses/claude-101/introduction-to-projects). platform.claude.com: [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) · [Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) · [Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) · [models](https://platform.claude.com/docs/en/about-claude/models/overview) · [system prompt Sonnet 5.5](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-5-5) · [release notes](https://platform.claude.com/docs/en/release-notes/overview). anthropic.com: [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). arXiv (preprint): [2608.02639](https://arxiv.org/abs/2608.02639) · [2607.19257](https://arxiv.org/abs/2607.19257v1) · [2604.09443](https://arxiv.org/html/2604.09443v2) · [2404.13208](https://arxiv.org/abs/2404.13208).
**Tier 2.** nessuna fonte usata in questa notte.
**Tier 3.** nessuna fonte usata.

## Guida semplice per l'utente
Per scrivere le Istruzioni di un Project nell'app Claude. Ogni passo ha un esempio.

1. **Che cosa sono.** Sono il foglio di istruzioni di un solo Project: valgono per tutte le sue chat e per nessun'altra. Si aprono dalla pagina del Project, con «Set project instructions».
2. **Il nome e la descrizione del Project Claude non li legge.** Se una cosa serve, scrivila nelle Istruzioni o caricala come documento.
3. **Istruzioni e documenti hanno compiti diversi.** Le Istruzioni dicono come comportarsi («rispondi in italiano, prima la risposta»). I documenti contengono il materiale (elenchi, tabelle, dati).
4. **Scrivi poco e preciso.** Meglio dieci righe chiare che una pagina. Per ogni riga chiediti: se la tolgo, Claude sbaglia? Se no, cancellala.
5. **Di' che cosa fare, non solo che cosa evitare, e spiega perché.** «Scrivi frasi brevi: le leggo dal telefono» funziona meglio di «non scrivere frasi lunghe».
6. **Non gridare.** Evita «ASSOLUTAMENTE» e «SEMPRE» ripetuti: i modelli recenti li prendono troppo alla lettera.
7. **Dì che fare se manca qualcosa.** Per esempio: «Se un file non si apre, dimmelo e fermati».
8. **Una regola, una sola casa.** Non scriverla anche nelle istruzioni del profilo o nella memoria: nessuna pagina dice quale vince, e Claude può seguirne una a caso.
9. **Le regole che contano vanno nelle Istruzioni, non solo nella memoria.** Una prova del 25 ottobre (una sola) ha mostrato che una regola scritta solo nella memoria non è stata applicata subito.
10. **Documenti collegati.** Un documento Google si aggiorna da solo (Project privati). Un repository GitHub si aggiorna solo con «Sync now».
11. **Prova dopo ogni modifica.** Fai 5 o 6 domande vere e 2 o 3 domande a trabocchetto, e leggi le risposte.
12. **Con un modello piccolo (Haiku) le regole lunghe si perdono più facilmente.** Per ricerche e controlli usa un modello più forte.
13. **Quando esce un modello nuovo** (per esempio Opus 5.6, non ancora uscito al 26 ottobre), rileggi le Istruzioni e togli ciò che non serve più.
14. **Code e Cowork non leggono da soli le Istruzioni di un Project dell'app.** Per Code le regole vanno in `CLAUDE.md`, ad esempio `D:\Workspace\best_practice\CLAUDE.md`.
