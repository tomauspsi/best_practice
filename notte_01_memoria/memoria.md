---
tema: memoria nei prodotti Claude (claude.ai, Claude Code, API, sessioni cloud)
versione: 2
base: f1d5d1e
verificato_il: 2026-10-19
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes che toccano la memoria; oppure 2026-12-18"
versioni_rilevate:
  claude_code: "2.1.303 del 2026-10-18 (changelog code.claude.com, riletto)"
  app_claude_ai: "nessun numero di versione nelle release notes; ultima voce sulla memoria: 2026-08-25"
  modelli: "claude-opus-5-5 (2026-09-22), claude-sonnet-5-5 (2026-09-28), claude-haiku-5-5 (2026-10-07), claude-fable-5-1 (2026-09-01); claude-mythos-5-1 solo Project Glasswing"
  api: "memory tool memory_20250818 senza beta header; compaction on demand compact-2026-09-04 (2026-09-14); Dreams research preview dreaming-2026-04-21"
---

# Memoria nei prodotti Claude: stato al 19 ottobre 2026 (v2)

v2 corregge la v1 (commit `f1d5d1e`): rilegge le pagine troncate, chiude o riclassifica le domande aperte e confronta i due report del 18 ottobre in [precedenti/](../precedenti/).

## Risposta breve
- Le memorie sono cinque e separate: memoria di claude.ai (account e Project), ricerca nelle chat passate, `CLAUDE.md`/`AGENTS.md`, auto memory locale di Claude Code, memory tool dell'API (storage tuo). In più, la project memory dei Projects di Claude Code (beta).
- Una sessione cloud fresca, anche da routine, parte da un clone del repo: vede `CLAUDE.md` e `.claude/rules/` del repo, non vede `C:\Users\Tommi\.claude\CLAUDE.md` né l'auto memory locale.
- Che la memoria chat dell'account arrivi a Claude Code cloud: nessuna prova trovata in sei pagine ufficiali. Va trattata come assente.
- Il canale documentato e versionabile per un agente notturno sono i file nel repo. La memoria è contesto, non vincolo: per bloccare un'azione servono gli hook.
- "Dreams" esiste solo come API di Managed Agents in research preview. Non è una funzione di Claude Code.

## REGOLE OPERATIVE PER AGENTI
1. Non assumere che una sessione cloud conosca la memoria dell'account claude.ai: metti il contesto nel prompt o nel repo. [Inferenza] · T1 · nessuna menzione di Claude Code nell'help center: <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
2. Scrivi il prompt di una routine autosufficiente: ogni run è una sessione nuova e non ne riusa altre. [Verificato] · T1 · <https://code.claude.com/docs/en/routines>
3. Metti le istruzioni per il cloud in `./CLAUDE.md` o `./.claude/rules/` del repo: fanno parte del clone. [Verificato] · T1 · <https://code.claude.com/docs/en/cloud-environments>
4. Non contare su `~/.claude/CLAUDE.md`, skill, agent e command utente nel cloud: committali in `.claude/` o falli scrivere da uno setup script. [Verificato] · T1 · <https://code.claude.com/docs/en/cloud-environments>
5. Non contare sull'auto memory locale nel cloud: non è condivisa tra macchine né con gli ambienti cloud. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
6. Tieni ogni `CLAUDE.md` sotto le 200 righe e sposta il resto in `.claude/rules/`, con `paths` per le regole locali. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
7. Metti in cima a `MEMORY.md` ciò che conta: all'avvio si caricano solo le prime 200 righe o 25 KB. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
8. Se il repo ha sia `AGENTS.md` sia `CLAUDE.md`, scrivi `@AGENTS.md` dentro `CLAUDE.md`: senza import Claude Code legge solo `CLAUDE.md`. La lettura nativa di `AGENTS.md` (da 2.1.277) vale solo senza alcun `CLAUDE.md` o `CLAUDE.local.md`. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
9. Per vincoli di sicurezza usa hook `PreToolUse`, non `CLAUDE.md`, che è contesto e non configurazione imposta. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
10. In claude.ai isola la memoria con un Project, e disattiva "Use account memory" per isolarla del tutto. La ricerca nelle chat passate non attraversa i Project. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
11. Non affidare dati sensibili alla memoria di claude.ai. I temi sensibili sono esclusi di default, e cancellare una chat non cancella le memorie derivate. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
12. Non far scrivere in memoria testo preso da pagine esterne senza revisione. Un preprint mostra che agenti che scrivono e recuperano memoria più aggressivamente sono più attaccabili e che le difese anti-injection esistenti non coprono il caso. [Inferenza] dal fatto citato · T1 (preprint) · <https://arxiv.org/abs/2606.04329>
13. Con il memory tool dell'API valida ogni path sotto `/memories` (path traversal) e limita dimensione e scadenza dei file. [Verificato] · T1 · <https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>
14. Nelle sessioni API lunghe abbina compaction (riassume) e memory tool (conserva ciò che deve sopravvivere al riassunto). [Verificato] · T1 · <https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>
15. Non citare "Auto Dream" come funzione di Claude Code: la parola "dream" non compare nell'indice delle docs di Claude Code. [Verificato] per l'assenza; il claim positivo è [Segnale T3] · T1 · <https://code.claude.com/docs/llms.txt>

