import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { BigTitle, Rise, Scrim, Subtitle } from "../components/Overlays";

export const ResultScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const scale = interpolate(frame, [0, 120], [1.12, 1.02]);
  return (
    <AbsoluteFill>
      <div style={{ transform: `scale(${scale})`, width: "100%", height: "100%" }}>
        <ClipLayer src={scene.src} label={scene.id} />
      </div>
      <Scrim strength={1.1} />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          padding: 60,
        }}
      >
        <Rise>{scene.title ? <BigTitle size={140}>{scene.title}</BigTitle> : null}</Rise>
        <Rise delay={8}>
          {scene.subtitle ? <Subtitle>{scene.subtitle}</Subtitle> : null}
        </Rise>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
