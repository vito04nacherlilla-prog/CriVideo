import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { FPS, Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import {
  Grade,
  Kicker,
  KineticTitle,
  Rise,
  SegmentedProgress,
  Subtitle,
  TipCard,
} from "../components/Overlays";

export const StepScene: React.FC<{
  scene: Scene;
  index: number;
  count: number;
}> = ({ scene, index, count }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

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
          padding: 60,
          paddingBottom: 110,
          gap: 20,
        }}
      >
        <Rise>{scene.kicker ? <Kicker>{scene.kicker}</Kicker> : null}</Rise>
        <div>
          {scene.title ? (
            <KineticTitle size={92} delay={4}>
              {scene.title}
            </KineticTitle>
          ) : null}
          <Rise delay={10}>
            {scene.subtitle ? <Subtitle>{scene.subtitle}</Subtitle> : null}
          </Rise>
        </div>
        {scene.tip ? <TipCard delay={18}>{scene.tip}</TipCard> : null}
      </AbsoluteFill>
      <SegmentedProgress
        count={count}
        index={index}
        sceneProgress={frame / durationInFrames}
      />
    </AbsoluteFill>
  );
};
