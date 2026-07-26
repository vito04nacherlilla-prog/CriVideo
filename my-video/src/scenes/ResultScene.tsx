import { AbsoluteFill } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Fade, Grade, Subtitle, Title } from "../components/Overlays";

export const ResultScene: React.FC<{ scene: Scene }> = ({ scene }) => {
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
        }}
      >
        <Fade>
          {scene.emoji ? (
            <div style={{ fontSize: 72, lineHeight: 1, marginBottom: 8 }}>
              {scene.emoji}
            </div>
          ) : null}
          {scene.title ? (
            <Title size={112} align="center">
              {scene.title}
            </Title>
          ) : null}
          {scene.subtitle ? (
            <Subtitle align="center" size={40}>
              {scene.subtitle}
            </Subtitle>
          ) : null}
        </Fade>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
