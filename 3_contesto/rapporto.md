---
tema: contesto di Claude (finestra, cosa la riempie, degrado, compattazione, chat e sessioni lunghe) in app, Claude Code e API
versione: 1
base: 22121a5
verificato_il: 2026-10-27
rivalutare_se: "nuovo modello Claude, per esempio Opus 5.6; release notes dell'app, di Code o dell'API che toccano contesto, compaction o limiti; oppure 2026-12-18"
versioni_rilevate:
  modelli: "claude-fable-5-1, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5: 1M token di contesto, 128K di output (models overview)"
  claude_code: "2.1.311 del 2026-10-26 (changelog)"
  app_claude_ai: "senza numero di versione; ultima voce delle release notes 2026-10-21"
  api: "ultima voce delle release notes 2026-10-23; compaction on demand compact-2026-09-04; compaction a soglia compact-2026-01-12; context editing context-management-2025-06-27"
  opus_5_6_sonnet_5_6: "non usciti al 2026-10-27 (release notes app e API, models overview, una ricerca)"
---

# Contesto di Claude: stato al 27 ottobre 2026 (v1)

Prima passata del tema 3. Temi già chiusi, non rifatti qui: [1_comportamento/rapporto.md](../1_comportamento/rapporto.md) (tema 1), [2_istruzioni_project/rapporto.md](../2_istruzioni_project/rapporto.md) (tema 2), [4_memoria/rapporto.md](../4_memoria/rapporto.md) (tema 4).

## Risposta breve
- Il contesto è tutto ciò che Claude ha davanti in una richiesta: prompt di sistema, istruzioni, strumenti, file, cronologia e la risposta stessa, ragionamento compreso. I quattro modelli correnti hanno 1M token (circa 555.000 parole).
- Più contesto non vuol dire risposte migliori: Anthropic chiama «context rot» il calo di accuratezza e richiamo al crescere dei token. I preprint lo misurano anche su Claude (Claude 4.5 Opus: 96,0% a 8K, 14,7% a 256K in un benchmark di agenti), mai sui modelli 5.x.
- Quando la finestra si riempie, tutte e tre le superfici riassumono: l'app (solo piani a pagamento con esecuzione di codice attiva), Code (in automatico verso circa 967K token sui modelli da 1M, o a mano con `/compact`), l'API (compaction on demand o a soglia). Il riassunto perde dettagli: le regole stabili vanno nei file che si ricaricano.
- Nell'uso quotidiano il problema non è finire lo spazio ma pagarlo: ogni richiesta rimanda tutta la conversazione. `/clear` (Code) o una chat nuova (app) tra lavori diversi è la mossa che rende di più.

