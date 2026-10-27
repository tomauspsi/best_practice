---
tema: memoria nei prodotti Claude (claude.ai, Claude Code, API, sessioni cloud)
versione: 3
base: d0a1c7c
verificato_il: 2026-10-19
aggiornato_il: 2026-10-27 (ripassata finale: 15 regole rilette sulle pagine del giorno; correzioni delle notti 02-05; riordino del repo)
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes che toccano la memoria; oppure 2026-12-18"
versioni_rilevate:
  claude_code: "2.1.303 del 2026-10-18 al 19-ott; 2.1.312 del 2026-10-27 secondo il changelog letto dalla notte 05"
  app_claude_ai: "senza numero di versione; memoria: ultima voce 2026-08-25; ultima voce in assoluto 2026-10-07"
  modelli: "claude-opus-5-5 (2026-09-22), claude-sonnet-5-5 (2026-09-28), claude-haiku-5-5 (2026-10-07, 1M di contesto), claude-fable-5-1 (2026-09-01)"
  api: "memory tool memory_20250818; compaction on demand (2026-09-14); ultima voce delle release notes API riletta: 2026-10-15"
---

# Memoria nei prodotti Claude: stato al 19 ottobre 2026 (v3, conclusiva)

v3 chiude le domande aperte di v2 (base `f1d5d1e`) e v1. Parte da `d0a1c7c` (main). I fatti [Verificato] di v2 sono riusati; sono stati riletti alla fonte quelli citati con frasi nuove.

## Risposta breve
- Le memorie sono cinque e separate: memoria di claude.ai (account e Project), ricerca nelle chat passate, `CLAUDE.md`/`AGENTS.md`, auto memory locale di Claude Code, memory tool dell'API. In più la project memory dei Projects di Claude Code (beta).
- Una sessione cloud fresca (anche da routine) vede il clone del repo, non `C:\Users\<utente>\.claude\CLAUDE.md` né l'auto memory locale. La memoria chat dell'account: nessuna prova nelle docs e, nella prova su questa sessione, nessun blocco di memoria nel contesto. Trattala come assente.
- Non esiste una regola ufficiale di precedenza tra profilo, Project, memoria e `CLAUDE.md`. In Claude Code i file sono concatenati, non sovrascritti: se si contraddicono, Claude può seguirne uno a caso.
- Un Project di chat con GitHub resta aggiornato solo se premi "Sync now".
- La memoria è contesto, non vincolo: per bloccare un'azione servono gli hook.

