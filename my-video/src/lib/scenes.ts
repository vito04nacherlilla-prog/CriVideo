// ============================================================================
// STORYBOARD — La vera Focaccia Barese (Reel verticale 9:16)
// Stile: video food professionale da TikTok. Stacchi netti, didascalie ricche.
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

export type SceneKind = "hook" | "ingredients" | "step" | "result";

export type Scene = {
  id: string;
  kind: SceneKind;
  src?: string;
  /** Sfondo immagine fissa (in public), alternativo alla clip video. */
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

  // 1. INGREDIENTI (sfondo immagine fissa, niente loop/judder) --------------
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

  // 2. IMPASTO — acqua, lievito, zucchero -----------------------------------
  {
    id: "impasto-1",
    kind: "step",
    src: "videos/impasto-slurry.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 4.5,
    emoji: "💧",
    title: "Acqua, lievito, zucchero",
    subtitle: "nella planetaria",
  },

  // 3. IMPASTO — olio -------------------------------------------------------
  {
    id: "impasto-olio",
    kind: "step",
    src: "videos/impasto-olio.mp4",
    clipDurationInSeconds: 3.5,
    durationInSeconds: 4,
    emoji: "🫒",
    title: "Poi l'olio EVO",
    subtitle: "100 g",
  },

  // 4. IMPASTO — farine -----------------------------------------------------
  {
    id: "impasto-farine",
    kind: "step",
    src: "videos/impasto-semola.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 4.5,
    emoji: "🌾",
    title: "Farina 0 e semola",
    subtitle: "400 g + 550 g",
  },

  // 5. IMPASTO — sale -------------------------------------------------------
  {
    id: "impasto-sale",
    kind: "step",
    src: "videos/impasto-lavora.mp4",
    clipDurationInSeconds: 4.0,
    durationInSeconds: 4.5,
    emoji: "🧂",
    title: "Il sale",
    subtitle: "30 g, a impasto grezzo",
  },

  // 6. IMPASTO — liscio -----------------------------------------------------
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

  // 7. PANETTI --------------------------------------------------------------
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

  // 8. IN TEGLIA ------------------------------------------------------------
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

  // 9. STESURA --------------------------------------------------------------
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

  // 10. STESURA — buchi -----------------------------------------------------
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

  // 11. CONDIMENTO — pomodoro -----------------------------------------------
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

  // 12. CONDIMENTO — olive --------------------------------------------------
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

  // 13. CONDIMENTO — olio ---------------------------------------------------
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

  // 14. LIEVITAZIONE --------------------------------------------------------
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

  // 15. FORNO ---------------------------------------------------------------
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

  // 16. RISULTATO / CHIUSURA ------------------------------------------------
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

/** Durata totale in frame (stacchi netti: somma delle scene). */
export const totalDurationInFrames = () =>
  SCENES.reduce((acc, s) => acc + Math.round(s.durationInSeconds * FPS), 0);
