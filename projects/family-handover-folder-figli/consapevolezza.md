# Ricerca sul Livello di Consapevolezza del Mercato — Pubblico "Figli" (Dana)

> Output di `awareness-researcher`. Framework: Livelli di Consapevolezza di Eugene
> Schwartz (Breakthrough Advertising).
> Nicchia: digital estate-planning / family emergency organizer — kit di passaggio
> di consegne familiare posizionato come **regalo**.
> Prodotto: **The Thoughtful Gift Bundle** (Leave It Sorted / leaveitsorted.com), €47.
> Paese target: **USA** (mercato anglofono primario; scalabile su UK/CA/AU/NZ).
> Pubblico valutato: **Dana Whitfield** — figlio/a adulto/a (44-58) di genitore
> anziano (72-88), che compra/considera il kit **come regalo/passaggio di consegne**,
> NON come death/funeral planner.
> Data analisi: 8-15 ottobre 2026. Finestra fonti analizzate: 2013-2026 (concentrate
> 2023-2026).

---

## NOTA METODOLOGICA CRITICA (limiti dell'ambiente di ricerca)

Va dichiarato onestamente, perché incide sul livello di fiducia delle percentuali.

In questa sessione l'accesso diretto alle piattaforme per lo scraping di
commenti/recensioni grezzi **è risultato bloccato dalla policy di egress**:
- **Agent Reach / CLI Reddit: NON configurato** in questa sessione.
- **Reddit**: bloccato a livello di proxy (403 CONNECT su `www.reddit.com` e sulle
  API JSON dei subreddit) → impossibile contare commenti thread-per-thread.
- **WebFetch**: errori di risoluzione DNS (`getaddrinfo ENOTFOUND`) su quasi tutti
  gli host esterni (Trustpilot, Nokbox, Kimola, ecc.).
- **curl via Bash**: `403 CONNECT tunnel failed` su tutti gli host web generici
  (anche Wikipedia); solo alcune CLI pre-autorizzate e i registry di pacchetti
  passano il proxy.

**Conseguenza:** l'unico strumento di ricerca affidabile è stato **WebSearch** (~22
query, ognuna con 9 link + sintesi multi-fonte), che ha permesso di toccare 100+
fonti distinte e di estrarre contenuti/citazioni e statistiche pubblicate, ma **non**
di scaricare i conteggi grezzi commento-per-commento richiesti dal protocollo
(es. "247 commenti Reddit, di cui 12%..."). Le percentuali di distribuzione della
consapevolezza qui sotto sono quindi **triangolazioni stimate** da: (1) evidenza
qualitativa emersa dalle ricerche, (2) survey e report pubblicati, (3) volumi di
recensioni dei competitor come proxy di domanda. **Non** sono conteggi diretti di
singoli commenti. Dove indico "X% di Y commenti" per Reddit/YouTube/recensioni, è una
**stima ragionata sui pattern osservati nelle sintesi di ricerca**, non un dato
scrapato. Il livello di fiducia è tarato di conseguenza (vedi sezioni C ed F).

Questo è coerente con l'istruzione del protocollo: "Se non riesci a raggiungere i
volumi richiesti per una fonte, dichiaralo onestamente invece di gonfiare le cifre."

---

## A. Riepilogo della Ricerca

- **Fonti Totali Toccate:** ~110 fonti distinte (via ~22 query WebSearch, standard +
  extended), di cui ~70 rilevanti e citate/usate nella triangolazione.
- **Suddivisione per Categoria:**
  - **Social Media e Forum:** ~15 fonti (sintesi di thread Reddit non accessibili in
    diretta, forum Caregiver.com, ProductReview.com.au, articoli che riportano
    contenuti TikTok/Facebook, Quora). Punti dati qualitativi estratti: ~60 citazioni/
    pattern. **Scraping diretto di commenti: NON disponibile (vedi nota).**
  - **Ricerca e SEO:** ~8 fonti/strumenti (RankHero/Etsy keyword data, Backlinko,
    SearchVolume.io, discussioni su Keyword Planner/Ahrefs/Semrush; nessun accesso
    live a un tool keyword a pagamento — Google nasconde i volumi esatti in Keyword
    Planner senza spesa attiva).
  - **Intelligence di Mercato:** ~9 report (Verified Market Research, The Business
    Research Company, Ken Research, IBISWorld, Business Research Insights, StartUs
    Insights, Caring.com, AARP/NAC, Pew/Care.com).
  - **Analisi Concorrenza / E-commerce:** ~20 fonti (Nokbox, Everplans, Trustworthy,
    My Estate Kit, "I'm Dead Now What", Walmart binders, Etsy planners, The Estate
    Organiser, Elayne, Aura Life, Legacy Compass). Volumi recensioni aggregati come
    proxy: **Nokbox ~9.400-15.400 recensioni; "I'm Dead Now What" ~11.529 rating
    Amazon; Walmart binder vari**. Testo recensione-per-recensione NON scrapabile.
  - **Contenuti e Influencer:** ~12 fonti (Trustworthy blog, Overture, NPR, Fidelity,
    US Bank, Capital One, Neptune Society, Next Avenue, podcast Black Parents Aging,
    video Bryan Fagan, Dave Ramsey legacy drawer, AHA/Mother.ly).
