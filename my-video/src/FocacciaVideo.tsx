import { AbsoluteFill, Series } from "remotion";
import { FPS, Scene, SCENES } from "./lib/scenes";
import { HookScene } from "./scenes/HookScene";
import { IngredientsScene } from "./scenes/IngredientsScene";
import { StepScene } from "./scenes/StepScene";
import { ResultScene } from "./scenes/ResultScene";

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
  }
};

// Montaggio a stacchi netti (hard cut), stile food professionale.
export const FocacciaVideo: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <Series>
        {SCENES.map((scene) => (
          <Series.Sequence
            key={scene.id}
            durationInFrames={Math.round(scene.durationInSeconds * FPS)}
          >
            <SceneRenderer scene={scene} />
          </Series.Sequence>
        ))}
      </Series>
    </AbsoluteFill>
  );
};
