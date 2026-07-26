// ============================================================================
// STORYBOARD — La vera Focaccia Barese (Reel verticale 9:16)
// Stile: video food professionale da TikTok. Didascalie ricche + emoji.
// Stacchi ammorbiditi da una micro-dissolvenza (niente tagli netti).
// ----------------------------------------------------------------------------
// Ricetta reale (dall'audio dello chef):
//   Impasto: 500 g acqua · 25 g lievito · 10 g zucchero · 100 g olio EVO ·
//            400 g farina 0 · 550 g semola · 30 g sale (a impasto grezzo)
//   Panetti da 350 g → in teglia con olio abbondante → stesura →
//   pomodoro a grappolo a pezzetti · olive · origano · sale · olio EVO →
//   lievita 1 ora → forno 220°C per 15 minuti.
// ============================================================================

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;
export const TRANSITION_FRAMES = 8; // micro-dissolvenza tra le scene (~0,27s)

export type SceneKind = "hook" | "ingredients" | "step" | "result";

export type Scene = {
  id: string;
  kind: SceneKind;
  src?: string;
  bgImage?: string;
  durationInSeconds: number;
  clipDurationInSeconds?: number;
  clipStartInSeconds?: number;
  emoji?: string;
  title?: string;
  subtitle?: string;
  list?: { label: string; value?: string }[];
  listFooter?: string;
};

