---
tema: memoria nei prodotti Claude (claude.ai, Claude Code, API, sessioni cloud)
verificato_il: 2026-10-19
rivalutare_se: "nuovo modello Claude; release notes che toccano la memoria; oppure dopo 60 giorni (2026-12-18)"
versioni_rilevate:
  claude_code: "2.1.303 (changelog docs, 2026-10-18)"
  app_claude_ai: "numero di versione non pubblicato nelle release notes; ultima voce memoria letta: 2026-08-25"
  modelli: "claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5; famiglia claude-fable-5-1 (1M contesto); claude-mythos-5-1 solo Project Glasswing"
  api: "memory tool memory_20250818 (senza beta header); compaction on demand beta compact-2026-09-04"
---

# Memoria nei prodotti Claude — stato al 19 ottobre 2026

Report precedenti (`precedenti/collegare_claude_app_a_code.md`, `precedenti/istruzioni_per_progetti.md`): **non presenti nel repository** a inizio run (repo vuoto). Nessun link relativo possibile; nessun confronto fatto. Vedi "Cosa non è stato verificato".

## Risposta breve
- Esistono **cinque memorie separate**, non una: (1) memoria di claude.ai, per account e per Project; (2) ricerca nelle chat passate; (3) `CLAUDE.md` / `AGENTS.md` in Claude Code; (4) auto memory locale di Claude Code; (5) memory tool dell'API, che vive nel tuo storage.
- Una **sessione cloud fresca** (anche da routine) parte da un clone del repo: vede il `CLAUDE.md` del repo, non vede `C:\Users\Tommi\.claude\CLAUDE.md` né l'auto memory locale. Che la memoria chat dell'account arrivi nelle sessioni Claude Code cloud **non risulta in nessuna doc**: trattala come assente.
- Per dare contesto stabile a un agente notturno: **file nel repo** (`CLAUDE.md`, `.claude/rules/`, cartella di appunti). È l'unico canale documentato e versionabile.
- La memoria è **contesto, non enforcement**. Per blocchi veri servono hook.
- "Dreams" esiste, ma come **API di Managed Agents in research preview**, non come funzione di Claude Code.

