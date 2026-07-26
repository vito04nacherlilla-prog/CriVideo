// Design tokens — "Focaccia Barese" viral vertical short.
// Mood: CALDO E GRINTOSO. Palette pugliese satura: forno, terracotta, oro, pomodoro.

import { FONT_BODY, FONT_DISPLAY } from "./fonts";

export const COLORS = {
  crema: "#FBF3E4",
  cremaScura: "#E9DCC3",
  terracotta: "#C0562B",
  terracottaScura: "#7E3117",
  oroForno: "#F2A81D",
  oroChiaro: "#FFCB5C",
  pomodoro: "#D6321B",
  verdeOliva: "#6B7A34",
  carbone: "#1A130D",
  nero: "#0C0906",
  bianco: "#FFFFFF",
};

// Font: Anton (display) caricato da public/fonts, Montserrat per il corpo.
export const FONTS = {
  display: `"${FONT_DISPLAY}", "Arial Black", Impact, system-ui, sans-serif`,
  body: `"${FONT_BODY}", "Helvetica Neue", Arial, system-ui, sans-serif`,
};

export const SHADOW = {
  testo: "0 4px 24px rgba(0,0,0,0.6)",
  testoForte:
    "0 3px 0 rgba(0,0,0,0.35), 0 6px 30px rgba(0,0,0,0.6)",
  card: "0 20px 60px rgba(0,0,0,0.5)",
};
