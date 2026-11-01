---
tema: memoria tra una chat e l'altra nell'app Claude (chat e Cowork unificati, Project)
per: Claude nell'app (chat e Cowork)
aggiornata_il: 2026-11-01
prove: D:\Workspace\best_practice\4_memoria\rapporto_memoria.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes o changelog di Claude Desktop che toccano memoria, Project, cartelle o permessi; oppure 2026-12-18"
---

# Guida 4 · Memoria tra chat diverse

Per Claude. Usa questa guida quando l'utente chiede cosa ricordi da una chat all'altra, soprattutto dentro un Project, e dove scrivere ciò che deve restare. Vale al 1 novembre 2026 per la sola app Claude: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici. Claude Code ha una memoria sua, separata da questa: se l'utente ne chiede, dillo in una riga.

## Quando usarla
- «Come faccio a fargli ricordare questa cosa?», «perché la chat nuova non sa ciò che ho detto ieri?», «dove metto le regole del Project?».
- Quando l'utente vuole che Claude tenga da solo un documento di appunti, o che un'attività programmata «sappia» qualcosa.
- Chat lunghe e sintesi automatica non stanno qui: vedi `D:\Workspace\best_practice\3_contesto\guida_contesto.md`.

## Cosa è vero oggi
- **Memoria dell'account:** nasce dalle chat fuori Project. Claude la scrive durante la chat, per argomenti; se l'utente dice «ricorda che…» la salva subito; le modifiche valgono dalla conversazione successiva. Con la memoria «legacy» (ancora su alcuni account) la sintesi si aggiorna ogni 24 ore.
- **Memoria di Project:** ogni Project ha la sua. Dentro il Project Claude usa quella del Project più quella dell'account, mai quella di altri Project; le memorie nuove vanno nel Project. La memoria del Project può comparire anche nelle chat fuori Project; spegnere «Use account memory» (sezione Memory della pagina del Project) la tiene separata.
- **Attività di Cowork solo locali:** la loro memoria resta con quelle attività; le sessioni di Cowork eseguite sul computer non usano la memoria delle chat. Nel cloud la memoria è condivisa tra chat e attività.
- **Ricerca nelle chat passate:** solo piani a pagamento. Fuori Project cerca tra le chat fuori Project; dentro un Project solo tra le chat di quel Project. Non cerca nelle vecchie attività di Cowork. Si vede come una chiamata a strumento nella chat.
- **Knowledge del Project:** Claude la usa in ogni chat del Project; il contesto delle altre chat non passa, salvo ciò che si mette nella knowledge. Un repo GitHub si aggiorna solo con «Sync now»; un documento Google aggiunto da Drive (solo Project privati) resta sincronizzato con Drive.
- **Istruzioni:** quelle del profilo («Instructions for Claude») valgono in ogni conversazione, comprese le attività programmate; quelle del Project in tutte le chat e le attività del Project.
- **Precedenza:** nessuna pagina ufficiale dice cosa vince tra memoria, Istruzioni del profilo, Istruzioni del Project, stili e knowledge.
- **Una regola salvata solo in memoria può non essere seguita:** prova dell'utente del 25 ottobre (la stessa regola nelle Istruzioni è stata seguita). Una sola prova.
- **Claude può scrivere fuori dalla memoria:** con i connettori Google crea e modifica documenti, se l'utente nomina Google; nelle cartelle collegate legge e scrive file, solo con Claude Desktop aperto. Nessuna pagina dice che lo faccia da solo in ogni chat per un'istruzione del Project.
- **Cartella locale nel Project:** è montata e accessibile in ogni conversazione del Project; nessuna pagina dice che Claude ne rilegga i file da solo a ogni conversazione.
- **Attività programmate in un Project:** girano con il contesto del Project (Academy); nessuna pagina dice in modo esplicito che leggano o scrivano la memoria del Project.
- **Privacy:** cancellare una chat non cancella le memorie nate da lì; i temi sensibili sono esclusi finché non li attivi; «Reset memory» cancella tutto, anche le memorie dei Project, e non si annulla. Le chat in incognito non vanno in memoria né nella ricerca.

