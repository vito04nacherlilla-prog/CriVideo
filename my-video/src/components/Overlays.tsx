import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

// Sfumatura scura in alto/basso per far risaltare il testo sopra il video.
export const Scrim: React.FC<{ strength?: number }> = ({ strength = 1 }) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(to bottom, rgba(0,0,0,${0.45 * strength}) 0%, rgba(0,0,0,0) 28%, rgba(0,0,0,0) 55%, rgba(0,0,0,${0.72 * strength}) 100%)`,
    }}
  />
);

// Entrata "spring" dal basso + fade, riutilizzabile.
export const Rise: React.FC<{
  children: React.ReactNode;
  delay?: number;
  distance?: number;
}> = ({ children, delay = 0, distance = 60 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 200 } });
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

// Etichetta piccola (STEP 1, ecc.)
export const Kicker: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      display: "inline-block",
      fontFamily: FONTS.body,
      fontWeight: 800,
      fontSize: 30,
      letterSpacing: 4,
      textTransform: "uppercase",
      color: COLORS.carbone,
      background: COLORS.oroForno,
      padding: "10px 22px",
      borderRadius: 999,
      boxShadow: SHADOW.card,
    }}
  >
    {children}
  </div>
);

// Titolo grande da impatto (supporta \n per andare a capo).
export const BigTitle: React.FC<{ children: string; size?: number }> = ({
  children,
  size = 96,
}) => (
  <div
    style={{
      fontFamily: FONTS.display,
      fontSize: size,
      lineHeight: 0.98,
      color: COLORS.bianco,
      textShadow: SHADOW.testoForte,
      whiteSpace: "pre-line",
      letterSpacing: -1,
    }}
  >
    {children}
  </div>
);

export const Subtitle: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      fontFamily: FONTS.body,
      fontWeight: 600,
      fontSize: 40,
      color: COLORS.crema,
      textShadow: SHADOW.testo,
      marginTop: 14,
    }}
  >
    {children}
  </div>
);

// Badge "chicca / trucco" — il gancio virale.
export const TipCard: React.FC<{ children: React.ReactNode; delay?: number }> = ({
  children,
  delay = 0,
}) => (
  <Rise delay={delay} distance={40}>
    <div
      style={{
        display: "flex",
        gap: 16,
        alignItems: "flex-start",
        maxWidth: 820,
        background: "rgba(20,15,11,0.72)",
        backdropFilter: "blur(6px)",
        border: `2px solid ${COLORS.oroForno}`,
        borderRadius: 22,
        padding: "20px 24px",
        boxShadow: SHADOW.card,
      }}
    >
      <div style={{ fontSize: 40, lineHeight: 1 }}>💡</div>
      <div
        style={{
          fontFamily: FONTS.body,
          fontWeight: 600,
          fontSize: 34,
          lineHeight: 1.25,
          color: COLORS.crema,
        }}
      >
        {children}
      </div>
    </div>
  </Rise>
);

// Barra di avanzamento globale in cima al video.
export const ProgressBar: React.FC<{ progress: number }> = ({ progress }) => (
  <AbsoluteFill style={{ justifyContent: "flex-start" }}>
    <div style={{ height: 10, width: "100%", background: "rgba(255,255,255,0.18)" }}>
      <div
        style={{
          height: "100%",
          width: `${Math.min(100, Math.max(0, progress * 100))}%`,
          background: COLORS.oroForno,
        }}
      />
    </div>
  </AbsoluteFill>
);
