import { AbsoluteFill } from "remotion";
import { FPS, Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Fade, Grade, Subtitle, Title } from "../components/Overlays";

export const StepScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  return (
    <AbsoluteFill>
      <ClipLayer
        src={scene.src}
        clipDurationInSeconds={scene.clipDurationInSeconds}
        sceneDurationInSeconds={scene.durationInSeconds}
        startFrom={
          scene.clipStartInSeconds
            ? Math.round(scene.clipStartInSeconds * FPS)
            : undefined
        }
        label={scene.id}
      />
      <Grade scrim="bottom" />
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "flex-start",
          padding: 64,
          paddingBottom: 120,
        }}
      >
        <Fade>
          {scene.title ? <Title size={72}>{scene.title}</Title> : null}
          {scene.subtitle ? <Subtitle>{scene.subtitle}</Subtitle> : null}
        </Fade>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
