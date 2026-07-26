import { ANTON_URL, MONTSERRAT_URL } from "./fontData";

// Font incorporati via @font-face (dati base64, nessun fetch).
// NIENTE delayRender: Remotion ricarica la pagina durante i render lunghi e un
// loadFont bloccante può restare appeso; qui invece i dati sono locali, il font
// è disponibile subito e il render non può mai bloccarsi.

export const FONT_DISPLAY = "Anton";
export const FONT_BODY = "Montserrat";

if (typeof document !== "undefined") {
  const style = document.createElement("style");
  style.textContent = `
@font-face{font-family:'Anton';src:url('${ANTON_URL}') format('truetype');font-weight:400;font-style:normal;font-display:swap;}
@font-face{font-family:'Montserrat';src:url('${MONTSERRAT_URL}') format('truetype');font-weight:700;font-style:normal;font-display:swap;}
`;
  document.head.appendChild(style);
  // Avvia subito il caricamento (best-effort, senza bloccare il render).
  const fontsApi = (document as unknown as { fonts?: FontFaceSet }).fonts;
  if (fontsApi) {
    fontsApi.load("400 100px Anton").catch(() => undefined);
    fontsApi.load("700 40px Montserrat").catch(() => undefined);
  }
}
