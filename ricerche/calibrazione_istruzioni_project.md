# Calibrazione fonti, notte 03 (istruzioni di un Project, v1, 2026-10-26)

## Cosa ha funzionato
- **Tutto Tier 1 Anthropic**: support.claude.com (11 articoli), code.claude.com, platform.claude.com, anthropic.com, claude.com, academy.claude.com, arxiv.org. Nessuna fonte di Tier 2 o 3 necessaria: le domande A–F si chiudono sulle pagine ufficiali.
- Le pagine del Help Center portano quasi sempre solo «Updated this week» o «Updated over a week ago»: la data in pagina c'è solo per RAG (2026-09-10), la pagina CLAUDE.md (2026-04-15), projects-redesigned (2026-09-17) e il post di engineering (2025-09-29).
- Le pagine più lunghe (`claude-projects`, 60 KB) vengono salvate su file dallo strumento: si leggono con `grep` e `sed` sulle sezioni.
- Le risposte di WebFetch sono riassunti di un modello piccolo: i virgolettati del README sono quelli visti nel testo ricevuto; per i preprint solo abstract.
- `claude.com/docs/cowork/guide/projects.md` (suffisso `.md`) restituisce il testo originale della pagina: più fedele dei riassunti.

## Cosa è stato bloccato
| Dominio | Esito | Trattamento |
|---|---|---|
| support.claude.com (2 articoli), code.claude.com, academy.claude.com | PROVENANCE_REQUIRED al primo tentativo, nel primo gruppo di quattro letture parallele | secondo tentativo sugli stessi URL riuscito, senza altri permessi; nessun aggiramento |
| Reddit, Stack Overflow, help.openai.com | non interrogati (tema 2: nessuna fonte di Tier 2 necessaria) | — |

## Esito dei permessi (prova richiesta)
- Il repo pre-approva in `.claude/settings.json` i domini ufficiali con `WebFetch(domain:...)`; tutti gli URL del prompt erano elencati nel messaggio. **Richieste di permesso o errori PROVENANCE_REQUIRED comparsi: sì, 4 (le prime quattro letture, lanciate in parallelo).**
  | Lettura | Esito |
  |---|---|
  | support.claude.com 9519177 | tentativo 1 PROVENANCE_REQUIRED; tentativo 2 ok |
  | support.claude.com 10185728 | tentativo 1 PROVENANCE_REQUIRED; tentativo 2 ok |
  | code.claude.com/docs/en/claude-projects | tentativo 1 PROVENANCE_REQUIRED; tentativo 2 ok |
  | academy.claude.com (corso Project) | tentativo 1 PROVENANCE_REQUIRED; tentativo 2 ok |
  | tutte le altre 27 letture (support, platform, code, claude.com, anthropic.com, arxiv.org) | ok al primo tentativo, nessuna richiesta |
- Lettura dei dati: le regole `allow` non hanno evitato le prime quattro richieste, né quelle sugli URL scritti nel prompt (che erano solo quattro dei sei). Dopo il secondo tentativo non sono comparse altre richieste, nemmeno per domini nuovi (`arxiv.org`, `claude.com`). Spiegazione possibile: il primo gruppo di letture della sessione chiede conferma, i tentativi successivi no. [Inferenza]: non provata; basata su una sola run.
- Nota: `academy.claude.com` non è in `.claude/settings.json` (c'è solo `claude.com`).
- Gli URL `platform.claude.com/.../claude-prompting-best-practices` e `anthropic.com/engineering/...` (nel prompt) non hanno dato errori al primo tentativo, perché lanciati dopo.

## Distribuzione dei Tier (registro, calcolata con un comando)
- 35 righe (31 di ricerca, 4 di raggiungibilità per la notte 04): T1 35 · T2 0 · T3 0.
- Esiti: ok 29, ok parziale 2, bloccato dallo strumento 4.
- Metodo: fetch 35, snippet 0.
Comando: `python3 -I -c "import csv,collections; r=list(csv.DictReader(open('ricerche/registro_fonti_istruzioni_project.csv'))); print(len(r), collections.Counter(x['tier'] for x in r), collections.Counter(x['esito'] for x in r), collections.Counter(x['metodo'] for x in r))"`

## Domini per la notte successiva (tema 3, contesto), una lettura ciascuno
| Dominio | Esito di raggiungibilità |
|---|---|
| [platform.claude.com context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) | ok (context rot, compaction, context awareness; circa 20 KB) |
| [code.claude.com context-window](https://code.claude.com/docs/en/context-window) | ok (cosa si carica e cosa sopravvive alla compaction) |
| [platform.claude.com context-editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) | ok (circa 40 KB, beta) |
| [support.claude.com 11647753](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) | ok (chat lunghe, riassunto dei turni vecchi) |
| anthropic.com/engineering context engineering | ok (già letto in questa notte) |
Altre pagine trovate dalla ricerca, non lette: compaction (`platform.claude.com/docs/en/build-with-claude/compaction`), `compaction-threshold`, `compaction-on-demand`, `code.claude.com/docs/en/how-claude-code-works`, `code.claude.com/docs/en/model-config`.

## Modifiche proposte al prompt
1. Il prompt dice che `9519177` copre anche Drive, GitHub e «Sync now»: non è vero. Quelle voci stanno in `10166901` (Google Workspace) e `10167454` (GitHub): indicare gli URL giusti.
2. Per la prima lettura: dire all'agente di fare un solo primo tentativo di lettura per URL e, in caso di PROVENANCE_REQUIRED, riprovare una volta (è ciò che ha funzionato qui). Oppure lanciare le prime letture una alla volta.
3. Aggiungere `academy.claude.com` a `.claude/settings.json`.
4. I limiti di lunghezza dei Project classici non si trovano nelle pagine: se serve il numero, proporre una prova nell'interfaccia (incollare testo crescente nelle Istruzioni) invece di altre ricerche.
5. Per i preprint: convertire il PDF con `pdftotext` solo se si cita un numero; qui sono usati solo abstract, dichiarato nel README.
6. Lasciare ai Project la domanda «le Istruzioni di un Project di chat arrivano a una sessione Code o Cowork?»: nessuna pagina la chiude; solo una prova dell'utente può chiuderla.

## Costo
- Letture di pagina (WebFetch): 35 (di cui 4 bloccate al primo tentativo, 4 di raggiungibilità per il tema 3). Ricerche web: 8. Sottoagenti: 0. Durata: circa 15 minuti (23:01-23:16, Europe/Rome).
- Il consumo in dollari non è visibile all'agente: confrontare il saldo prima e dopo (saldo prima di questa run: 23 USD, dichiarato dall'utente il 26 ottobre).