- **Periodo di Tempo Analizzato:** contenuti 2013-2026, con il grosso 2023-2026.

---

## B. Mercato Totale Indirizzabile (TAM)

Non esiste un report che isoli esattamente "consumer family-emergency-organizer
digitale venduto come regalo negli USA". Serve triangolare mercati adiacenti + un
modello bottom-up sul segmento Dana.

**Mercati adiacenti (fonti multiple, valute in USD):**

| Mercato (definizione) | Dimensione | CAGR | Fonte |
|---|---|---|---|
| Estate planning **software** (globale) | $1,62B (2025) → $3,83B (2033) | 11,4% | Verified Market Research |
| Digital legacy (globale, def. ampia) | $21,86B (2025) → $25,63B (2026) → $47,88B (2030) | 17,2% | The Business Research Company |
| Digital legacy (globale, def. alt.) | $25B (2025) → $54B (2031) | 13,8% | Ken Research |
| Estate planning **services** (globale) | ~$114B (2026) | 4,5% | Business Research Insights |
| US trusts & estates (industria, escl. drafting) | ~$284,5B (2026) | 2,8% | IBISWorld |
| Death-tech (funding privato globale) | 948 aziende, ~$837M raccolti | — | StartUs Insights |

Nota: il Nord America pesa ~42% del mercato estate-planning-software (VMR) ed è la
regione a maggior quota del digital legacy (CB Insights).

**Modello bottom-up sul segmento Dana (USA):**
- Adulti USA ~258M; **~1 su 4 è "sandwich generation"** (Pew, citato in report
  Care.com 2026) ≈ 60M+.
- AARP/NAC 2025: **~17M** fanno contemporaneamente da caregiver a un figlio e a un
  adulto con condizione medica complessa; caregiver totali stimati 50-63M a seconda
  del metodo di conteggio.
- Bacino realistico di "figli adulti 44-58 con genitore anziano che potrebbe
  plausibilmente comprare un organizer come regalo" ≈ **30-40M persone**.
- A €47/$~50 one-time: TAM teorico "1 acquisto a testa" ≈ **$1,5B-$2,0B**; questo è
  in pratica più un SAM, perché l'adozione attuale del *formato-regalo* è bassa.

**Stima TAM consolidata per questo prodotto/segmento:**
> **Intervallo $0,7B - $2,0B** come segmento consumer US di organizer/vault di
> passaggio di consegne (sottoinsieme del mercato digital-legacy/estate-software di
> $1,6B-$25B+ globale), con **CAGR atteso ~11-17%** trainato da invecchiamento
> popolazione, "death-tech", e normalizzazione culturale (Swedish death cleaning,
> AARP). Fonti: VMR, The Business Research Company, Ken Research, IBISWorld, StartUs,
> + bottom-up Pew/AARP/Care.com. (≥5 fonti indipendenti.)

Segnale di domanda reale (non sondaggi ma vendite): **Nokbox ~9.400-15.400
recensioni**, **"I'm Dead Now What" ~11.529 rating Amazon**, acquisizione di
Everplans da parte di Precoa (ott 2024), round di funding Aura Life / Legacy Compass
2025-2026 → la categoria è in crescita e monetizza.

---

## C. Suddivisione per Stadio di Consapevolezza (QUANTIFICATA — STIMA TRIANGOLATA)

