# Manifest run Reddit: run piccolo da 1 € (esito: NON utilizzabile)

- Data: 2026-10-16 (UTC 07:11 → 07:12)
- Run ID: oo9nLrhhmjhl9dncW — SUCCEEDED
- Dataset ID: bU6jH1KFOCq6HYIJe — 407 item al momento della lettura
  (il run aveva dichiarato 374: il numero è cresciuto dopo la chiusura del run)
- Costo: basso (compute units 0,0056, tetto di spesa $1)

## Configurazione
- searchTerms (10, generate per la nicchia):
  how to get my parents to organize their finances · parents not sharing bank account passwords ·
  how do I find out what my dad owns · help my mom with her estate paperwork ·
  how to talk to parents about their will · parents refuse to write down passwords ·
  where do I find my parents important documents · adult child guide to helping aging parents with finances ·
  wish my parents had a list of accounts · what to do if mom cannot access her bank account
- searchPosts: true · searchComments: false · searchSort: top · searchTime: year
- maxPostsCount: 5 per keyword · crawlCommentsPerPost: true · maxCommentsPerPost: 10

## Esito
- Problema principale: searchSort "top" fa emergere post virali e fuori tema (gatti, politica, cronaca,
  serie TV, post di relazioni). Su circa 45 post letti, solo 1 è vicino al tema
  ("my parents removed me from their will").
- I commenti raccolti appartengono quasi tutti a quei post fuori tema: quindi non sono utili all'analisi.
- Il run precedente con searchSort "relevance" (manifest precedenti) aveva risultati molto più pertinenti
  (es. r/GriefSupport, r/personalfinance).

## Decisione proposta
- Tornare a searchSort "relevance" per la ricerca, e filtrare per voti dopo la raccolta.
- Affinare le keyword: frasi più specifiche su conti, documenti, testamento, password.
