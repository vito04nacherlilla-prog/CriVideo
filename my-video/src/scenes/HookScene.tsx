import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { BigTitle, Rise, Scrim, Subtitle } from "../components/Overlays";

export const HookScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  // Leggero zoom-in per dare energia al primo secondo.
  const scale = interpolate(frame, [0, 90], [1.08, 1.16]);
  return (
    <AbsoluteFill>
      <div style={{ transform: `scale(${scale})`, width: "100%", height: "100%" }}>
        <ClipLayer src={scene.src} label={scene.id} />
      </div>
      <Scrim strength={1.15} />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          padding: 60,
        }}
      >
        <Rise>{scene.title ? <BigTitle size={128}>{scene.title}</BigTitle> : null}</Rise>
        <Rise delay={10}>
          {scene.subtitle ? <Subtitle>{scene.subtitle}</Subtitle> : null}
        </Rise>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