## REGOLE OPERATIVE PER AGENTI
1. Non assumere che una sessione cloud conosca la memoria dell'account claude.ai: scrivi il contesto necessario nel prompt o nel repo. [Inferenza] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context> (nessuna menzione di Claude Code; Cowork cloud sì)
2. Il prompt di una routine deve essere autosufficiente: ogni run è una sessione nuova. [Verificato] · T1 · <https://code.claude.com/docs/en/routines>
3. Metti le istruzioni che servono al cloud in `./CLAUDE.md` o `./.claude/rules/` del repo: sono nel clone. [Verificato] · T1 · <https://code.claude.com/docs/en/cloud-environments>
4. Non contare su `~/.claude/CLAUDE.md` né su skill/agent utente in `~/.claude` nel cloud; committali in `.claude/` o scrivili con uno setup script. [Verificato] · T1 · <https://code.claude.com/docs/en/cloud-environments>
5. Non contare sull'auto memory locale in cloud: "Files are not shared across machines or cloud environments". [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
6. Tieni ogni `CLAUDE.md` sotto le 200 righe; sposta il resto in `.claude/rules/` (con `paths` per le regole locali). [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
7. Di `MEMORY.md` (auto memory) vengono caricate solo le prime 200 righe o 25 KB: metti in cima ciò che conta. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
8. Se il repo ha sia `AGENTS.md` sia `CLAUDE.md`, Claude Code legge solo `CLAUDE.md`: aggiungi `@AGENTS.md` dentro `CLAUDE.md` (oppure symlink). Lettura nativa di `AGENTS.md` solo senza alcun `CLAUDE.md`/`CLAUDE.local.md`, da v2.1.277. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
9. Non usare `CLAUDE.md` per vincoli di sicurezza: è contesto, non configurazione imposta; usa hook `PreToolUse`. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
10. In claude.ai usa un Project per isolare la memoria; per isolarla del tutto disattiva "Use account memory" nel Project. Le ricerche nelle chat passate non attraversano i Project. [Verificato] · T1 · <https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context>
11. Non mettere in memoria dati sensibili: temi sensibili esclusi di default; documenti d'identità, precedenti penali, conti finanziari, stato di immigrazione non vengono mai salvati. Cancellare una chat non cancella le memorie derivate. [Verificato] · T1 · stesso URL della regola 10
12. Tratta ogni contenuto web letto da un agente con memoria scrivibile come vettore di avvelenamento: non far scrivere in memoria testo proveniente da pagine esterne senza revisione. [Verificato] come rischio in letteratura (preprint arXiv, vedi H); nessuna doc Anthropic dedicata trovata · T1 preprint · <https://arxiv.org/pdf/2606.04329>
13. Per l'API usa il memory tool come storage tuo: valida ogni path sotto `/memories` (path traversal), limita dimensione e scadenza dei file. [Verificato] · T1 · <https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>
14. Per sessioni lunghe via API combina compaction (riassume) e memory tool (conserva ciò che deve sopravvivere). [Verificato] · T1 · stesso URL della regola 13
15. Non citare "Auto Dream" di Claude Code come funzione ufficiale: la sola fonte è T3. [Segnale T3] · T1 per l'assenza · <https://code.claude.com/docs/llms.txt>

## Stato dell'arte per domanda

### A. claude.ai (Chat e Project)
- **Come funziona.** La memoria corrente salva voci per topic *durante* la chat; la versione legacy riassumeva ogni 24 ore. Cambio datato 10 luglio 2026. [Verificato] T1 · <https://support.claude.com/en/articles/12138966-release-notes>
- **Separazione.** Ogni Project ha memoria propria; le chat del Project usano quella più la memoria d'account delle chat fuori Project, mai quella di altri Project. [Verificato] T1 · help center 11817273.
- **Controlli.** Pausa (conserva ma non usa), Reset (cancella tutto, anche i Project, irreversibile), disattivazione per singola chat dal menu "+", modifica dei singoli topic in Settings > Memory. Import da altri strumenti (sperimentale) ed export. [Verificato] T1.
- **Piani.** Attiva di default su Free, Pro, Max; su Team/Enterprise la abilita l'owner e ogni membro resta spento finché non aderisce; non disponibile con accordi HIPAA, settore pubblico o retention personalizzata. [Verificato] T1 · help center 11817273.
- **Ricerca nelle chat passate.** Solo piani a pagamento, RAG, con citazioni; mai tra Project; Incognito escluso. Toggle "Search and reference chats". [Verificato] T1.
- **Project knowledge.** File e testo usati come contesto in ogni chat del Project; sui piani a pagamento passa a RAG quando si avvicina al limite. Non è memoria: è contenuto fornito da te. Il contesto non si condivide tra chat del Project se non lo aggiungi alla knowledge. [Verificato] T1 · <https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
- **Cowork.** La memoria è condivisa con Cowork solo quando Cowork gira in cloud; locale non la usa. [Verificato] T1 · help center 11817273.
- **Import/export.** L'help center dice che l'export della memoria legacy è possibile "until September 9, 2026" (scaduto). Vedi conflitti.

### B. Claude Code
- **Due sistemi**, entrambi caricati a inizio sessione: `CLAUDE.md` (scritto da te) e auto memory (scritta da Claude). [Verificato] T1 · <https://code.claude.com/docs/en/memory>
- **Ambiti `CLAUDE.md`:** policy gestita (Linux `/etc/claude-code/CLAUDE.md`), utente `~/.claude/CLAUDE.md`, progetto `./CLAUDE.md` o `./.claude/CLAUDE.md`, locale `CLAUDE.local.md`. Import con `@path`, profondità massima 4. [Verificato] T1.
- **`.claude/rules/`:** ricorsiva, supporta symlink; senza `paths` carica sempre, con `paths` solo sui file corrispondenti. Regole personali in `~/.claude/rules/`. [Verificato] T1.
- **Limiti:** consigliato < 200 righe per `CLAUDE.md`; un file fino a 4 MiB si carica intero, oltre viene saltato. `MEMORY.md`: prime 200 righe o 25 KB. [Verificato] T1.
- **Auto memory:** `~/.claude/projects/<project>/memory/` con indice `MEMORY.md` e un file per topic; quattro tipi (`user`, `feedback`, `project`, `reference`); `<project>` deriva dal repo git, condiviso tra worktree; esclusa dalla pulizia delle trascrizioni; locale alla macchina. Attiva di default nelle sessioni locali, spenta di default negli ambienti self-hosted. Controlli: `autoMemoryEnabled`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, `autoMemoryDirectory`. [Verificato] T1.
- **`/memory`:** apre l'elenco dei file e il toggle auto memory (dal 2.1.287 i tasti freccia lo commutano; dal 2.1.285 non si riattiva da una sessione in background). [Verificato] T1 · <https://code.claude.com/docs/en/changelog>
- **`AGENTS.md`:** vedi regola 8. Impostazione "Project instructions": `claude-md-or-agents-md` (default), `claude-md-and-agents-md`, `managed-only`. Prima della 2.1.281 alcune sessioni (Bedrock, telemetria spenta) leggevano solo `CLAUDE.md`. [Verificato] T1.
- **"Dreams":** nelle docs di Claude Code la parola non compare (pagina memory e `llms.txt`: zero occorrenze). Esiste come **API di Managed Agents**: un job asincrono legge un memory store e fino a 100 trascrizioni e produce un nuovo store deduplicato; research preview, richiede accesso, header `dreaming-2026-04-21`; l'input non viene modificato. [Verificato] T1 · <https://platform.claude.com/docs/en/managed-agents/dreams>. "Auto Dream" in Claude Code: solo blog terzi. [Segnale T3]

### C. API e Agent SDK
- **Memory tool** `memory_20250818`: client-side, directory `/memories`, comandi `view`, `create`, `str_replace`, `insert`, `delete`, `rename`; modelli Claude 4 e successivi; nessun beta header; l'API aggiunge al system prompt l'istruzione di guardare la memoria all'inizio. [Verificato] T1 · <https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>
- **Context editing:** lato server, beta (`context-management-2025-06-27`); con il memory tool Claude riceve un avviso prima della cancellazione per salvare ciò che serve. Il clearing invalida il prefisso della cache. [Verificato] T1 · <https://platform.claude.com/docs/en/build-with-claude/context-editing>
- **Compaction:** riassunto lato server dei turni vecchi; on demand in beta con `compact-2026-09-04` (14 set 2026). [Verificato] T1 · <https://platform.claude.com/docs/en/build-with-claude/compaction>
- **Prompt caching:** TTL 5 minuti (1 ora a costo extra); cambiare le definizioni dei tool invalida tutta la cache. Rapporto con compaction non letto (pagina letta per 100k su 160k caratteri). [Verificato] / [Inferenza] sul resto · T1.
- **Managed Agents:** memory stores con header `agent-memory-2026-07-22`, webhook `memory_store.*`. [Verificato] T1 · <https://platform.claude.com/docs/en/release-notes/overview>
- **Contesto:** il "context rot" (accuratezza e recall calano al crescere dei token) è documentato; la compaction server-side è la strategia primaria. [Verificato] T1 · <https://platform.claude.com/docs/en/build-with-claude/context-windows>

### D. Sessioni cloud, routine, attività pianificate (decisiva)
| Cosa | In una sessione cloud fresca? | Fonte (T1) |
|---|---|---|
| `CLAUDE.md`, `.claude/rules/`, skill/agent/command del repo | Sì (nel clone) | cloud-environments |
| `~/.claude/CLAUDE.md`, skill/agent/command utente | No (ricreabili con setup script) | cloud-environments |
| Auto memory locale | No | memory |
| Impostazioni utente `~/.claude/settings.json` | No; arrivano solo i managed settings server | cloud-environments |
| Skill abilitate su claude.ai, connettori dell'account | Sì | cloud-environments, routines |
| Memoria chat di claude.ai | Non documentato → [Inferenza]: no | help center 11817273 |
| Project memory (`MEMORY.md` del Project, beta Pro/Max) | Sì, in ogni thread cloud del Project | claude-projects |
- Una routine è prompt salvato + repo + connettori; ogni run crea una sessione nuova e non ne riusa. Il testo passato al fire è dato non fidato. [Verificato] T1 · <https://code.claude.com/docs/en/routines>
- Il thread di un Project eseguito sul tuo computer parte con le istruzioni del Project ma **senza** i file di memoria. [Verificato] T1 · <https://code.claude.com/docs/en/claude-projects>
- Che le routine create da un Project ereditino la project memory non è documentato. [Inferenza]
- Questa stessa sessione conferma l'ordine di grandezza: repo appena clonato, nessun `CLAUDE.md`.

### E. Passaggio di contesto tra chat
- Le docs API descrivono il degrado di accuratezza con il contesto (context rot) e raccomandano di curare cosa c'è nel contesto; per agenti multi-sessione indicano file di stato (progress log, checklist) letti all'avvio. [Verificato] T1 · context-windows; memory-tool ("Multisession software development pattern").
- Per claude.ai (Chat) le docs lette **non** danno una soglia per aprire una nuova chat: nessuna regola quantitativa verificata. [Inferenza] che un documento di handoff nel Project sia il pattern equivalente (Project knowledge è usata in ogni chat).

### F. Pattern esterni
| Pattern | Fonte e Tier | Costo | Rischio |
|---|---|---|---|
| `AGENTS.md` + cartella appunti nel repo | docs ufficiali, T1 | 0 | istruzioni ignorabili (non enforcement) |
| Server MCP `memory` ufficiale (grafo locale `memory.jsonl`) | github.com/modelcontextprotocol/servers, T2 (stelle e attività non lette) | 0 | file in chiaro, nessuna cifratura |
| mem0 | github.com/mem0ai/mem0, 67,4k stelle, Apache-2.0, T2 | libreria libera; cloud a pagamento (prezzi non letti) | cloud = dati verso terzi |
| basic-memory | github.com/basicmachines-co/basic-memory, 4,3k stelle, AGPL-3.0, T2 | 0 | licenza AGPL; fonte unica |
| mem0-mcp-selfhosted, guide Medium | directory/blog, T3 (87 stelle, marzo 2026) | 0 | [Segnale T3] |
Date degli ultimi commit non rilevabili (API GitHub 403 per il proxy).

### G. Confronto breve (solo ciò che cambia una decisione)
- ChatGPT, Gemini, Copilot: memorie di prodotto legate all'account; spegnere non cancella (ChatGPT e Copilot: serve cancellazione esplicita). [Verificato] su riassunti; T2/T1 provvisorio.
- Gemini: "past chats" è diventata "memory" (marzo 2026), con import da altre AI; non per account business. T1 · <https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/>
- Cursor: Rules in `.cursor/rules` e `AGENTS.md` (root e sottocartelle); le Memories sarebbero state rimosse dalla 2.1.x ma la sola fonte è un forum. [Segnale T3]
- Conseguenza pratica: `AGENTS.md` è l'unico standard comune a Claude Code e Cursor.

### H. Rischi
- **Privacy:** temi sensibili fuori di default, opt-in separato; Incognito non salva; la retention della chat non cancella le memorie derivate. [Verificato] T1.
- **Avvelenamento:** letteratura accademica (preprint, quasi tutti letti solo da snippet): memory poisoning, MemoryGraft, eTAMP, MINJA. [Verificato] come esistenza del rischio, T1-preprint · <https://arxiv.org/pdf/2606.04329>, <https://arxiv.org/abs/2512.16962>, <https://arxiv.org/pdf/2604.02623>. Nessuna doc Anthropic specifica per la memoria di claude.ai. [Inferenza]
- **Obsolescenza e igiene:** istruzioni in conflitto → Claude "may pick one arbitrarily"; `/doctor` ha un audit di `CLAUDE.md`, `AGENTS.md` e regole; Claude accorcia `MEMORY.md` quando è vicino al limite. [Verificato] T1.
- **Bug recenti (T1, github.com/anthropics/claude-code, issue chiuse):** #100205 memoria claude.ai non iniettata dopo il rollout "one Claude" (chiusa 10 ott 2026); #101785 contesto che dichiara la memoria disattivata quando è attiva (16 ott); #101732 `AGENTS.md` non caricato alla prima sessione in una nuova cartella su 2.1.296 (13 ott). Stato del fix non riverificato. [Verificato] come esistenza.

### I. Novità ultimi 90 giorni
- 2026-07-10: memoria claude.ai per topic; riepilogo mensile (beta) richiede memoria attiva (09-lug). 2026-08-25: memoria in Cowork, topics modificabili, opzione "Include sensitive topics". [Verificato] T1 · release notes support.
- API: memory stores Managed Agents (2-lug, 22-lug, 19-ago), compaction on demand (14-set). [Verificato] T1.
- Claude Code: 2.1.285 (auto memory non riattivabile da background), 2.1.287 (frecce in `/memory`), 2.1.288 (regole path-scoped con Write/Edit), 2.1.290 (fix `AGENTS.md` di sottocartella e symlink), 2.1.292/295 (Code Review usa `CLAUDE.md` della base). Corrente 2.1.303. [Verificato] T1.
- Modelli: Opus 5 (24-lug), Fable 5.1 e Mythos 5.1 (1-set), Opus 5.5 (22-set), Sonnet 5.5 (28-set), Haiku 5.5 (7-ott). [Verificato] T1.

## Tabella conflitti
| Tema | Fonte A | Fonte B | Come l'ho trattato |
|---|---|---|---|
| Scadenza export memoria legacy | Help center 11817273 (T1, s.d.): "Until September 9, 2026" | Release notes (T1, 10-lug-2026) e articolo 12123587 (T1): nessuna scadenza | Riporto entrambe; la data è passata; verifica direttamente in Settings > Memory |
| "Dreams" / "Auto Dream" | Docs Anthropic (T1): API Managed Agents, research preview | Blog implicator.ai, claudefa.st, pilot-shell (T3): funzione di Claude Code con toggle in `/memory` | Vale la T1; il resto è [Segnale T3] |
| Memorie Cursor | Docs Cursor (T2 prov.): non citano Memories | Forum Cursor (T3): rimosse dalla 2.1.x (2.1.17 vs 2.1.x) | [Segnale T3] |
| Toggle memoria ChatGPT | help.openai.com via snippet (T2): due interruttori collegati | Blog terzi: controllo unico | Non risolto; pagina 403 |
| Disponibilità Gemini memory | Blog Google: "not available to everyone" | Altre fonti: regionale | Non risolto |

## Cosa non è stato verificato
- `precedenti/` assente: nessun confronto con i due report del 18 ottobre.
- Reddit non raggiungibile: nessun dato Tier 2 da Reddit. Medium 403.
- Memoria chat dell'account → Claude Code cloud: assenza di documentazione, non prova di assenza.
- Date degli ultimi commit e stelle del server MCP `memory`; prezzi mem0; pagina `learn.microsoft.com` sulla memoria di Copilot.
- Changelog di Claude Code letto solo per ~200k caratteri (di ~1 MB): voci 2.1.277/2.1.281 e anteriori al 20 luglio non lette. API release notes lette per 100k su 127k; prompt caching per 100k su 160k.
- Preprint arXiv letti solo da snippet; la sede ICML 2026 di 2606.04329 non è stata aperta.
- Rapporto tra routine create da un Project e project memory.
- Cosa succede a una chat lunga in claude.ai oltre il context rot: nessuna soglia ufficiale trovata.

## Fonti per Tier
**Tier 1** — code.claude.com: [memory](https://code.claude.com/docs/en/memory) · [cloud-environments](https://code.claude.com/docs/en/cloud-environments) · [routines](https://code.claude.com/docs/en/routines) · [claude-projects](https://code.claude.com/docs/en/claude-projects) · [changelog](https://code.claude.com/docs/en/changelog) · [llms.txt](https://code.claude.com/docs/llms.txt). platform.claude.com: [memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) · [context-editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) · [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) · [prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · [context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) · [dreams](https://platform.claude.com/docs/en/managed-agents/dreams) · [release notes](https://platform.claude.com/docs/en/release-notes/overview). support.claude.com: [11817273](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) · [12138966](https://support.claude.com/en/articles/12138966-release-notes) · [12123587](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude) · [9519177](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects). GitHub: [anthropics/claude-code issues](https://github.com/anthropics/claude-code/issues). Google: [blog.google](https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/). arXiv (preprint): [2606.04329](https://arxiv.org/pdf/2606.04329) · [2512.16962](https://arxiv.org/abs/2512.16962) · [2604.02623](https://arxiv.org/pdf/2604.02623).
**Tier 2** — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) · [mem0](https://github.com/mem0ai/mem0) · [basic-memory](https://github.com/basicmachines-co/basic-memory) · [help.openai.com 11146739](https://help.openai.com/en/articles/11146739) (snippet) · [cursor.com/docs/context/rules](https://cursor.com/docs/context/rules) (provvisorio).
**Tier 3** — [forum.cursor.com](https://forum.cursor.com/t/are-my-memories-gone/144057) · [implicator.ai](https://www.implicator.ai/anthropic-adds-auto-dream-to-claude-code-fixing-memory-decay-between-sessions) · [claudefa.st](https://claudefa.st/blog/guide/mechanics/auto-dream) · [vantaige.io](https://vantaige.io/blog/claude-code-dreaming-memory-consolidation-setup-2026) · [simonwillison.net](https://simonwillison.net/search/?q=claude+memory).
