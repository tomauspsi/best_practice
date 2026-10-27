---
tema: memoria tra una chat e l'altra (claude.ai, Project, Claude Code, sessioni cloud, API)
per: Claude (chat, Cowork, Code) quando aiuta l'utente su questo tema
aggiornata_il: 2026-10-27
prove: D:\Workspace\best_practice\4_memoria\rapporto_memoria.md
rivalutare_se: "nuovo modello Claude (per esempio Opus 5.6); release notes che toccano la memoria; oppure 2026-12-18"
---

# Guida 4 · Memoria tra chat diverse

Per Claude. Usa questa guida quando l'utente chiede cosa Claude ricorda da una chat all'altra, dove salvare regole e fatti perché restino, o perché una sessione non sa una cosa detta altrove. Vale al 27 ottobre 2026: se una pagina ufficiale più recente dice altro, vince la pagina e lo dici.

## Quando usarla
- «Come faccio a fargli ricordare questa cosa?», «perché Code non sa ciò che ho detto in chat?», «dove metto le regole?».
- Quando l'utente vuole una memoria condivisa tra app, Cowork e Code.

## Cosa è vero oggi
- Le memorie sono separate e non si parlano: memoria dell'account e dei Project (app e Cowork cloud), ricerca nelle chat passate, `CLAUDE.md`/`AGENTS.md`, auto memory locale di Code, memory tool dell'API, memoria dei Projects di Code (beta).
- Ogni Project dell'app ha la sua memoria e usa anche quella delle chat fuori Project, mai quella di altri Project; «Use account memory» lo isola. La ricerca nelle chat passate non attraversa i Project.
- La memoria è un promemoria, non una regola: una regola salvata solo lì può non essere seguita (prova dell'utente del 25 ottobre).
- Claude non aggiorna da solo un documento esterno (per esempio Google Docs) usato come memoria: lo fa solo se glielo chiedi e ha un connettore che scrive.
- L'auto memory di Code sta sul PC; una sessione o un'attività nel cloud vede solo il repo clonato, non `C:\Users\<utente>\.claude\`, e nessuna prova dice che riceva la memoria della chat.
- Cancellare una chat non cancella le memorie che ne sono nate; i temi sensibili sono esclusi di default.

## Regole da applicare
1. Una casa per ogni informazione: regole sempre valide nelle Istruzioni (profilo per tutte le chat, Project per un lavoro, `CLAUDE.md` per Code); fatti e documenti nella knowledge del Project o nel repo.
2. Ciò che deve valere per tutti gli strumenti va in un file del repo; nell'app lo si carica nella knowledge del Project e lo si ricarica quando cambia.
3. Non promettere che Claude «si ricorderà»: se conta, va scritto in un posto che si rilegge da solo.
4. Per una sessione cloud o un'attività: tutto ciò che serve sta nel prompt o nel repo.
5. In Code tieni `CLAUDE.md` sotto le 200 righe e metti in cima all'indice della memoria ciò che conta: si caricano solo 200 righe o 25 KB.
6. Niente dati sensibili nella memoria dell'app; il testo preso da pagine esterne non va salvato in memoria senza rileggerlo (rischio di avvelenamento).
7. Per un blocco vero servono hook o permessi, non la memoria.

Schema «dove va cosa» da proporre:
| Cosa | Dove | Chi lo legge |
|---|---|---|
| Regole di un repo | `CLAUDE.md` del repo | Code sul PC e nel cloud, attività |
| Preferenze personali di Code | `C:\Users\<utente>\.claude\CLAUDE.md` | Code sul PC |
| Preferenze per tutte le chat | Istruzioni del profilo | Chat e Cowork |
| Regole di un lavoro | Istruzioni del Project | Chat di quel Project |
| Fatti e documenti di un lavoro | Knowledge del Project | Chat di quel Project |
| Contesto di un'attività | Prompt dell'attività e repo | L'attività |

## Come rispondere all'utente
Rispondi in italiano semplice, con un elenco numerato di cose da fare, una per riga, con il posto esatto (menu dell'app o percorso Windows completo). Di' chiaramente cosa non verrà ricordato.

Elenco tipo, da adattare al caso:
1. Decidi chi deve ricordare: tutte le chat, un solo Project o Claude Code.
2. Se è una regola, scrivila nelle Istruzioni di quel posto (profilo, Project o `CLAUDE.md`), una sola volta.
3. Se è un fatto o un documento, caricalo nella knowledge del Project con un nome chiaro.
4. Quando il documento cambia, ricaricalo nel Project: non si aggiorna da solo.
5. Per vedere o cancellare ciò che l'app ricorda: Settings > Your Claude > Manage.
6. Non contare sulla memoria per le cose obbligatorie: se Claude sbaglia, sposta la regola nelle Istruzioni.

## Cosa non sappiamo
- Se un'attività creata da un Project di Code legga la memoria del Project (dedotto, non scritto).
- Se la memoria della chat arrivi mai alle sessioni cloud di Code (nessuna prova; trattala come assente).

## Prove
Regole numerate, tabella delle sessioni cloud, rischi e studi sull'avvelenamento: `D:\Workspace\best_practice\4_memoria\rapporto_memoria.md`.