## Stato dell'arte per domanda

### A. claude.ai (Chat e Project)
- **Funzionamento.** Dal 10 luglio 2026 la memoria è un insieme di voci per categoria, lette e aggiornate durante la chat; la versione legacy era una sintesi aggiornata ogni 24 ore. [Verificato] T1 · [release notes](https://support.claude.com/en/articles/12138966-release-notes)
- **Separazione.** Ogni Project ha la sua memoria. Le sue chat usano anche la memoria d'account delle chat fuori Project, mai quella di altri Project. [Verificato] T1 · [help 11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- **Controlli.** Pausa, Reset (irreversibile, anche per i Project), spegnimento per singola chat, modifica dei topic. Import sperimentale ("Memory imports are experimental and still in active development") ed export. [Verificato] T1 · [help 12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)
- **Piani.** Attiva di default su Free, Pro e Max. Su Team ed Enterprise la abilita l'owner. Non disponibile con accordi HIPAA, settore pubblico o retention personalizzata. [Verificato] T1 · help 11817273.
- **Cowork.** Dal 25 agosto 2026 "Memory now works across chat and Cowork in the cloud". Cowork locale non usa la memoria. [Verificato] T1 · release notes; help 11817273.
- **Ricerca nelle chat passate.** Solo piani a pagamento, via RAG, con citazioni. Mai tra Project diversi; esclude Incognito. [Verificato] T1.
- **Project knowledge.** È contenuto fornito da te e usato in ogni chat del Project; sui piani a pagamento passa a RAG vicino al limite. Il contesto non passa tra chat del Project se non lo metti nella knowledge. [Verificato] T1 · [help 9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)

### B. Claude Code
- **Ambiti `CLAUDE.md`.** Policy gestita, utente `~/.claude/CLAUDE.md`, progetto `./CLAUDE.md` o `./.claude/CLAUDE.md`, locale `CLAUDE.local.md`. Import `@path` con "a maximum depth of four hops". [Verificato] T1 · [memory](https://code.claude.com/docs/en/memory)
- **`.claude/rules/`.** Ricorsiva, supporta symlink; senza `paths` carica sempre, con `paths` solo sui file corrispondenti. Dal 2.1.288 le regole con path e i `CLAUDE.md` annidati si caricano anche con Write ed Edit. [Verificato] T1 · [changelog](https://code.claude.com/docs/en/changelog)
- **Limiti.** Meno di 200 righe consigliate per `CLAUDE.md`; un file fino a 4 MiB si carica intero, uno più grande viene saltato. Di `MEMORY.md` si caricano 200 righe o 25 KB. [Verificato] T1 · memory.
- **Auto memory.** Si trova in `~/.claude/projects/<project>/memory/`, con indice `MEMORY.md` e un file per topic, di tipo `user`, `feedback`, `project` o `reference`. È condivisa tra i worktree dello stesso repo e locale alla macchina. Attiva di default in locale, spenta di default negli ambienti self-hosted. Si controlla con `autoMemoryEnabled`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` e `autoMemoryDirectory`. [Verificato] T1 · memory.
- **`/memory` e menu.** 2.1.274 aggiunge le voci Memory e Instructions al menu Customize. 2.1.275 permette di vedere, modificare e cancellare una memoria salvata. 2.1.284 neutralizza caratteri invisibili e tag che imitano il markup di Claude Code nel caricamento dell'auto memory. 2.1.285 vieta di riattivare l'auto memory da una sessione in background. 2.1.287 commuta le impostazioni con i tasti freccia. [Verificato] T1 · changelog.
- **`AGENTS.md`.** 2.1.277 (18-set-2026): "in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead". 2.1.281 lo estende a Bedrock, Vertex e Foundry. 2.1.290 corregge `AGENTS.md` di sottocartella e i symlink. Le opzioni sono `claude-md-or-agents-md` (default), `claude-md-and-agents-md` e `managed-only`. [Verificato] T1 · changelog; memory.
- **Igiene.** `/doctor prompt-audit` (da 2.1.283) cerca istruzioni obsolete o in conflitto, perché con due istruzioni contraddittorie Claude "may pick one arbitrarily". Vicino al limite, Claude chiede di accorciare `MEMORY.md` ("merge or drop stale entries"). [Verificato] T1 · memory.
- **Dreams.** È un job asincrono di Managed Agents che legge un memory store e da 1 a 100 trascrizioni e produce un nuovo store deduplicato, senza toccare l'input. Research preview, richiede accesso, header `dreaming-2026-04-21`. [Verificato] T1 · [dreams](https://platform.claude.com/docs/en/managed-agents/dreams). "Auto Dream" in Claude Code compare solo in blog terzi. [Segnale T3]

### C. API e Agent SDK
- **Memory tool `memory_20250818`.** Lato client, directory `/memories`, comandi `view`, `create`, `str_replace`, `insert`, `delete` e `rename`. Funziona con Claude 4 e successivi, senza beta header; l'API aggiunge l'istruzione di guardare la memoria all'inizio. [Verificato] T1 · [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
- **Context editing.** Lato server, in beta con `context-management-2025-06-27`. Con il memory tool, Claude riceve un avviso prima della cancellazione. La pulizia dei tool result invalida il prefisso in cache. [Verificato] T1 · [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)
- **Compaction.** Lato server, riassume i turni vecchi; "can now compact a conversation on demand" dal 2026-09-14. [Verificato] T1 · [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction); [release notes API](https://platform.claude.com/docs/en/release-notes/overview)
- **Prompt caching.** TTL di 5 minuti (1 ora a pagamento); cambiare i tool invalida tutta la cache, e cambiare un breakpoint invalida quel segmento e i successivi. Dal 2026-09-01 i system message per turno, in beta, "don't invalidate the prompt cache". La pagina sul caching, letta fino in fondo, non tratta compaction né memory tool. [Verificato] T1 · [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Managed Agents.** Webhook `memory_store.*` dal 2026-07-22; memory stores nelle sandbox self-hosted dal 2026-08-19. [Verificato] T1 · release notes API.
- **Context rot.** Accuratezza e recall calano al crescere dei token; la compaction è la strategia primaria. [Verificato] T1 · [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)

### D. Sessioni cloud, routine e attività pianificate (domanda decisiva)
| Cosa | Presente in una sessione cloud fresca? | Fonte T1 |
|---|---|---|
| `CLAUDE.md`, `.claude/rules/`, skill, agent e command del repo | Sì, nel clone | [cloud-environments](https://code.claude.com/docs/en/cloud-environments) |
| `~/.claude/CLAUDE.md`, skill, agent e command utente | No; si ricreano con uno setup script | cloud-environments |
| Auto memory locale | No | memory |
| Skill abilitate su claude.ai, connettori dell'account | Sì | cloud-environments, routines |
| Memoria chat di claude.ai | Nessuna prova trovata: [Inferenza] no | sei pagine, vedi conflitti |
| Project memory (`MEMORY.md` del Project, beta Pro e Max) | Sì, in ogni thread cloud del Project | [claude-projects](https://code.claude.com/docs/en/claude-projects) |
- Una routine è prompt, repo e connettori; ogni run è una sessione nuova e la pagina delle routine non nomina mai la memoria. [Verificato] T1 · routines.
- Il thread di un Project eseguito sul tuo computer parte con le istruzioni del Project ma senza i file di memoria. [Verificato] T1 · claude-projects.
- Se le routine create da un Project ereditino la project memory non è scritto da nessuna parte: le docs dicono solo che compaiono nella tab Routines. Nessuna prova trovata. [Inferenza]
- Auto-compaction nel cloud: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` è impostato dalla sessione; `/compact` funziona, `/clear` no. [Verificato] T1 · [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)

### E. Passaggio di contesto tra chat
- In claude.ai, con l'esecuzione di codice attiva, "Claude summarizes earlier messages to continue the conversation seamlessly"; le chat lunghe consumano più limite d'uso. Il consiglio è di aprire una nuova chat se ci si avvicina al limite. Non esiste una soglia numerica. [Verificato] T1 · [usage limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits)
- Per agenti multi-sessione le docs API indicano file di stato (progress log, checklist) letti all'avvio e aggiornati a fine sessione. [Verificato] T1 · memory tool.
- Un documento di handoff nel Project è un pattern di comunità: [Segnale T3] da mirror Reddit ([snapshot](https://reddit.sentinel-team.org/posts/1rfwxr2/snapshots/2026-02-27T16%3A40%3A54.76432Z)). Con la Project knowledge è coerente con le docs. [Inferenza]

### F. Pattern esterni
| Pattern | Fonte e Tier | Costo | Rischio |
|---|---|---|---|
| `AGENTS.md` più una cartella di appunti nel repo | docs ufficiali, T1 | 0 | istruzioni ignorabili, non vincolanti |
| Server MCP `memory` ufficiale (grafo in `memory.jsonl`) | [servers](https://github.com/modelcontextprotocol/servers), 91,4k stelle, ultimo commit su `src/memory` 2026-10-19: T2 | 0 | file in chiaro |
| mem0 | [mem0](https://github.com/mem0ai/mem0), 67,4k stelle, release "25 Sep" senza anno: T2 (anno dedotto) | libreria libera, cloud a pagamento | dati verso terzi se si usa il cloud |
| basic-memory | [basic-memory](https://github.com/basicmachines-co/basic-memory), 4,3k stelle, AGPL-3.0, release v0.23.2 "25 Aug" senza anno: T2 (anno dedotto) | 0 | licenza AGPL |

### G. Confronto breve (solo ciò che cambia una decisione)
- **Copilot (M365).** Attiva di default. Spegnerla "doesn't remove saved memories"; le policy Purview non si applicano e l'admin non può limitare cosa entra in memoria. Le memorie stanno nella mailbox Exchange. [Verificato] T1 · [Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory)
- **Gemini.** Memoria delle chat passate solo per account personali, dai 18 anni, con Keep Activity attivo; non funziona in Gems e Live. [Verificato] T1 · [help Gemini](https://support.google.com/gemini/answer/16598469?hl=en&co=GENIE.Platform%3DDesktop)
- **ChatGPT.** Due interruttori collegati: spegnere le memorie salvate spegne anche la cronologia. Le pagine OpenAI rispondono 403: solo snippet. [Inferenza] T2.
- **Cursor.** Rules in `.cursor/rules` e `AGENTS.md` in root e sottocartelle. Le docs e il changelog visibile (10 set - 16 ott 2026) non citano le Memories. [Verificato] T2 · [Cursor rules](https://cursor.com/docs/context/rules). Rimozione delle Memories: [Segnale T3].
- **Conseguenza.** `AGENTS.md` è comune a Claude Code, Cursor, Copilot e Codex; solo Claude Code richiede l'import quando esiste anche `CLAUDE.md`.

### H. Rischi
- **Privacy.** In claude.ai i temi sensibili sono esclusi di default con opt-in separato; Incognito non salva; la scadenza di una chat non cancella le memorie derivate. [Verificato] T1.
- **Avvelenamento: cosa dimostrano i paper**, tutti preprint senza sede dichiarata:
  - [2606.04329](https://arxiv.org/abs/2606.04329) (3-giu-2026): "agents designed to write and retrieve memory more aggressively are more exploitable"; le difese anti-injection esistenti non coprono il caso. Nessun tasso numerico nell'abstract.
  - [2512.16962](https://arxiv.org/abs/2512.16962) (MemoryGraft, 18-dic-2025): pochi record avvelenati coprono gran parte delle esperienze recuperate. Nessuna difesa proposta.
  - [2604.02623](https://arxiv.org/abs/2604.02623) (eTAMP, 3-apr-2026): una sola osservazione contaminata avvelena la memoria; successo dell'attacco fino al 32,5% su GPT-5-mini. Nessuna difesa specifica.
  - [Verificato] sugli abstract. **Cosa consiglio:** regola 12. [Inferenza]
- **Superficie in Claude Code.** 2.1.284 neutralizza tag che imitano il markup nel caricamento dell'auto memory. [Verificato] T1 · changelog.
- **Bug recenti.** Issue chiuse su github.com/anthropics: memoria claude.ai non iniettata dopo il rollout "one Claude" (#100205, 10-ott); `AGENTS.md` non caricato alla prima sessione su 2.1.296 (#101732). [Verificato] come esistenza, il fix non è riverificato · [issue chiuse](https://github.com/anthropics/claude-code/issues?q=is%3Aissue+memory+is%3Aclosed)

### I. Novità ultimi 90 giorni (21-lug - 19-ott-2026)
- **claude.ai.** 07-09 riepilogo mensile (beta, richiede memoria). 07-10 memoria per voci. 08-25 memoria in Cowork cloud, topic modificabili, opzione per i temi sensibili. 09-16 Cowork in ogni conversazione. [Verificato] T1.
- **API.** 07-22 webhook memory store. 07-24 Opus 5 e tool modificabili senza perdere la cache. 08-01 Dreams su Opus 5. 08-19 memory stores self-hosted. 09-01 Fable 5.1, Mythos 5.1 e system message per turno. 09-14 compaction on demand. 09-22 Opus 5.5. 09-23 cache diagnostics GA. 09-28 Sonnet 5.5. 10-01 Dreams sui modelli 5.5 e 5.1. 10-07 Haiku 5.5. [Verificato] T1.
- **Claude Code.** Da 2.1.274 a 2.1.303: voci in B. [Verificato] T1.

## Raccordo con i report precedenti
Fonti: [collegare_claude_app_a_code.md](../precedenti/collegare_claude_app_a_code.md) e [istruzioni_per_progetti.md](../precedenti/istruzioni_per_progetti.md), entrambi del 18-10-2026.
| Affermazione del 18 ottobre | Stato al 19 ottobre | Fonte |
|---|---|---|
| Memoria claude.ai = "riassunto ogni 24 h" | **Cambiata**: voci per categoria dal 10-lug-2026; le 24 h valgono solo per la legacy residua | release notes; help 11817273 |
| Cowork usa la memoria claude.ai | **Ancora vera solo in cloud**: Cowork locale non la usa | help 11817273 |
| Code tab: memoria claude.ai "non documentata" | **Ancora vera**; nessuna prova trovata nemmeno per le sessioni cloud | sez. D |
| `AGENTS.md` letto da 2.1.277 senza `CLAUDE.md`, altrimenti `@AGENTS.md` | **Ancora vera**; in più 2.1.281 (Bedrock, Vertex, Foundry) e l'opzione `claude-md-and-agents-md` | changelog; memory |
| Cursor legge `AGENTS.md`: "non verificato" | **Ora verificata**: root e sottocartelle | Cursor rules |
| Skill dell'account sincronizzate in Code | **Coerente**: le sessioni cloud caricano le skill abilitate su claude.ai | cloud-environments |
| `claude mcp serve` su Windows/MSIX | **Non riesaminato** (fuori tema memoria) | — |
| Istruzioni dei Projects beta: tetto di 16.000 caratteri | **Ancora vera** | claude-projects |
| `CLAUDE.md` sotto 200 righe | **Ancora vera** | memory |
| Chat lunghe: nuova chat più handoff = consenso Reddit | **Parzialmente ufficiale**: sintesi automatica e consiglio di aprire una nuova chat, senza soglia | usage limits |
| Precedenza tra istruzioni, profilo e memoria: nessuna regola | **Non riesaminato**; nessuna contraddizione trovata | — |
| Server memory MCP "più povero del Markdown"; mem0 e basic-memory | **Coerente**; stelle e attività aggiornate in F | GitHub |

## Tabella conflitti
| Tema | Fonte A (data, Tier) | Fonte B (data, Tier) | Stato |
|---|---|---|---|
| Scadenza export memoria legacy | help 11817273 ("Updated this week", T1): "until September 9, 2026" | help 12123587 ("Updated this week", T1): nessuna scadenza; release notes: nessuna voce | **Risolto**: non è un conflitto ma un silenzio; vale 11817273 e la data è passata |
| Dreams / Auto Dream | docs Dreams (corrente, T1): API Managed Agents | implicator.ai, claudefa.st (2026, T3): funzione di Claude Code | **Risolto** a favore della T1 |
| Memories di Cursor | docs e changelog Cursor (ott-2026, T2): nessuna menzione | forum Cursor (fine 2025, T3): rimosse dalla 2.1.x | **Non risolto**: changelog vecchio non letto |
| Toggle di ChatGPT | snippet help.openai.com (s.d., T2): collegati | annunci OpenAI più vecchi (snippet, T2): indipendenti | **Non risolto**: pagine 403 |
| Memoria account e Claude Code cloud | 6 pagine T1 (correnti): nessuna menzione | — | **Non risolto**: assenza di prova |

## Cosa non è stato verificato
- Memoria chat dell'account nelle sessioni Claude Code cloud. Pagine controllate: help 11817273, cloud-environments, claude-code-on-the-web, routines, claude-projects, memory. Nessuna prova in un senso o nell'altro.
- Eredità della project memory nelle routine create da un Project.
- Help center OpenAI (403); Reddit e Stack Overflow rifiutati dallo strumento; Reddit visto solo da mirror.
- Date complete dei commit di mem0 e basic-memory: GitHub mostra la data senza anno.
- Changelog di Claude Code letto da 2.1.269 a 2.1.303 (400k caratteri su 1,1 MB); le versioni precedenti sono fuori finestra.
- I preprint letti solo nell'abstract, non nel testo completo.
- `claude mcp serve` e la precedenza tra istruzioni non sono stati riesaminati.

## Fonti per Tier
**Tier 1.** code.claude.com: [memory](https://code.claude.com/docs/en/memory) · [cloud-environments](https://code.claude.com/docs/en/cloud-environments) · [routines](https://code.claude.com/docs/en/routines) · [claude-projects](https://code.claude.com/docs/en/claude-projects) · [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web) · [changelog](https://code.claude.com/docs/en/changelog) · [llms.txt](https://code.claude.com/docs/llms.txt). platform.claude.com: [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) · [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) · [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) · [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) · [dreams](https://platform.claude.com/docs/en/managed-agents/dreams) · [release notes](https://platform.claude.com/docs/en/release-notes/overview). support.claude.com: [11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) · [12138966](https://support.claude.com/en/articles/12138966-release-notes) · [12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude) · [9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) · [11647753](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits). GitHub: [issue chiuse](https://github.com/anthropics/claude-code/issues?q=is%3Aissue+memory+is%3Aclosed). arXiv (preprint): [2606.04329](https://arxiv.org/abs/2606.04329) · [2512.16962](https://arxiv.org/abs/2512.16962) · [2604.02623](https://arxiv.org/abs/2604.02623). Microsoft: [Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory). Google: [help Gemini](https://support.google.com/gemini/answer/16598469?hl=en&co=GENIE.Platform%3DDesktop)
**Tier 2.** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · [mem0](https://github.com/mem0ai/mem0) · [basic-memory](https://github.com/basicmachines-co/basic-memory) · [Cursor rules](https://cursor.com/docs/context/rules) (provvisorio) · [help.openai.com](https://help.openai.com/en/articles/8590148-memory-in-chatgpt) (solo snippet)
**Tier 3.** [mirror Reddit](https://reddit.sentinel-team.org/posts/1rfwxr2/snapshots/2026-02-27T16%3A40%3A54.76432Z) · [forum Cursor](https://forum.cursor.com/t/are-my-memories-gone/144057) · [implicator.ai](https://www.implicator.ai/anthropic-adds-auto-dream-to-claude-code-fixing-memory-decay-between-sessions) · [claudefa.st](https://claudefa.st/blog/guide/mechanics/auto-dream)
