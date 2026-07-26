// ============================================================================
// STORYBOARD — La vera Focaccia Barese (Reel verticale 9:16)
// ----------------------------------------------------------------------------
// Montaggio basato sulle clip reali girate in cucina (chef professionista).
// Tutto il video è guidato da questi dati:
//   - L'ordine dell'array SCENES = l'ordine nel video.
//   - `src` punta a un file in public/videos (già convertiti in MP4 verticale).
//   - Durata totale e barra di avanzamento si ricalcolano da sole.
//
// CLIP DISPONIBILI in public/videos (oltre a quelle usate qui sotto, restano
// pronte come alternative da agganciare quando vuoi):
//   impasto-acqua, impasto-mix, impasto-slurry, impasto-farina1, impasto-farina2,
//   impasto-semola, impasto-olio, impasto-lavora, impasto-liscio, impasto-banco,
//   panetti, stesura, stesura-dita, pomodorini, olive, teglie, olio,
//   beauty-cruda, forno, hero-morso, hero-finale
// ============================================================================

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

export type SceneKind =
  | "hook"
  | "ingredients"
  | "step"
  | "result"
  | "outro";

export type Scene = {
  id: string;
  kind: SceneKind;
  /** File in public/videos, es. "videos/stesura.mp4". Se assente → placeholder. */
  src?: string;
  durationInSeconds: number;
  /** Punto di start della clip in secondi (per tagliare l'inizio). */
  clipStartInSeconds?: number;
  /** Durata reale della clip: se indicata e la scena è più lunga, va in loop. */
  clipDurationInSeconds?: number;
  /** Etichetta piccola in alto, es. "L'IMPASTO". */
  kicker?: string;
  /** Titolo grande della scena. */
  title?: string;
  /** Sottotitolo / descrizione breve. */
  subtitle?: string;
  /** La "chicca" virale mostrata in un badge. */
  tip?: string;
  /** Lista (usata dalla scena ingredienti). */
  list?: { label: string; value?: string }[];
};

