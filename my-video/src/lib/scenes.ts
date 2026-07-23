// ============================================================================
// STORYBOARD — La vera Focaccia Barese (Reel verticale 9:16)
// ----------------------------------------------------------------------------
// Tutto il video è guidato da questi dati. Per montare il video vero:
//   1. Metti le clip del tuo amico in  public/videos/
//   2. In ogni scena, imposta  src: "videos/nome-file.mp4"
//      (finché src è undefined viene mostrato un placeholder colorato)
//   3. Regola durationInSeconds / testi / trucchi come vuoi
// L'ordine dell'array = l'ordine nel video. Aggiungere o togliere scene è
// sufficiente: durata totale e barra di avanzamento si ricalcolano da sole.
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
  /** File in public/videos, es. "videos/impasto.mp4". Se assente → placeholder. */
  src?: string;
  durationInSeconds: number;
  /** Punto di start della clip in secondi (per tagliare l'inizio). */
  clipStartInSeconds?: number;
  /** Etichetta piccola in alto, es. "STEP 1 / 6". */
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
  // ---- 0. HOOK (primi 3 secondi: devono inchiodare lo spettatore) ----------
  {
    id: "hook",
    kind: "hook",
    src: undefined, // → metti qui la clip più bella: il morso croccante o la teglia appena sfornata
    durationInSeconds: 3,
    title: "LA VERA\nFOCACCIA BARESE",
    subtitle: "quella che non compri, la fai",
  },

  // ---- 1. INGREDIENTI ------------------------------------------------------
  {
    id: "ingredienti",
    kind: "ingredients",
    src: undefined,
    durationInSeconds: 6,
    kicker: "GLI INGREDIENTI",
    title: "Ti serve solo questo",
    list: [
      { label: "Semola rimacinata", value: "300 g" },
      { label: "Farina 0", value: "200 g" },
      { label: "Patata lessa", value: "1 media" },
      { label: "Acqua tiepida", value: "400 ml" },
      { label: "Lievito di birra", value: "7 g" },
      { label: "Olio EVO + sale grosso", value: "q.b." },
      { label: "Pomodorini + olive baresane", value: "q.b." },
    ],
  },

  // ---- 2. STEP 1 — IMPASTO -------------------------------------------------
  {
    id: "impasto",
    kind: "step",
    src: undefined, // videos/impasto.mp4
    durationInSeconds: 5,
    kicker: "STEP 1",
    title: "L'impasto",
    subtitle: "Semola + farina 0 + patata schiacciata",
    tip: "La patata lessa è il segreto: rende la mollica soffice per giorni.",
  },

  // ---- 3. STEP 2 — IDRATAZIONE ---------------------------------------------
  {
    id: "idratazione",
    kind: "step",
    src: undefined,
    durationInSeconds: 5,
    kicker: "STEP 2",
    title: "Impasto molle",
    subtitle: "Aggiungi l'acqua poco alla volta",
    tip: "Alta idratazione (~80%): dev'essere appiccicoso, non tirarlo!",
  },

  // ---- 4. STEP 3 — LIEVITAZIONE --------------------------------------------
  {
    id: "lievitazione",
    kind: "step",
    src: undefined,
    durationInSeconds: 4,
    kicker: "STEP 3",
    title: "La lievitazione",
    subtitle: "Copri e lascia raddoppiare",
    tip: "2 ore al caldo. Niente fretta: qui nasce l'alveolatura.",
  },

  // ---- 5. STEP 4 — STESURA IN TEGLIA ---------------------------------------
  {
    id: "stesura",
    kind: "step",
    src: undefined,
    durationInSeconds: 5,
    kicker: "STEP 4",
    title: "In teglia",
    subtitle: "Stendi con le dita, senza schiacciare",
    tip: "Teglia unta d'olio abbondante: è ciò che frigge il fondo croccante.",
  },

  // ---- 6. STEP 5 — CONDIMENTO ----------------------------------------------
  {
    id: "condimento",
    kind: "step",
    src: undefined,
    durationInSeconds: 5,
    kicker: "STEP 5",
    title: "Pomodorini & olive",
    subtitle: "Affonda pomodorini e olive baresane",
    tip: "Schiaccia i pomodorini con la buccia: rilasciano più succo e sapore.",
  },

  // ---- 7. STEP 6 — EMULSIONE -----------------------------------------------
  {
    id: "emulsione",
    kind: "step",
    src: undefined,
    durationInSeconds: 4,
    kicker: "STEP 6",
    title: "L'emulsione",
    subtitle: "Acqua + olio + sale grosso in superficie",
    tip: "Il trucco dei fornai: superficie lucida e croccante, cuore morbido.",
  },

  // ---- 8. STEP 7 — COTTURA -------------------------------------------------
  {
    id: "cottura",
    kind: "step",
    src: undefined,
    durationInSeconds: 5,
    kicker: "STEP 7",
    title: "In forno",
    subtitle: "Forno bollente, parte bassa",
    tip: "250°C statico: il colpo di calore dà la crosta dorata.",
  },

  // ---- 9. RISULTATO --------------------------------------------------------
  {
    id: "risultato",
    kind: "result",
    src: undefined, // videos/morso.mp4 — il morso croccante
    durationInSeconds: 4,
    title: "Pronta.",
    subtitle: "Croccante fuori, morbida dentro.",
  },

  // ---- 10. OUTRO / CTA -----------------------------------------------------
  {
    id: "outro",
    kind: "outro",
    src: undefined,
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
