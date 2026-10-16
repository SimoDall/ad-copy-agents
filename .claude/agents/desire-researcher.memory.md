# Memoria progetto — desire-researcher

## Nicchia: digital estate-planning / family emergency organizer come REGALO (pubblico "Figli"/Dana, USA)
Progetto: `projects/family-handover-folder-figli/` (Leave It Sorted / The Thoughtful Gift Bundle).

### 5 desideri di massa stabili (saturano in fretta, re-validati su 2 run)
1. "Voglio sapere dove trovare tutto se succede qualcosa." (un solo posto: conti/password/documenti)
2. "Voglio sollevare il discorso senza offenderli o litigare." (blocco RELAZIONALE, non informativo — driver dominante)
3. "Voglio vivere il lutto senza restare intrappolata nella burocrazia." (conti congelati, probate 3-6 mesi)
4. "Voglio smettere di avere quell'ansia di sottofondo." (peace of mind; ricerca da panico "2am")
5. "Voglio essere pronta senza prendere il controllo dei miei genitori." (permesso psicologico; rispetto autonomia)
- Conflitto tra fratelli = driver secondario dentro #1/#3/#4, NON sesto desiderio.
- Linguaggio da riusare: "one place", "peace of mind", "I didn't know where anything was", "I just wanted to be ready", "without taking over", "months, not days". Da EVITARE: death/funeral/end of life/when I'm gone.
- Distinguere SEMPRE profilo Dana (figlia in preparazione, genitore vivo) da post post-lutto: le keyword "what to do when a parent dies / parent passed away / how to help elderly parent plan for death" pescano in prevalenza fuori profilo; usarle solo per documentare il "dolore futuro" dietro #1/#3.

### Pattern ambiente/strumenti (IMPORTANTE per run futuri)
- **Reddit è la fonte più preziosa ma la più fragile.** In questa infrastruttura è ricorrentemente INACCESSIBILE: www/old.reddit → 403, pullpush → irraggiungibile, WebFetch su reddit.com → "unable to fetch".
- **Scraper Apify fisso (`harshmaur/reddit-scraper`): verificare SUBITO che i tool MCP siano realmente esposti.** Nel run 2026-10-16 il server `apify-reddit-scraper` risultava "connesso" ma NON offriva alcun tool (`harshmaur--reddit-scraper`, `get-actor-run`, `call-actor` → "server connected but does not offer this tool here"). Nessun `APIFY_TOKEN` in env (API → 401), Agent Reach assente (command not found). Risultato: 0 post/0 commenti, $0, nessun run.
  - Prima di promettere dati Reddit: fare un probe rapido dei tool MCP + `printenv APIFY_TOKEN`. Se entrambi mancano, dichiarare subito il blocco e non rilanciare.
- Fonti accessibili affidabili per questa nicchia: blog advisor/estate-planning (Greenbush, Commerce Bank, Synchrony, Savant, Kiplinger, Next Avenue), colonne "questions to ask your parents", recensioni Etsy MadeSimpleUS + Nokbox (Loox) + Walmart + Goodreads, guide "track down accounts when a parent dies" (Elayne, Adams Brown, Fidelity CA). Volume realistico ~70-95 voci, lontano dal target 700-1000 del prompt.
- Le percentuali dei driver sono rimaste STIME in entrambi i run: le frequenze contate dipendono dallo sblocco Apify/Reddit, ancora da ottenere.
