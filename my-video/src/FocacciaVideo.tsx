import { AbsoluteFill } from "remotion";
import {
  linearTiming,
  TransitionSeries,
} from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { FPS, Scene, SCENES, TRANSITION_FRAMES } from "./lib/scenes";
import { HookScene } from "./scenes/HookScene";
import { IngredientsScene } from "./scenes/IngredientsScene";
import { StepScene } from "./scenes/StepScene";
import { ResultScene } from "./scenes/ResultScene";
import { OutroScene } from "./scenes/OutroScene";

const SceneRenderer: React.FC<{ scene: Scene; index: number; count: number }> = ({
  scene,
  index,
  count,
}) => {
  const props = { scene, index, count };
  switch (scene.kind) {
    case "hook":
      return <HookScene {...props} />;
    case "ingredients":
      return <IngredientsScene {...props} />;
    case "step":
      return <StepScene {...props} />;
    case "result":
      return <ResultScene {...props} />;
    case "outro":
      return <OutroScene {...props} />;
  }
};

// Presentazioni alternate per un montaggio vario ma coerente.
const presentations = [
  slide({ direction: "from-right" }),
  fade(),
  slide({ direction: "from-bottom" }),
  slide({ direction: "from-left" }),
];

export const FocacciaVideo: React.FC = () => {
  const count = SCENES.length;
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
              <SceneRenderer scene={scene} index={i} count={count} />
            </TransitionSeries.Sequence>,
          ];
          if (i < SCENES.length - 1) {
            nodes.push(
              <TransitionSeries.Transition
                key={`t-${scene.id}`}
                presentation={presentations[i % presentations.length]}
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
