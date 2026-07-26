import { AbsoluteFill } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { BigTitle, Kicker, Rise, Scrim, Subtitle, TipCard } from "../components/Overlays";

export const StepScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  return (
    <AbsoluteFill>
      <ClipLayer
        src={scene.src}
        startFrom={
          scene.clipStartInSeconds
            ? Math.round(scene.clipStartInSeconds * 30)
            : undefined
        }
        clipDurationInSeconds={scene.clipDurationInSeconds}
        label={scene.id}
      />
      <Scrim />
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "flex-start",
          padding: 64,
          paddingBottom: 120,
          gap: 22,
        }}
      >
        <Rise>{scene.kicker ? <Kicker>{scene.kicker}</Kicker> : null}</Rise>
        <div>
          <Rise delay={4}>
            {scene.title ? <BigTitle size={92}>{scene.title}</BigTitle> : null}
          </Rise>
          <Rise delay={8}>
            {scene.subtitle ? <Subtitle>{scene.subtitle}</Subtitle> : null}
          </Rise>
        </div>
        {scene.tip ? <TipCard delay={16}>{scene.tip}</TipCard> : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
