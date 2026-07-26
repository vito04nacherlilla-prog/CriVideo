// ============================================================================
// STORYBOARD — La vera Focaccia Barese (Reel verticale 9:16)
// ----------------------------------------------------------------------------
// Ricetta reale (dall'audio dello chef):
//   Impasto: 500 g acqua · 25 g lievito · 10 g zucchero · 100 g olio EVO ·
//            400 g farina 0 · 550 g semola · 30 g sale (a impasto grezzo)
//   Panetti da 350 g → in teglia con olio abbondante → stesura →
//   pomodoro a grappolo a pezzetti · olive · origano · sale · olio EVO →
//   lievita 1 ora → forno 220°C per 15 minuti.
//
// STILE: caldo e grintoso, dinamico. Per ora SENZA voce: il testo racconta.
// Ritmo volutamente più lento così ogni scritta si legge bene.
//
// `clipDurationInSeconds` = durata reale della clip: serve a rallentarla
// automaticamente (slow-motion) per riempire scene più lunghe senza scatti.
// ============================================================================

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;
export const TRANSITION_FRAMES = 10; // sovrapposizione fra scene

export type SceneKind = "hook" | "ingredients" | "step" | "result" | "outro";

export type Scene = {
  id: string;
  kind: SceneKind;
  src?: string;
  durationInSeconds: number;
  clipDurationInSeconds?: number;
  clipStartInSeconds?: number;
  kicker?: string;
  title?: string;
  subtitle?: string;
  tip?: string;
  list?: { label: string; value?: string }[];
  listFooter?: string;
};

