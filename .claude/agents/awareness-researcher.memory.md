# Memoria di progetto — awareness-researcher

Pattern ricorrenti e risultati per nicchia. Aggiornato ad ogni run.

## family-handover-folder-figli (digital estate-planning / family emergency organizer come REGALO) — USA — 15 ott 2026
- **Pubblico valutato:** "Figli" (persona Dana Whitfield, 44-58, genitori 72-88),
  acquirente-regalo, distinto da "Barb" (auto-acquirente).
- **Livello dominante: PROBLEM AWARE (~50%).** Distribuzione: Unaware 15% · Problem
  Aware 50% · Solution Aware 25% · Product Aware 8% · Most Aware 2%. Fiducia Medio-Alta
  sul dominante, Media sulle %.
- **Insight chiave:** il problema è intensamente sentito e cercato (query reattive
  notturne, rapporto Problema:Soluzione:Prodotto ≈ 6:2:1), ma il *formato-soluzione
  "organizer come regalo"* è a bassa salienza; le soluzioni note sono vissute come
  fai-da-te o death planner morboso → alto attrito. Blocco relazionale, non informativo.
- **Soluzioni fallite top:** (1) conversazione a voce, (2) spreadsheet fai-da-te,
  (3) death/"when I'm gone" planner morboso, (4) solo POA/testamento.
- **Competitor/segnali domanda:** Nokbox (~9-15k recensioni), "I'm Dead Now What"
  (~11,5k rating Amazon), Everplans (acq. Precoa), My Estate Kit (UK-only),
  Trustworthy, Etsy/Walmart binder. Caring.com 2025: solo 24% ha un testamento.
- **Vincolo ambiente:** Agent Reach non configurato; Reddit 403; WebFetch/curl
  bloccati → quantificazione triangolata da WebSearch + survey + volumi recensioni,
  NON da scraping grezzo di commenti. Per run futuri su questa nicchia, mettere in
  conto lo stesso limite e tararlo nel livello di fiducia.
- **Raccomandazione copy:** movimento Problem→Solution dentro l'annuncio; advertorial
  long-form; framing "regalo premuroso, NON death planner".

## family-handover-folder-barb-de (Notfallordner, uso personale) — GERMANIA — 29 ott 2026
- **Pubblico:** Barb, che compra per sé, 55-78 anni. Ricerca in tedesco, output in
  italiano.
- **Livello dominante: SOLUTION AWARE (~42%).** Distribuzione: Unaware 12 · Problem
  18 · Solution 42 · Product 20 · Most 8. Fiducia Alta sul livello dominante, Media
  sulle percentuali.
- **Insight chiave:** in Germania la categoria è già educata. "Notfallordner" è un
  termine noto, con modelli gratuiti di comuni, casse malattia, Warentest (oltre 1,2M
  copie) e BMJ, e il suo volume di ricerca è cresciuto del +260% in 12 mesi. Il
  nemico è l'alternativa GRATUITA più la procrastinazione ("leerer Ordner seit 8
  Monaten"), più la sfiducia verso chi lo vende (Strukkis/Tecis). La consapevolezza
  è asimmetrica: alta sul livello legale (VV, PV, testamento), bassa sul livello
  pratico (conti, contratti, accessi, chi chiamare). Il kit Leave It Sorted va
  localizzato: oggi ha contenuti UK (5-6-12, IHT, probate).
- **Soluzioni fallite top:** notaio, Vollmacht respinta dalla banca o Erbschein,
  USB/cloud, foglietto o moduli standard (UKE: solo il 23% dei documenti è reperibile
  in ospedale).
- **Ambiente:** Apify reddit-scraper FUNZIONA (usare get-dataset-items senza limite:
  il file viene salvato in tool-results e lo si analizza con python). WebFetch
  funziona su suggestqueries.google.com (autocomplete) e rankhero.com/keywords/<kw>
  (volumi mensili, ma molti slug danno errore). Restano bloccati Amazon, Etsy,
  YouTube, Trends, gutefrage e Thalia. Rapporto autocomplete P:S:Pr circa 1:5,3:1,1,
  contro circa 6:2:1 per il progetto Figli in USA.