export const SCENES: Scene[] = [
  // ---- 0. HOOK — lo chef che morde la focaccia (primi 3 secondi) -----------
  {
    id: "hook",
    kind: "hook",
    src: "videos/hero-morso.mp4",
    durationInSeconds: 3,
    title: "LA VERA\nFOCACCIA\nBARESE",
    subtitle: "quella dei fornai, fatta in casa",
  },

  // ---- 1. INGREDIENTI (macro della focaccia condita cruda) -----------------
  {
    id: "ingredienti",
    kind: "ingredients",
    src: "videos/beauty-cruda.mp4",
    clipDurationInSeconds: 3,
    durationInSeconds: 5,
    kicker: "GLI INGREDIENTI",
    title: "Ti serve solo questo",
    list: [
      { label: "Semola rimacinata", value: "300 g" },
      { label: "Farina 0", value: "200 g" },
      { label: "Patata lessa", value: "1 media" },
      { label: "Acqua tiepida", value: "400 ml" },
      { label: "Lievito di birra", value: "7 g" },
      { label: "Olio EVO + sale", value: "q.b." },
      { label: "Pomodorini + olive", value: "q.b." },
    ],
  },

  // ---- 2. IMPASTO — olio nell'impasto --------------------------------------
  {
    id: "impasto-olio",
    kind: "step",
    src: "videos/impasto-olio.mp4",
    durationInSeconds: 3.5,
    kicker: "L'IMPASTO",
    title: "Si parte da qui",
    subtitle: "Acqua, lievito, olio e le farine",
    tip: "La patata lessa nell'impasto è il segreto: mollica soffice per giorni.",
  },

  // ---- 3. IMPASTO — lavorazione --------------------------------------------
  {
    id: "impasto-lavora",
    kind: "step",
    src: "videos/impasto-lavora.mp4",
    durationInSeconds: 3.5,
    kicker: "L'IMPASTO",
    title: "Impasto molle",
    subtitle: "Semola + farina 0, tanta acqua",
    tip: "Alta idratazione (~80%): deve restare appiccicoso, non aggiungere farina!",
  },

  // ---- 4. IMPASTO — liscio ed elastico -------------------------------------
  {
    id: "impasto-liscio",
    kind: "step",
    src: "videos/impasto-liscio.mp4",
    durationInSeconds: 3,
    kicker: "L'IMPASTO",
    title: "Liscio ed elastico",
    subtitle: "Fino a che si stacca dalle pareti",
  },

  // ---- 5. IMPASTO — sul banco ----------------------------------------------
  {
    id: "impasto-banco",
    kind: "step",
    src: "videos/impasto-banco.mp4",
    durationInSeconds: 2.8,
    kicker: "L'IMPASTO",
    title: "Si porziona",
    subtitle: "Panetti da mettere in teglia",
  },

  // ---- 6. LIEVITAZIONE (panetti nelle teglie oliate) -----------------------
  {
    id: "lievitazione",
    kind: "step",
    src: "videos/panetti.mp4",
    durationInSeconds: 2,
    kicker: "LA LIEVITAZIONE",
    title: "Ora si aspetta",
    subtitle: "Panetti in teglia ben oliata",
    tip: "Lascia raddoppiare ~2 ore: qui nasce l'alveolatura.",
  },

  // ---- 7. STESURA in teglia ------------------------------------------------
  {
    id: "stesura",
    kind: "step",
    src: "videos/stesura.mp4",
    durationInSeconds: 4.5,
    kicker: "IN TEGLIA",
    title: "Stendi con le dita",
    subtitle: "Senza schiacciare, riempi la teglia",
    tip: "Olio abbondante sul fondo: è ciò che frigge e rende la base croccante.",
  },

  // ---- 8. STESURA — i buchi con le dita ------------------------------------
  {
    id: "stesura-dita",
    kind: "step",
    src: "videos/stesura-dita.mp4",
    durationInSeconds: 3,
    kicker: "IN TEGLIA",
    title: "I classici buchi",
    subtitle: "Affonda i polpastrelli su tutta la superficie",
  },

  // ---- 9. CONDIMENTO — pomodorini ------------------------------------------
  {
    id: "pomodorini",
    kind: "step",
    src: "videos/pomodorini.mp4",
    durationInSeconds: 4.5,
    kicker: "IL CONDIMENTO",
    title: "Pomodorini",
    subtitle: "Affondali bene nell'impasto",
    tip: "Schiacciali con la buccia: rilasciano più succo e sapore in cottura.",
  },

  // ---- 10. CONDIMENTO — olive ----------------------------------------------
  {
    id: "olive",
    kind: "step",
    src: "videos/olive.mp4",
    durationInSeconds: 3.5,
    kicker: "IL CONDIMENTO",
    title: "Olive baresane",
    subtitle: "Con l'origano, quello vero",
  },

  // ---- 11. IL TOCCO — filo d'olio / emulsione ------------------------------
  {
    id: "olio",
    kind: "step",
    src: "videos/olio.mp4",
    durationInSeconds: 3.5,
    kicker: "IL TOCCO FINALE",
    title: "Un giro d'olio",
    subtitle: "Olio, un po' d'acqua e sale grosso",
    tip: "L'emulsione acqua-olio-sale: superficie lucida e croccante, cuore morbido.",
  },

  // ---- 12. COTTURA ---------------------------------------------------------
  {
    id: "cottura",
    kind: "step",
    src: "videos/forno.mp4",
    durationInSeconds: 4,
    kicker: "IN FORNO",
    title: "Forno bollente",
    subtitle: "Fino a doratura",
    tip: "250°C: il colpo di calore dà la crosta dorata e i bordi croccanti.",
  },

  // ---- 13. RISULTATO (4K, focaccia tagliata a spicchi) ---------------------
  {
    id: "risultato",
    kind: "result",
    src: "videos/hero-finale.mp4",
    durationInSeconds: 4,
    title: "Pronta.",
    subtitle: "Croccante fuori, morbida dentro.",
  },

  // ---- 14. OUTRO / CTA -----------------------------------------------------
  {
    id: "outro",
    kind: "outro",
    src: "videos/teglie.mp4",
    durationInSeconds: 3,
    title: "Salva la ricetta",
    subtitle: "Segui per la vera cucina pugliese 🫒",
  },
];

/** Durata totale del video in frame (ricalcolata dall'array SCENES). */
export const totalDurationInFrames = () =>
  Math.round(
    SCENES.reduce((sum, s) => sum + s.durationInSeconds, 0) * FPS,
  );
