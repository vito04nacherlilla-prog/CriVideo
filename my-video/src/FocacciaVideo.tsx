import { AbsoluteFill } from "remotion";
import { linearTiming, TransitionSeries } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { FPS, Scene, SCENES, TRANSITION_FRAMES } from "./lib/scenes";
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

// Stacchi rapidi ammorbiditi da una micro-dissolvenza (solo fade, breve):
// fonde il movimento a fine clip invece di tagliarlo di netto.
export const FocacciaVideo: React.FC = () => {
  const timing = linearTiming({ durationInFrames: TRANSITION_FRAMES });

  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <TransitionSeries>
        {SCENES.flatMap((scene, i) => {
          const nodes = [
            <TransitionSeries.Sequence
              key={scene.id}
              durationInFrames={Math.round(scene.durationInSeconds * FPS)}
            >
              <SceneRenderer scene={scene} />
            </TransitionSeries.Sequence>,
          ];
          if (i < SCENES.length - 1) {
            nodes.push(
              <TransitionSeries.Transition
                key={`t-${scene.id}`}
                presentation={fade()}
                timing={timing}
              />,
            );
          }
          return nodes;
        })}
      </TransitionSeries>
    </AbsoluteFill>
  );
};
