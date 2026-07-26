import { AbsoluteFill } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { BigTitle, Rise, Scrim, Subtitle } from "../components/Overlays";
import { COLORS } from "../lib/theme";

export const OutroScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  return (
    <AbsoluteFill style={{ background: COLORS.terracottaScura }}>
      <ClipLayer
        src={scene.src}
        clipDurationInSeconds={scene.clipDurationInSeconds}
        label={scene.id}
      />
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at center, rgba(0,0,0,0.15), rgba(0,0,0,0.78))`,
        }}
      />
      <Scrim strength={0.6} />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          padding: 60,
          gap: 6,
        }}
      >
        <Rise>{scene.title ? <BigTitle size={104}>{scene.title}</BigTitle> : null}</Rise>
        <Rise delay={8}>
          {scene.subtitle ? <Subtitle>{scene.subtitle}</Subtitle> : null}
        </Rise>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