## REGOLE OPERATIVE PER AGENTI
1. Metti le regole che devono durare nel `CLAUDE.md` della radice o in regole senza `paths:`: si ricaricano dal disco dopo la compattazione; regole con `paths:` e `CLAUDE.md` annidati vengono riassunti via e tornano solo su richiesta. [Verificato] · T1 · <https://code.claude.com/docs/en/context-window>
2. Prima di un compito lungo e nuovo usa `/compact` con un fuoco esplicito, oppure una sezione «Compact Instructions» nel `CLAUDE.md`: il riassunto automatico tiene richieste e codice chiave ma può perdere le istruzioni date all'inizio. [Verificato] · T1 · <https://code.claude.com/docs/en/how-claude-code-works>
3. Usa `/clear` tra lavori non collegati (non costa nulla) e, dopo due correzioni fallite sulla stessa cosa, `/clear` più un prompt nuovo che riassume ciò che hai imparato. [Verificato] · T1 · <https://code.claude.com/docs/en/best-practices>
4. Per abbandonare una strada usa `/rewind` invece di `/compact`: torna a un prefisso già in cache, mentre la compattazione legge tutta la conversazione e ne costruisce uno nuovo. [Verificato] · T1 · <https://code.claude.com/docs/en/prompt-caching>
5. Scegli modello ed effort all'inizio della sessione: cambiare modello rilegge tutta la cronologia senza cache; una modifica a `CLAUDE.md` a sessione aperta vale solo dopo `/clear`, `/compact` o un riavvio. [Verificato] · T1 · <https://code.claude.com/docs/en/prompt-caching>
6. Non dare per scontata la soglia di compattazione: sui modelli da 1M è circa 967K token, sui modelli senza contesto esteso il confine è 200K; `/autocompact` la porta tra 100K e 1M e `CLAUDE_CODE_AUTO_COMPACT_WINDOW` vince su tutto. [Verificato] · T1 · <https://code.claude.com/docs/en/model-config>
7. Fai girare ogni run lunga come sessione a sé: Claude Code manda tutta la conversazione a ogni richiesta, quindi una domanda di una riga in una sessione aperta da ore consuma per tutta la cronologia. [Verificato] · T1 · <https://code.claude.com/docs/en/costs>
8. Sposta le procedure specifiche da `CLAUDE.md` alle skill e scrivi in cima a `SKILL.md` ciò che conta: dopo la compattazione ogni skill usata torna troncata a 5.000 token (25.000 in tutto), tenendo l'inizio del file. [Verificato] · T1 · <https://code.claude.com/docs/en/context-window>
9. Usa i sottoagenti per lavoro parallelo, output rumorosi o una revisione indipendente, non «per proteggere il contesto» né per una risposta migliore: le docs correnti mettono queste due idee tra i consigli superati, e ogni sottoagente costa token propri. [Verificato] · T1 · <https://code.claude.com/docs/en/best-practices>
10. Nelle chat dell'app non contare sulla sintesi automatica senza esecuzione di codice attiva: serve per riassumere i messaggi vecchi vicino al limite; la cronologia resta, ma le chat lunghe consumano più limite d'uso. [Verificato] · T1 · <https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans>
11. Nei Project lascia lavorare il RAG, che parte da solo vicino al limite (fino a 10 volte la capacità, sui piani a pagamento) e non si regola; tieni brevi le Istruzioni e togli i file che non servono più. [Verificato] · T1 · <https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects>
12. Via API preferisci la compaction on demand dove c'è; nelle `instructions` (fino a 16.384 caratteri) di' cosa conservare e di non chiamare strumenti; dopo il riassunto rimanda immagini, documenti e istruzioni di sistema date a metà conversazione, che vanno persi. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand>
13. Negli agenti API con molti strumenti usa il context editing `clear_tool_uses_20250919` con `clear_at_least` ed `exclude_tools`: ogni pulizia invalida la cache del prefisso, quindi deve liberare abbastanza da valerne la pena. [Verificato] · T1 · <https://platform.claude.com/docs/en/build-with-claude/context-editing>
14. Non riempire il contesto solo perché c'è spazio: in un benchmark di agenti Claude 4.5 Opus scende da 96,0% a 14,7% tra 8K e 256K token, e la gestione del contesto (soprattutto la chiamata programmatica degli strumenti) recupera parte del calo. [Inferenza] sul preprint · T1 (preprint) · <https://arxiv.org/html/2602.07962>
15. A ogni nuovo modello rileggi finestre, conservazione del ragionamento e tabella di compatibilità prima di fidarti dei numeri di questo file; context awareness, per esempio, non c'è su Opus 5.5, Sonnet 5.5, Haiku 5.5 e Fable 5.1. [Inferenza] · T1 · <https://platform.claude.com/docs/en/build-with-claude/context-windows>

## Stato dell'arte

