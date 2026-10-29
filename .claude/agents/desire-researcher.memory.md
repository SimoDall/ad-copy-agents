# Memoria progetto — desire-researcher

## Nicchia: digital estate-planning / family emergency organizer come REGALO (pubblico "Figli"/Dana, USA)
Progetto: `projects/family-handover-folder-figli/` (Leave It Sorted / The Thoughtful Gift Bundle).

### 5 desideri di massa stabili — ora con CONTEGGI reali (run 2026-10-16, dataset Reddit R4foHL2efKAGfemUG, 526 item)
Base conteggio: 79 voci del profilo Dana (figlia che si prepara, genitore vivo) mappate a un desiderio.
1. "Voglio sapere dove trovare tutto se succede qualcosa." — **33 voci, 42% — DOMINANTE** (doppio del secondo; i 2 post più votati del dataset, 978 e 583, sono qui)
2. "Voglio sollevare il discorso senza offenderli o litigare." — **16 voci, 20%** (blocco RELAZIONALE, 2° forte; colpisce i bonus Dear Mom/Dad Letter + Conversation Card)
3. "Voglio vivere il lutto senza restare intrappolata nella burocrazia." — **10 voci, 13%** (ma evidenza soprattutto POST-LUTTO; come angolo primario rischia profilo sbagliato)
4. "Voglio smettere di avere quell'ansia di sottofondo." — **10 voci, 13% MA gonfiato**: solo ~3 ansia pura, ~7 sono in realtà la paura economica di mantenere i genitori (candidato ND-A). Desiderio più debole dei 5 sui dati reali.
5. "Voglio essere pronta senza prendere il controllo dei miei genitori." — **10 voci, 13%** (permesso psicologico; "it's not my money", rispetto autonomia)

### Candidati nuovi emersi (tutti SOTTO soglia ~15 voci → NON promossi)
- ND-A: "non voglio essere prosciugata mantenendo genitori impreparati" — ~10 voci, voti altissimi (121/128/165), ma DIFENSIVO verso il genitore → in tensione con angolo "regalo d'amore". Ruba peso a D4.
- ND-B: "la POA che ho preparato deve funzionare davvero (banche non la onorano)" — ~4 voci → driver di D1/D5.
- ND-C: "proteggere il genitore da frodi/abuso finanziario (POA predatorio)" — ~4-6 voci → driver D1/D5.
- ND-D: "evitare che un fratello nasconda/litighi l'eredità" — ~4-6 voci → driver D1/D3 ("three siblings, one answer").
- ND-E: "creare un trust per risparmiare probate ai figli" — ~2 voci, troppo poche (più Barb che Dana).

### Insight stabili
- Conflitto fratelli = driver dentro #1/#3, NON sesto desiderio (confermato dai conteggi).
- Linguaggio verbatim da riusare: "one place", "peace of mind", "I just wanted to be ready", "without taking over", "make this easy on your kids", "it's not my money". EVITARE: death/funeral/end of life/when I'm gone.
- Distinguere SEMPRE profilo Dana (figlia in preparazione, genitore vivo) da post-lutto: nel dataset Dana ~20% (107/526), post-lutto ~16% (85), fuori tema ~64% (334).

### Pattern ambiente/strumenti
- **Reddit via Apify `harshmaur/reddit-scraper` HA FUNZIONATO in questo run.** Procedura a 2 passi (A: searchSort "relevance" NON "top", maxPostsCount 10/keyword, solo post; B: commenti dei post scelti, maxCommentsPerPost 10) con tetto ~$1. Risultato: dataset 526 item, 49 post + ~477 commenti. Passo B interrotto dal tetto di spesa → commenti = CAMPIONE per thread (non ordinati per voto dallo scraper, non i top assoluti).
- Keyword su password/bank/privacy pescano MOLTO rumore inverso (genitori che controllano conti di figli adolescenti): ~64% del dataset è fuori tema. Filtrarlo sempre.
- In run passati lo stesso server MCP era risultato "connesso ma senza tool esposti" e senza APIFY_TOKEN: fare un probe rapido dei tool + budget prima di promettere dati.
- Le % dei DESIDERI ora sono conteggi reali; le % dei DRIVER dentro ogni desiderio restano una ripartizione ragionata dei conteggi di quel desiderio.

## Nicchia: digital estate-planning / family emergency organizer come USO PERSONALE (pubblico "Barb", Germania — "Notfallordner")
Progetto: `projects/family-handover-folder-barb-de/` (Leave It Sorted). Run 2026-10-29, dataset Reddit tedesco ~135-140 voci totali (molto sotto il target 700-1000+; Reddit DE su questo tema è scarso e skewed 25-50 anni, non 55-78).

### 5 desideri di massa (stime, NON conteggi solidi come nel run USA/Figli — campione piccolo)
1. "Voglio che la mia famiglia trovi tutto senza cercare" — ~21% Reddit. Headline di categoria già usata da concorrenti e comuni/enti pubblici tedeschi.
2. "Voglio che le mie volontà vengano rispettate" — ~36% grezzo ma GONFIATO da 2 keyword (Patientenverfügung/Testament). Priorità #1 negli over-55 (studio Commerzbank).
3. "Voglio risparmiare ai miei figli la burocrazia dopo di me" — ~20%. Citazione forte sul padre che preparava anche le lettere di disdetta contratti. Rischio concreto citato: Erbschein 1.800-3.600€.
4. "Voglio togliermi finalmente questo pensiero" — ~9% ma post/commento più votati del dataset (308/314 voti): raccoglitore lasciato vuoto per mesi, colpa/sollievo.
5. "Voglio che i miei cari possano agire subito per me" — ~14%, in parte bisogno NON ancora consapevole (62% over-60 crede erroneamente che i parenti possano decidere automaticamente per loro).

### Insight stabili sul mercato tedesco
- Il Notfallordner è già un concetto mainstream, spesso gratis (comuni, Stiftung Warentest oltre 1M copie distribuite) → awareness/scetticismo diverso da USA/UK.
- Diffidenza diffusa: percepito come esca di marketing da consulenti finanziari; cercano esplicitamente qualcosa "das nicht nach Abzocke aussieht" (che non sembri una fregatura).
- ~79% dei post Reddit trovati erano fuori tema (vs ~64% nel run USA/Figli) — il rumore è ancora più alto in tedesco.

### Pattern ambiente/strumenti (run Germania)
- Amazon.de bloccato; Facebook, YouTube e gutefrage.net NON raggiungibili in questo run. Su Etsy.de nessun Notfallordner in tedesco con recensioni.
- Attenzione al budget Apify: in questo run i tetti di spesa impostati sui 2 passi hanno sommato $1,75 (sopra il budget $1 previsto dal prompt); il tool non espone la spesa reale in $, solo stime indirette. Verificare sempre che `callOptions.maxTotalChargeUsd` dei due passi sommi ≤ budget PRIMA di lanciare, non dopo.
- Se un run sembra incompleto, ricontrollare lo stato invece di rilanciare subito una seconda raccolta: in questo run una "seconda raccolta commenti" lanciata per sospetto di dataset parziale si è rivelata in gran parte un doppione (la prima si era completata da sola nel frattempo).
