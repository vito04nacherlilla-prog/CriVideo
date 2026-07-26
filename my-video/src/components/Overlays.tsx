import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

// Grana fine per il look "gritty" (statica, leggera).
const GRAIN =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>\")";

// Grade caldo + vignetta + grana + scrim per la leggibilità del testo.
export const Grade: React.FC<{ scrim?: "bottom" | "center" | "full" }> = ({
  scrim = "bottom",
}) => {
  const scrimBg =
    scrim === "center"
      ? "radial-gradient(circle at 50% 55%, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 60%)"
      : scrim === "full"
        ? "linear-gradient(to bottom, rgba(0,0,0,0.35), rgba(0,0,0,0.6))"
        : "linear-gradient(to bottom, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0) 26%, rgba(0,0,0,0) 46%, rgba(0,0,0,0.82) 100%)";
  return (
    <AbsoluteFill>
      {/* tinta calda */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(242,168,29,0.10) 0%, rgba(0,0,0,0) 40%, rgba(126,49,23,0.16) 100%)",
          mixBlendMode: "overlay",
        }}
      />
      {/* scrim per il testo */}
      <AbsoluteFill style={{ background: scrimBg }} />
      {/* vignetta */}
      <AbsoluteFill
        style={{
          boxShadow: "inset 0 0 300px rgba(0,0,0,0.6)",
        }}
      />
      {/* grana */}
      <AbsoluteFill
        style={{
          backgroundImage: GRAIN,
          backgroundSize: "140px 140px",
          opacity: 0.07,
          mixBlendMode: "overlay",
        }}
      />
    </AbsoluteFill>
  );
};

// Entrata generica dal basso con overshoot.
export const Rise: React.FC<{
  children: React.ReactNode;
  delay?: number;
  distance?: number;
}> = ({ children, delay = 0, distance = 50 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({
    frame: frame - delay,
    fps,
    config: { damping: 16, stiffness: 120, mass: 0.7 },
  });
  return (
    <div
      style={{
        transform: `translateY(${interpolate(s, [0, 1], [distance, 0])}px)`,
        opacity: Math.min(1, s * 1.4),
      }}
    >
      {children}
    </div>
  );
};

// Chip etichetta (kicker) in oro.
export const Kicker: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      display: "inline-block",
      fontFamily: FONTS.body,
      fontWeight: 800,
      fontSize: 30,
      letterSpacing: 3,
      textTransform: "uppercase",
      color: COLORS.nero,
      background: `linear-gradient(180deg, ${COLORS.oroChiaro}, ${COLORS.oroForno})`,
      padding: "11px 22px",
      borderRadius: 999,
      boxShadow: SHADOW.card,
    }}
  >
    {children}
  </div>
);

// Titolo cinetico: ogni parola "poppa" in sequenza (supporta \n).
export const KineticTitle: React.FC<{
  children: string;
  size?: number;
  align?: "left" | "center";
  delay?: number;
}> = ({ children, size = 100, align = "left", delay = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const lines = children.split("\n");
  let wordIndex = 0;

  return (
    <div
      style={{
        fontFamily: FONTS.display,
        fontSize: size,
        lineHeight: 0.98,
        color: COLORS.bianco,
        textShadow: SHADOW.testoForte,
        letterSpacing: 0.5,
        textAlign: align,
      }}
    >
      {lines.map((line, li) => (
        <div
          key={li}
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "0 0.26em",
            justifyContent: align === "center" ? "center" : "flex-start",
          }}
        >
          {line.split(" ").map((word, wi) => {
            const d = delay + wordIndex * 3;
            wordIndex += 1;
            const s = spring({
              frame: frame - d,
              fps,
              config: { damping: 13, stiffness: 130, mass: 0.6 },
            });
            return (
              <span
                key={wi}
                style={{
                  display: "inline-block",
                  transform: `translateY(${interpolate(s, [0, 1], [46, 0])}px) scale(${interpolate(
                    s,
                    [0, 1],
                    [0.86, 1],
                  )})`,
                  opacity: Math.min(1, s * 1.6),
                }}
              >
                {word}
              </span>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export const Subtitle: React.FC<{
  children: React.ReactNode;
  align?: "left" | "center";
}> = ({ children, align = "left" }) => (
  <div
    style={{
      fontFamily: FONTS.body,
      fontWeight: 700,
      fontSize: 40,
      color: COLORS.crema,
      textShadow: SHADOW.testo,
      marginTop: 12,
      textAlign: align,
    }}
  >
    {children}
  </div>
);

// Badge "chicca / trucco".
export const TipCard: React.FC<{ children: React.ReactNode; delay?: number }> = ({
  children,
  delay = 0,
}) => (
  <Rise delay={delay} distance={36}>
    <div
      style={{
        display: "flex",
        gap: 14,
        alignItems: "flex-start",
        maxWidth: 860,
        background: "rgba(16,11,7,0.74)",
        backdropFilter: "blur(6px)",
        borderLeft: `6px solid ${COLORS.oroForno}`,
        borderRadius: 16,
        padding: "18px 22px",
        boxShadow: SHADOW.card,
      }}
    >
      <div style={{ fontSize: 36, lineHeight: 1 }}>💡</div>
      <div
        style={{
          fontFamily: FONTS.body,
          fontWeight: 700,
          fontSize: 33,
          lineHeight: 1.25,
          color: COLORS.crema,
        }}
      >
        {children}
      </div>
    </div>
  </Rise>
);

// Barra di avanzamento segmentata (una tacca per scena).
export const SegmentedProgress: React.FC<{
  count: number;
  index: number;
  sceneProgress: number;
}> = ({ count, index, sceneProgress }) => (
  <AbsoluteFill style={{ justifyContent: "flex-start" }}>
    <div style={{ display: "flex", gap: 5, padding: 18 }}>
      {Array.from({ length: count }).map((_, i) => {
        const fill = i < index ? 1 : i === index ? sceneProgress : 0;
        return (
          <div
            key={i}
            style={{
              flex: 1,
              height: 6,
              borderRadius: 999,
              background: "rgba(255,255,255,0.28)",
              overflow: "hidden",
            }}
          >
            <div
              style={{
                width: `${fill * 100}%`,
                height: "100%",
                background: COLORS.oroForno,
              }}
            />
          </div>
        );
      })}
    </div>
  </AbsoluteFill>
);