export const SCENES: Scene[] = [
  // 0. HOOK ------------------------------------------------------------------
  {
    id: "hook",
    kind: "hook",
    src: "videos/hero-morso.mp4",
    clipDurationInSeconds: 5.1,
    durationInSeconds: 3.5,
    title: "FOCACCIA\nBARESE",
    subtitle: "la ricetta vera, dei fornai",
  },

  // 1. INGREDIENTI -----------------------------------------------------------
  {
    id: "ingredienti",
    kind: "ingredients",
    src: "videos/beauty-cruda.mp4",
    clipDurationInSeconds: 3.0,
    durationInSeconds: 7,
    kicker: "GLI INGREDIENTI",
    title: "L'impasto",
    list: [
      { label: "Acqua", value: "500 g" },
      { label: "Lievito di birra", value: "25 g" },
      { label: "Zucchero", value: "10 g" },
      { label: "Olio EVO", value: "100 g" },
      { label: "Farina 0", value: "400 g" },
      { label: "Semola rimacinata", value: "550 g" },
      { label: "Sale", value: "30 g" },
    ],
    listFooter: "+ pomodoro a grappolo · olive · origano",
  },

  // 2. IMPASTO — acqua, lievito, zucchero ------------------------------------
  {
    id: "impasto-1",
    kind: "step",
    src: "videos/impasto-slurry.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 5,
    kicker: "L'IMPASTO",
    title: "Si parte dai liquidi",
    subtitle: "Acqua, lievito e zucchero",
    tip: "Lievito e zucchero insieme: la lievitazione parte alla grande.",
  },

  // 3. IMPASTO — olio --------------------------------------------------------
  {
    id: "impasto-olio",
    kind: "step",
    src: "videos/impasto-olio.mp4",
    clipDurationInSeconds: 3.5,
    durationInSeconds: 4.5,
    kicker: "L'IMPASTO",
    title: "Poi l'olio",
    subtitle: "100 g di extravergine",
  },

  // 4. IMPASTO — le farine ---------------------------------------------------
  {
    id: "impasto-farine",
    kind: "step",
    src: "videos/impasto-semola.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 5,
    kicker: "L'IMPASTO",
    title: "Le due farine",
    subtitle: "400 g farina 0 + 550 g semola",
    tip: "La semola rimacinata dà colore, profumo e croccantezza.",
  },

  // 5. IMPASTO — il sale -----------------------------------------------------
  {
    id: "impasto-sale",
    kind: "step",
    src: "videos/impasto-lavora.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 5,
    kicker: "L'IMPASTO",
    title: "Il sale",
    subtitle: "30 g, quando è ancora grezzo",
    tip: "Il sale sempre a fine impasto, mai a contatto col lievito.",
  },

  // 6. IMPASTO — liscio ------------------------------------------------------
  {
    id: "impasto-liscio",
    kind: "step",
    src: "videos/impasto-liscio.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 4,
    kicker: "L'IMPASTO",
    title: "Impasta",
    subtitle: "Fino a questa consistenza",
  },

  // 7. PANETTI ---------------------------------------------------------------
  {
    id: "panetti",
    kind: "step",
    src: "videos/impasto-banco.mp4",
    clipDurationInSeconds: 2.85,
    durationInSeconds: 4.5,
    kicker: "SUL BANCO",
    title: "Forma i panetti",
    subtitle: "Da 350 g l'uno",
  },

  // 8. IN TEGLIA -------------------------------------------------------------
  {
    id: "in-teglia",
    kind: "step",
    src: "videos/panetti.mp4",
    clipDurationInSeconds: 2.1,
    durationInSeconds: 4.2,
    kicker: "IN TEGLIA",
    title: "Tanto olio sotto",
    subtitle: "Adagia i panetti nelle teglie",
    tip: "L'olio sul fondo frigge la base e la rende croccante.",
  },

  // 9. STESURA ---------------------------------------------------------------
  {
    id: "stesura",
    kind: "step",
    src: "videos/stesura.mp4",
    clipDurationInSeconds: 6.2,
    durationInSeconds: 5,
    kicker: "IN TEGLIA",
    title: "Stendi le focacce",
    subtitle: "Con le dita, senza schiacciare",
  },

  // 10. STESURA — i buchi ----------------------------------------------------
  {
    id: "stesura-dita",
    kind: "step",
    src: "videos/stesura-dita.mp4",
    clipDurationInSeconds: 3.0,
    durationInSeconds: 3.5,
    kicker: "IN TEGLIA",
    title: "I classici buchi",
    subtitle: "Affonda i polpastrelli",
  },

  // 11. CONDIMENTO — pomodoro ------------------------------------------------
  {
    id: "pomodoro",
    kind: "step",
    src: "videos/pomodorini.mp4",
    clipDurationInSeconds: 6.3,
    durationInSeconds: 4.5,
    kicker: "IL CONDIMENTO",
    title: "Pomodoro a grappolo",
    subtitle: "Tagliato a pezzettini",
    tip: "A grappolo: più dolce e succoso in cottura.",
  },

  // 12. CONDIMENTO — olive, origano, sale ------------------------------------
  {
    id: "olive",
    kind: "step",
    src: "videos/olive.mp4",
    clipDurationInSeconds: 5.6,
    durationInSeconds: 4.5,
    kicker: "IL CONDIMENTO",
    title: "Olive, origano e sale",
    subtitle: "Il profumo della Puglia",
  },

  // 13. CONDIMENTO — olio ----------------------------------------------------
  {
    id: "olio",
    kind: "step",
    src: "videos/olio.mp4",
    clipDurationInSeconds: 3.6,
    durationInSeconds: 4,
    kicker: "IL TOCCO FINALE",
    title: "Un giro d'olio EVO",
    subtitle: "Generoso, in superficie",
  },

  // 14. LIEVITAZIONE ---------------------------------------------------------
  {
    id: "lievitazione",
    kind: "step",
    src: "videos/teglie.mp4",
    clipDurationInSeconds: 3.9,
    durationInSeconds: 4,
    kicker: "LA LIEVITAZIONE",
    title: "Riposa 1 ora",
    subtitle: "Coperta, al caldo",
  },

  // 15. FORNO ----------------------------------------------------------------
  {
    id: "forno",
    kind: "step",
    src: "videos/forno.mp4",
    clipDurationInSeconds: 4.05,
    durationInSeconds: 4.5,
    kicker: "IN FORNO",
    title: "220°C · 15 minuti",
    subtitle: "Fino a doratura",
    tip: "Il colpo di calore dà la crosta dorata e i bordi croccanti.",
  },

  // 16. RISULTATO ------------------------------------------------------------
  {
    id: "risultato",
    kind: "result",
    src: "videos/hero-finale.mp4",
    clipDurationInSeconds: 4.4,
    durationInSeconds: 4,
    title: "Eccola qua.",
    subtitle: "Croccante fuori, morbida dentro.",
  },

  // 17. OUTRO ----------------------------------------------------------------
  {
    id: "outro",
    kind: "outro",
    src: "videos/hero-morso.mp4",
    clipDurationInSeconds: 5.1,
    clipStartInSeconds: 1.4,
    durationInSeconds: 3.5,
    title: "Buon appetito 🫒",
    subtitle: "Salva la ricetta e seguici",
  },
];

/** Durata totale in frame, tenendo conto delle sovrapposizioni fra scene. */
export const totalDurationInFrames = () => {
  const sum = SCENES.reduce(
    (acc, s) => acc + Math.round(s.durationInSeconds * FPS),
    0,
  );
  return sum - (SCENES.length - 1) * TRANSITION_FRAMES;
};
