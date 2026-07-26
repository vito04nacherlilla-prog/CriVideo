import { AbsoluteFill } from "remotion";
import { FPS, Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Caption, Grade } from "../components/Overlays";

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
          padding: 56,
          paddingBottom: 128,
        }}
      >
        <Caption
          emoji={scene.emoji}
          title={scene.title}
          subtitle={scene.subtitle}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