### A. Che cos'è e cosa lo riempie
- **Definizione.** Tutto il testo a cui il modello può riferirsi nel generare, risposta compresa: una «working memory», diversa dai dati di addestramento. [Verificato] T1 · [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **API: cosa conta.** Prompt di sistema, ogni messaggio (risultati di strumenti, immagini, documenti), definizioni degli strumenti, l'output del turno con il ragionamento esteso. I token in cache contano lo stesso: la cache cambia il prezzo, non lo spazio. Fino a 600 immagini o pagine PDF per richiesta. [Verificato] T1 · context windows
- **API: ragionamento.** Su Opus 4.5 e successivi, Sonnet 4.6 e successivi, Haiku 5.5 e Fable 5.1 i blocchi di ragionamento dei turni precedenti restano e contano come input; sui modelli più vecchi l'API li toglie. [Verificato] T1 · context windows
- **Finestre per modello.** Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5: 1M token di default, senza header beta, 128K di output; Haiku 5.5 costa di più sopra 100.000 token di prompt. 1M token sono circa 555.000 parole. [Verificato] T1 · context windows; [models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- **App (chat), per modello.** 1M: Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Haiku 5.5. 500K: Fable 5, Opus 4.8, 4.7, 4.6, Sonnet 4.6. Gli altri 200K. La pagina copre solo i piani a pagamento e non dà cifre per piano; il piano Free non è citato. Una parte della finestra è riservata alla risposta. [Verificato] T1 · [help 8606394](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans); [help 11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- **Cowork.** 1M per la maggior parte dei modelli correnti, ma Haiku 5.5 500K; Sonnet 5 compatta a 500K. [Verificato] T1 · help 8606394
- **App: cosa la riempie.** Nessuna pagina elenca il contenuto per intero. Le pagine dicono: Project con RAG (entra solo il pertinente), Istruzioni del Project da tenere brevi, strumenti e connettori «token-intensive». Che vi entrino anche cronologia, file allegati, Istruzioni e memoria è [Inferenza] coerente con la definizione dell'API. · help 8606394; help 11647753
- **Claude Code, prima di scrivere.** `CLAUDE.md` (o `AGENTS.md`), auto memory (prime 200 righe o 25 KB di `MEMORY.md`), nomi degli strumenti MCP (definizioni rinviate di default), descrizioni delle skill, prompt di sistema, output style. Poi ogni file letto, regole con `paths:` accanto ai file che toccano, output degli hook, promemoria di sistema (file cambiati sul disco, righe di attribuzione). `/context` mostra la ripartizione reale. [Verificato] T1 · [context window](https://code.claude.com/docs/en/context-window); [how it works](https://code.claude.com/docs/en/how-claude-code-works)
- **Claude Code, 1M.** Fable, Sonnet 5 e successivi, Haiku 5.5 e Opus 4.7 e successivi hanno 1M nativo, senza suffisso; Opus 4.6 e Sonnet 4.6 solo con `[1m]` e, su Pro, crediti d'uso. `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` lo spegne. [Verificato] T1 · [model-config](https://code.claude.com/docs/en/model-config)

### B. Degrado
- **Cosa dice Anthropic (consiglio, non misura).** «As token count grows, accuracy and recall degrade»: context rot; quindi conta scegliere cosa mettere quanto lo spazio. [Verificato] T1 · context windows. La compattazione serve anche perché «response quality degrades as a conversation grows». [Verificato] T1 · [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction)
- **Perché (spiegazione di Anthropic).** Ogni token consuma un «attention budget»; il transformer crea «n² pairwise relationships» e i modelli hanno visto meno sequenze lunghe in addestramento. Post del 2025-09-29 (oltre 12 mesi), coerente con la pagina context windows corrente. [Verificato] T1 · [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **In Code.** «instructions from early in the conversation can get lost»: le regole stabili vanno in `CLAUDE.md`. [Verificato] T1 · how it works. Ma con 1M e compattazione vicina al tetto «you'll rarely run out of context»: il guaio è il costo, e un contesto concentrato dà risposte migliori. [Verificato] T1 · [best practices](https://code.claude.com/docs/en/best-practices)
- **Misure (preprint, Tier 1 con nota «preprint»).**
  - Lunghezza da sola: con recupero perfetto, calo tra 13,9% e 85% su matematica, domande e codice, «well within the models' claimed lengths»; cinque modelli, nominato solo GPT-4o; rimedio: far recitare le prove prima di rispondere (+4% su RULER). Solo abstract. [2510.05381](https://arxiv.org/abs/2510.05381) (2025-10-06)
  - Posizione: risultati migliori con l'informazione all'inizio o alla fine, peggiori nel mezzo. Modelli del 2023, solo abstract, [Obsoleto?] per i modelli correnti. [2307.03172](https://arxiv.org/abs/2307.03172)
  - Numero di istruzioni: con 500 istruzioni i migliori modelli arrivano al 68%; preferenza per le prime istruzioni. 20 modelli, versioni Claude non nominate nell'abstract. [2507.11538](https://arxiv.org/abs/2507.11538) (2025-07-15)
  - Agenti con contesto che cresce (LOCA-bench, testo completo): da 8K a 256K Claude-4.5-Opus 96,0% → 14,7%, GPT-5.2-Medium 72,0% → 21,3%, Gemini-3-Flash 64,0% → 17,3%; distacchi da circa 32K. A 128K pulizia dei risultati e del ragionamento danno guadagni piccoli; la chiamata programmatica degli strumenti i più costanti; Claude provato solo con questa (34,0 → 40,0; 49,3 con l'implementazione di Anthropic). 15 compiti, dipende dallo scaffold. [2602.07962](https://arxiv.org/html/2602.07962) (2026-02-08)
  - Profili per lunghezza (ATLAS, 26 modelli, 8K-1M): le classifiche cambiano molto tra 128K e 1M; Claude-Opus-4.6 primo a 1M. Solo abstract. [2605.28079](https://arxiv.org/abs/2605.28079) (2026-05-27)
- **Distinzione.** Misurato: calo con la lunghezza e con la densità di istruzioni, su modelli fino a Opus 4.6 e 4.5. Non misurato: Claude 5.x, l'app, la compattazione di Code. Il consiglio «tieni il contesto concentrato» è di Anthropic; il legame con i numeri dei preprint è [Inferenza].

### C. Compattazione e riassunto
- **App.** «For users on paid plans with code execution enabled, Claude automatically manages your conversation context»: vicino al limite riassume i messaggi vecchi, la cronologia completa resta consultabile, compare «organizing its thoughts»; casi rari (primo messaggio enorme, errori) arrivano comunque al limite. «Longer conversations that trigger automatic context management use more of your usage limit.» Nessuna soglia numerica per la chat. [Verificato] T1 · help 8606394; help 11647753
- **Code, quando.** Automatica vicino al limite: circa 967K token sui modelli con 1M nativo; al confine di 200K sui modelli senza contesto esteso; per un ID non riconosciuto alla finestra presunta (200K). `/autocompact 500k` per modello, `autoCompactWindow` per tutti, intervallo 100K-1M. Compattazione da inattività sulle sessioni con cache di un'ora oltre circa 200K, poco prima che la cache scada; si spegne con `idleCompaction: false`. [Verificato] T1 · model-config; best practices; [prompt caching](https://code.claude.com/docs/en/prompt-caching)
- **Code, cosa sopravvive.** Prompt di sistema e output style restano; `CLAUDE.md` della radice, regole senza `paths:`, auto memory e piano rientrano dal disco; descrizioni delle skill ricostruite (v2.1.304+); fino a cinque file letti o modificati, i più recenti (oltre 5.000 token solo come riferimento); corpi delle skill usate fino a 5.000 token ciascuna e 25.000 in tutto; contesto aggiunto dagli hook riassunto; hook `SessionStart` con sorgente `compact` rieseguiti. Regole con `paths:` e `CLAUDE.md` annidati: riassunti via, ricaricati quando servono. [Verificato] T1 · context window
- **Code, come orientarla.** `/compact` con un fuoco; sezione «Compact Instructions» in `CLAUDE.md`; `/rewind` con «Summarize from here» o «up to here»; se un solo file riempie subito il contesto, dopo qualche tentativo Code si ferma con un errore invece di girare a vuoto. [Verificato] T1 · context window; how it works
- **Code, novità recenti.** 2.1.304: il riassunto riporta i nomi degli strumenti usati e la lista delle skill torna dopo la compattazione. 2.1.311 (26-ott): chiede il riassunto una volta in più prima di sostituire la conversazione; corretto un caso in cui Claude vedeva `MEMORY.md` e `CLAUDE.md` vecchi subito dopo la compattazione. [Verificato] T1 · [changelog](https://code.claude.com/docs/en/changelog)
- **API, due tipi.** On demand (`compact-2026-09-04`, parametro `compaction`, decide l'applicazione; il blocco firmato va primo in `messages` e i messaggi riassunti si tolgono; si può ricompattare) e a soglia (`compact-2026-01-12`, `compact_20260112`, default 150.000 token di input, minimo 50.000, `pause_after_compaction`, l'API scarta ciò che precede il blocco). «Use on-demand compaction wherever it is available.» Non si combinano `compaction` e `context_management` nella stessa richiesta. Il costo del riassunto sta in `usage.iterations`. [Verificato] T1 · compaction; [on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand); [a soglia](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold)
- **API, cosa si perde.** Immagini, documenti, `container_upload` e URL letti nei messaggi riassunti; le istruzioni dei messaggi `system` interni all'intervallo; il livello di effort per messaggio. Sui modelli 5.5 e Fable 5.1 la compaction a soglia non porta avanti il ragionamento precedente. [Verificato] T1 · on demand; a soglia
- **API, context editing.** Beta `context-management-2025-06-27`: pulizia dei risultati degli strumenti (`clear_tool_uses_20250919`, soglia default 100.000 token, `keep` 3 coppie, `clear_at_least`, `exclude_tools`, segnaposto al posto del risultato) e dei blocchi di ragionamento (`clear_thinking_20251015`). La pulizia dei risultati invalida la cache; con il memory tool Claude riceve un avviso per salvare prima. Per la maggior parte dei casi la strategia principale resta la compaction lato server. Letti 100.000 di 103.379 caratteri. [Verificato] T1 · [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)

### D. Cosa caricare e quando
- **Ibrido.** Anthropic descrive due vie: caricare tutto prima o tenere riferimenti leggeri (percorsi, query) e leggere al momento; Claude Code fa entrambe, `CLAUDE.md` subito e glob e grep per il resto. Il recupero al momento è più lento. [Verificato] T1 (2025-09-29) · context engineering
- **Skill.** Si vedono nome e descrizione; il corpo entra solo quando servono. `disable-model-invocation: true` toglie anche la descrizione finché non le chiami. Le procedure di un flusso pesano meno in una skill che in `CLAUDE.md`. [Verificato] T1 · how it works; [costs](https://code.claude.com/docs/en/costs)
- **MCP.** Definizioni rinviate di default (tool search): fino all'uso entrano solo nomi e istruzioni del server; le CLI come `gh` restano più leggere. [Verificato] T1 · costs
- **Sottoagenti.** Finestra propria, tornano con un riassunto (Anthropic parla di 1.000-2.000 token nel post del 2025). Le best practices correnti però: «Running out of context is rarely the problem anymore», ogni sottoagente costa token e non migliora la risposta. [Verificato] T1 · context engineering; best practices
- **Project dell'app.** Il RAG parte da sé vicino al limite e porta fino a 10 volte la capacità; la pagina non dice se le Istruzioni ci rientrino. [Verificato] T1 · [RAG](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects). Fatti già verificati su `CLAUDE.md`, skill e Istruzioni: [1_comportamento/rapporto.md](../1_comportamento/rapporto.md), [2_istruzioni_project/rapporto.md](../2_istruzioni_project/rapporto.md).

### E. Chat e sessioni lunghe
- **App, consigli ufficiali.** Vicino al limite d'uso apri una conversazione nuova; usa i Project; Istruzioni brevi; togli i file inutili; spegni ragionamento esteso, connettori e ricerca web quando non servono; abbassa l'effort per i compiti di routine. [Verificato] T1 · help 11647753
- **Code, comandi.** `/clear` tra lavori diversi (gratis; `/clear nome` dà un nome alla sessione); `/compact` con fuoco, che però legge tutta la conversazione ed è costoso a cache scaduta; `/rewind` per tornare indietro o riassumere una parte; `/btw` per una domanda a lato che non resta nella cronologia; `/rename` e `claude --resume nome` per i lavori di più giorni. Ogni sessione nuova parte senza la cronologia delle altre. [Verificato] T1 · best practices; how it works
- **Costi e limiti.** Ogni richiesta rimanda tutta la conversazione, e ogni uso di strumenti una richiesta in più. Cache: circa un'ora in abbonamento, cinque minuti con chiave API, provider cloud o crediti d'uso; cinque minuti per i sottoagenti. Dopo una pausa più lunga la cache scade e si riprocessa tutto. Anche attività programmate, messaggi tra sessioni, sottoagenti e compagni di squadra consumano mentre la sessione è ferma. [Verificato] T1 · costs; best practices
- **Prompt caching in breve.** La cache confronta l'inizio esatto della richiesta: cambiare modello, attivare la modalità veloce, aggiungere o togliere server MCP o plugin con server MCP, vietare un intero strumento senza tool search, compattare, accumulare immagini o aggiornare Code la invalidano. Sui modelli 5.5 e Fable 5.1 cambiare effort non la invalida (chiave API o abbonamento). Modificare file o `CLAUDE.md`, cambiare modalità dei permessi o stile, usare skill, `/recap` e `/rewind` la conservano. [Verificato] T1 · prompt caching
- **Documento di passaggio.** Nessuna pagina ufficiale lo chiama così: pratica di comunità [Segnale T3]. Due cose vicine sono ufficiali: scrivere uno `SPEC.md` e ricominciare in una sessione fresca (best practices), e progettare file di stato perché una nuova sessione si rimetta in pari in fretta (context windows). Quindi un documento di passaggio è coerente con le docs [Inferenza].

### F. Modelli
| Modello | ID API | Finestra API | Output max | Effort default API | Note sul contesto |
| --- | --- | --- | --- | --- | --- |
| Fable 5.1 | `claude-fable-5-1` | 1M | 128K | high | ragionamento sempre attivo; nessuna context awareness |
| Opus 5.5 | `claude-opus-5-5` | 1M | 128K | medium | ragionamento sempre attivo; nessuna context awareness |
| Sonnet 5.5 | `claude-sonnet-5-5` | 1M | 128K | high | nessuna context awareness |
| Haiku 5.5 | `claude-haiku-5-5` | 1M (500K in Cowork) | 128K | medium | prompt oltre 100K costano di più |
Fonti: [models overview](https://platform.claude.com/docs/en/about-claude/models/overview); context windows; help 8606394. [Verificato] T1. In Claude Code l'effort predefinito è `medium` per Opus 5.5, Sonnet 5.5 e Haiku 5.5 (model-config): diverso dall'API per Sonnet 5.5, perché sono due prodotti.
- **Context awareness.** Solo Sonnet 5, Sonnet 4.6, Sonnet 4.5 e Haiku 4.5 ricevono il conto dei token rimasti; Opus 4.7 e successivi, Sonnet 5.5, Fable 5.1 e Haiku 5.5 no: per loro c'è il budget di compito (beta). [Verificato] T1 · context windows
- **Opus 5.6 e Sonnet 5.6.** Non risultano usciti al 27 ottobre: assenti dalle release notes dell'app (ultima voce 2026-10-21), da quelle dell'API (ultima 2026-10-23, letti 100.000 di 133.491 caratteri), dal models overview e da una ricerca web. [Verificato] T1 · [release notes app](https://support.claude.com/en/articles/12138966-release-notes); [release notes API](https://platform.claude.com/docs/en/release-notes/overview)
- **Come rivalutare.** Le best practices di Code hanno una tabella «What you can stop doing»: consigli giusti per i modelli vecchi (gestire il contesto in modo aggressivo, sottoagenti per proteggerlo, maiuscole) oggi superati. A ogni modello nuovo: rileggere context windows (finestra, ragionamento conservato, context awareness), le liste di compatibilità della compaction, le soglie di model-config, e guardare `/context` in una sessione vera. [Inferenza] sui passi · best practices; context windows

### G. Raccordo
Vedi la sezione «Raccordo con i report precedenti».

### H. Modello di pratica (generico, [Inferenza] su ogni voce)
Per chi usa l'app:
1. Un Project per lavoro; Istruzioni brevi; solo i file che servono (A, D, E).
2. Un argomento per chat; quando cambi argomento o la chat è lunga, chat nuova nello stesso Project con tre righe su dove eri (B, E).
3. Esecuzione di codice attiva se vuoi che le chat lunghe si riassumano da sole; sapendo che il riassunto perde dettagli (C).
4. Connettori, ricerca web e ragionamento esteso accesi solo quando servono (E).
5. Le cose che contano all'inizio o alla fine del messaggio, non sepolte in mezzo (B, preprint).
Per chi usa Code:
6. Regole stabili nel `CLAUDE.md` della radice, sotto 200 righe; procedure nelle skill, con l'essenziale in cima (A, C, D).
7. Modello ed effort scelti all'inizio; niente cambi a metà compito (E).
8. `/clear` tra compiti; `/rename` prima se vuoi tornarci (E).
9. `/compact` con un fuoco alle pause naturali, non a metà; `/rewind` per abbandonare una strada (C, E).
10. Dopo due correzioni fallite: `/clear` e un prompt nuovo che contiene ciò che hai imparato (E).
11. Output rumorosi (test, log) filtrati da un hook o mandati a un sottoagente, sapendo che il sottoagente costa (D).
12. Run lunghe come sessioni a sé, con il contesto nel prompt e nel repo (E; [4_memoria/rapporto.md](../4_memoria/rapporto.md)).
13. `/context` e `/usage` quando i consumi salgono senza motivo (A, E).
14. A ogni modello nuovo, rileggere numeri e regole (F).

## Raccordo con i report precedenti
| Punto | Report | Stato al 27-ott |
| --- | --- | --- |
| Chat lunghe: sintesi automatica, cronologia conservata, nessuna soglia | [4_memoria/rapporto.md](../4_memoria/rapporto.md) regola 15 ed E | Ancora vero. In più: solo piani a pagamento con esecuzione di codice attiva; le chat lunghe consumano più limite. L'articolo 11647753 ha cambiato titolo e indirizzo («how-do-usage-and-length-limits-work») |
| `CLAUDE.md` della radice sopravvive a `/compact` | memoria.md B | Ancora vero; ora c'è la tabella completa (auto memory, skill, cinque file) |
| Compattazione da inattività (2.1.299, oltre 200K, circa 54 minuti) | memoria.md B | Cambiato nella forma: le docs ora la legano alla cache di un'ora; versione del controllo in conflitto (vedi tabella) |
| Cache con TTL di 5 minuti (API) | memoria.md C | Ancora vero per chiave API; in Code con abbonamento la conversazione principale ha un'ora |
| Compaction on demand dal 2026-09-14 | memoria.md C | Ancora vero (release notes API) |
| Claude Code 2.1.303 | memoria.md intestazione | Superato: 2.1.311 del 2026-10-26 |
| Context rot: accuratezza e richiamo calano con i token | memoria.md C; istruzioni_project.md C | Ancora vero, stessa pagina |
| `CLAUDE.md` sotto 200 righe; gli import non riducono il costo | [1_comportamento/rapporto.md](../1_comportamento/rapporto.md) regola 2 | Ancora vero (costs: «under 200 lines») |
| Sottoagente come contesto separato | comportamento.md (tabella) | Ancora vero, ma «usali per proteggere il contesto» è ora un consiglio superato |
| Context rot non misurato su Claude 5.5 | [2_istruzioni_project/rapporto.md](../2_istruzioni_project/rapporto.md) C | Ancora vero: i preprint arrivano a Opus 4.6 |
| RAG nei Project fino a 10x; Istruzioni dentro o fuori: ignoto | istruzioni_project.md A | Ancora vero; ancora ignoto |
| Documenti lunghi in alto, domanda in fondo (+30%) | istruzioni_project.md C | Non riletto qui; coerente con 2307.03172 |
| README, punto 11: le chat molto lunghe peggiorano | [README](../README.md) | Coerente con context rot e consigli dell'app |

## Tabella conflitti
| Tema | Fonte A (data, Tier) | Fonte B (data, Tier) | Stato |
| --- | --- | --- | --- |
| Sintesi automatica dell'app e limite d'uso | snippet di ricerca attribuito a help 8606394: non conta sul limite (data ignota, T1 non letto) | help 8606394 letto: usa più limite (corrente, T1) | Risolto a favore della pagina letta |
| Versione del controllo `idleCompaction` | prompt caching: richiede v2.1.290 (corrente, T1) | memoria.md: introdotta in 2.1.299 (2026-10-14, T1 changelog) | Non risolto: forse impostazione e funzione hanno date diverse; changelog non riletto oltre 2.1.300 |
| Suffisso `[1m]` | model-config: varianti `[1m]` documentate (corrente, T1) | changelog 2.1.311: «drop the `[1m]` suffix and its label» nei nomi (2026-10-26, T1) | Non risolto: probabile modifica solo di visualizzazione |
| Sottoagenti per il contesto | context engineering: architetture a sottoagenti (2025-09-29, T1) | best practices: consiglio superato (corrente, T1) | Risolto a favore della pagina corrente; i sottoagenti restano utili per altri scopi |
| Effort predefinito di Sonnet 5.5 | models overview: high nell'API (corrente, T1) | model-config: medium in Code (corrente, T1) | Risolto: due prodotti diversi |
| Finestra di Haiku 5.5 | API e chat: 1M (corrente, T1) | Cowork: 500K (corrente, T1) | Risolto: dipende dalla superficie |

## Cosa non è stato verificato
- Elenco ufficiale di cosa entra nel contesto di una chat dell'app (memoria, profilo, stili, allegati): nessuna pagina lo dà; pagine controllate: help 8606394, help 11647753, RAG.
- Soglia della sintesi automatica nell'app e cosa conserva; finestra del piano Free.
- Se le Istruzioni di un Project rientrano nel RAG.
- Testo completo dei preprint 2510.05381, 2307.03172, 2507.11538, 2605.28079 (letti solo come abstract); nessuna misura su Claude 5.x.
- Changelog di Code oltre i primi 100.000 caratteri (versioni sotto 2.1.300); ultimi 3.379 caratteri di context editing, ultimi 14.607 di compaction a soglia (esempi di codice), ultimi 33.491 delle release notes API.
- Pagina `settings-reference` (`idleCompaction`) non letta: il dettaglio dei minuti resta quello di memoria.md.
- Pagina routines letta solo nell'anteprima (serve al tema 5).

## Fonti per Tier
**Tier 1.** code.claude.com: [context-window](https://code.claude.com/docs/en/context-window) · [how-claude-code-works](https://code.claude.com/docs/en/how-claude-code-works) · [model-config](https://code.claude.com/docs/en/model-config) · [costs](https://code.claude.com/docs/en/costs) · [best-practices](https://code.claude.com/docs/en/best-practices) · [prompt-caching](https://code.claude.com/docs/en/prompt-caching) · [changelog](https://code.claude.com/docs/en/changelog). platform.claude.com: [context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) · [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) · [compaction-on-demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) · [compaction-threshold](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold) · [context-editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) · [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) · [release notes](https://platform.claude.com/docs/en/release-notes/overview). support.claude.com: [8606394](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans) · [11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) · [11473015](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) · [12138966](https://support.claude.com/en/articles/12138966-release-notes). anthropic.com: [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). arXiv (preprint): [2510.05381](https://arxiv.org/abs/2510.05381) · [2307.03172](https://arxiv.org/abs/2307.03172) · [2507.11538](https://arxiv.org/abs/2507.11538) · [2602.07962](https://arxiv.org/html/2602.07962) · [2605.28079](https://arxiv.org/abs/2605.28079)
**Tier 2.** Nessuna fonte usata: per il tema 3 bastavano le pagine ufficiali.
**Tier 3.** Nessuna fonte letta; il documento di passaggio resta [Segnale T3] senza fonte citata.

## Guida
Le istruzioni d'uso per Claude e i passi per l'utente stanno in `D:\Workspace\best_practice\3_contesto\guida.md`.