**Dichiarazione di Metodologia:** "Basato sulla triangolazione di ~70 fonti rilevanti
(su ~110 toccate) e di diverse centinaia di punti dati qualitativi estratti dalle
sintesi di ricerca, incrociati con survey pubblicate (Caring.com, AARP/NAC,
Pew/Care.com) e con i volumi di recensioni dei competitor come proxy di domanda, la
distribuzione della consapevolezza del pubblico **Dana (figlio-acquirente-regalo)**
negli USA è stimata come segue. Le percentuali sono stime ragionate, non conteggi
grezzi di commenti (vedi Nota Metodologica)."

**TABELLA DI DISTRIBUZIONE DELLA CONSAPEVOLEZZA (persona: Dana, prodotto come regalo)**

| Stage | % of Market | Confidence | Evidence Base |
| --- | --- | --- | --- |
| Unaware | **15%** | Med | Chi non ha ancora avuto un trigger, assume che "ci pensi il coniuge/altro fratello", o crede "i nostri affari non sono complicati". Attivazione improvvisa (caduta/diagnosi) li sposta a Problem Aware. |
| **Problem Aware** | **50%** | **High** | **DOMINANTE.** Ecosistema di contenuti e query reattive enorme ("what to do when a parent dies", "how to find parent's bank accounts", "financial scavenger hunt"); sandwich gen 1/4 adulti; 80% si dichiara sopraffatto. Dana sa *cosa* le servirebbe — il blocco è relazionale, non informativo. |
| Solution Aware | **25%** | Med | Sa che esistono organizer/binder/"legacy drawer" come categoria (Nokbox, Everplans, Etsy, Dave Ramsey) ma li vede come death/estate planning o fai-da-te (spreadsheet), non come *regalo pronto*. |
| Product Aware | **8%** | Med | Conosce brand specifici (Nokbox, Everplans, My Estate Kit, "I'm Dead Now What") — spesso perché il *genitore* li ha comprati o per ricerca post-crisi, non come acquisto-regalo del figlio. |
| Most Aware | **2%** | Low | Pronti a comprare un prodotto-regalo specifico ora. Minimo: il framing "regalo, non death planner" è nuovo e la landing Dana non è ancora pubblicata; "nessun player tratta il momento del regalo". |

---

### UNAWARE — 15% del Mercato
- **Validazione Incrociata delle Fonti:**
  - Reddit/forum (stima): ~10-15% dei contributi riflette "non ci avevo pensato" o
    "tanto non serve, non è complicato" fino a un evento scatenante.
  - Survey: Caring.com 2025 — solo **24%** degli americani ha un testamento (in calo
    da 33% nel 2022), **>50% non ha nulla**; 40% dice "non ho abbastanza beni per
    giustificare la pianificazione" → segnale di non-percezione del problema a monte.
  - Dati di ricerca: il picco di query è **reattivo/post-evento**, non preventivo →
    molti arrivano al problema solo quando scoppia.
- **Linguaggio Rappresentativo:** "Our affairs aren't that complicated." / "I figured
  my brother/mom has it handled." / "We're not old enough to worry about that yet." /
  "I'll deal with it when I have to."
- **Canali Principali:** nessuno specifico — è assenza di ricerca. Intercettabili solo
  con contenuti di interruzione (advertorial, ads su community sandwich gen).

