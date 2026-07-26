import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

// Scrim pulito per la leggibilità del testo (niente barre, niente chip).
export const Grade: React.FC<{ scrim?: "bottom" | "center" }> = ({
  scrim = "bottom",
}) => {
  const scrimBg =
    scrim === "center"
      ? "radial-gradient(circle at 50% 60%, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 62%)"
      : "linear-gradient(to bottom, rgba(0,0,0,0.28) 0%, rgba(0,0,0,0) 22%, rgba(0,0,0,0) 50%, rgba(0,0,0,0.78) 100%)";
  return (
    <AbsoluteFill>
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(242,168,29,0.06) 0%, rgba(0,0,0,0) 45%, rgba(126,49,23,0.12) 100%)",
          mixBlendMode: "overlay",
        }}
      />
      <AbsoluteFill style={{ background: scrimBg }} />
      <AbsoluteFill style={{ boxShadow: "inset 0 0 260px rgba(0,0,0,0.45)" }} />
    </AbsoluteFill>
  );
};

// Entrata pulita: fade + leggera salita, senza rimbalzi.
export const Fade: React.FC<{
  children: React.ReactNode;
  delay?: number;
  distance?: number;
}> = ({ children, delay = 0, distance = 26 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({
    frame: frame - delay,
    fps,
    config: { damping: 200 },
    durationInFrames: 12,
  });
  return (
    <div
      style={{
        transform: `translateY(${interpolate(s, [0, 1], [distance, 0])}px)`,
        opacity: s,
      }}
    >
      {children}
    </div>
  );
};

// Titolo pulito (Anton), supporta \n. Nessuna animazione parola-per-parola.
export const Title: React.FC<{
  children: string;
  size?: number;
  align?: "left" | "center";
}> = ({ children, size = 70, align = "left" }) => (
  <div
    style={{
      fontFamily: FONTS.display,
      fontSize: size,
      lineHeight: 1.0,
      color: COLORS.bianco,
      textShadow: SHADOW.testo,
      letterSpacing: 0.5,
      textAlign: align,
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

export const Subtitle: React.FC<{
  children: React.ReactNode;
  align?: "left" | "center";
  size?: number;
}> = ({ children, align = "left", size = 36 }) => (
  <div
    style={{
      fontFamily: FONTS.body,
      fontWeight: 700,
      fontSize: size,
      color: COLORS.crema,
      textShadow: SHADOW.testo,
      marginTop: 10,
      textAlign: align,
      letterSpacing: 0.2,
    }}
  >
    {children}
  </div>
);
