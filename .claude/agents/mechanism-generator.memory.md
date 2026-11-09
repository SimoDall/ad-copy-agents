# Memoria progetto — mechanism-generator

## Nicchia: digital estate-planning / family emergency organizer come USO PERSONALE (pubblico "Barb", Germania — "Notfallordner")
Progetto: `projects/family-handover-folder-barb-de/`. Run 2026-10-29, desiderio lavorato: "Voglio che la mia famiglia trovi tutto senza cercare" (Desiderio #1), target Solution Aware (~42%).

### 4 UMP/UMS generati
1. **Il Paradosso del Nascondiglio** (L2) — ciò che è ben nascosto dai ladri è nascosto anche a chi dovrebbe trovarlo in emergenza.
2. **L'Effetto Raccoglitore Vuoto** (L2) — i modelli gratuiti dicono COSA metterci ma non COME/QUANDO, da cui l'overwhelm (non pigrizia) che lascia il raccoglitore vuoto per mesi.
3. **Il Divario tra Permesso Legale e Mappa Pratica** (L3) — una Vollmacht/testamento dice CHI può agire ma non DOVE trovare conti/contratti/password.
4. **Il Singolo Punto di Guasto della Memoria** (L2) — "gliel'ho già detto" è memoria con un solo punto di accesso; serve un sistema esterno aggiornabile.

### Insight stabili
- Priorità di test consigliata: #2 e #1 per primi (prova osservabile diretta, zero gergo legale), poi #3 (smonta la credenza più radicata/rischiosa "ho già la Vollmacht, sono a posto", ma richiede una frase in più per essere capito), #4 più adatto a storytelling emotivo in prima persona che a una headline diretta.
- Combinazione d'impatto suggerita: #1+#2 nello stesso copy (si rinforzano); #3 va tenuto isolato per non confondere i messaggi con gli altri due.
- Il Divario Legale-Pratico (#3) è lo stesso meccanismo centrale già individuato da angle-generator come Angolo 4 ("Vorsorgevollmacht e mappa pratica sono due problemi diversi") — i due agent sono arrivati in modo indipendente alla stessa intuizione, segno che è il gap più solido per questa nicchia in Germania.
- Nessun dato nuovo raccolto in questo run: tutte le prove osservabili sono citazioni/statistiche già presenti in desideri.md/consapevolezza.md (Agent Reach non disponibile in questa sessione, niente scraping Reddit aggiuntivo).

### Pattern ambiente/strumenti
- Il subagent (eseguito come general-purpose con le istruzioni di mechanism-generator.md) non ha accesso a uno strumento di memoria proprio: questo file viene mantenuto dall'orchestratore sulla base del riepilogo restituito a fine run.
- Agent Reach (`agent-reach` via Bash) non installato in questa sessione — se serve scraping Reddit dedicato in run futuri su questo subagent, verificare prima la disponibilità.

---

## Nicchia: digital estate-planning / family emergency organiser per genitori anziani — mercato USA (Leave It Sorted)
Progetto: `projects/leave-it-sorted-usa/`. Run 2026-11-09, desiderio lavorato: "Voglio lasciare tutto in un unico posto, pronto da trovare" (Desiderio #1), target Problem Aware (~34%, dominante; mercato a cavallo Problem/Solution Aware ~64% combinato).

### 4 UMP/UMS generati
1. **Il Punto Unico di Guasto / The Single Point of Failure** (L2) — l'handover verbale ("gliel'ho già detto") fallisce perché l'informazione vive in una sola testa, senza copia di backup.
2. **La Trappola del Raccoglitore Vuoto / The Empty Binder Trap** (L2) — il binder DIY fallisce per blank-page overwhelm (nessuno dice cosa scrivere dove), non per pigrizia; il Kit risolve con 21 sezioni pre-etichettate e numerate.
3. **Il Bersaglio Mobile / The Moving Target** (L3) — anche chi ha già organizzato tutto una volta non è al sicuro: le informazioni invecchiano silenziosamente (conti chiusi, password cambiate); leva sugli "aggiornamenti gratuiti a vita" del prodotto.
4. **Il Vuoto tra Permesso e Posizione / The Permission-vs-Location Gap** (L3) — il testamento dice CHI eredita, non DOVE si trova ciò che eredita; riformulazione propria del fatto di mercato condiviso "will ≠ plan" (il competitor myestatekit.co.uk lo usa come ad #7, ma è anche già un argomento sul sito stesso di Leave It Sorted — non è proprietà del competitor).

### Vincolo competitor rispettato
Nessuno dei 4 meccanismi riusa nomi/linguaggio di myestatekit.co.uk (5-28-6, Secure/Notify/Settle, "references only never passwords", trappole delle 5 telefonate, buco di 28 giorni, 7 porte, 19 organizzazioni, 26 documenti come framing pubblicitario). Il mechanism #4 tocca lo stesso fatto di mercato "will ≠ plan" del competitor ma con analogia propria (busta/indirizzo) e focus ristretto alla LOCALIZZAZIONE (non alla sequenza operativa Secure/Notify/Settle).

### Insight stabili
- Priorità di test consigliata: #2 (Raccoglitore Vuoto) prima — prova osservabile fortissima, colpisce chi ha già provato quaderni Etsy/Amazon; poi #1 (Punto Unico di Guasto) per storytelling emotivo in prima persona; poi #4 (Permesso vs Posizione) per smontare l'obiezione "abbiamo già il testamento"; #3 (Bersaglio Mobile) ultimo, da riservare a un pubblico già esposto al brand (richiede che il lettore si senta "già a posto" per colpire bene).
- Combinazione d'impatto: #1+#2 nello stesso copy si rinforzano (doppia causa del caos: nessun backup + nessuna struttura). #4 va tenuto isolato dagli altri per non diluire il messaggio di smontaggio obiezione.
- Le soluzioni fallite più citate nella ricerca (DIY binder 24%, handover verbale 16%, testamento-come-se-bastasse 15% — somma ~55% delle menzioni totali in consapevolezza.md) cadono tutte nell'area "localizzazione/centralizzazione", confermando che il Desiderio #1 è il più ricco di materiale per questo prodotto.
- Gap di conoscenza trasversale individuato (poco sfruttato dal competitor): l'idea che "organizzare" sia un'azione con un punto di arrivo, non un sistema da mantenere — alla base sia del meccanismo #2 (mai iniziato) sia del #3 (iniziato ma invecchiato).
- Se in run futuri su questo stesso prodotto si lavora sugli altri desideri (#2 soldi/conti persi, #3 accesso digitale, #4 un pomeriggio, #5 non lasciare un peso), generare meccanismi nuovi e distinti da questi 4, mantenendo lo stesso vincolo sul nome/linguaggio della soluzione.

### Pattern ambiente/strumenti
- Agent Reach non configurato anche in questa sessione (comando `agent-reach` non trovato). Ricerca aggiuntiva via WebSearch mirato sui gap di conoscenza specifici, a complemento dei documenti `desideri.md`/`consapevolezza.md` già molto ricchi di citazioni verbatim per questo prodotto.