### PROBLEM AWARE — 50% del Mercato (DOMINANTE)
- **Validazione Incrociata delle Fonti:**
  - Reddit/forum (stima): ~45-55% dei contributi in r/AgingParents / caregiving
    esprime il problema ("non saprei dove sono i conti/le password") senza citare un
    prodotto come soluzione.
  - YouTube/contenuti: il grosso dei video/articoli è "how to talk to parents about
    finances", "29 documents to gather", "get affairs in order" = educazione sul
    problema, non comparazione prodotti.
  - Recensioni (proxy): molte recensioni/aneddoti partono da "una mia amica ha avuto
    un incubo burocratico quando è morto il genitore" → problema vissuto, non prodotto.
  - Dati di ricerca: dominano le query-problema reattive ("what to do when a parent
    dies", "how to find a deceased parent's bank accounts", "parents won't talk about
    finances") → chiaro skew Problem Aware.
  - Survey: sandwich gen = 1 su 4 adulti (Pew); Haven Life — 80% sopraffatto (84%
    donne); AARP — 48% caregiving ad alta intensità.
- **Linguaggio Rappresentativo (gamma):**
  1. "If something happened tomorrow, I wouldn't know where to even start looking."
  2. "I have no idea where my mom's accounts or passwords are."
  3. "If you don't have the passwords, the bank won't tell you anything."
  4. "I'm scared of the 2am phone call and not knowing what to do."
  5. "My parents won't talk about any of this."
  6. "I don't want to feel like I'm asking because I think they're dying."
  7. "A friend's dad died and she had no idea where anything was — it took months."
  8. "I know I should get this sorted, I just don't know how to bring it up."
  9. "I'm the organized one, so it'll fall on me — and I'm not ready."
  10. "Everything's in my dad's head. That terrifies me."
  11. "I don't want to be googling 'what to do when a parent dies' at 2am."
  12. "How do I even ask without it turning into a fight?"
  13. "We keep saying we'll do it 'someday'."
  14. "I'm already drowning between my kids and my parents."
  15. "I just want to be ready, not take over."
- **Canali Principali:** r/AgingParents (~58k), r/CaregiverSupport, gruppi Facebook
  "sandwich generation"/caregiver, TikTok caregiving ("default daughter"/"only
  daughter"), ricerca Google notturna reattiva, articoli NPR/Fidelity/US Bank/AARP.

### SOLUTION AWARE — 25% del Mercato
- **Validazione Incrociata delle Fonti:**
  - Reddit/forum (stima): ~20-25% menziona una *categoria* di soluzione (binder,
    "legacy drawer", organizer, spreadsheet, password manager) ma non un brand come
    regalo.
  - E-commerce: esiste una categoria matura e vendibile (Walmart "emergency binder",
    Etsy "end of life planner", Dave Ramsey legacy drawer) → la soluzione-categoria è
    nota a una fetta reale.
  - **Segnale negativo chiave:** cercando "best gift for elderly parents" emergono
    medical alert, gadget, memory book — **NON** organizer/emergency kit. Il
    *formato-regalo* dell'organizer è a bassa salienza → molti Solution Aware pensano
    "fai-da-te" o "death planner", non "regalo pronto".
  - Dati di ricerca: query-soluzione ("estate organizer", "when I'm gone binder",
    "legacy drawer", "emergency binder") esistono ma a volume nettamente inferiore
    alle query-problema.
- **Linguaggio Rappresentativo:**
  1. "Couldn't I just make a spreadsheet myself?"
  2. "We started a notebook but never kept it up."
  3. "Is there like a binder or template for this?"
  4. "Dave Ramsey talks about a 'legacy drawer' — is that enough?"
  5. "Should they just use a password manager?"
  6. "I found some 'when I'm gone' planners but they feel so morbid."
  7. "There are templates on Etsy, are they any good?"
  8. "We put the will in the safe deposit box — isn't that covered?"
  9. "I keep meaning to build one of those emergency binders."
  10. "I need something that isn't a whole estate-planning ordeal."
- **Canali Principali:** Etsy/Walmart/Amazon ricerca categoria, blog (Trustworthy,
  Overture, Dave Ramsey), Pinterest "emergency binder", YouTube "how to make a legacy
  binder".

### PRODUCT AWARE — 8% del Mercato
- **Validazione Incrociata delle Fonti:**
  - E-commerce: brand con traction reale — **Nokbox (~9.400-15.400 recensioni)**,
    **"I'm Dead Now What" (~11.529 rating Amazon, 4,6★)**, Everplans, Trustworthy,
    My Estate Kit. Ma le recensioni "regalo" osservate riguardano spesso l'acquisto
    *per sé* o *dal genitore per i figli*, o acquisti multipli come gadget-regalo
    ("bought several as Christmas gifts").
  - Reddit/forum (stima): ~5-10% nomina un brand specifico.
  - Nokbox stesso promuove il "gift for parents/grandparents" → il mercato branded sul
    lato regalo esiste ma è giovane.
- **Linguaggio Rappresentativo:**
  1. "Has anyone tried the Nokbox? Is it worth it?"
  2. "I'm looking at Everplans vs Trustworthy."
  3. "I bought 'I'm Dead Now What' for my siblings."
  4. "My Estate Kit is UK-only though, right?"
  5. "Is the Nokbox overkill or actually useful for my parents?"
- **Canali Principali:** pagine prodotto/recensioni (Loox, Amazon, Trustpilot), Reddit
  thread "X vs Y", Wirecutter/recensioni comparative.

### MOST AWARE — 2% del Mercato
- **Validazione Incrociata delle Fonti:** segmento minimo. Il framing specifico
  "regalo premuroso, non death planner" (The Thoughtful Gift Bundle) è nuovo e la
  landing Dana non è pubblicata. Nessun competitor tratta esplicitamente il momento
  del regalo come leva → quasi nessuno è "pronto a comprare questo prodotto, ora".
- **Linguaggio Rappresentativo:** "This is exactly what I was looking for to give my
  mom — not a death planner, just a way to be ready." / "Adding to cart."
- **Canali Principali:** retargeting, lista clienti esistente Leave It Sorted, chi ha
  già comprato per sé (Barb) e considera di regalarlo ai genitori.

---

## D. Analisi dei Dati di Ricerca

**Vincolo:** nessun accesso live a un keyword tool a pagamento; Google Keyword Planner
nasconde i volumi esatti senza spesa attiva. Le cifre sotto sono **stime direzionali**
dai dati surfacati (RankHero/Etsy keyword, pattern autocomplete/PAA emersi nelle
query) + ordinamento relativo osservato. Vanno verificate con Ahrefs/Semrush prima di
tarare il budget.

**Parole Chiave Relative al Problema (reattive/preventive) — volume ALTO:**
`what to do when a parent dies` · `how to find a deceased parent's bank accounts` ·
`how to find my parents' bank accounts` · `parents won't talk about finances` ·
`how to talk to elderly parents about money` · `financial scavenger hunt` ·
`what documents do I need when a parent dies` · `how to get your affairs in order` ·
`help aging parents get organized` · `power of attorney aging parent` · `29 documents
aging parents` · `where is the will` · `my parent died and I don't know their accounts`
· `elderly parent finances overwhelmed` · `sandwich generation caregiver` ·
`what to do after a parent dies checklist` · `locate deceased parent assets` ·
`dad won't do estate planning` · `getting parents paperwork in order` · `aging parent
emergency binder`.
- Ricerche mensili combinate (stima direzionale): **molto alto** (centinaia di
  migliaia/mese aggregate negli USA; query "what to do when a parent dies" e famiglia
  "find deceased parent accounts" sono testate di categoria).

**Parole Chiave Relative alla Soluzione (categoria) — volume MEDIO:**
`estate organizer` · `when I'm gone binder` · `legacy drawer` · `emergency binder for
aging parents` · `end of life planner` (proxy "life planner" ~8.100/mese su Etsy) ·
`in case of emergency binder` · `legacy binder` · `executor binder` · `estate planning
binder template` · `death folder` · `next of kin organizer` · `family emergency
organizer` · `document organizer for parents` · `what if binder` · `caregiver binder
aging parent` · `important documents organizer` · `digital estate organizer` ·
`password vault for family` · `final wishes planner` · `after I'm gone organizer`.
- Ricerche mensili combinate (stima): **medio** (nettamente inferiore alle
  query-problema; "life planner" ~8.100/mese come singolo proxy più alto).

**Parole Chiave Relative al Prodotto/Marchio — volume BASSO:**
`Nokbox` · `Nokbox reviews` · `Everplans` · `Everplans review` · `Trustworthy app` ·
`My Estate Kit` · `I'm Dead Now What book` · `Nokbox vs Everplans` · `Aura Life` ·
`Elayne` · `Leave It Sorted` (+ varianti brand).
- Ricerche mensili combinate (stima): **basso**.

**Rapporto Volume di Ricerca (direzionale, da verificare):**
> **Problema : Soluzione : Prodotto ≈ 6 : 2 : 1**

- **Questo rapporto suggerisce che il mercato è prevalentemente: PROBLEM AWARE.** La
  domanda è trainata dall'ansia-problema (spesso reattiva/notturna), non dalla ricerca
  di una categoria-soluzione e ancor meno di un brand.

---

## E. Analisi delle Soluzioni Fallite (QUANTIFICATA — STIMA)

"Triangolate ~80-100 menzioni di soluzioni precedenti attraverso forum, recensioni
competitor e articoli. Percentuali come quota stimata delle 'soluzioni fallite'
citate." (Stima, non conteggio grezzo — vedi Nota Metodologica.)

**1. "Avere la conversazione" a voce con il genitore — ~24% delle soluzioni fallite**
- Perché l'hanno provata: è la mossa "ovvia" e gratuita.
- Perché ha fallito: blocco **relazionale**; il genitore deflette ("perché, sto
  morendo?"), si offende o cambia discorso; Dana rimanda.
- Citazioni: "Every time I bring it up my mom shuts down." / "He thinks I'm after his
  money." / "It turned into a fight, so I dropped it."

**2. Spreadsheet / quaderno fai-da-te — ~20%**
- Perché: Dana è "quella organizzata", crede di poterselo fare.
- Perché ha fallito: nessuno lo mantiene; il genitore non lo compila; manca tempo
  ("I'm already drowning"); resta incompleto.
- Citazioni: "We started a notebook and never kept it up." / "Couldn't I just make a
  spreadsheet?" (poi mai fatto).

**3. "Tutto in testa al genitore"/carte sparse (non-soluzione di default) — ~16%**
- Perché: inerzia; "ci ha sempre pensato lui/lei".
- Perché ha fallito: in emergenza nessuno trova niente — "financial scavenger hunt".
- Citazioni: "Everything's in my dad's head." / "I had no idea where anything was."

**4. Death/estate planner o "when I'm gone" binder generico — ~14%**
- Perché: l'hanno trovato su Amazon/Etsy/Walmart.
- Perché ha fallito: tono **morboso/da fine vita** → "telling mom she's dying"; resta
  nel cassetto; il genitore non lo compila; terminologia legale intimidente.
- Citazioni: "The 'when I'm gone' planners feel so morbid." / "It just sat in a
  drawer." / "I didn't want to hand my mom a death planner."

**5. Solo documenti legali (POA/testamento) — ~10%**
- Perché: "abbiamo fatto il testamento/la procura, basta così".
- Perché ha fallito: password e *posizione* dei conti restano ignote; la POA decade
  alla morte; le password non danno autorità.
- Citazioni: "We did the POA but I still don't know the logins." / "Passwords aren't
  authority."

**6. Cassetta di sicurezza / cassaforte ignifuga — ~7%**
- Perché: "sicuro".
- Perché ha fallito: Dana non ha accesso/non sa cosa c'è dentro; in crisi è bloccata.
- Citazioni: "The will's in the safe deposit box but I can't get in."

**7. Password manager — ~5%**
- Perché: soluzione "tech".
- Perché ha fallito: il genitore non è abbastanza tech-savvy; Dana non ha la master.
- Citazioni: "Told them to use a password manager — they never set it up."

**8. Aspettare la crisi / Googlare al 2am (non-soluzione) — ~4%**
- Perché: procrastinazione/evitamento.
- Perché ha fallito: panico, tempo perso, incubo burocratico durante il lutto.
- Citazioni: "I don't want to be googling this at 2am." / "I'll deal with it when I
  have to."

---

## F. Determinazione Finale della Consapevolezza

- **LIVELLO DI CONSAPEVOLEZZA DOMINANTE: PROBLEM AWARE (Consapevole del Problema).**
- **Distribuzione:** ~**50%** del mercato Dana è in questa fase (con il 15% Unaware
  "sotto" e il 25% Solution Aware "sopra").
- **Livello di Fiducia:** **Medio-Alto sul livello dominante**; **Medio** sulle
  percentuali esatte (per i vincoli di scraping descritti nella Nota Metodologica).
- **Motivazione (prove triangolate):**
  1. Dana sa benissimo *cosa le servirebbe* (dove sono conti/password/documenti): il
     blocco è **relazionale**, non informativo — lo dice la ricerca prodotto e lo
     conferma la saturazione di contenuti "come parlarne col genitore".
  2. La domanda è trainata da **query-problema reattive** (rapporto stimato
     Problema:Soluzione:Prodotto ≈ 6:2:1), non dalla ricerca di una categoria o di un
     brand.
  3. Il *formato-soluzione* (comprare un organizer come **regalo**) è a **bassa
     salienza**: cercando "gift for elderly parents" non emergono organizer ma medical
     alert/gadget → chi sa del problema spesso NON pensa "regalo pronto".
  4. Le soluzioni note alla fetta Solution Aware sono vissute come **fai-da-te** o
     **death planner morboso**, entrambe ad alto attrito → non convertono Dana.
  5. Esiste domanda reale e brand con traction (Nokbox ~9-15k recensioni, "I'm Dead
     Now What" ~11,5k rating), ma la Product/Most Awareness *sul lato regalo di Dana*
     è piccola e il framing "regalo, non death planner" è scoperto dal mercato.
- **Accordo tra le Fonti:**
  - **Social media/forum:** Problem Aware (dominano ansia e blocco relazionale).
  - **Dati di ricerca:** Problem Aware (skew query-problema reattive).
  - **Analisi recensioni/e-commerce:** Solution→Product Aware *per chi già compra*, ma
    è una minoranza e spesso auto-uso/genitore-compra; conferma domanda, non sposta il
    dominante di Dana.
  - **Intelligence di mercato:** Problem/Solution Aware (adozione estate planning
    bassa — 24% ha un testamento — ma categoria in forte crescita).
  - **Divergenza e risoluzione:** l'e-commerce potrebbe suggerire "Solution/Product
    Aware" guardando i volumi di recensioni; ma quelle vendite catturano
    prevalentemente auto-acquirenti e genitori-compratori di death planner, NON Dana
    che regala. Pesando per la *persona Dana-come-acquirente-regalo* e per la struttura
    della domanda (reattiva, problema-centrica, bassa salienza del formato-regalo), il
    dominante resta **Problem Aware**, con un ponte strategico verso Solution Aware.

**Implicazione per il copy (hand-off al mechanism/angle):** partire dal **problema
vissuto e riconosciuto** (la scena del "2am", il "non saprei dove cercare") e
**costruire la categoria-soluzione come regalo non-morboso** — cioè spostare Dana da
Problem Aware a Solution/Product Aware *dentro* l'annuncio. Non dare per scontato che
Dana stia già confrontando organizer: va educata che (a) esiste un prodotto, (b) non è
un death planner, (c) non deve costruirselo da sola. Advertorial long-form
problema→soluzione è il formato nativo per un mercato Problem Aware.

---

## G. Documentazione delle Fonti (per categoria)

> Fonti accedute via WebSearch (sintesi + link). Scraping diretto bloccato (vedi Nota).
> "Punti dati" = citazioni/pattern/statistiche estratti dalle sintesi, non conteggi
> grezzi di commenti.

**Social Media / Forum / Community (data accesso: 8-15 ott 2026)**
- r/AgingParents, r/CaregiverSupport, r/estateplanning — accesso diretto BLOCCATO
  (403); pattern ricostruiti da sintesi di ricerca. Risultato: dominanza Problem Aware
  + blocco relazionale.
- caregivers.com / portal.prod.caregivers.com — thread "mother won't put anyone on her
  checking account", "good book a lady 81 could use". Problem/Solution Aware.
- ProductReview.com.au — recensione estate organizer ("friend had a drawn-out process
  because parents hadn't written down where anything was"). Problem→Solution.
- Quora (via surfacing) — "how to find out parents' bank accounts". Problem Aware.
- TikTok (via Mother.ly) — post virale caregiving padre 83 anni → "community of
  caregivers". Problem Aware/emotivo.
- Facebook caregiver groups (via DailyCaring directory) — gruppi "Sandwich Generation".

**Ricerca / SEO**
- RankHero (life-planner ~8.100/mese, funeral-planner), SearchVolume.io, Backlinko
  keyword tool, Keyword Planner/Ahrefs/Semrush (discussione metodologica),
  AccuRanker, KeywordsEverywhere. Risultato: skew query-problema.

**Intelligence di Mercato**
- Verified Market Research (estate planning software $1,62B→$3,83B, 11,4% CAGR).
- The Business Research Company (digital legacy $21,86B→$25,63B, 17,2%).
- Ken Research (digital legacy $25B→$54B, 13,8%).
- Business Research Insights (estate planning services ~$114B, 4,5%).
- IBISWorld (US trusts & estates ~$284,5B, 2,8%).
- StartUs Insights (948 death-tech companies, ~$837M funding).
- Caring.com Wills Survey 2025 (24% ha testamento; >50% nulla) + 2024 (32%).
- AARP/NAC Caregiving in the US 2025 (17M sandwich dual-care; 50-63M caregiver).
- Pew / Care.com 2026 (1/4 adulti sandwich gen; ~24h/sett care).

**Concorrenza / E-commerce**
- Nokbox (thenokbox.com; Loox ~9.394-15.394 recensioni; Shop.app ~4,3k rating 4,5★;
  pagine "aging parents", "gift", "sandwich generation"). Solution/Product Aware +
  gift framing emergente.
- "I'm Dead Now What" (Peter Pauper Press) — ~11.529 rating Amazon 4,6★ (2023);
  Walmart 252 recensioni, badge bestseller. Acquisti multipli come regalo.
- Everplans (acquisito da Precoa, ott 2024); Trustworthy (blog elderly-parents);
  My Estate Kit (myestatekit.co.uk; Trustpilot frammentato 3,8-4,6, pochi review,
  UK-only, angolo "adult children"/"Four Professionals"); The Estate Organiser (AU);
  Elayne (find deceased parent accounts); Aura Life; Legacy Compass.
- Walmart "emergency binder"/"Putting Things in Order" (4,6★/15), Veleron "If I Die
  Binder" (bestseller, 2,9★/16); Etsy "end of life planner"/estate binder (MadeSimpleUS
  ecc.).

**Contenuti / Influencer**
- Trustworthy blog, Overture "29 documents", NPR "big talk", Fidelity "financial
  scavenger hunt", US Bank/Capital One checklist, Neptune Society, Next Avenue,
  LegalZoom, Western & Southern, Dave Ramsey legacy drawer, podcast "Black Parents
  Aging", video Bryan Fagan, AHA/Mother.ly sandwich generation, Swedish death cleaning
  (Wikipedia/PureWow/Ideal Home).

**Fonti Uniche Totali (toccate):** ~110. **Rilevanti/usate:** ~70.
**Punti Dati estratti (citazioni/pattern/statistiche):** diverse centinaia
(qualitativi). **Conteggi grezzi commento-per-commento:** NON disponibili per vincoli
di egress — dichiarato onestamente.

---

## H. Riepilogo Esecutivo

- **Livello di Consapevolezza del Mercato: PROBLEM AWARE (Consapevole del Problema) —
  ~50% del mercato Dana.** Distribuzione completa: Unaware 15% · **Problem Aware 50%**
  · Solution Aware 25% · Product Aware 8% · Most Aware 2%.
- **Cosa Significa:** Dana **sa** di avere un problema serio e lo sente emotivamente
  (se succede qualcosa al genitore, non saprebbe dove sono conti/password/documenti, e
  vivrebbe un incubo burocratico durante il lutto). Quello che in gran parte **non** sa
  è che (1) esiste un **prodotto-regalo già pronto** pensato apposta, (2) che **non è
  un death planner** morboso, e (3) che **non deve costruirselo da sola**. Il suo
  blocco è relazionale ("come lo dico a mamma senza offenderla?") più che informativo.
- **Fiducia nella Valutazione: Medio-Alta** sul livello dominante; Media sulle
  percentuali esatte.
- **Motivo del Livello di Fiducia:** forte convergenza qualitativa di tutte le
  categorie di fonti (social, ricerca, mercato) sul dominante Problem Aware, e
  rapporto di ricerca Problema:Soluzione:Prodotto ≈ 6:2:1; ma la precisione numerica è
  limitata dall'**impossibilità di scraping diretto** di Reddit/recensioni/keyword
  tool in questa sessione (Agent Reach non configurato, Reddit 403, WebFetch/curl
  bloccati). Le % sono triangolazioni, non conteggi grezzi.
- **Soluzioni Fallite Più Comuni (per il mechanism-generator, in ordine di frequenza
  stimata):**
  1. **"Avere la conversazione" a voce** → fallisce per blocco relazionale/difesa del
     genitore.
  2. **Spreadsheet / quaderno fai-da-te** → fallisce perché mai mantenuto/compilato.
  3. **Death/estate planner o "when I'm gone" binger generico** → fallisce perché
     morboso, resta nel cassetto, "sembra dire a mamma che sta morendo".
  4. **Solo documenti legali (POA/testamento)** → fallisce perché password e posizione
     dei conti restano ignote (le password non danno autorità; la POA decade).

**Raccomandazione strategica per la pipeline:** trattare il copy come **movimento
Problem→Solution dentro l'annuncio** — hook sul problema riconosciuto (la scena del
"2am", "I had no idea where anything was"), poi introdurre la categoria-soluzione come
**regalo premuroso e NON death planner**, abbattendo i tre attriti chiave
(morbosità/"le sto dicendo che muore", fai-da-te, "non ci serve"). Formato nativo:
**advertorial long-form** (coerente con mercato Problem Aware e ricerca reattiva).
