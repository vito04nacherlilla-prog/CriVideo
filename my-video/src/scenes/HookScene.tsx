import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import {
  Grade,
  KineticTitle,
  Rise,
  SegmentedProgress,
  Subtitle,
} from "../components/Overlays";

export const HookScene: React.FC<{
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
        label={scene.id}
      />
      <Grade scrim="center" />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          padding: 60,
          gap: 6,
        }}
      >
        {scene.title ? (
          <KineticTitle size={132} align="center">
            {scene.title}
          </KineticTitle>
        ) : null}
        <Rise delay={12}>
          {scene.subtitle ? (
            <Subtitle align="center">{scene.subtitle}</Subtitle>
          ) : null}
        </Rise>
      </AbsoluteFill>
      <SegmentedProgress
        count={count}
        index={index}
        sceneProgress={frame / durationInFrames}
      />
    </AbsoluteFill>
  );
};
