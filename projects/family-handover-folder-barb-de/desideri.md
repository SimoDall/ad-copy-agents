# Desideri di massa — Pubblico "Barb" (auto-acquirente), mercato tedesco

> Output di `desire-researcher` (Prompt 1, "The Psychological Scaling Model").
> **Categoria:** digital estate-planning / family emergency organizer per uso personale, non come
> regalo. In Germania si chiama **"Notfallordner"**.
> **Paese:** Germania. **Prodotto:** leaveitsorted.com, The Family Handover Kit (DE: "Der
> Notfallordner — Das Komplettset für Ihre Familie", 34 € scontato). **Concorrente:**
> Digistore24 #457702, Andreas Jansen, 19,99 €.
> **Pubblico:** Barb, 55-78 anni, che organizza le proprie cose per sé e la propria famiglia
> (non il profilo "Figli"/Dana).
> **Lingua:** ricerca condotta in TEDESCO; output in italiano con citazioni originali in tedesco.
> **Data run:** 2026-10-29.

---

## 1. Nota metodologica e limiti (leggere prima dei dati)

### Volume raggiunto per piattaforma

| Piattaforma | Fonti analizzate | Voci utili | Note |
|---|---|---|---|
| **Reddit (Apify, DE)** | 96 post trovati, 22 selezionati, 219 commenti | **~103** classificate | Il 79% dei post del passo A è fuori tema. Dettagli in `reddit-raw/2026-10-29-YUopucnh3ib23Peb3-manifest.md` |
| Recensioni (Trustpilot, LovelyBooks, eBay, Digistore24, Payhip, Ex Libris) | 9 pagine prodotto/recensioni | ~22 | Afilio: 20 recensioni lette su 258. Le pagine Digistore24 (4 prodotti), Payhip ed Ex Libris **non hanno recensioni** |
| Ricerche, studi e stampa (Deutsche Bank/Allensbach, Commerzbank/Ipsos, forsa/Central, Aeternitas, Stiftung Warentest) | 6 | dati quantitativi | Usati per triangolare l'ordine dei desideri |
| Blog e guide istituzionali (Apotheken Umschau, LV1871, Kreis SÜW, Erlangen, utopia, DHZ, biallo, bankdaten, WiWo/Versicherungsbote) | 10 | ~10 | Mostrano soprattutto come il mercato inquadra il tema, raramente la voce del cliente |
| **Amazon.de** | 0 | 0 | **Bloccato** (robots_disallowed). Recensioni non accessibili |
| **gutefrage.net, seniorentreff, feierabend.de** | 0 | 0 | Nessun thread emerso dalle ricerche WebSearch; non raggiungibili in modo mirato |
| **Facebook, Instagram, TikTok, commenti YouTube** | 0 | 0 | Non accessibili con gli strumenti disponibili |
| **Etsy.de** | 3 ricerche | 0 | Nessun Notfallordner/Vorsorgeordner in tedesco con recensioni. Solo planner in inglese su Payhip/Etsy |

**Totale: circa 135-140 voci distinte, lontano dal target del prompt (700-1000+).** Le
percentuali qui sotto sono quindi **conteggi su un campione piccolo**, non misure del mercato.
Le percentuali dei driver emotivi sono **stime** ricavate dalla frequenza con cui il tema
ricorre nelle voci di ciascun desiderio.

### Limiti critici
1. **Reddit DE non è la piattaforma di Barb.** Chi scrive su r/Finanzen, r/de_EDV e
   r/KeineDummenFragen ha in genere 25-50 anni. Indizi espliciti: "Ich bin 36", "ich bin noch
   keine 70", figli di genitori di 70-85 anni. **La voce diretta di persone di 55-78 anni è
   quasi assente.** Barb compare soprattutto in modo indiretto: la madre che "möchte mit uns
   über Patientenverfügung sprechen", il "Vati" che aveva preparato tutto, la madre che ha
   "Vollmacht über den Tod hinaus".
2. **Le keyword condizionano i conteggi.** Due keyword su dieci erano su Patientenverfügung e
   Testament, e hanno portato thread di medici e di diritto. Per questo **D2 (volontà
   rispettate) è sovrastimato** nel conteggio grezzo. D4 ha pochi item, ma include il post e il
   commento con più voti dell'intero dataset.
3. **Profilo delle voci Reddit classificate (circa 103):**
   - persone che organizzano per sé stesse, cioè il comportamento di Barb ma più giovani: ~53%
   - figli che parlano dei genitori (Dana): ~17%
   - medici e soccorritori: ~11%
   - persone in lutto: ~12%
   - terzi o casi legali: ~7%
4. **Dato di mercato tedesco fondamentale:** il Notfallordner è **mainstream e spesso gratuito**.
   Comuni e Landkreise come Erlangen (5 €) e SÜW (gratis, "zuletzt häufig nachgefragt") lo
   distribuiscono, e il Vorsorge-Set di Stiftung Warentest ha superato **1 milione di copie**.
   Su Reddit si legge "Es gibt genug Vorlagen im Netz". **Il desiderio esiste, ma la soluzione
   di base è considerata gratuita.** Va tenuto presente per il posizionamento (lo
   approfondisce awareness-researcher).

### Saturazione e valore per piattaforma
- **Reddit:** saturazione raggiunta su D1, D2 e D3: gli ultimi thread non hanno aggiunto temi
  nuovi. È la fonte più ricca per i driver emotivi.
- **Studi e sondaggi bancari:** la fonte più preziosa per Barb, perché Commerzbank ha un
  campione solo di over 55 e Deutsche Bank segmenta per età.
- **Recensioni:** scarse e poco utili. Parlano di requisiti di prodotto ("Leicht zu verstehen",
  "Einfache Handhabung"), non di desideri.
- **Piattaforme da coprire in un run futuro:** commenti dei Pin di Pinterest DE (canale del
  concorrente), gruppi Facebook 60+, recensioni Amazon.de di "Vorsorge-Set" e "Mein
  Notfallordner" tramite uno scraper dedicato.

---

## 2. Conteggi per desiderio (Reddit, voce primaria assegnata)

Base: 103 voci Reddit pertinenti, cioè 22 post e circa 81 commenti su 219. A ogni voce è
assegnato un solo desiderio primario.

| Desiderio | Voci | % su 103 | Esempi di voci con alto engagement |
|---|---|---|---|
| D1 Famiglia trova tutto senza cercare | 22 | 21% | Post "Notfallhandbuch für Familie" (240), thread "Notfalldose" |
| D2 Volontà rispettate | 37 | 36% ⚠️ | Thread di medici in r/medizin, thread sul testamento. Gonfiato dalle keyword |
| D3 Figli senza burocrazia del lutto | 21 | 20% | Commento "Im Todesfall-Liste" (192), "Kündigungsschreiben" (19) |
| D4 Togliersi il pensiero (finirlo) | 9 | 9% | **Post più votato del tema (308) e commento più votato (314)** |
| D5 Cari possono agire per me | 14 | 14% | "Deine Frau bekommt im Krankenhaus null Info" (22) |

Scartate: circa 138 voci tra fuori tema, ringraziamenti, battute, la polemica generazionale sui
pensionati e i dettagli tecnici sui servizi funebri.

**Ordine finale (triangolato).** Non segue solo il conteggio grezzo; tiene conto anche di:
- quanto il desiderio è centrale nella categoria, cioè nelle headline dei concorrenti e nelle
  guide istituzionali;
- i dati sugli over 55 (Commerzbank, Deutsche Bank, Aeternitas);
- l'engagement su Reddit.

Il risultato: **D1 > D2 > D3 > D4 > D5.**

---

## 3. I 5 desideri superficiali primari

### Desiderio superficiale #1: "Voglio che la mia famiglia trovi tutto senza cercare"

**Piattaforme:** Reddit (r/de_EDV, r/KeineDummenFragen, r/FinanzenGER, r/Ratschlag,
r/LegaladviceGerman), headline di tutti i concorrenti Digistore24, guide istituzionali
(Apotheken Umschau, Kreis SÜW, Erlangen).
È il desiderio che **definisce la categoria** in Germania: lo usa ogni concorrente e ogni ente
pubblico.

**Citazioni:**
- *"Wenn mir was passiert, wäre meine Familie wahrscheinlich ziemlich aufgeschmissen. Niemand
  weiß wo was ist und wie es funktioniert."* (Reddit r/de_EDV, post da 240 voti)
- *"Doch Wissen: Wo die Vorsorgevollmacht und die Patientenverfügung abgelegt ist! Bringt
  nichts, wenn es sie gibt, aber keiner weiß wo."* (Reddit r/Ratschlag, commento)
- *"Damit deine Familie im Ernstfall nicht suchen muss."* (headline del concorrente "Der Gelbe
  Notfallordner", Digistore24 #698950). Variante: *"damit du im Notfall nicht lange suchen
  musst"* (Jansen, #457702)
- Contesto: *"Wir haben also zu Haus nochmal alles gründlich durchsucht und das Sparbuch nicht
  gefunden, es sollen ca. 30000 Euro drauf sein."* (Reddit r/LegaladviceGerman, figlio dopo un
  decesso)

**Driver emotivi:**
1. **Mi sento in ansia quando penso a un imprevisto improvviso** (un incidente sfiorato,
   un'operazione, un ricovero), perché so che in quel momento "niemand weiß wo was ist" e non
   potrò spiegarlo io. Il trigger tipico è un quasi-incidente: *"vor einer Woche wäre ich fast in
   einen Autounfall geraten… Seitdem mache ich mir viel Gedanken"*. **~45%**
2. **Sento il peso della responsabilità perché sono io quella che tiene in mano tutto in
   famiglia** (conti, contratti, password), e se manco io gli altri restano "aufgeschmissen".
   Nella coppia di Barb spesso solo uno dei due "sa dove sono le cose". **~35%**
3. **Provo sollievo e serenità quando so che tutto è in un unico posto riconoscibile**, perché
   l'ho visto funzionare: *"Zuhause habe ich alle relevanten Daten in einer 'Wichtig'-Mappe…
   Hat viel Ruhe reingebracht."* (Reddit, persona con invalidità grave, con figli). **~20%**

---

### Desiderio superficiale #2: "Voglio che le mie volontà vengano rispettate"

**Piattaforme:** Reddit (r/medizin, r/KeineDummenFragen, r/LegaladviceGerman, r/Erben,
r/Finanzen), studio Commerzbank su over 55, studio Deutsche Bank/Allensbach.
**Triangolazione per Barb:** nello studio Commerzbank (2024, 500 persone di 55+ anni) la
**priorità n. 1** nella pianificazione è *far rispettare la propria volontà*. Il 21% vuole
evitare liti tra gli eredi. Secondo Deutsche Bank, il 67% dei potenziali testatori ritiene
importante che la ripartizione sia "klar geregelt".
⚠️ Il prodotto non crea documenti legalmente vincolanti (Patientenverfügung, testamento). Il
risultato che offre è che **le volontà sono scritte, trovabili e comunicate**: lettera "in caso
succeda qualcosa", checklist dei documenti.

**Citazioni:**
- *"Das wäre auch mein Alptraum, von Maßnahme zu Maschine geschoben zu werden."* (Reddit
  r/KeineDummenFragen, commento: il padre aveva escluso per iscritto la figlia con mentalità
  "Leben um jeden Preis")
- *"Will um jedem Fall verhindern dass irgendwer aus meiner Familie mit Entscheidungen über
  meinen Verbleib konfrontiert wird."* (Reddit r/LegaladviceGerman)
- *"…und auf die Frage nach Therapielimitierungen guckt die Familie einen an wie ein Reh im
  Scheinwerferlicht. 'Öh, haben wir noch nie drüber gesprochen.'"* (Reddit r/Finanzen, medico
  di terapia intensiva, 128 voti)
- Segnale per Barb: *"Meine Mutter möchte morgen mit uns… über diverse Themen sprechen, darunter
  auch Patientenverfügung."* (Reddit r/KeineDummenFragen: è la madre a prendere l'iniziativa)

**Driver emotivi:**
1. **Ho paura di perdere il controllo su di me quando non potrò più parlare**: essere tenuta in
   vita "um jeden Preis", attaccata alle macchine, oppure finire con decisioni prese da
   estranei. **~40%**
2. **Mi sento in colpa all'idea che i miei figli debbano decidere al posto mio o litigare tra
   loro**: la decisione sulla rianimazione, l'eredità contesa ("Erbstreit"), il fratello che
   gestisce i soldi della nonna. Voglio togliere loro quel peso. **~35%**
3. **Mi sento insicura che quello che scrivo valga davvero**: *"ob das so juristisch
   wasserdicht ist"*, *"99% der Patientenverfügungen sind ja praktisch nutzlos"*, testamenti
   scritti con ChatGPT pieni di errori. Temo di fare tutto e scoprire che non serviva. **~25%**

---

### Desiderio superficiale #3: "Voglio risparmiare ai miei figli la burocrazia dopo di me"

**Piattaforme:** Reddit (r/Finanzen, r/KeineDummenFragen, r/Ratschlag, r/LegaladviceGerman,
r/de_EDV), Aeternitas (sondaggio Infratest), guide di LV1871 e Kreis SÜW.
**Triangolazione per Barb:** secondo Aeternitas/Infratest (2005) l'interesse per la previdenza
cresce con l'età e le persone di **oltre 50 anni "non vogliono gravare sui familiari"**. Nelle
visite a domicilio le Gemeindeschwestern del Kreis SÜW notano che *"wichtige Unterlagen für
Notfälle oder Krankenhauseinlieferungen oft fehlen"*.

**Citazioni:**
- *"Mein Vati hatte das gemacht. Sogar vorbereitete Kündigungsschreiben für Verträge, in die man
  nur noch das Datum eintragen und unterschreiben musste. Hat Mutti und mir nach seinem Tod
  enorm geholfen… Jemanden verlieren ist schlimm genug; da kann man zumindest die Bürokratie
  einfacher machen für den Liebsten."* (Reddit r/Finanzen, commento)
- *"…die Familie hat Monate gebraucht, um überhaupt rauszufinden, welche Konten, Verträge und
  Versicherungen existieren. Kündigungsfristen verpasst, Geld verbrannt, Nerven sowieso."*
  (Reddit r/Finanzen, post da 308 voti)
- *"Mir ist wichtig dass im Falle meines plötzlichen Ablebens meine Frau und meine Kinder genau
  eine Telefonnummer wählen müssen."* (Reddit r/KeineDummenFragen)
- *"…nochmal mache ich das nicht mit, dass nichts geklärt ist."* (Reddit, figlio che dopo la
  morte della madre ha sistemato tutto per sé e per il padre)

**Driver emotivi:**
1. **Sento amore e protezione verso i miei figli quando immagino il loro lutto**: non voglio che
   al dolore si aggiungano moduli, banche e scadenze. *"Jemanden verlieren ist schlimm genug"*.
   **~45%**
2. **Ho paura delle conseguenze concrete che ho visto succedere ad altri**:
   - mesi persi a cercare i contratti;
   - Kündigungsfristen scadute;
   - Erbschein da 1.800-3.600 € perché mancava la Vollmacht;
   - Bestattungskosten divise tra fratelli;
   - polizza vita da notificare entro 24 ore.

   Il dolore immaginato è molto concreto e spesso economico. **~35%**
3. **Provo orgoglio, e non voglio essere un peso**: voglio che dopo di me basti "una sola
   telefonata" e che i figli non debbano anticipare soldi o tempo. È il motivo "non gravare"
   tipico degli over 50. **~20%**

---

### Desiderio superficiale #4: "Voglio togliermi finalmente questo pensiero"

**Piattaforme:** Reddit (r/Finanzen, r/de_EDV, r/KeineDummenFragen, r/LegaladviceGerman), studio
Deutsche Bank (il 64% affronta il tema "ungern").
Sono poche voci, ma hanno **l'engagement più alto dell'intero dataset**: il post da 308 voti e
il commento da 314 voti riguardano entrambi *il non riuscire a finire*.
Il risultato concreto per il cliente: il Notfallordner **completato e sulla scrivania**, invece
del pensiero che si trascina da mesi.

**Citazioni:**
- *"Seitdem nehme ich mir vor, diesen berühmten Notfallordner anzulegen… Der liegt nun seit 8
  Monaten als leerer Ordner auf dem Schreibtisch. Ehrliche Frage: Hat das hier jemand wirklich
  durchgezogen?"* (Reddit r/Finanzen, post da 308 voti)
- *"Einfach anfangen und dann nach und nach befüllen, statt alles auf einmal machen zu wollen und
  es nicht zu tun."* (Reddit r/Finanzen, commento da 314 voti)
- *"…meine Schwester hat auch damit angefangen und sie finden den Aufwand so 'enorm', dass sie es
  immer weiter vor sich herschiebt."* (Reddit r/Finanzen, commento da 50 voti)
- *"Ich habe es damals ausgedruckt, mit zu den Schwiegereltern genommen und jeden Punkt mit denen
  besprochen… gibt gerade der älteren Generation etwas Sicherheit."* (Reddit r/KeineDummenFragen)

**Driver emotivi:**
1. **Mi sento frustrata e un po' in colpa perché lo rimando da mesi**: so che è importante, ho
   comprato il raccoglitore, e lui resta lì vuoto a ricordarmelo. *"Vergisst man recht schnell
   im Alltag"* (94 voti). **~45%**
2. **Mi sento sopraffatta quando provo a iniziare**: troppe sezioni, troppa burocrazia (*"Dieser
   ganze Prozess fühlt sich… unnötig bürokratisch an"*), non so da dove partire e il tema della
   morte mette a disagio (il 64% lo affronta "ungern", Deutsche Bank). **~35%**
3. **Provo pace e sicurezza quando finalmente è fatto e datato**: *"Hat viel Ruhe
   reingebracht"*, *"gibt… Sicherheit"*. Posso tornare a vivere senza quel pensiero in
   sottofondo. **~20%**

---

### Desiderio superficiale #5: "Voglio che i miei cari possano agire subito per me"

Il risultato è che il partner e i figli possono accedere a conti, informazioni mediche e
account digitali e mandare avanti la casa se io non posso.

**Piattaforme:** Reddit (r/de_EDV, r/FinanzenGER, r/Finanzen, r/Ratschlag), sondaggio
forsa/Central, guide bankdaten.de e DHZ.
**Triangolazione per Barb:** secondo forsa/Central, **il 62% degli over 60 crede che i parenti
stretti possano decidere automaticamente per loro**, ma non è così. Solo il 26% ha una
Vorsorgevollmacht. Il 69% non ha mai pensato al proprio patrimonio digitale (Deutsche Bank).
Il desiderio quindi esiste, ma spesso **non è ancora consapevole** (tema per
awareness-researcher).

**Citazioni:**
- *"Deine Frau bekommt im Krankenhaus null Info. Schweigepflicht gilt auch gegenüber nahen
  Angehörigen. Ich habe es selbst erlebt."* (Reddit r/de_EDV, vedovo, 22 voti)
- *"Am meisten Sorgen macht mir die Tatsache, dass meine Liebsten zwar alle Zugänge haben, aber
  keiner ohne teuren IT Spezialisten in der Lage ist das alles am Laufen zu halten."* (Reddit
  r/de_EDV)
- *"Ohne ausdrückliche Vollmacht dürfen selbst Ehepartner und leibliche Kinder NICHT auf Ihr
  Bankkonto zugreifen."* (guida bankdaten.de "Für Senioren")
- *"Das große Problem wäre, wenn meine Mutter und ich gleichzeitig unter die Räder kommen."*
  (Reddit r/FinanzenGER)

**Driver emotivi:**
1. **Ho paura di lasciare il mio partner impotente proprio quando ha più bisogno**: in ospedale
   senza informazioni, senza accesso al conto per pagare le bollette, bloccato dalla banca. È
   forte nelle coppie in cui uno solo gestisce le finanze. **~40%**
2. **Mi sento a disagio e confusa davanti al mondo digitale**: password, email, PIN, account
   che si chiudono. Chi mi resta non saprà entrare né sapere *quali* account esistono (*"Welche
   Kundennummer/welche Email wurde da nochmal verwendet? \*grillenzirpen\*"*, figlio di un
   padre di 70 anni). **~35%**
3. **Temo che decidano estranei o lo Stato invece della mia famiglia**: rechtliche Betreuung,
   *"ein Fremder als Betreuer"* (Stiftung Warentest), settimane o mesi di attesa e costi. **~25%**

---

## 4. Punto di verifica
- 5 desideri primari ✓
- 3 driver emotivi per desiderio, 15 in totale ✓
- Tutti i desideri sono risultati vissuti dal cliente o dai suoi beneficiari, non
  caratteristiche del prodotto ✓
  - Scartati come requisiti di prodotto: "leicht zu verstehen", "einfache Handhabung",
    "juristisch wasserdicht" come qualità del modulo, "analog und digital".
- Citazioni testuali con il tipo di fonte ✓

---

## 5. Segnali utili fuori dai 5 desideri (per i passi successivi)

**Obiezioni ricorrenti (barriere, non desideri):**
- *"…oder gibt's dafür was Digitales, das nicht nach Abzocke aussieht?"* (post da 308 voti)
- Il thread su Tecis (39 voti, commenti fino a 114 voti) mostra che in Germania il
  "Notfallordner" è **usato come esca dai consulenti finanziari del Strukturvertrieb**, e c'è
  diffidenza.
- *"Es gibt genug Vorlagen im Netz"*, e le versioni gratuite di comuni ed enti pubblici sono
  diffuse.
- Sicurezza: *"Dieses Buch wäre für Einbrecher Gold wert."*

**Candidato emerso ma non in top 5:** lasciare ricordi e storia di famiglia. Ne parla un
figlio: *"…die persönlichen Sachen und Familiengeschichten, die irgendwann niemand mehr erzählen
kann"*. È collegato alla lettera "in caso succeda qualcosa" del kit. Pochi segnali (2 voci).

**Stereotipo da evitare (e da ribaltare):** il thread da 1.124 voti "Finanzielle Verwahrlosung…
von Rentnern" mostra come i figli 30-40enni vedono i genitori anziani: "Übersicht über die
Verträge Null". Un angolo possibile per Barb è l'orgoglio di **non essere quel genitore**.
È un'ipotesi da validare.

**Trigger d'acquisto osservati:**
- un quasi-incidente;
- un'operazione imminente;
- un lutto nella cerchia vicina (Deutsche Bank: 39% malattia grave di un familiare, 28%
  decesso);
- la morte di un genitore, che porta a "nochmal mache ich das nicht mit".

---

## Fonti principali
- Reddit, dataset Apify `xwNNOnUlCe0f3uNTf` (post), `MkN7RpDeUYICvglSB` e `ClHHq1MRw676yKQ3I`
  (commenti). Vedi il manifest in `reddit-raw/`
- [Digistore24 #457702 (Jansen)](https://www.digistore24.com/product/457702),
  [#457703](https://www.digistore24.com/product/457703),
  [#698950 "Der Gelbe Notfallordner"](https://www.digistore24.com/product/698950)
- [Payhip "Vorsorge-Komplettpaket Familie"](https://payhip.com/b/nNEfX)
- [leaveitsorted.com](https://leaveitsorted.com)
- [Trustpilot Afilio](https://uk.trustpilot.com/review/afilio.de),
  [Trustpilot meinlebensordner](https://de.trustpilot.com/review/meinlebensordner.de),
  [LovelyBooks VorsorgePlaner](https://www.lovelybooks.de/autor/Otto-N.-Bretzinger/Der-VorsorgePlaner-14142833052-w/)
- [Deutsche Bank: Erben und Vererben 2024](https://www.db.com/news/detail/20241126-deutsche-bank-studie-erben-und-vererben-2024),
  [Nordkurier/dpa sullo stesso studio](https://www.nordkurier.de/wirtschaft/grosse-summen-grosse-sorgen-tabuthema-erbschaft-3110621)
- [Commerzbank: studio 55+ (2024)](https://commerzbank.de/konzern/newsroom/pressemitteilungen/2024/20240611-pm-vermoegen-sichern.pdf)
- [Cash/forsa-Central: Vorsorgevollmacht](https://www.cash-online.de/a/deutsche-schlecht-auf-den-pflegefall-vorbereitet-203597/)
- [Aeternitas/Infratest 2005](https://www.aeternitas.de/fileadmin/user_upload/Meinungsforschung/Bis_2022/2005_trauerfall-vorsorge.pdf)
- [Stiftung Warentest: Vorsorge-Set oltre 1 milione](https://www.test.de/presse/pressemitteilungen/Vorsorge-Set-knackt-Millionen-Auflage-Fuer-den-Ernstfall-vorsorgen-mit-praktischen-Infos-und-Formularen-6098746-0/)
- [Kreis SÜW: Vorsorgeordner](https://www.wochenblatt-reporter.de/landau/c-lokales/neuer-vorsorgeordner-im-kreis-suew-wo-seniorinnen-und-senioren-ihn-bekommen_a830909),
  [Erlangen: Notfallordner](https://erlangen.de/en/aktuelles/der-neue-notfallordner-ist-da)
- [Apotheken Umschau](https://www.apotheken-umschau.de/familie/freizeit-alltag/recht-finanzen-familie/notfallordner-erstellen-was-fuer-den-ernstfall-hineingehoert-1446851.html),
  [LV1871](https://www.lv1871.de/magazin/gesundheit/notfallordner/),
  [bankdaten.de](https://www.bankdaten.de/ratgeber/bankunterlagen-fuer-angehoerige-vorbereiten.html)
