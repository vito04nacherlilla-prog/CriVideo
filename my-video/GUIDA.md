# 🍞 Focaccia Barese — Video Reel (9:16)

Progetto [Remotion](https://remotion.dev) per montare un video verticale virale
sulla vera focaccia barese, partendo dalle clip girate dal tuo amico.

Il video è **guidato dai dati**: tutta la struttura (scene, ordine, durate, testi,
trucchi) vive in un unico file, `src/lib/scenes.ts`. Non serve toccare il codice
grafico per cambiare il montaggio.

---

## 1. Avviare l'anteprima

```bash
cd my-video
npm run dev        # apre Remotion Studio su http://localhost:3000
```

Nello Studio vedi la composizione **FocacciaBarese** e puoi scrubbare la timeline.

## 2. Aggiungere le clip del tuo amico

1. Copia i file video dentro `public/videos/` (es. `impasto.mp4`, `stesura.mp4`…).
2. Apri `src/lib/scenes.ts` e su ogni scena imposta il campo `src`:

```ts
{
  id: "impasto",
  kind: "step",
  src: "videos/impasto.mp4",   // ← qui il tuo file
  clipStartInSeconds: 2,        // (opzionale) taglia i primi 2s della clip
  ...
}
```

Finché `src` è `undefined` la scena mostra un **placeholder** ("clip mancante"),
così puoi montare la struttura anche prima di avere tutti i video.

> Formato consigliato per il verticale: clip **1080×1920** (9:16). Se le clip
> sono orizzontali vengono ritagliate al centro (`objectFit: cover`).

## 3. Modificare storyboard, testi e trucchi

Sempre in `src/lib/scenes.ts`:

- **Ordine del video** = ordine dell'array `SCENES`. Sposta gli oggetti per
  riordinare, cancellane uno per toglierlo, duplicane uno per aggiungerlo.
- `durationInSeconds` → quanto dura la scena.
- `kicker` / `title` / `subtitle` → testi in sovraimpressione.
- `tip` → la "chicca" virale nel badge giallo 💡.
- La **durata totale** e la **barra di avanzamento** si ricalcolano da sole.

## 4. Tipi di scena disponibili

| `kind`        | A cosa serve                                    |
|---------------|-------------------------------------------------|
| `hook`        | Apertura d'impatto (primi 3s), titolo enorme    |
| `ingredients` | Lista ingredienti animata                       |
| `step`        | Passaggio della ricetta con badge + chicca      |
| `result`      | Il risultato finale / il morso croccante        |
| `outro`       | Chiusura + call to action (segui / salva)       |

## 5. Renderizzare il video finale

```bash
npx remotion render FocacciaBarese out/focaccia.mp4
```

> ⚠️ In questo ambiente cloud il download automatico di Chromium è bloccato.
> Se il render fallisce, usa il Chromium già presente:
>
> ```bash
> npx remotion render FocacciaBarese out/focaccia.mp4 \
>   --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
> ```

---

## Struttura del codice

```
src/
  lib/
    scenes.ts        ← STORYBOARD (modifica qui il montaggio)
    theme.ts         ← colori e font
  components/
    ClipLayer.tsx    ← player video + placeholder
    Overlays.tsx     ← titoli, badge, chicche, barra avanzamento, animazioni
  scenes/
    HookScene.tsx  IngredientsScene.tsx  StepScene.tsx
    ResultScene.tsx  OutroScene.tsx
  FocacciaVideo.tsx  ← assembla le scene in sequenza
  Composition.tsx    ← registra la composizione (formato 1080×1920, 30fps)
```

## Prossimi passi

1. **Inserire le clip** vere e sistemare tagli/durate scena per scena.
2. **Musica**: mettere una traccia in `public/audio/` e aggiungere un
   `<Audio>` in `FocacciaVideo.tsx`.
3. **Copy & voce**: quando la struttura è definitiva, scriviamo il testo dello
   speakeraggio per ogni scena e lo registriamo come voce fuori campo.
