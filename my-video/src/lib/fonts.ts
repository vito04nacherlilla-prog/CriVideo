import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

// Font caricati localmente da public/fonts (nessuna dipendenza di rete).
// Anton = titoli d'impatto; Montserrat = testi secondari.

export const FONT_DISPLAY = "Anton";
export const FONT_BODY = "Montserrat";

export const fontsReady = Promise.all([
  loadFont({
    family: FONT_DISPLAY,
    url: staticFile("fonts/Anton-Regular.ttf"),
    weight: "400",
  }),
  loadFont({
    family: FONT_BODY,
    url: staticFile("fonts/Montserrat.ttf"),
    weight: "700",
  }),
]);
