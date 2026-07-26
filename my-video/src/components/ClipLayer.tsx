import {
  AbsoluteFill,
  interpolate,
  Loop,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS, FONTS } from "../lib/theme";

// Player della clip con:
//  - slow-motion automatico (playbackRate) per riempire scene più lunghe della clip
//  - loop di sicurezza se la clip resta comunque corta
//  - zoom "Ken Burns" continuo (in/out) per dare sempre movimento
export const ClipLayer: React.FC<{
  src?: string;
  clipDurationInSeconds?: number;
  sceneDurationInSeconds?: number;
  startFrom?: number;
  label?: string;
}> = ({ src, clipDurationInSeconds, sceneDurationInSeconds, startFrom, label }) => {
  const { fps } = useVideoConfig();
  const frame = useCurrentFrame();

  const sceneFrames = Math.max(1, Math.round((sceneDurationInSeconds ?? 4) * fps));
  const p = interpolate(frame, [0, sceneFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  // Direzione dello zoom alternata in modo deterministico dalla sorgente.
  const zoomIn = (src?.length ?? 0) % 2 === 0;
  const scale = zoomIn
    ? interpolate(p, [0, 1], [1.02, 1.09])
    : interpolate(p, [0, 1], [1.09, 1.02]);

  if (!src) {
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
            color: "rgba(255,255,255,0.4)",
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
            <div style={{ fontSize: 26, marginTop: 10, opacity: 0.8 }}>{label}</div>
          ) : null}
        </div>
      </AbsoluteFill>
    );
  }

  let playbackRate = 1;
  if (clipDurationInSeconds && sceneDurationInSeconds) {
    playbackRate = Math.min(
      1,
      Math.max(0.5, clipDurationInSeconds / sceneDurationInSeconds),
    );
  }

  const video = (
    <OffthreadVideo
      src={staticFile(src)}
      startFrom={startFrom}
      playbackRate={playbackRate}
      muted
      style={{ width: "100%", height: "100%", objectFit: "cover" }}
    />
  );

  // Lunghezza effettiva della clip riprodotta (con slow-motion), in frame.
  const playedFrames = clipDurationInSeconds
    ? Math.floor((clipDurationInSeconds / playbackRate) * fps)
    : undefined;

  const inner =
    playedFrames && !startFrom ? (
      <Loop durationInFrames={playedFrames}>{video}</Loop>
    ) : (
      video
    );

  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ transform: `scale(${scale})` }}>{inner}</AbsoluteFill>
    </AbsoluteFill>
  );
};
