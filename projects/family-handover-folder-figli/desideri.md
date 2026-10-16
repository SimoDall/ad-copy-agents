# Desideri di massa — Pubblico "Figli" (Dana Whitfield)

> Output di `desire-researcher` per il Family Handover Folder / The Thoughtful Gift Bundle.
> Categoria: digital estate-planning / family emergency organizer posizionato come REGALO.
> Paese target: USA (mercato anglofono; scalabile UK/CA/AU/NZ).
> Pubblico analizzato: **Dana** — figlia/o adulto 44-58 anni di genitori 72-88, acquirente-regalo.
> NON il genitore ("Barb"), NON il figlio già in piena crisi (Notify Everyone Kit).
> Ricerca condotta in inglese (mercato target); output in italiano.
>
> **Run corrente: 2026-10-16 (secondo tentativo).** Obiettivo del re-run: ampliare
> i dati Reddit con lo scraper Apify `harshmaur/reddit-scraper`. **Obiettivo NON
> raggiunto in questa sessione** — vedi nota metodologica. I 5 desideri sono quelli
> del run precedente, **ri-validati** da un nuovo passaggio su fonti accessibili;
> non sono emersi desideri nuovi.

---

## NOTA METODOLOGICA E LIMITI (leggere prima dei dati)

### Run 2026-10-16 — lo scraper Apify NON è stato eseguibile

Questo re-run era stato richiesto specificamente per sostituire le stime con
frequenze contate, ampliando la raccolta Reddit tramite lo scraper Apify con la
configurazione fissa. **La raccolta Apify non è stata possibile in questa
sessione.** Dettaglio tecnico di ciò che è stato tentato, in ordine:

1. **Strumenti MCP `mcp__apify-reddit-scraper__*` — NON disponibili.** Il server
   MCP `apify-reddit-scraper` risulta "connesso", ma non espone alcun tool
   chiamabile in questa sessione. Tentate e fallite tutte e tre le chiamate:
   - `harshmaur--reddit-scraper` → *"No such tool available ... server connected but does not offer this tool here"*
   - `get-actor-run` → stesso errore
   - `call-actor` → stesso errore
   Lo scraper con la configurazione fissa (10 searchTerms, searchPosts+comments,
   maxPostsCount 20, maxCommentsPerPost 10, tetto spesa $8, waitSecs 45) **non è
   mai partito**: nessun run creato, **costo/run = $0**, nessun runId.
2. **API Apify via Bash — NON autenticabile.** Nessuna variabile `APIFY_TOKEN`
   nell'ambiente; `GET https://api.apify.com/v2/acts` → **HTTP 401**. Impossibile
   lanciare o leggere dataset via `curl`.
3. **Agent Reach — NON installato.** `agent-reach: command not found`.
4. **Reddit diretto — bloccato dal proxy.** `www.reddit.com/search.json` → **403**;
   `old.reddit.com` → **CONNECT tunnel failed, 403**; `api.pullpush.io` (mirror) →
   irraggiungibile (000); WebFetch su `reddit.com` → *"unable to fetch"*.

**Conseguenza.** In questo run **non è stato raccolto alcun post o commento Reddit**
(0 post, 0 commenti per tutte e 10 le keyword). La cartella
`projects/family-handover-folder-figli/reddit-raw/` è stata creata ma è **vuota**:
nessun dataset grezzo da salvare, perché nessun run è stato prodotto. Non sono stati
inventati conteggi, citazioni o percentuali "contate".

### Cosa è stato fatto invece (validazione su fonti accessibili)

