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
