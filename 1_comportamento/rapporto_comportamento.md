---
tema: comportamento degli agenti con file di istruzioni (CLAUDE.md, AGENTS.md, rules, prompt)
versione: 1
base: a2d1a0c
verificato_il: 2026-10-25
aggiornato_il: 2026-10-27 (correzioni verificate dalle notti 03 e 04, riordino del repo)
rivalutare_se: "nuovo modello Claude, per esempio Opus 5.6; release notes di Claude Code che toccano CLAUDE.md, AGENTS.md, rules o hook; oppure 2026-12-18"
versioni_rilevate:
  claude_code: "2.1.310 del 2026-10-23 (changelog, primi 100.000 caratteri su 126.198; nessuna voce su AGENTS.md o prompt-audit dopo la 2.1.303)"
  modelli: "claude-fable-5-1, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5 (pagina models overview, senza date di rilascio; Opus 5.6 e Sonnet 5.6 non compaiono)"
  standard_agents_md: "agents.md: nessun numero di versione né data sulla pagina"
  altri_strumenti: "Codex, Copilot, Cursor, Gemini CLI, VS Code: documentazione corrente, senza numero di versione letto"
---

# Comportamento degli agenti: file di istruzioni, stato al 25 ottobre 2026 (v1)

Prima passata del tema 1. Parte da `main` (`a2d1a0c`). Non rifà il tema memoria: rimanda a [4_memoria/rapporto_memoria.md](../4_memoria/rapporto_memoria.md). Tag: [Verificato] [Inferenza] [Obsoleto/Conflitto] [Segnale T3]. Le docs di Anthropic non hanno date: la data è quella della lettura (2026-10-25), salvo dove indicato.

## Risposta breve
- Claude Code legge `CLAUDE.md`, non `AGENTS.md`; legge `AGENTS.md` solo se non c'è nessun `CLAUDE.md` (né `.claude/CLAUDE.md`, né `CLAUDE.local.md`) nella cartella di lavoro o sopra. Con entrambi i file: `@AGENTS.md` dentro `CLAUDE.md`.
- Un file di istruzioni è contesto, non vincolo: i divieti veri vanno in hook, permessi o impostazioni gestite.
- Pochi fatti concreti battono molte regole: meno di 200 righe per `CLAUDE.md`; procedure nelle skill; regole per cartella in `.claude/rules/` con `paths`.
- Un solo preprint misura l'effetto di `AGENTS.md`: i file scritti da un LLM non migliorano il successo e costano circa il 20% in più. È una misura, non una legge.
- I file di regole sono un vettore di attacco (caratteri Unicode invisibili, repo di terzi): trattali come codice.
- Opus 5.6 e Sonnet 5.6: non risultano usciti al 25 ottobre. Rivalutare tutto quando escono.