È stato eseguito un nuovo passaggio mirato di WebSearch su fonti accessibili
(blog estate-planning, financial advisor, colonne di news locali, forum/recensioni
indicizzate, pagine prodotto Etsy/Walmart/Trustpilot). Risultato: **i 5 desideri del
run precedente sono stati ri-confermati e nessun sesto nucleo è emerso** — di nuovo
saturazione tematica rapida. Un paio di nuove formulazioni verbatim utili sono state
aggiunte sotto (opener "Where do you keep important documents—and how would I find
them?" e "It doesn't all have to be done overnight"), ma rafforzano i desideri
esistenti, non ne aprono di nuovi.

### Stato delle percentuali

Le **percentuali restano STIME** identiche al run precedente: senza i conteggi
Reddit dello scraper non è stato possibile sostituirle con frequenze censite.
Questo era l'unico vero deliverable aggiuntivo atteso dal re-run, e **resta aperto**.

### Quota profilo "Dana" (figlia in preparazione, genitore ancora vivo)

Il filtro richiesto (distinguere i post di figlie che si preparano con calma dai post
di persone **già in lutto**) **non è calcolabile su Reddit in questo run**, perché
nessun post Reddit è stato recuperato (0/0). Dichiarazione onesta sul trattamento:

- Sulla popolazione Reddit prevista dalle 10 keyword, 3 keyword ("what to do when a
  parent dies", "parent passed away no passwords", "how to help elderly parent plan
  for death") pescano strutturalmente molti **post post-lutto / fuori profilo Dana**;
  5 keyword ("parents won't talk about finances", "help my parents get organized",
  "aging parent financial organization", "wish I had organized my parents documents",
  "dad won't talk about his will") sono **centrate sul profilo Dana**; 2 sono miste.
  **Questa è una previsione di design, non una misura**: andrà verificata quando lo
  scraper sarà eseguibile, etichettando ogni post come `in-profilo` / `post-lutto` /
  `altro` e riportando la quota reale.
- Le **fonti accessibili** usate in questo run sono invece in prevalenza
  **on-profilo Dana** (blog "how to talk to your aging parents", advisor su cosa
  dovrebbero sapere i figli adulti, recensioni di organizer comprati in prevenzione):
  è su queste che poggiano i desideri. Le fonti "post-lutto" (guide "what to do when a
  parent dies", storie di esecutori) sono state usate **solo** per documentare il
  *dolore futuro concreto* dietro i desideri #1 e #3 (ciò che Dana teme), non come
  voce diretta di Dana.

### Conteggio fonti per piattaforma (run 2026-10-16)

| Piattaforma | Stato accesso | Post/commenti o voci raccolte | Valore per questa categoria |
|---|---|---|---|
| **Reddit via Apify (scraper fisso)** | **FALLITO — tool non offerto / $0 / 0 run** | **0 post, 0 commenti** | Alto (atteso), ma non ottenuto |
| Reddit diretto (www/old/pullpush/WebFetch) | **Bloccato** (403 / 000 / unable to fetch) | 0 | — |
| Agent Reach | **Non installato** | 0 | — |
| Blog estate-planning / advisor (Greenbush, Commerce Bank, Synchrony, Savant, Kiplinger, Next Avenue) | OK via WebSearch | ~10-12 | Alto per #2 e #3 |
| Colonne news / "questions to ask your parents" (East Idaho, Democrat Chronicle, Not Too Late Substack) | OK via snippet | ~5 | Medio-alto per #2 |
| Guide "track down accounts / tasks when a parent dies" (Elayne, Adams Brown, Fidelity CA, Fox Business) | OK via snippet | ~6 | Alto per #3 (dolore futuro) |
| Recensioni Etsy (MadeSimpleUS), Walmart, Trustpilot (Estate Organiser), Goodreads (Get It Together) | OK via snippet | ~8 | Alto per #1 e #4 |
| Blog/Substack personali ("digital afterlife", password lockout) | OK | ~4 | Alto per #1/#3 (storie reali) |
| Dati survey citati (Haven Life 80%, Grow Therapy 43%) | OK (dal run precedente) | 2 | Supporto quantitativo trasversale |

**Voci distinte effettivamente osservate (cumulate con il run precedente): ~70-95.**
Lontane dal target 700-1000+ del prompt, per i blocchi sopra. **Piattaforma più
preziosa ma ancora inaccessibile: Reddit** — resta la raccomandazione #1 da sbloccare.

---

## I 5 DESIDERI SUPERFICIALI PRIMARI

Tutti e cinque superano il test fondamentale: sono **risultati che Dana ottiene
USANDO il kit** (sapere dove è tutto, aprire il discorso, non annegare nella
burocrazia, dormire tranquilla, essere pronta senza invadere), non caratteristiche
del prodotto. **Invariati e ri-validati rispetto al run precedente.**

---

### Desiderio Superficiale #1
**"Voglio sapere dove trovare tutto se succede qualcosa."**

Il risultato n.1 e più trasversale: un unico posto dove stanno conti, password,
documenti e contatti, così che un'emergenza non diventi una caccia al tesoro.

**Piattaforme viste:** recensioni Etsy (MadeSimpleUS), Walmart ("Putting Things In
Order"), recensioni Nokbox (Loox), blog "digital afterlife"
(Substack/CBC/HumbleDollar), articoli estate-planning (Kiplinger, Trustworthy,
Greenbush Financial), executive summary (query reattive notturne).

**Citazioni testuali (EN):**
- *"I have a sense of peace knowing everything is organized and in one place for my family for when the day comes."* — recensione Etsy (MadeSimpleUS)
- *"I have been handling my father's estate without ANY of this information."* — recensione Nokbox (widget Loox)
- *"It took months to gain and regain control of my parents' online accounts... much of this could have been avoided with proper password management."* — blog personale (Substack "digital afterlife")

**Driver emotivi (3):**
- Mi sento **in panico / impreparata** quando immagino di dover cercare a tappeto conti e password mentre il genitore è in ospedale e non c'è tempo. *(stima ~45%)*
- Mi sento **sollevata** quando penso che esista un solo posto dove guardare, invece di decine di cassetti, email e banche da ricostruire. *(stima ~35%)*
- Mi sento **esposta / vulnerabile** perché so che senza le password "le istituzioni finanziarie non ti danno nessuna informazione" e resterei bloccata fuori da tutto. *(stima ~20%)*

---

### Desiderio Superficiale #2
**"Voglio sollevare il discorso senza offenderli o litigare."**

Il blocco di Dana non è informativo, è **relazionale**: sa cosa le servirebbe
sapere, ma non come chiederlo senza che suoni come "stai invecchiando/stai morendo".
Il risultato desiderato è una conversazione che avviene con dolcezza.

**Piattaforme viste:** blog "how to talk to your parents about estate planning"
(Kiplinger, Next Avenue, Commerce Bank, Synchrony, Savant Wealth, Offit Kurman,
LegalZoom), colonne "questions to ask your parents" (East Idaho, Democrat Chronicle,
Not Too Late Substack), executive summary, forum caregiver.

**Citazioni testuali (EN):**
- *"Where do you keep important documents—and how would I find them?"* — opener suggerito, colonna news locale (East Idaho / Democrat Chronicle)
- *"Make clear that your aim is to carry out their wishes, not to get a share or take control. Don't undermine their wishes or try to take control."* — St Law Firm
- *"I mean, you're my parents, but I was wondering, would you look at this?"* — citazione VoC riportata nell'executive summary

**Driver emotivi (3):**
- Mi sento **in colpa / a disagio** perché temo che chiedere suoni come un'accusa sull'età o la salute del genitore. *(stima ~45%)*
- Mi sento **bloccata / rimandataria** quando so che dovrei parlarne ma non trovo mai le parole giuste e rinvio ancora. *(stima ~35%)*
- Mi sento **imbarazzata** all'idea di essere io "quella burocratica" che tira fuori moduli e documenti in un momento familiare. *(stima ~20%)*

---

### Desiderio Superficiale #3
**"Voglio vivere il lutto senza restare intrappolata nella burocrazia."**

Il risultato è evitare il futuro-dolore ben documentato: conti congelati, mesi di
probate, certificati di morte a dozzine, caccia agli account — tutto mentre si sta
elaborando una perdita.

**Piattaforme viste:** guide "what to do when a parent dies / track down accounts"
(Elayne, Adams Brown CPA, Fidelity CA, Fox Business, Protective, Darrow, Fatherly),
blog probate/studi legali (Pierce Law, Hugill & Ip), blog "digital afterlife"
(CBC, Substack), forum caregivers.com.

**Citazioni testuali (EN):**
- *"Funds stay locked until a court grants the executor authority — typically 3 to 6 months or longer, depending on probate complexity."* — guida probate (Hugill & Ip / sintesi guide US)
- *"In one day, the mom lost online access to credit cards, utilities, bank accounts, retirement accounts, and more... she spent three months navigating bureaucracy."* — storia personale (CBC "Out In The Open" / blog digital afterlife)
- *"It doesn't all have to be done overnight."* — testimonianza personale (figlia che ha impiegato un intero anno fiscale a chiudere conti sconosciuti, via guida "financial tasks when a parent dies")

**Driver emotivi (3):**
- Mi sento **sopraffatta / in affanno** all'idea di dover fare l'esecutrice senza sapere da dove si comincia, proprio nei giorni più duri. *(stima ~45%)*
- Mi sento **in trappola** quando penso ai conti congelati e alle bollette insolute mentre aspetto che un tribunale mi dia l'autorità. *(stima ~30%)*
- Mi sento **derubata del tempo del lutto**, perché la burocrazia prende lo spazio che vorrei dare al dolore e alla famiglia. *(stima ~25%)*

---

### Desiderio Superficiale #4
**"Voglio smettere di avere quell'ansia di sottofondo."**

Il risultato emotivo puro: poter dire "ho tutto sotto controllo", dormire, togliere
dalla testa il pensiero fisso del "e se succedesse ora?".

**Piattaforme viste:** recensioni Nokbox (Loox), recensioni Etsy (MadeSimpleUS),
Goodreads ("Get It Together"), guida canadese Heritage ("Before It's Too Late"), blog
stress caregiver (Grow Therapy, Tanner), survey (Haven Life, Grow Therapy), executive
summary (ricerca "2 di notte").

**Citazioni testuali (EN):**
- *"I love the peace of mind this is giving me."* — recensione Nokbox (widget Loox)
- *"You will be able to enjoy the peace of mind knowing that this important task is taken care of."* — guida organizer (Heritage, "Before It's Too Late")
- *"43% of adult children report chronic stress when caring for aging parents."* — Grow Therapy (dato di supporto al vissuto d'ansia diffuso)

**Driver emotivi (3):**
- Mi sento **in ansia costante / sopraffatta** perché sono già allo stremo tra figli, lavoro e genitori e questo pensiero resta sullo sfondo (80% della sandwich generation si dichiara spesso sopraffatta — Haven Life). *(stima ~45%)*
- Mi sento **in pace / finalmente leggera** quando so che, qualunque cosa accada, è già tutto scritto in un posto solo. *(stima ~35%)*
- Mi sento **spaventata di notte** quando mi parte la ricerca da panico ("what to do when a parent dies") e realizzo che non saprei cosa fare. *(stima ~20%)*

---

### Desiderio Superficiale #5
**"Voglio essere pronta senza prendere il controllo dei miei genitori."**

Chiave per la psicologia del regalo: Dana non vuole "gestire" la vita del genitore,
vuole solo essere pronta. Il risultato è preservare l'indipendenza e la dignità del
genitore avendo comunque le informazioni "nel caso". È ciò che distingue Dana da un
figlio che prende in mano la situazione.

**Piattaforme viste:** AARP, Griswold Care, Lifeline, Greenbush Financial ("locate,
don't hand over"), Savant Wealth ("recognize their independence, privacy and
autonomy"), forum caregivers.com, executive summary, blog regali per anziani.

**Citazioni testuali (EN):**
- *"Some parents may view their children's moves as 'takeover' attempts and experience their help as a loss of independence."* — AARP
- *"Be respectful, and recognize their independence, privacy and autonomy. You don't need to cover everything at once."* — Savant Wealth / sintesi advisor
- *"I wasn't trying to take over my dad's life. I just wanted to be ready."* — hook VoC riportato nell'executive summary

**Driver emotivi (3):**
- Mi sento **in colpa all'idea di invadere** perché voglio rispettare l'autonomia dei miei genitori, non trattarli come se non fossero più capaci. *(stima ~40%)*
- Mi sento **tranquilla / rispettosa** quando è il genitore a compilare, con i propri tempi e nella sua voce, e io sono solo pronta "nel caso". *(stima ~35%)*
- Mi sento **sotto pressione come figlia responsabile**, spesso l'unica o la più coinvolta, e temo di sbagliare prendendo decisioni che non spettano a me. *(stima ~25%)*

---

## PUNTO DI VERIFICA / CONTROLLO QUALITÀ

- **5 desideri primari** totali. ✓
- **Esattamente 3 driver emotivi per desiderio = 15 voci totali.** ✓ (3+3+3+3+3)
- **I desideri sono risultati, non caratteristiche.** ✓
- **Citazioni incluse** per ogni desiderio (3 ciascuno, in EN con tipo di fonte). ✓
- **Formato "Voglio [risultato]"**, max ~10 parole, un solo risultato, senza "e/o". ✓
- **Formato driver "Mi sento [emozione] perché/quando [situazione]" + % stima.** ✓

---

## DIFFERENZE RISPETTO AL RUN PRECEDENTE (run 1 → run 2026-10-16)

- **Nessun cambiamento ai 5 desideri né ai 15 driver né alle percentuali.** Il
  secondo passaggio su fonti accessibili ha ri-confermato gli stessi 5 nuclei, con
  saturazione rapida; nessun sesto desiderio emerso.
- **Lo scraper Apify — motivo del re-run — NON è stato eseguibile** (tool MCP non
  offerto, nessun token per l'API, Agent Reach assente, Reddit diretto 403).
  **0 post / 0 commenti Reddit raccolti; $0 di spesa; nessun run creato.** Il run
  precedente era già senza dati Reddit diretti: su questo fronte **la situazione è
  invariata**, l'ampliamento atteso non è avvenuto.
- **Citazioni aggiornate/aggiunte** (rafforzano desideri esistenti, non ne creano di
  nuovi): opener "Where do you keep important documents—and how would I find them?"
  (#2), "It doesn't all have to be done overnight" (#3), guida Heritage "peace of
  mind" (#4), Savant "recognize their independence" e Greenbush "locate, don't hand
  over" (#5).
- **Fonti nuove toccate** rispetto al run 1: Greenbush Financial, Commerce Bank,
  Synchrony, Savant Wealth, East Idaho News / Democrat Chronicle, Not Too Late
  Substack, Elayne, Adams Brown CPA, Fidelity CA, Walmart listing, Goodreads "Get It
  Together", guida canadese Heritage.
- **La quota profilo Dana su Reddit resta non misurata** (0 post recuperati); resta
  solo la previsione di design sulle 10 keyword (vedi nota metodologica).

---

## OSSERVAZIONI STRATEGICHE PER LE FASI SUCCESSIVE

- **Il blocco dominante è relazionale (#2 + #5), non pratico.** Dana sa cosa serve;
  non sa come chiederlo/regalarlo senza offendere. I due bonus del bundle (Dear
  Mom/Dad Starter Letter, Conversation Starter Card) colpiscono esattamente qui.
- **#1 e #3 sono il "dolore futuro" concreto** che giustifica razionalmente
  l'acquisto; #4 è il beneficio emotivo che chiude; #5 è il permesso psicologico
  che rende l'acquisto compatibile con l'identità di "figlia che rispetta".
- **Conflitto tra fratelli** resta un driver secondario dentro #1/#3/#4, non un
  sesto desiderio a sé.
- **Linguaggio da riusare nel copy (EN, verbatim dal mercato):** "one place",
  "peace of mind", "I didn't know where anything was", "I just wanted to be ready",
  "without taking over", "they aren't going to give you any information",
  "months, not days", "where do you keep important documents—and how would I find
  them?", "locate, don't hand over", "it doesn't all have to be done overnight".
- **Linguaggio da EVITARE:** "death", "end of life", "when I'm gone", "funeral".
  Framing vincente: "just in case / an ordinary Tuesday".

---

## RACCOMANDAZIONE DI VALIDAZIONE (per l'orchestratore) — PRIORITÀ ALTA

L'unico deliverable che il re-run doveva aggiungere (frequenze contate da Reddit)
**resta aperto** perché lo scraper non era eseguibile. Prima di scalare budget:

1. **Sbloccare l'accesso Apify**: verificare che il server MCP `apify-reddit-scraper`
   esponga davvero i tool (`harshmaur--reddit-scraper`, `get-actor-run`,
   `get-dataset-items`) a questo agente, **oppure** fornire un `APIFY_TOKEN`
   nell'ambiente così da poter lanciare l'actor via API. In questa sessione nessuna
   delle due condizioni era soddisfatta.
2. Ri-eseguire lo scraper con la configurazione fissa, salvare il grezzo in
   `reddit-raw/`, etichettare ogni post `in-profilo Dana` / `post-lutto` / `altro` e
   **riportare la quota reale**.
3. Sostituire le percentuali-stima con frequenze contate e ri-ordinare i 5 desideri
   se i dati Reddit lo impongono.
