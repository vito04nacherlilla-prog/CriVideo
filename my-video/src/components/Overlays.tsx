import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

// Scrim caldo per la leggibilità del testo.
export const Grade: React.FC<{ scrim?: "bottom" | "center" }> = ({
  scrim = "bottom",
}) => {
  const scrimBg =
    scrim === "center"
      ? "radial-gradient(circle at 50% 58%, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 62%)"
      : "linear-gradient(to bottom, rgba(0,0,0,0.32) 0%, rgba(0,0,0,0) 24%, rgba(0,0,0,0) 44%, rgba(0,0,0,0.82) 100%)";
  return (
    <AbsoluteFill>
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(242,168,29,0.08) 0%, rgba(0,0,0,0) 42%, rgba(126,49,23,0.16) 100%)",
          mixBlendMode: "overlay",
        }}
      />
      <AbsoluteFill style={{ background: scrimBg }} />
      <AbsoluteFill style={{ boxShadow: "inset 0 0 260px rgba(0,0,0,0.5)" }} />
    </AbsoluteFill>
  );
};

const useSpring = (delay: number, cfg?: object) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - delay, fps, config: cfg ?? { damping: 200 } });
};

// Sfuma via la didascalia poco prima della fine della scena, così durante la
// micro-dissolvenza le scritte non si accavallano.
const useExit = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return interpolate(
    frame,
    [durationInFrames - 9, durationInFrames - 2],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
};

// Entrata pulita: fade + salita.
export const Fade: React.FC<{
  children: React.ReactNode;
  delay?: number;
  distance?: number;
}> = ({ children, delay = 0, distance = 26 }) => {
  const s = useSpring(delay, { damping: 200 });
  const exit = useExit();
  return (
    <div
      style={{
        transform: `translateY(${interpolate(s, [0, 1], [distance, 0])}px)`,
        opacity: s * exit,
      }}
    >
      {children}
    </div>
  );
};

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
      textShadow: SHADOW.testoForte,
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
  color?: string;
}> = ({ children, align = "left", size = 36, color = COLORS.crema }) => (
  <div
    style={{
      fontFamily: FONTS.body,
      fontWeight: 700,
      fontSize: size,
      color,
      textShadow: SHADOW.testo,
      marginTop: 8,
      textAlign: align,
      letterSpacing: 0.2,
    }}
  >
    {children}
  </div>
);

// Didascalia "ricca" stile TikTok food: pannello pulito, accento oro,
// emoji che poppa, titolo con micro-pop, sottotitolo in oro.
export const Caption: React.FC<{
  emoji?: string;
  title?: string;
  subtitle?: string;
}> = ({ emoji, title, subtitle }) => {
  const card = useSpring(0, { damping: 18, stiffness: 120, mass: 0.7 });
  const titlePop = useSpring(3, { damping: 12, stiffness: 140, mass: 0.6 });
  const emojiPop = useSpring(1, { damping: 10, stiffness: 160, mass: 0.5 });
  const exit = useExit();

  return (
    <div
      style={{
        transform: `translateY(${interpolate(card, [0, 1], [40, 0])}px)`,
        opacity: card * exit,
        display: "inline-flex",
        flexDirection: "column",
        maxWidth: 860,
        background:
          "linear-gradient(180deg, rgba(20,13,9,0.55), rgba(12,8,5,0.68))",
        backdropFilter: "blur(7px)",
        WebkitBackdropFilter: "blur(7px)",
        borderLeft: `7px solid ${COLORS.oroForno}`,
        borderRadius: 20,
        padding: "22px 30px 24px 26px",
        boxShadow: SHADOW.card,
      }}
    >
      {emoji ? (
        <div
          style={{
            fontSize: 56,
            lineHeight: 1,
            marginBottom: 10,
            transform: `scale(${interpolate(emojiPop, [0, 1], [0.3, 1])})`,
            transformOrigin: "left center",
          }}
        >
          {emoji}
        </div>
      ) : null}
      {title ? (
        <div
          style={{
            transform: `scale(${interpolate(titlePop, [0, 1], [0.9, 1])})`,
            transformOrigin: "left bottom",
          }}
        >
          <Title size={66}>{title}</Title>
        </div>
      ) : null}
      {subtitle ? (
        <Subtitle color={COLORS.oroChiaro} size={38}>
          {subtitle}
        </Subtitle>
      ) : null}
    </div>
  );
};
