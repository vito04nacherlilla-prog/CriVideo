import { AbsoluteFill, OffthreadVideo, staticFile } from "remotion";
import { COLORS, FONTS } from "../lib/theme";

// Mostra la clip video se `src` è definito, altrimenti un placeholder colorato
// con il nome della scena, così la struttura è visibile prima di avere i video.
export const ClipLayer: React.FC<{
  src?: string;
  startFrom?: number;
  label?: string;
}> = ({ src, startFrom, label }) => {
  if (src) {
    return (
      <AbsoluteFill>
        <OffthreadVideo
          src={staticFile(src)}
          startFrom={startFrom}
          muted
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(150deg, ${COLORS.terracotta} 0%, ${COLORS.terracottaScura} 55%, ${COLORS.carbone} 100%)`,
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          fontFamily: FONTS.body,
          color: "rgba(255,255,255,0.35)",
          fontSize: 34,
          letterSpacing: 2,
          textTransform: "uppercase",
          border: "2px dashed rgba(255,255,255,0.25)",
          borderRadius: 24,
          padding: "28px 44px",
          textAlign: "center",
        }}
      >
        <div style={{ fontSize: 64, marginBottom: 12 }}>🎬</div>
        clip mancante
        {label ? (
          <div style={{ fontSize: 26, marginTop: 10, opacity: 0.8 }}>
            {label}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