export const SCENES: Scene[] = [
  // 0. HOOK -----------------------------------------------------------------
  {
    id: "hook",
    kind: "hook",
    src: "videos/hero-morso.mp4",
    clipDurationInSeconds: 5.1,
    durationInSeconds: 3.2,
    title: "FOCACCIA\nBARESE",
    subtitle: "la ricetta vera dei fornai",
  },

  // 1. INGREDIENTI (sfondo immagine fissa) ----------------------------------
  {
    id: "ingredienti",
    kind: "ingredients",
    bgImage: "images/ricetta-bg.jpg",
    durationInSeconds: 7,
    emoji: "📝",
    title: "Ingredienti",
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

  // 2. IMPASTO — acqua ------------------------------------------------------
  {
    id: "impasto-acqua",
    kind: "step",
    src: "videos/impasto-acqua.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 3.5,
    emoji: "💧",
    title: "L'acqua",
    subtitle: "500 g nella planetaria",
  },

  // 3. IMPASTO — lievito e zucchero -----------------------------------------
  {
    id: "impasto-lievito",
    kind: "step",
    src: "videos/impasto-slurry.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 3.5,
    emoji: "🫧",
    title: "Lievito e zucchero",
    subtitle: "25 g + 10 g",
  },

  // 4. IMPASTO — olio -------------------------------------------------------
  {
    id: "impasto-olio",
    kind: "step",
    src: "videos/impasto-olio.mp4",
    clipDurationInSeconds: 3.5,
    durationInSeconds: 3.5,
    emoji: "🫒",
    title: "L'olio EVO",
    subtitle: "100 g",
  },

  // 5. IMPASTO — farina 0 ---------------------------------------------------
  {
    id: "impasto-farina",
    kind: "step",
    src: "videos/impasto-farina1.mp4",
    clipDurationInSeconds: 4.5,
    durationInSeconds: 3.5,
    emoji: "🌾",
    title: "Farina 0",
    subtitle: "400 g",
  },

  // 6. IMPASTO — semola -----------------------------------------------------
  {
    id: "impasto-semola",
    kind: "step",
    src: "videos/impasto-semola.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 3.5,
    emoji: "🌾",
    title: "Semola rimacinata",
    subtitle: "550 g",
  },

  // 7. IMPASTO — sale -------------------------------------------------------
  {
    id: "impasto-sale",
    kind: "step",
    src: "videos/impasto-lavora.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 4,
    emoji: "🧂",
    title: "Il sale",
    subtitle: "30 g, a impasto grezzo",
  },

  // 8. IMPASTO — liscio -----------------------------------------------------
  {
    id: "impasto-liscio",
    kind: "step",
    src: "videos/impasto-liscio.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 3.5,
    emoji: "👐",
    title: "Impasta",
    subtitle: "fino a che è liscio",
  },

  // 9. PANETTI --------------------------------------------------------------
  {
    id: "panetti",
    kind: "step",
    src: "videos/impasto-banco.mp4",
    clipDurationInSeconds: 2.85,
    durationInSeconds: 3.8,
    emoji: "🤲",
    title: "Panetti da 350 g",
    subtitle: "sul banco",
  },

  // 10. IN TEGLIA -----------------------------------------------------------
  {
    id: "in-teglia",
    kind: "step",
    src: "videos/panetti.mp4",
    clipDurationInSeconds: 2.1,
    durationInSeconds: 3.8,
    emoji: "🫗",
    title: "In teglia",
    subtitle: "con tanto olio sotto",
  },

  // 11. STESURA -------------------------------------------------------------
  {
    id: "stesura",
    kind: "step",
    src: "videos/stesura.mp4",
    clipDurationInSeconds: 6.2,
    durationInSeconds: 4,
    emoji: "👐",
    title: "Stendi con le dita",
    subtitle: "senza schiacciare",
  },

  // 12. STESURA — buchi -----------------------------------------------------
  {
    id: "stesura-dita",
    kind: "step",
    src: "videos/stesura-dita.mp4",
    clipDurationInSeconds: 3.0,
    durationInSeconds: 3.5,
    emoji: "👇",
    title: "I classici buchi",
    subtitle: "su tutta la superficie",
  },

  // 13. CONDIMENTO — pomodoro -----------------------------------------------
  {
    id: "pomodoro",
    kind: "step",
    src: "videos/pomodorini.mp4",
    clipDurationInSeconds: 6.3,
    durationInSeconds: 4,
    emoji: "🍅",
    title: "Pomodoro a grappolo",
    subtitle: "tagliato a pezzettini",
  },

  // 14. CONDIMENTO — olive --------------------------------------------------
  {
    id: "olive",
    kind: "step",
    src: "videos/olive.mp4",
    clipDurationInSeconds: 5.6,
    durationInSeconds: 4,
    emoji: "🫒",
    title: "Olive e origano",
    subtitle: "e un pizzico di sale",
  },

  // 15. CONDIMENTO — olio ---------------------------------------------------
  {
    id: "olio",
    kind: "step",
    src: "videos/olio.mp4",
    clipDurationInSeconds: 3.6,
    durationInSeconds: 3.5,
    emoji: "🫗",
    title: "Un giro d'olio",
    subtitle: "generoso, in superficie",
  },

  // 16. LIEVITAZIONE --------------------------------------------------------
  {
    id: "lievitazione",
    kind: "step",
    src: "videos/teglie.mp4",
    clipDurationInSeconds: 3.9,
    durationInSeconds: 3.5,
    emoji: "⏳",
    title: "Lievita 1 ora",
    subtitle: "coperta, al caldo",
  },

  // 17. FORNO ---------------------------------------------------------------
  {
    id: "forno",
    kind: "step",
    src: "videos/forno.mp4",
    clipDurationInSeconds: 4.05,
    durationInSeconds: 4,
    emoji: "🔥",
    title: "Forno 220°C",
    subtitle: "per 15 minuti",
  },

  // 18. RISULTATO / CHIUSURA ------------------------------------------------
  {
    id: "risultato",
    kind: "result",
    src: "videos/hero-finale.mp4",
    clipDurationInSeconds: 4.4,
    durationInSeconds: 4.5,
    emoji: "😋",
    title: "Buon appetito",
    subtitle: "salva la ricetta 🫒",
  },
];

/** Durata totale in frame, tenendo conto delle micro-dissolvenze. */
export const totalDurationInFrames = () => {
  const sum = SCENES.reduce(
    (acc, s) => acc + Math.round(s.durationInSeconds * FPS),
    0,
  );
  return sum - (SCENES.length - 1) * TRANSITION_FRAMES;
};