## REGOLE OPERATIVE PER AGENTI
1. Scrivi istruzioni abbastanza concrete da poterle verificare («Run `npm test` before committing», non «Test your changes»). [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
2. Tieni ogni `CLAUDE.md` sotto le 200 righe; sposta ciò che vale per una parte del codice in `.claude/rules/` con `paths`. Gli import `@` organizzano ma non riducono il costo di contesto. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
3. Includi ciò che Claude non può dedurre dal codice (comandi, stile diverso dal default, etichetta dei branch, trappole d'ambiente); escludi documentazione API, tutorial, descrizioni file per file. Test per ogni riga: toglierla farebbe sbagliare Claude? Se no, cancellala. [Verificato] · T1 · <https://code.claude.com/docs/en/best-practices>
4. Non scrivere due istruzioni che si contraddicono: i file sono concatenati e Claude può seguirne una a caso (regole utente e di progetto: nessuna prevale). Controlla con `/doctor prompt-audit`. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
5. Con `AGENTS.md` e `CLAUDE.md` insieme, metti `@AGENTS.md` nel `CLAUDE.md` (oppure imposta `claude-md-and-agents-md` in `/config`). Attenzione: un `CLAUDE.local.md` conta come `CLAUDE.md` e spegne la lettura di `AGENTS.md`. Serve Claude Code 2.1.277 o successivo. [Verificato] · T1 · <https://code.claude.com/docs/en/memory>
6. Per ciò che deve accadere sempre o non accadere mai usa un hook `PreToolUse` o i permessi, non `CLAUDE.md` né una skill: sono una richiesta, non una garanzia. [Verificato] · T1 · <https://code.claude.com/docs/en/features-overview>
7. Fatti e convenzioni sempre valide in `CLAUDE.md`; procedure e materiale di consultazione in una skill (`SKILL.md` sotto 500 righe; il corpo si carica solo all'uso). Se una sezione di `CLAUDE.md` è diventata una procedura, trasformala in skill. [Verificato] · T1 · <https://code.claude.com/docs/en/skills>
8. Un sottoagente carica `CLAUDE.md` (tranne Explore e Plan, e i custom con `omitClaudeMd: true`) ma non vede la conversazione: ripeti nel prompt di delega le regole che gli servono. [Verificato] · T1 · <https://code.claude.com/docs/en/sub-agents>
9. Nei prompt: di' cosa fare, non cosa evitare; dai il motivo; esempi diversi tra loro; tag XML coerenti; niente «CRITICAL: MUST» (i modelli recenti reagiscono troppo). Se una sola regola viene saltata, dai enfasi a quella riga soltanto. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>
10. A ogni cambio di modello rileggi le istruzioni: quelle scritte per modelli vecchi possono essere inutili (Opus 5.5: «Re-evaluate model-specific prompt instructions»). Esegui `/doctor prompt-audit` e rimuovi impalcature come «riassumi ogni 3 chiamate». [Verificato] · T1 · <https://platform.claude.com/docs/en/models/opus-5-5/migration-guide.md>
11. Non generare `AGENTS.md`/`CLAUDE.md` in automatico e lasciarli: in uno studio i file scritti da un LLM non hanno migliorato il successo e hanno aumentato il costo di circa il 20%. Tieni solo istruzioni non standard, assenti dal README, e misura l'effetto di ogni modifica. [Inferenza] sul preprint (un solo studio, un solo tipo di compito) · T1 (preprint) · <https://arxiv.org/pdf/2602.11988>
12. Tratta i file di istruzioni di repo di terzi come codice non fidato: rivedili prima di aprirli con un agente, non aggirare il dialogo di fiducia, ricorda che una sessione `-p` non lo mostra, e preferisci sandbox o VM. [Verificato] · T1 · <https://code.claude.com/docs/en/security>
13. Per più strumenti sullo stesso repo tieni una sola casa: `AGENTS.md` come file principale (letto da Codex, Cursor, Copilot, Gemini CLI con impostazione, VS Code), `CLAUDE.md` che lo importa; evita copie della stessa regola. [Verificato] per l'elenco di strumenti · T2 · <https://agents.md/>
14. Per Codex tieni la catena di `AGENTS.md` sotto 32 KiB (`project_doc_max_bytes`) e dividi in sottocartelle: oltre il limite il caricamento si ferma. [Verificato] · T2 · <https://learn.chatgpt.com/docs/agent-configuration/agents-md>
15. Per Gemini CLI il file è `GEMINI.md`; per fargli leggere `AGENTS.md` aggiungi il nome a `context.fileName` in `settings.json`. [Verificato] · T1 · <https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md>

## Stato dell'arte

### A. Chi legge cosa
| Strumento | File che legge | Annidati e precedenza | Limiti | Fonte e tag |
|---|---|---|---|---|
| Claude Code | `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md`, `.claude/rules/*.md`; gestito `/etc/claude-code/CLAUDE.md`; `AGENTS.md` solo se manca ogni `CLAUDE.md` | Dalla radice alla cartella di lavoro, concatenati; i file delle sottocartelle si caricano quando Claude vi legge un file; nessuna precedenza, in caso di conflitto «may pick one arbitrarily» | meno di 200 righe consigliate; `AGENTS.md` da 2.1.277 | [Verificato] T1 · [memory](https://code.claude.com/docs/en/memory) |
| Codex | `~/.codex/AGENTS.override.md` o `AGENTS.md`; per cartella: `AGENTS.override.md`, poi `AGENTS.md`, poi i nomi in `project_doc_fallback_filenames` | Un file per cartella, dalla radice Git alla cartella di lavoro; i più vicini vengono dopo e prevalgono | 32 KiB di default; catena costruita una volta per run | [Verificato] T2 · [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| Standard `AGENTS.md` | `AGENTS.md` in radice e nei sottoprogetti | «The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything» | nessun formato obbligatorio, nessun limite dichiarato; Aider e Gemini CLI richiedono configurazione | [Verificato] T2 provvisorio · [agents.md](https://agents.md/) |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo`, `excludeAgent`), `AGENTS.md` ovunque, oppure un `CLAUDE.md`/`GEMINI.md` in radice | Personali > repo > organizzazione, tutti forniti; il più vicino `AGENTS.md` prevale; repo-wide e path-specific: usati entrambi | nessun limite di dimensione dichiarato; per la review legge il branch di testa della PR | [Verificato] T2 provvisorio · [GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) |
| Cursor | `.cursor/rules/*.mdc` (`alwaysApply`, `globs`, `description`), `AGENTS.md` in radice e sottocartelle, User Rules, Team Rules | Team, Project, User: «earlier sources take precedence»; `AGENTS.md` annidato: il più specifico prevale | regole sotto 500 righe; `.md` semplici in `.cursor/rules` ignorati; `CLAUDE.md` non citato nella pagina | [Verificato] T2 provvisorio · [Cursor](https://cursor.com/docs/context/rules) |
| Gemini CLI | `~/.gemini/GEMINI.md`, `GEMINI.md` nel workspace e nei genitori, just-in-time nelle cartelle toccate | Tutti concatenati e mandati a ogni prompt; import `@file.md`; `/memory show` mostra il testo inviato | nome configurabile con `context.fileName` | [Verificato] T1 · [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md) |
| VS Code (Copilot) | `.github/copilot-instructions.md`, `*.instructions.md`, `AGENTS.md` (annidato sperimentale e spento di default), `CLAUDE.md` con `chat.useClaudeMdFile` | «Applicable instruction sources are additive»; nessuna precedenza: non affidarti all'ordine | le istruzioni non valgono per i suggerimenti inline | [Verificato] T1 · [VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) |

### B. Scrivere un buon CLAUDE.md
- Ambiti in ordine di caricamento, dal più ampio: gestito, utente (`~/.claude/CLAUDE.md`), progetto (`./CLAUDE.md` o `./.claude/CLAUDE.md`), locale (`./CLAUDE.local.md`, da mettere in `.gitignore`). `/init` genera una bozza e, se il file esiste, propone miglioramenti. Il `claudeMdExcludes` salta file di monorepo ma non quello gestito. I commenti HTML a blocco sono tolti prima dell'iniezione. [Verificato] T1 · [memory](https://code.claude.com/docs/en/memory)
- `.claude/rules/` senza `paths` si carica all'avvio; con `paths` solo quando Claude usa Read, Write o Edit su file corrispondenti. Le regole utente caricano prima di quelle di progetto. [Verificato] T1 · memory
- Anthropic: «Keep it concise»; i `CLAUDE.md` troppo lunghi fanno ignorare le istruzioni; trattalo come codice (rivedilo quando qualcosa va storto, potalo). Per una regola saltata: enfasi su quella riga sola. `/context` conferma il caricamento, `/doctor` propone tagli. [Verificato] T1 · [best-practices](https://code.claude.com/docs/en/best-practices)
- Il `CLAUDE.md` è caricato in anticipo, mentre altri file arrivano con glob e grep: approccio ibrido. Il post è del 2025-09-29 (più vecchio di 12 mesi) ma coerente con la pagina memory corrente. [Verificato] T1 · [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Una nota nuova rispetto a `memoria.md`: un `CLAUDE.md` annidato oltre il limite di dimensione ne carica solo l'inizio (2.1.309). [Verificato] T1 · [changelog](https://code.claude.com/docs/en/changelog)

### C. Istruzioni, skill, hook, sottoagenti, permessi
| Serve a | Strumento | Si carica | Costo di contesto | Fonte |
|---|---|---|---|---|
| Fatti e regole «sempre» | `CLAUDE.md` | A ogni sessione | A ogni richiesta | [features](https://code.claude.com/docs/en/features-overview) |
| Regole per cartella o linguaggio | `.claude/rules/` con `paths` | Quando si aprono file corrispondenti | Solo allora | features |
| Procedure, riferimenti | Skill | Descrizione sempre, corpo all'uso | Basso | [skills](https://code.claude.com/docs/en/skills) |
| Lavoro isolato che restituisce un riassunto | Sottoagente | Alla delega | Contesto separato (usarlo «per proteggere il contesto» è ora un consiglio superato nelle best practices: vedi [3_contesto/rapporto_contesto.md](../3_contesto/rapporto_contesto.md), regola 9) | [sub-agents](https://code.claude.com/docs/en/sub-agents) |
| Cose che devono accadere sempre | Hook | All'evento | Zero, salvo output | features |
| Tono e formato della risposta | Output style | A inizio sessione | A ogni richiesta | features |
- Cosa NON va in `CLAUDE.md` (tutte [Verificato] T1): divieti assoluti («an instruction is the wrong tool»: usa hook, permessi, impostazioni gestite), comportamenti da ripetere ogni volta (hook), procedure lunghe (skill), regole di percorso (rules), preferenze personali (file utente). [Verificato] T1 · [blog Anthropic, 2026-06-18](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- Livelli: `CLAUDE.md` è additivo; skill e sottoagenti si sovrascrivono per nome; gli hook si fondono. Skill duplicata: enterprise batte personale, personale batte progetto. [Verificato] T1 · features; skills
- Hook: possono bloccare un'azione (`PreToolUse`, exit 2) e `InstructionsLoaded` scatta quando si carica un file di istruzioni. [Verificato] T1 · [hooks-guide](https://code.claude.com/docs/en/hooks-guide) (letta in parte con grep)

### D. Scrivere le istruzioni nel prompt
- Principi (modelli attuali): chiarezza («show your prompt to a colleague» è il test), motivo dietro la regola, positivo meglio che negativo, 3-5 esempi in `<example>`, tag XML coerenti, ruolo in una frase, documenti lunghi in alto e domanda in fondo (fino a +30% nei test della pagina). Reazione forte al system prompt: ammorbidisci il maiuscolo. [Verificato] T1 · [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Agenti: avvisa dei limiti di contesto, limita i sottoagenti per i compiti semplici, chiedi conferma prima di azioni irreversibili, dai regole di perimetro contro l'eccesso di ingegneria. [Verificato] T1 · stessa pagina
- Opus 5.5: risponde a istruzioni specifiche e a «named prohibitions» meglio che a consigli generici; è sensibile al tempo trascorso; togli i «think carefully» e le istruzioni che spostano il ragionamento nella risposta; aggiunte lunghe al system prompt vanno alla prima richiesta. [Verificato] T1 · [Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- Opus 5: risposte più lunghe, chiedi brevità in modo esplicito; Fable 5.1: pochi aggiornamenti, chiedili. Sonnet 5.5 e Haiku 5.5 hanno guide proprie, lette dalla notte 03: vedi [2_istruzioni_project/rapporto_istruzioni_project.md](../2_istruzioni_project/rapporto_istruzioni_project.md), sezione F. [Verificato] T1 · prompting best practices
- Altezza giusta: né logica fragile né indicazioni vaghe; parti da un prompt minimo e aggiungi dopo i fallimenti osservati. [Verificato] T1 (2025-09-29) · context engineering

### E. Prove e studi
| Fonte | Cosa dimostra | Cosa non dimostra | Tag |
|---|---|---|---|
| [arXiv 2602.11988](https://arxiv.org/pdf/2602.11988) (preprint, 2026-02) | I file di contesto «do not generally improve» il successo e alzano il costo oltre il 20% (LLM: −0,5% su SWE-bench, −2% su CTXBench, non significativi; costo +20% e +23%); i file scritti da sviluppatori +2,4% su CTXBench, non significativo (p = 0,21) e meglio di quelli LLM (p = 0,038) | Non misura `CLAUDE.md` di Claude Code né modelli 5.x; con ogni altra documentazione rimossa i file LLM migliorano di circa il 2,7% | [Verificato] sul testo, via riassunto |
| [arXiv 2507.11538](https://arxiv.org/abs/2507.11538) (IFScale, preprint, 2025-07-15) | 20 modelli, 500 istruzioni di inclusione di parole: il migliore arriva al 68%; c'è un favore per le istruzioni iniziali | Compito sintetico, non agenti di codice; modelli vecchi | [Verificato] sull'abstract |
- Il consiglio «meno righe» di Anthropic è un consiglio; le due misure sopra lo sostengono in modo indiretto. [Inferenza]

### F. Sicurezza dei file di istruzioni
- Anthropic: per contenuti non fidati rivedi i comandi, evita di passare contenuti non fidati a Claude, verifica le modifiche a file critici, usa VM; il dialogo di fiducia non compare nelle sessioni `-p`; nel cloud VM isolate, rete limitata, push solo su branch. Nessuna pagina letta dice che i file di istruzioni sono scansionati. [Verificato] T1 · [security](https://code.claude.com/docs/en/security)
- Rules File Backdoor (Pillar, 2025-03-18): istruzioni nascoste in caratteri Unicode invisibili nei file di regole; riguardava Cursor e Copilot; secondo l'autore Cursor ha risposto che non era una vulnerabilità sua, GitHub ha aggiunto l'1-mag-2025 un avviso sul testo Unicode nascosto. Mitigazioni: audit dei file, revisione come codice. [Segnale T3] (blog di fornitore, non confermato da una fonte vendor letta)
- [arXiv 2601.17548](https://arxiv.org/abs/2601.17548) (SoK, 2026-01-24): 78 studi, 42 tecniche, 18 difese; oltre l'85% di successo contro difese allo stato dell'arte con attacchi adattivi; propone mitigazioni architetturali. Letto solo l'abstract; non cita `AGENTS.md`. [Verificato] sull'abstract
- [arXiv 2605.25871](https://arxiv.org/abs/2605.25871) (preprint, senza data): file di regole avvelenati su Cursor e Copilot, successo 41-84% (314 payload); cita CVE su un file di regole di Cursor e su una configurazione di progetto di Claude Code eseguita prima del dialogo di fiducia. I CVE non sono stati verificati alla fonte. [Verificato] sul riassunto; CVE [Inferenza]
- Difese convergenti: revisione dei file di istruzioni come codice, sandbox e permessi, hook, non fidarsi di regole importate. Nessun filtro è affidabile da solo.

### G. Un file solo per più strumenti
- Strategia documentata: `AGENTS.md` principale; per rinominare un file esistente, rinomina e crea un link simbolico col vecchio nome ([agents.md](https://agents.md/)). Claude Code: `@AGENTS.md` in `CLAUDE.md`, oppure impostazione `claude-md-and-agents-md`; un `AGENTS.md` già importato o linkato non è letto due volte. [Verificato] T2/T1 · [memory](https://code.claude.com/docs/en/memory)
- Limiti noti: Claude Code non segue link verso percorsi di rete e in sessioni Cowork salta un `~/.claude/CLAUDE.md` che sia un link simbolico; non legge `AGENTS.override.md`, `AGENTS.local.md` né `.agents/`. [Verificato] T1 · memory
- Gemini CLI e Aider richiedono configurazione; Cursor e Copilot leggono `AGENTS.md`; VS Code legge anche `CLAUDE.md` se abilitato. Windows e link simbolici: nessuna prova trovata.
- Raccomandazione per chi usa Claude Code con Cursor o Codex: un `AGENTS.md` con le regole comuni; un `CLAUDE.md` con la sola riga `@AGENTS.md` più le note specifiche di Claude; niente `CLAUDE.local.md` senza impostare `claude-md-and-agents-md`. [Inferenza] sui fatti citati

### H. Cosa cambia con un nuovo modello
- Opus 5.6 e Sonnet 5.6: la ricerca del 2026-10-25 non ha trovato un rilascio e la pagina dei modelli elenca solo Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5. Pagina senza data: «nessuna prova trovata» di una versione 5.6. [Verificato] T1 · [models](https://platform.claude.com/docs/en/about-claude/models/overview)
- Le guide ufficiali dicono che i modelli cambiano comportamento (Opus 4.7 aggiunge aggiornamenti di avanzamento da solo; Opus 5.5 con meno token; effort predefinito diverso): rileggi e togli l'impalcatura superata; `/claude-api migrate` applica le modifiche al codice. [Verificato] T1 · [migrazione Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide.md)
- Come rivalutare: `/doctor prompt-audit`, riesame delle istruzioni specifiche del modello, una prova su un compito noto prima e dopo. [Inferenza]

### I. Raccordo
Vedi la sezione seguente.

## Raccordo con i report precedenti
| Punto | Report | Stato oggi |
|---|---|---|
| Limite 200 righe, `AGENTS.md` solo senza `CLAUDE.md`, `@AGENTS.md`, hook contro `CLAUDE.md` | [4_memoria/rapporto_memoria.md](../4_memoria/rapporto_memoria.md) | Ancora vero, riletto da memory il 25-ott. Nuovo: `CLAUDE.local.md` conta come `CLAUDE.md` |
| `/doctor prompt-audit` | memoria.md | Ancora vero (memory) |
| Istruzioni brevi, positive, enfasi rara; nessuna precedenza ufficiale tra profilo, Project e memoria | report del 18 ottobre sui Project (rimosso il 27 ottobre; resta nella storia del repo) | Ancora vero per la parte su prompt (guida riletta). Parte sui Project: non ricontrollata in questa notte |
| `AGENTS.md` come strada comune e `@AGENTS.md` | report del 18 ottobre su app e Code (rimosso il 27 ottobre; resta nella storia del repo) | Confermato (memory, agents.md) |
| «Il cloud vede solo il repo» | memoria.md | Non riletto in questa notte; nessuna pagina letta lo contraddice |
| Memoria Cursor (rimozione) | memoria.md | Fuori tema, non riesaminato |

## Tabella conflitti
| Tema | Fonte A | Fonte B | Stato |
|---|---|---|---|
| Generare file con `/init` | memory: `/init` crea una bozza da rifinire (T1, corrente) | arXiv 2602.11988 (T1 preprint, 2026-02): omettere i file LLM | Non risolto: l'articolo misura `AGENTS.md` generati e lasciati com'erano, `/init` propone di rifinirli |
| Enfasi | prompting best practices: ammorbidire «CRITICAL» (T1) | best-practices: aggiungere «IMPORTANT» a una sola riga (T1) | Conciliabile: enfasi solo su una riga, mai diffusa |
| Precedenza | agents.md, Codex, Cursor: il più vicino/specifico prevale (T2) | Claude Code: concatenazione, nessuna precedenza (T1) | Divergenza reale tra strumenti, non risolta: non scrivere regole opposte |
| `AGENTS.md` e `copilot-instructions.md` | docs.github (T2): precedenza non indicata | VS Code (T1): fonti additive, non affidarsi all'ordine | Concordano: nessuna precedenza dichiarata |
| Risposta di Cursor al Rules File Backdoor | Pillar 2025-03-18 (T3): «non una vulnerabilità» | nessuna fonte vendor letta | Non risolto [Segnale T3] |

## Cosa non è stato verificato
- Il changelog di Claude Code è stato letto solo nei primi 100.000 caratteri (la pagina è più lunga); `skills` e `sub-agents` sono stati letti per 100.000 caratteri su circa 114.000; `hooks-guide` e `migration guide` con grep.
- I tre preprint sulla sicurezza e IFScale: solo abstract o riassunto; i CVE citati da 2605.25871 non sono stati controllati.
- Reddit, Stack Overflow e help.openai.com non sono stati interrogati; nessun dato su Windows e link simbolici per `AGENTS.md`.
- Rimando a memoria.md per la sessione cloud fresca; non ripetuta.
- Le istruzioni dei Project (tema 2) e il report del 18 ottobre sui Project non sono stati riverificati.

## Fonti per Tier
**Tier 1.** code.claude.com: [memory](https://code.claude.com/docs/en/memory) · [best-practices](https://code.claude.com/docs/en/best-practices) · [hooks-guide](https://code.claude.com/docs/en/hooks-guide) · [skills](https://code.claude.com/docs/en/skills) · [sub-agents](https://code.claude.com/docs/en/sub-agents) · [features-overview](https://code.claude.com/docs/en/features-overview) · [security](https://code.claude.com/docs/en/security) · [changelog](https://code.claude.com/docs/en/changelog). platform.claude.com: [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) · [migrazione](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide.md) · [models](https://platform.claude.com/docs/en/about-claude/models/overview). anthropic.com e claude.com: [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [steering](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more). Google: [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md). Microsoft: [VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions). arXiv (preprint): [2602.11988](https://arxiv.org/pdf/2602.11988) · [2507.11538](https://arxiv.org/abs/2507.11538) · [2601.17548](https://arxiv.org/abs/2601.17548) · [2605.25871](https://arxiv.org/abs/2605.25871).
**Tier 2.** [agents.md](https://agents.md/) · [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) · [GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) · [Cursor](https://cursor.com/docs/context/rules)
**Tier 3.** [Pillar](https://pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents)

## Guida
Le istruzioni d'uso per Claude e i passi per l'utente stanno in `D:\Workspace\best_practice\1_comportamento\guida_comportamento.md`.