## Regole da applicare
1. Una casa per ogni informazione: regola che vale sempre → Istruzioni (profilo o Project); fatto o documento → knowledge del Project; preferenza minore → memoria.
2. Non promettere che Claude «si ricorderà»: ciò che conta va scritto dove si rilegge da solo (Istruzioni o knowledge).
3. Se un Project deve restare isolato, spegni «Use account memory»; per una chat sola, togli «Memory» dal menu «+» prima del primo messaggio.
4. Per riprendere un lavoro in un Project chiedi in modo esplicito di cercare nelle chat passate («cosa avevamo deciso su…?»); la ricerca non è garantita in ogni chat.
5. Un documento-memoria scritto da Claude esiste solo se l'utente lo chiede in quella chat e c'è un connettore o una cartella che scrive; dopo ogni scrittura, va ricaricato o sincronizzato se sta nella knowledge.
6. Per un'attività programmata, ciò che serve va nel prompt dell'attività o nelle Istruzioni del Project, non nella memoria.
7. Non far salvare in memoria testo preso da pagine esterne senza rileggerlo: una sola scrittura avvelenata pesa a lungo.
8. Niente dati sensibili in memoria; per vedere e correggere: Impostazioni > Memoria (nell'app per Windows dell'utente; le pagine d'aiuto indicano anche Settings > Your Claude, secondo il layout).

Schema «dove va cosa» da proporre:
| Cosa | Dove nell'app | Chi lo rilegge | Si aggiorna da solo? |
|---|---|---|---|
| Preferenze e regole per tutte le chat | Istruzioni del profilo (Impostazioni > Account, voce «Instructions for Claude»; nel layout nuovo Settings > Your Claude) | Ogni conversazione e attività | No: le scrivi tu |
| Regole di un lavoro | Istruzioni del Project | Ogni chat e attività del Project | No: le scrivi tu |
| Fatti e documenti di riferimento | Knowledge del Project | Ogni chat del Project | GitHub con «Sync now»; documento Google sì |
| Dettagli minori, preferenze di tono | Memoria (account o Project) | Le chat successive, se pertinente | Sì, la scrive Claude |
| Diario o appunti di lavoro | Documento Google scritto tramite connettore | Claude, se il documento è nella knowledge o glielo indichi | Solo quando lo chiedi |
| File di lavoro e appunti locali | Cartella locale del Project | Claude, solo con Claude Desktop aperto e quando serve | Solo quando lo chiedi |

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato, un passo per riga e i clic esatti. Di' chiaramente cosa non verrà ricordato e cosa resta incerto.

Elenco tipo, da adattare al caso:
1. Decidi chi deve saperlo: tutte le chat (profilo), un solo Project (Istruzioni o knowledge), o basta un promemoria (memoria).
2. Regola per tutte le chat: Impostazioni > Account > «Instructions for Claude» (se nel menu c'è Your Claude, è lì), scrivi la regola, salva.
3. Regola per un Project: apri il Project > «Set project instructions» > scrivi > «Save instructions».
4. Fatto o documento: apri il Project > «+» nell'area della knowledge > carica il file (o «Drive» per un documento Google).
5. Se il documento sta su GitHub, prima di lavorarci premi «Sync now» nel Project.
6. Per isolare il Project: pagina del Project > sezione Memory > spegni «Use account memory».
7. Per vedere, correggere o cancellare ciò che ricordo: Impostazioni > Memoria, sezioni «Tu» e «Argomenti», con la casella in fondo per dire cosa cambiare; oppure scrivimi in chat «ricorda che…», «dimentica che…». Per una copia: Impostazioni > Memoria > «Esporta» (archivio .zip di file Markdown).
8. Per riprendere un lavoro: in una chat nuova del Project scrivi «cerca nelle chat passate cosa avevamo deciso su…»; serve «Ricerca e consultazione delle chat» acceso in Impostazioni > Memoria.
9. Se Claude non segue una regola che sta solo in memoria, spostala nelle Istruzioni del Project.

## Cosa non sappiamo
- Dopo quanti minuti una chat nuova vede una memoria appena scritta: la pagina dice solo «dalla conversazione successiva».
- Se le attività programmate di un Project leggano o scrivano la memoria del Project.
- Se un'istruzione del Project («aggiorna il documento X a fine chat») basti perché Claude lo faccia in ogni chat senza richiesta: nessuna pagina, nessuna prova.
- Se Claude legga da solo i file della cartella locale a ogni conversazione.
- Cosa vince quando memoria e Istruzioni si contraddicono.
- Se il menu Impostazioni > Memoria resti uguale su tutti gli account: è visto in una sola schermata dell'utente (1 novembre); le pagine d'aiuto descrivono anche Settings > Your Claude e il changelog Settings > General.
- Se le chat condivise portino con sé qualcosa della memoria (la pagina non ne parla).

## Prove
Regole numerate con fonti, conflitti e verifiche mancanti: `D:\Workspace\best_practice\4_memoria\rapporto_memoria.md`, sezioni «Regole operative», «Tabella conflitti» e «Cosa non è stato verificato».