## REGOLE OPERATIVE PER AGENTI
1. Non assumere che una sessione cloud conosca la memoria dell'account claude.ai: metti il contesto nel prompt o nel repo. [Inferenza] · T1 · le docs non la nominano e una sessione cloud fresca non ne mostrava blocchi: <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
2. Scrivi il prompt di una routine autosufficiente: ogni run è una sessione nuova e non ne riusa altre. [Verificato] · T1 · <https://code.claude.com/docs/en/routines>
3. Metti le istruzioni per il cloud in `./CLAUDE.md` o `./.claude/rules/` del repo e committa skill e agent in `.claude/`: `~/.claude/` dell'utente non arriva nel cloud. [Verificato] · T1 · <https://code.claude.com/docs/en/cloud-environments>
4. Non contare sull'auto memory locale nel cloud: non è condivisa tra macchine né con gli ambienti cloud. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
5. Tieni ogni `CLAUDE.md` sotto le 200 righe (regole di cartella in `.claude/rules/` con `paths`) e metti in cima a `MEMORY.md` ciò che conta: si caricano solo 200 righe o 25 KB. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
6. Se esistono sia `AGENTS.md` sia `CLAUDE.md`, scrivi `@AGENTS.md` dentro `CLAUDE.md` (o imposta `claude-md-and-agents-md` in `/config`): senza import Claude Code legge solo `CLAUDE.md`, e anche un `CLAUDE.local.md` conta come `CLAUDE.md` e spegne la lettura di `AGENTS.md` (pagina riletta il 25-ott). [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
7. Per vincoli di sicurezza usa hook `PreToolUse`, non `CLAUDE.md`, che è contesto e non configurazione imposta. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
8. Non cercare una precedenza ufficiale: ogni informazione ha una sola casa e le istruzioni non si contraddicono; `/doctor prompt-audit` trova conflitti e istruzioni obsolete. [Verificato] per Claude Code; per profilo, Project e memoria nessuna regola trovata [Inferenza] · T1 · <https://code.claude.com/docs/en/memory>
9. In claude.ai isola la memoria con un Project e disattiva "Use account memory" per isolarla del tutto. La ricerca nelle chat passate non attraversa i Project. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
10. Non affidare dati sensibili alla memoria di claude.ai: i temi sensibili sono esclusi di default e cancellare una chat non cancella le memorie derivate. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
11. Non far scrivere in memoria testo preso da pagine esterne senza revisione: nei test dei preprint basta una scrittura avvelenata, e i filtri anti-injection non la intercettano in modo affidabile (migliore: 67,67% di rilevazione, dal testo completo letto il 19-ott; l'abstract della v2 del 18-giu, riletto il 27-ott, conferma che le difese esistenti non coprono l'avvelenamento della memoria). [Inferenza] sui fatti citati · T1 (preprint) · <https://arxiv.org/abs/2606.04329>
12. Con il memory tool dell'API valida ogni path sotto `/memories`, limita dimensione e scadenza dei file e abbinalo alla compaction nelle sessioni lunghe. [Verificato] · T1 · <https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>
13. Nei Projects di Claude Code, metti le regole del repo nel suo `CLAUDE.md` e le note del Project nella project memory: un thread locale riceve le istruzioni del Project ma non i file di memoria. [Verificato] · T1 · <https://code.claude.com/docs/en/claude-projects>
14. Per un Project di chat con un repo GitHub, premi "Sync now" prima di un'analisi: l'aggiornamento non è automatico e si sincronizzano solo nomi e contenuti di un branch. [Verificato] · T1 · <https://support.claude.com/en/articles/10167454-using-the-github-integration>
15. Nelle chat lunghe di claude.ai lascia fare la sintesi automatica (la cronologia resta; richiede l'esecuzione di codice attiva, e la pagina sulla finestra di contesto la lega ai piani a pagamento), tieni brevi le istruzioni e apri una nuova chat vicino al limite d'uso; non esiste una soglia numerica. Pagina riletta il 27-ott con il titolo nuovo «How do usage and length limits work». [Verificato] · T1 · <https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work>

## Stato dell'arte (compresso)

### A. claude.ai (Chat e Project)
- Dal 10-lug-2026 la memoria è un insieme di voci per categoria (prima: sintesi ogni 24 ore). [Verificato] T1 · [release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Ogni Project ha la sua memoria e usa anche quella delle chat fuori Project, mai quella di altri Project. Al contrario, la memoria creata in un Project può comparire anche nelle chat fuori Project se la memoria è attiva; «Use account memory» isola il Project (pagina riletta il 26-ott). Controlli: pausa, reset irreversibile, spegnimento per chat, topic modificabili, import sperimentale ed export. Attiva di default su Free, Pro, Max; su Team ed Enterprise l'owner decide se è disponibile, ma resta spenta per ogni membro finché il membro non la attiva (pagina riletta il 27-ott). Menu: Settings > Your Claude, «Manage» accanto a «Your memory». [Verificato] T1 · help 11817273
- Cowork: dal 25-ago-2026 la memoria vale in chat e Cowork cloud; Cowork locale non la usa. Ricerca nelle chat passate: piani a pagamento, RAG, non attraversa i Project. [Verificato] T1
- Project knowledge: contenuto tuo, usato in ogni chat del Project; sui piani a pagamento passa a RAG vicino al limite. Con l'integrazione GitHub: scegli repo, file e cartelle; "Sync" e "Sync now" aggiornano; i repo devono entrare nella finestra di contesto. [Verificato] T1 · [help 9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Istruzioni del profilo ("Instructions for Claude"): valgono per tutte le conversazioni; quelle di Project solo dentro il Project. L'articolo dice che le funzioni si usano "independently or in combination" e non fissa precedenza. [Verificato] T1 · [help 10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)

### B. Claude Code
- `CLAUDE.md` per ambito: gestito, utente, progetto, locale; ordine di caricamento dal più ampio al più specifico; import `@path` fino a quattro livelli. Tutti i file trovati sono concatenati, non si sovrascrivono. Le regole utente caricano prima di quelle di progetto, nessuna prevale. [Verificato] T1 · [memory](https://code.claude.com/docs/en/memory)
- Limiti: meno di 200 righe consigliate; `MEMORY.md` 200 righe o 25 KB. Il `CLAUDE.md` di root sopravvive a `/compact` (riletto da disco). [Verificato] T1
- Auto memory in `~/.claude/projects/<project>/memory/`, condivisa tra worktree dello stesso repo, locale alla macchina; controlli `autoMemoryEnabled`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, `autoMemoryDirectory`. [Verificato] T1 · memory
- `AGENTS.md`: letto da 2.1.277 solo senza `CLAUDE.md`; 2.1.281 lo estende a Bedrock, Vertex, Foundry. Desktop e CLI usano gli stessi `CLAUDE.md` e le stesse impostazioni. [Verificato] T1 · [changelog](https://code.claude.com/docs/en/changelog); [desktop](https://code.claude.com/docs/en/desktop)
- Novità sulla compattazione: 2.1.299 (14-ott) aggiunge la compaction da inattività per conversazioni oltre 200K token ferme circa 54 minuti (`"idleCompaction": false` la spegne). [Verificato] T1 · changelog
- Dreams: job di Managed Agents in research preview (`dreaming-2026-04-21`), non una funzione di Claude Code; "Auto Dream" compare solo in blog terzi. [Verificato] T1 · [dreams](https://platform.claude.com/docs/en/managed-agents/dreams); [Segnale T3] sul resto

### C. API e Agent SDK
- Memory tool `memory_20250818` lato client, directory `/memories`, senza beta header. Context editing in beta (`context-management-2025-06-27`); compaction lato server, on demand dal 2026-09-14; cache con TTL 5 minuti. [Verificato] T1 · [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing); [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction); [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Context rot: accuratezza e recall calano al crescere dei token. Webhook `memory_store.*` dal 2026-07-22; memory stores self-hosted dal 2026-08-19. [Verificato] T1 · [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows); [release notes API](https://platform.claude.com/docs/en/release-notes/overview)

### D. Sessioni cloud, routine, Projects di Claude Code
| Cosa | In una sessione cloud fresca? | Fonte T1 |
|---|---|---|
| `CLAUDE.md`, `.claude/rules/`, skill, agent del repo | Sì, nel clone | [cloud-environments](https://code.claude.com/docs/en/cloud-environments) |
| `~/.claude/CLAUDE.md` e auto memory locale | No | cloud-environments; memory |
| Skill abilitate su claude.ai, connettori dell'account | Sì (prova diretta: nel mio contesto comparivano skill e un connettore dell'account) | cloud-environments; routines |
| Blocchi di memoria chat o istruzioni del profilo | Nella prova su di me: no. Docs: nessuna menzione [Inferenza] | vedi Prova |
| Project memory (`MEMORY.md` del Project, beta Pro e Max) | Sì, in ogni thread cloud del Project; thread sul tuo computer: no | [claude-projects](https://code.claude.com/docs/en/claude-projects) |
- **Prova riproducibile (domanda 1).** Sessione cloud fresca avviata da attività pianificata, 2026-10-19 12:55. Nel contesto: prompt di sistema, `CLAUDE.md` del repo, indirizzo e-mail dell'account (contesto Claude Code, non memoria), elenco di skill dell'account, un connettore dell'account. Assenti: blocchi di memoria dell'account e istruzioni del profilo. Una sola osservazione, quindi [Inferenza]; si ripete leggendo il contesto all'avvio di una sessione cloud.
- **Project e routine (domanda 2).** Le istruzioni del Project (fino a 16.000 caratteri) vanno a ogni thread e alla conversazione; la memoria la leggono solo i thread cloud. Una routine creata da un Project "runs as threads in that project" e compare nella scheda Scheduled tasks del Project (prima «Routines»; nome verificato il 27-ott su claude-projects); le routine fuori da un Project restano indipendenti. Quindi una routine del Project dovrebbe leggere la sua memoria, ma nessuna pagina lo dice in modo esplicito. [Inferenza] T1 · claude-projects; routines
- Una routine è prompt, repo e connettori; è un account individuale. Nel cloud funzionano `/compact`, `/context` e anche `/clear` (nuova conversazione nella stessa sessione cloud: pagina riletta il 27-ott; il 19-ott risultava di no). [Verificato] T1 · [on the web](https://code.claude.com/docs/en/claude-code-on-the-web)

### E. Chat lunghe
- Con l'esecuzione di codice attiva claude.ai riassume i messaggi vecchi e "preserves" la cronologia completa; la sintesi non garantisce il dettaglio e le chat lunghe consumano più limite. Consigli ufficiali: Project (RAG), istruzioni brevi, file inutili rimossi, ragionamento esteso spento se non serve. [Verificato] T1 · [usage limits](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- Un documento di handoff nel Project è un pattern di comunità ([Segnale T3]), coerente con le docs [Inferenza].

### F. Pattern esterni
| Pattern | Fonte e Tier | Stato |
|---|---|---|
| `AGENTS.md` più appunti nel repo | docs, T1 | costo 0, non vincolante |
| Server MCP `memory` ufficiale | [servers](https://github.com/modelcontextprotocol/servers), 91,4k stelle, T2 | file in chiaro |
| mem0 | [mem0](https://github.com/mem0ai/mem0), 67,4k stelle; ultimo commit 2026-10-14, T2 | dati verso terzi se si usa il cloud |
| basic-memory | [basic-memory](https://github.com/basicmachines-co/basic-memory), 4,3k stelle; ultimo commit 2026-10-18, T2 | licenza AGPL-3.0 |
Gli anni dei commit di mem0 e basic-memory sono ora letti da [mem0 commits](https://github.com/mem0ai/mem0/commits/main) e [basic-memory commits](https://github.com/basicmachines-co/basic-memory/commits/main): l'etichetta "anno dedotto" è caduta.

### G. Concorrenti (solo ciò che cambia una decisione)
- **Copilot (M365).** Spegnere la memoria "doesn't remove saved memories"; le memorie stanno nella mailbox Exchange. [Verificato] T1 · [Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory)
- **Gemini.** Memoria delle chat solo per account personali con Keep Activity attivo. [Verificato] T1 · [help Gemini](https://support.google.com/gemini/answer/16598469?hl=en&co=GENIE.Platform%3DDesktop)
- **ChatGPT.** Pagine OpenAI ancora 403. Dagli snippet delle pagine OpenAI: spegnere "Reference saved memories" spegne anche "Reference chat history"; con le memorie salvate attive, la cronologia si gestisce a parte; cancellare una chat non cancella una memoria salvata. [Inferenza] T2 · [snippet](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-remembering-what-you-chat-about)
- **Cursor.** Rules e `AGENTS.md` (root e sottocartelle); Memories assenti dalle docs e dal changelog ufficiale (pagine dal 17-lug al 16-ott-2026 e release 2.1 del 21-nov-2025). La rimozione dalla 2.1.17 resta solo nel forum. [Verificato] T2 per l'assenza · [rules](https://cursor.com/docs/context/rules) · [2.1](https://cursor.com/changelog/2-1); rimozione [Segnale T3]
- `AGENTS.md` è comune a Claude Code (con import), Cursor, Copilot e Codex.

### H. Rischi e avvelenamento della memoria
- **Privacy.** Temi sensibili esclusi di default, Incognito non salva. [Verificato] T1 · help 11817273
- [2606.04329](https://arxiv.org/pdf/2606.04329) (preprint, 18-giu-2026, testo completo): quattro canali di scrittura, nove vulnerabilità, sei classi di attacco, benchmark MPBench su due agenti (HERMES, OpenClaw) con un solo modello open (GPT-OSS-120B), non Claude. ASR medio 66,67% su HERMES e 34,25% su OpenClaw. Quattro difese anti-injection pronte all'uso: rilevazione tra 28,86% e 84,44% sugli attacchi forti, tra 10,74% e 42,50% su quelli deboli; la migliore ha 67,67% di rilevazione e 1,00% di falsi positivi. Gli autori propongono isolamento delle fonti, provenienza delle scritture, filtri nella compaction e monitoraggio dopo la scrittura (proposte, non testate qui). [Verificato] sul testo
- [2512.16962](https://arxiv.org/pdf/2512.16962) (MemoryGraft, preprint, dic-2025): agente MetaGPT DataInterpreter con GPT-4o; 23 dei 48 record recuperati erano avvelenati (47,9%). Propone firme crittografiche e un reranking di coerenza, ma sono proposte non testate. Correzione di v2: la difesa c'è, solo teorica. [Verificato] sul testo
- [2604.02623](https://arxiv.org/pdf/2604.02623) (eTAMP, preprint, apr-2026): agenti web; attacco fino a 32,5% su GPT-5-mini, 23,4% su GPT-5.2, 19,5% su GPT-OSS-120B; sotto stress sale fino a 8 volte. Le difese non sono valutate (limite dichiarato). [Verificato] sul testo
- [2607.14611](https://arxiv.org/abs/2607.14611) (preprint, 16-lug-2026, solo abstract): su Claude Code e Codex (Haiku 4.5, Opus 4.7, GPT-5.2, GPT-5.5) è difficile far riscrivere i file di memoria con contenuto esterno non fidato, ma payload già presenti nei file attaccano le sessioni. [Verificato] sull'abstract
- **Cosa fa Anthropic.** Nessuna difesa specifica per la memoria di claude.ai: la pagina dice solo "We apply safeguards and conduct evaluations to memory" (help 11817273). Per Claude Code: 2.1.284 neutralizza caratteri invisibili e tag che imitano il markup nell'auto memory; permessi, WebFetch con chiamata separata e, in cloud, VM isolate e rete limitata ([security](https://code.claude.com/docs/en/security)). Nel post [How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude) (25-mag-2026) Anthropic indica l'avvelenamento della memoria come rischio in crescita e dice che la protezione a livello di modello non basta da sola. [Verificato] T1. Cisco riferisce una correzione nella 2.1.50 che toglie le memorie utente dal prompt di sistema e la posizione di Anthropic che l'utente locale è fidato ([Cisco](https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code), 1-apr-2026). [Segnale T3]
- Bug recenti (issue chiuse #100205 e #101732 su github.com/anthropics): esistenza verificata in v2, fix non riverificato.

### I. Novità dopo il 19 ottobre e ultimi 90 giorni
- Al 19-ott-2026: nessuna voce nuova nel changelog di Claude Code (ultima 2.1.303), nelle release notes di claude.ai (ultima 2026-10-07), né in quelle API (ultima 2026-10-15).
- Al 27-ott-2026 (letture delle notti 04 e 05): Claude Code 2.1.312; release notes dell'app fino al 2026-10-21, dell'API fino al 2026-10-23. Le voci sulla memoria non cambiano le regole sopra; quelle su contesto e attività sono in [3_contesto/rapporto_contesto.md](../3_contesto/rapporto_contesto.md) e [5_attivita/rapporto_attivita.md](../5_attivita/rapporto_attivita.md).
- Da v2: 2.1.299 (compaction da inattività), 2.1.296 (memoria di workspace e canale in Claude Tag), 2.1.302 (correzioni alle routine), 2026-10-15 (Compliance API restituisce "Instructions for Claude" e "Global instructions", beta Enterprise), 2026-10-07 (Haiku 5.5, 1M di contesto). [Verificato] T1 · changelog; [release notes API](https://platform.claude.com/docs/en/release-notes/overview)

## Raccordo con i report: v2 e precedenti/
| Punto | v1/v2 e report del 18 ottobre | Stato v3 |
|---|---|---|
| Memoria claude.ai = "riassunto ogni 24 h" | Cambiata il 10-lug-2026 (v2) | Confermata |
| Memoria account nel cloud | "Nessuna prova trovata" | Ancora nessuna prova nelle docs; la prova su me: nessun blocco |
| Eredità della project memory nelle routine | Non scritto da nessuna parte | Dedotta dalle docs: routine = thread del Project [Inferenza] |
| Precedenza tra istruzioni | "Non riesaminata" | Nessuna regola ufficiale; concatenazione in Claude Code |
| Preprint "letti solo nell'abstract" | Abstract | Testo completo; MemoryGraft ha difese proposte |
| `AGENTS.md` e `@AGENTS.md` | Verificato | Confermato (memory) |
| Project con GitHub | Non indagato | Sync manuale |
| Istruzioni dei Projects beta: 16.000 caratteri | Vera | Confermata |
| Chat lunghe: consenso Reddit | Parzialmente ufficiale | Ufficiale: sintesi automatica, nessuna soglia |
| Cursor Memories, ChatGPT, mem0, basic-memory | Aperti o con anno dedotto | Vedi G e F |
| `claude mcp serve` su Windows | Fuori tema | Non riesaminato |

## Tabella conflitti
| Tema | Fonte A | Fonte B | Stato |
|---|---|---|---|
| Scadenza export legacy | help 11817273: fino al 2026-09-09 (T1) | help 12123587: silenzio (T1) | Risolto: data passata |
| Dreams / Auto Dream | docs Dreams: API Managed Agents (T1) | blog terzi: funzione di Code (T3) | Risolto a favore della T1 |
| Memories di Cursor | docs e changelog ufficiale: assenti (T2) | forum, 2.1.17 (T3) | Parziale: il changelog tace, la rimozione non è confermata |
| Toggle di ChatGPT | v2: "collegati" (snippet) | v3: dipendenza a senso unico (snippet) | Raffinato, non confermato: 403 |
| Memoria account e Code cloud | 7 pagine T1: nessuna menzione | prova su di me: nessun blocco | Coerente: va trattata come assente |
| MemoryGraft: difese | v2: "nessuna difesa proposta" | testo completo: due difese proposte | Risolto: v2 sbagliata |

## Cosa non è stato verificato (resta aperto)
- Se una routine creata da un Project legga davvero la project memory: manca una frase esplicita; si può provare creandone una con una nota nella memoria.
- La prova sul contesto vale per una sessione; non è stata ripetuta su Desktop Code tab né sulla CLI (le docs consultate non dicono nulla).
- Help center e blog OpenAI (403), Reddit e Stack Overflow (bloccati dallo strumento).
- Rimozione delle Memories di Cursor: il changelog ufficiale è stato letto per le pagine 1-3 e la release 2.1, non per le 2.1.x intermedie.
- Il preprint 2607.14611 è letto solo nell'abstract. Del changelog di Claude Code la v3 ha riletto solo i primi 100K caratteri (le versioni più recenti); la finestra 2.1.269-2.1.303 è quella di v2.
- Le voci "Instructions for Claude" non sono state messe a confronto con la memoria in un test.

## Fonti per Tier
**Tier 1.** code.claude.com: [memory](https://code.claude.com/docs/en/memory) · [cloud-environments](https://code.claude.com/docs/en/cloud-environments) · [routines](https://code.claude.com/docs/en/routines) · [claude-projects](https://code.claude.com/docs/en/claude-projects) · [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web) · [changelog](https://code.claude.com/docs/en/changelog) · [desktop](https://code.claude.com/docs/en/desktop) · [security](https://code.claude.com/docs/en/security). platform.claude.com: [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) · [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) · [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) · [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) · [dreams](https://platform.claude.com/docs/en/managed-agents/dreams) · [release notes](https://platform.claude.com/docs/en/release-notes/overview). support.claude.com: [11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) · [12138966](https://support.claude.com/en/articles/12138966-release-notes) · [12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude) · [9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) · [11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) · [10167454](https://support.claude.com/en/articles/10167454-using-the-github-integration) · [10185728](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features). anthropic.com: [How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude). arXiv (preprint): [2606.04329](https://arxiv.org/abs/2606.04329) · [2512.16962](https://arxiv.org/abs/2512.16962) · [2604.02623](https://arxiv.org/abs/2604.02623) · [2607.14611](https://arxiv.org/abs/2607.14611). Microsoft: [Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory). Google: [help Gemini](https://support.google.com/gemini/answer/16598469?hl=en&co=GENIE.Platform%3DDesktop)
**Tier 2.** [servers](https://github.com/modelcontextprotocol/servers) · [mem0](https://github.com/mem0ai/mem0) · [basic-memory](https://github.com/basicmachines-co/basic-memory) · [Cursor rules](https://cursor.com/docs/context/rules) · [Cursor 2.1](https://cursor.com/changelog/2-1) · [snippet OpenAI](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-remembering-what-you-chat-about)
**Tier 3.** [Cisco](https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code) · [forum Cursor](https://forum.cursor.com/t/are-my-memories-gone/144057) · [implicator.ai](https://www.implicator.ai/anthropic-adds-auto-dream-to-claude-code-fixing-memory-decay-between-sessions) · [claudefa.st](https://claudefa.st/blog/guide/mechanics/auto-dream) · [mirror Reddit](https://reddit.sentinel-team.org/posts/1rfwxr2/snapshots/2026-02-27T16%3A40%3A54.76432Z)

## Guida
Le istruzioni d'uso per Claude e i passi per l'utente stanno in `D:\Workspace\best_practice\4_memoria\guida_memoria.md`.
