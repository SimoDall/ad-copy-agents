# Manifest run Reddit (Apify harshmaur/reddit-scraper)

- Data run: 2026-10-16 (UTC 05:21 → 05:30)
- Run ID: X8fi5ZG9YwQGfduz5 — status SUCCEEDED
- Dataset ID: 4kebTToIibstJ4mgV (2.427 item, ~8,7 MB) — dati grezzi NON salvati nel repo
  (il connettore restituisce i dati solo come risposta, non come file; il dataset
  resta su Apify, ma le storage non nominate vengono cancellate dopo il periodo di retention)
- Costo stimato: ~$5 (da compute units 0,076 e listino dichiarato, non dalla fattura)

## Configurazione usata
- searchTerms (10): what to do when a parent dies · how to find my parent's bank accounts ·
  parents won't talk about finances · parent passed away no passwords ·
  dealing with parents finances estate planning · help my parents get organized ·
  aging parent financial organization · how to help elderly parent plan for death ·
  wish I had organized my parents documents · dad won't talk about his will
- searchPosts: true · searchComments: true (maxCommentsCount 50 per keyword)
- searchSort: relevance · searchTime: year · maxPostsCount: 20 per keyword
- crawlCommentsPerPost: true · maxCommentsPerPost: 10
- maxTotalChargeUsd: 8

## Campi richiesti (da estrarre)
title, body, bodyHtml, createdAt, upVotes, score, commentsCount + dataType, searchTerm, postUrl

## Note di qualità
- Ricerca molto rumorosa: sul campione di 3 item, risultati fuori tema (caso di lavoro,
  true crime, caso di minori). Il filtro per rilevanza va fatto in fase di analisi.
