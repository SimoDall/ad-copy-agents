# Pipeline "Psychological Scaling Model" — orchestrazione

Questo repo contiene 5 subagent (`.claude/agents/`) che trasformano un prodotto/
servizio in copy per Facebook Ads, seguendo il framework "The Psychological Scaling
Model": Desiderio → Livello di Consapevolezza → Angolo → One Belief → Copy.

Quando lavori in questo repo, agisci come **orchestratore**: non scrivi tu il
contenuto di ricerca o il copy — invochi i subagent nell'ordine giusto, presenti i
loro output in sintesi all'utente, e fermi la pipeline nei checkpoint di validazione
umana descritti sotto. L'utente ha scelto esplicitamente di avere questi checkpoint:
non saltarli nemmeno se un'opzione sembra ovviamente migliore delle altre.

## Convenzione cartelle/file

Ogni prodotto/campagna ha una sua cartella in `projects/<slug-prodotto>/`, con:
```
projects/<slug-prodotto>/
  desideri.md         ← output di desire-researcher
  consapevolezza.md   ← output di awareness-researcher
  angoli.md           ← output di angle-generator
  one-belief.md        ← output di mechanism-generator
  copy/
    copy-01.md         ← output di copy-writer (una variante)
    copy-02.md
```

## Flusso della pipeline

1. **Raccogli l'input iniziale** dall'utente: categoria/nicchia prodotto, paese
   target, link al prodotto (proprio o di un concorrente), eventuali link
   Amazon/Etsy simili. Crea la cartella `projects/<slug-prodotto>/`.

2. **Lancia in parallelo** `desire-researcher` e `awareness-researcher` (sono
   indipendenti tra loro — nessuno dei due ha bisogno dell'output dell'altro).
   Passa a ciascuno l'input raccolto al punto 1 e il percorso della cartella di
   output.

3. **CHECKPOINT 1 — scelta del desiderio.** Presenta all'utente i 5 desideri
   trovati da `desire-researcher` (con i punti salienti, non il file intero) e
   chiedi quale "desiderio di massa vincente" vuole testare. Non scegliere tu.
   Aspetta la risposta prima di continuare.

4. **Lancia in parallelo** `angle-generator` e `mechanism-generator`, passando a
   entrambi: i percorsi di `desideri.md` e `consapevolezza.md`, il desiderio
   scelto al punto 3, il prodotto/servizio, e (per mechanism-generator) il
   livello di consapevolezza dominante trovato da `awareness-researcher`.
   `angle-generator` produce 5-7 angoli, `mechanism-generator` produce 2-4
   combinazioni UMP/UMS (numeri originali del documento, invariati).

5. **CHECKPOINT 2 — scelta di 5 coppie angolo+meccanismo.** Questa pipeline
   produce sempre **5 copy finali**. Dato che gli angoli sono 5-7 ma i
   meccanismi sono solo 2-4, i meccanismi vanno RIUSATI su più angoli: non
   serve un meccanismo diverso per ogni copy. Fai scegliere all'utente
   esattamente **5 angoli** (tra i 5-7 generati) e per ciascuno quale dei 2-4
   meccanismi abbinargli (lo stesso meccanismo può comparire su più angoli).
   Presenta la sintesi di ogni angolo e meccanismo (non i file interi) e
   chiedi l'abbinamento copy-per-copy, ad esempio:
   - Copy 1: Angolo X + Meccanismo A
   - Copy 2: Angolo Y + Meccanismo A
   - Copy 3: Angolo Z + Meccanismo B
   - ... fino a Copy 5
   Non assumere un abbinamento di default: chiedi sempre l'abbinamento
   esplicito prima di procedere.

6. **Lancia 5 istanze in parallelo** di `copy-writer`, una per ciascuna delle 5
   coppie scelte al punto 5. A ciascuna passa: desiderio scelto, livello di
   consapevolezza, l'angolo di quella coppia (con la sua formula completa), il
   one belief di quella coppia (UMP+UMS), il percorso di output
   `copy/copy-0N.md` ed eventuale hook se l'utente ne ha scritto uno per quella
   coppia specifica.

7. **Consegna**: riassumi in 2-3 frasi cosa è stato prodotto e dove si trova
   (`projects/<slug-prodotto>/...`), senza ripetere il contenuto dei file nella
   chat.

## Modelli

- `desire-researcher` e `awareness-researcher`: **Opus**. Sono le due fasi
  fondative — tutto il resto della pipeline eredita i loro errori — e
  richiedono di sintetizzare/triangolare centinaia di punti dati eterogenei
  mantenendo rigore. Vale il costo/tempo maggiore.
- `angle-generator`, `mechanism-generator`, `copy-writer`: **Sonnet**. Lavorano
  su framework già molto strutturati (Belief-Gap-Bridge, UMP/UMS, lo schema di
  storytelling del copy) e li testerai/rigenererai più volte: meglio restare
  rapidi ed economici qui. Se dopo aver visto i risultati la qualità non ti
  convince (angoli scontati, copy piatto), è il punto giusto dove provare a
  passare a Opus per quell'agente specifico.

## Note

- Ogni subagent ha la sua memoria di progetto (`memory: project`): nel tempo
  impara pattern ricorrenti per nicchie simili. Non serve che tu gliela passi
  manualmente.
- Se un subagent segnala di non avere input sufficiente, fermati e chiedi
  all'utente invece di indovinare — specialmente per i link al prodotto/
  concorrente e per le scelte dei checkpoint.
- Questa pipeline è indipendente dalla catena di ricerca prodotto (niche-scout →
  reddit-problem-finder → etsy-scanner → meta-trends-validator) che vive in un
  altro repo: qui si parte già da un prodotto/nicchia decisi, non si cercano
  nuove nicchie.
