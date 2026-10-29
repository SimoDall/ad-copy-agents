# Memoria progetto — angle-generator

## Nicchia: digital estate-planning / family emergency organizer come USO PERSONALE (pubblico "Barb", Germania — "Notfallordner")
Progetto: `projects/family-handover-folder-barb-de/`. Run 2026-10-29, desiderio di massa lavorato: "Voglio che la mia famiglia trovi tutto senza cercare" (Desiderio #1). Mercato Solution Aware (~42%, vedi consapevolezza.md).

### Insight stabili
- Gli angoli di **Livello 3** più solidi per questa nicchia sono quelli che separano il "permesso legale" (Vorsorgevollmacht/procura, chi decide) dalla "mappa pratica" (dove si trova cosa) — è il vero gap della categoria in Germania: il pubblico è molto informato sulla parte legale e poco su quella pratica (coerente con consapevolezza.md).
- Gli angoli di **Livello 1** basati su auto-verifica immediata in famiglia ("chiedi a un familiare dove si trova X e guarda se sa rispondere") funzionano bene come apertura perché verificabili all'istante, senza bisogno di fiducia preliminare.
- Le fonti già raccolte da desire-researcher e awareness-researcher (studio UKE Hamburg sui documenti reperibili in ospedale, survey Forsa/Central e Bitkom, citazioni Reddit DE sul raccoglitore lasciato vuoto) sono bastate come "prova osservabile/autorità" per tutti gli angoli: non è stata necessaria WebSearch aggiuntiva in questo run.
- Con un desiderio singolo lavorato (non tutti e 5), 6 angoli (non 5) sono stati generati per coprire bene i 4 livelli; priorità di test consigliata: angolo "permesso legale ≠ mappa pratica" (L3) prima di tutto, poi l'angolo di auto-verifica immediata (L1), poi l'angolo sul danno invisibile/progressivo (L4, es. banche che rifiutano procure standard, 62% crede erroneamente nel potere automatico dei parenti).
- Attenzione a sovrapposizione concettuale: un angolo "il cervello evita i compiti tutto-o-niente" (L3, procrastinazione) rischia di sovrapporsi a un angolo L2 "il raccoglitore vuoto non è colpa tua" (anch'esso su procrastinazione) — tenerne uno come riserva/variante B piuttosto che testarli entrambi come principali.

### Pattern ambiente/strumenti
- Il subagent (eseguito come general-purpose con le istruzioni di angle-generator.md) non ha accesso a uno strumento di memoria proprio: questo file viene mantenuto dall'orchestratore sulla base del riepilogo restituito a fine run.
