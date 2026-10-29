# Manifest run Reddit: Notfallordner DE, pubblico Barb

- Data: 2026-10-29 (UTC 05:54 → 05:56)
- Scraper: Apify `harshmaur/reddit-scraper`, via `mcp__apify-reddit-scraper__call-actor`
- Lingua delle keyword: TEDESCO (override per mercato non anglofono)

## Run

| Passo | Run ID | Dataset ID | Stato | Item letti |
|---|---|---|---|---|
| A, ricerca post | YUopucnh3ib23Peb3 | xwNNOnUlCe0f3uNTf | SUCCEEDED | 96 post |
| B1, commenti (20 post) | 9xki53IWAcAFpqgT8 | MkN7RpDeUYICvglSB | SUCCEEDED | 205 item (31 al primo controllo, poi cresciuti) |
| B2, commenti (16 post, ripetizione) | RdJZY43svxYUSoVO3 | ClHHq1MRw676yKQ3I | SUCCEEDED | 167 item |

Dopo aver unito B1 e B2 e tolto i doppioni: **22 post, 219 commenti distinti** (fino a 10 per post).

## Costo e deviazioni dalla procedura (dichiarate)
- Il tool non mostra il costo in USD, solo le compute unit (circa 0,001 CU per run).
  Stima con circa 470 item a pagamento: **$0,5–1,0**. Non è verificata.
- **Deviazione 1.** Al primo controllo il dataset B1 mostrava solo 31 item, cioè 4 post su 20.
  Ho quindi lanciato B2 sui 16 post che sembravano mancanti, con tetto di $0,5. Più tardi B1 è
  arrivato a 205 item: il dataset era ancora in scrittura, come era già successo nel run del
  2026-10-16. **B2 è quindi in gran parte un duplicato.** I tetti impostati sommano $1,75
  (0,3 + 0,95 + 0,5), oltre il budget di $1. La spesa reale stimata resta sotto $1, ma non posso
  verificarla. Prossima volta: dopo il passo B rileggere `get-actor-run` prima di rilanciare.
- **Deviazione 2.** In B2 sono finiti per errore 2 post fuori tema ("Habt ihr eine Notfallroutine?",
  r/Weibsvolk, su una ferita domestica; "Werdende Eltern…", r/Finanzen). Sono stati scartati dall'analisi.
- **Selezione nel passo A.** Molte keyword avevano meno di 5 post pertinenti, quindi ho preso tutti
  quelli pertinenti (20 in totale) invece di 5 per keyword.

## Parametri
- Passo A: `searchPosts` true, `searchComments` false, `searchSort` "relevance", `searchTime` "year",
  `maxPostsCount` 10, `crawlCommentsPerPost` false, `withinCommunity` "", `includeNSFW` false,
  `maxTotalChargeUsd` 0,3, `waitSecs` 45
- Passo B: `searchTerms` [], `startUrls` dei post scelti, `crawlCommentsPerPost` true,
  `maxCommentsPerPost` 10, `maxTotalChargeUsd` 0,95 (B1) e 0,5 (B2), `waitSecs` 45

## Keyword (10) e conteggi

| Keyword | Post nel passo A | Pertinenti selezionati |
|---|---|---|
| Notfallordner anlegen Tipps | 9 | 1 (Tecis/Notfallordner). Gli altri parlano di Notarzt, Ausländerbehörde, prepper |
| was müssen meine Kinder wissen wenn mir etwas passiert | 10 | 1 ("Was sollte man über seine Eltern wissen…"). Gli altri parlano di figli piccoli |
| Vorsorgevollmacht Patientenverfügung wo anfangen | 10 | 4 |
| Unterlagen ordnen für den Todesfall | 9 | 1 (Sparbuch). Gli altri sono in inglese o di genealogia |
| digitaler Nachlass Passwörter Angehörige | 10 | 1 (padre di 70 anni). I thread in inglese di r/AgingParents sono esclusi perché fuori mercato |
| Testament schreiben was muss ich beachten | 10 | 3 |
| Vorsorge regeln mit 60 | 10 | 0 (tutti su previdenza e investimenti) |
| Hinterbliebene Chaos Konten Versicherungen nicht gefunden | 10 | 2 |
| Notfallmappe Vorlage Erfahrungen | 8 | 3 |
| Bestattungsvorsorge sinnvoll Kinder entlasten | 10 | 4 |
| **Totale** | **96** | **20** (76 scartati come fuori tema, il 79%) |

Subreddit dei post selezionati: r/Finanzen, r/de_EDV, r/FinanzenGER, r/KeineDummenFragen,
r/LegaladviceGerman, r/Ratschlag, r/medizin, r/strukki_leaks, r/Erben, r/Austria.

## Commenti per post (dopo la deduplica)
I commenti sono un campione: fino a 10 per post, ordinati da me per `commentUpVotes`. Non sono i
10 più votati dell'intero thread. Dei 219 commenti, **circa 95 sono pertinenti** ai desideri; gli
altri sono fuori tema o polemici, per esempio lo sfogo generazionale sui pensionati o il dibattito
sui servizi funebri.

I dati grezzi restano nei dataset Apify elencati sopra.
