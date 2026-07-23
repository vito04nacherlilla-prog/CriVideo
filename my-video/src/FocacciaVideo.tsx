import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { FPS, Scene, SCENES } from "./lib/scenes";
import { HookScene } from "./scenes/HookScene";
import { IngredientsScene } from "./scenes/IngredientsScene";
import { StepScene } from "./scenes/StepScene";
import { ResultScene } from "./scenes/ResultScene";
import { OutroScene } from "./scenes/OutroScene";
import { ProgressBar } from "./components/Overlays";

const SceneRenderer: React.FC<{ scene: Scene }> = ({ scene }) => {
  switch (scene.kind) {
    case "hook":
      return <HookScene scene={scene} />;
    case "ingredients":
      return <IngredientsScene scene={scene} />;
    case "step":
      return <StepScene scene={scene} />;
    case "result":
      return <ResultScene scene={scene} />;
    case "outro":
      return <OutroScene scene={scene} />;
  }
};

export const FocacciaVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  let cursor = 0;
  const timeline = SCENES.map((scene) => {
    const from = cursor;
    const durationInFrames = Math.round(scene.durationInSeconds * FPS);
    cursor += durationInFrames;
    return { scene, from, durationInFrames };
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      {timeline.map(({ scene, from, durationInFrames }) => (
        <Sequence key={scene.id} from={from} durationInFrames={durationInFrames}>
          <SceneRenderer scene={scene} />
        </Sequence>
      ))}
      <ProgressBar progress={frame / durationInFrames} />
    </AbsoluteFill>
  );
};
