import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Grade, Kicker, KineticTitle, Rise, SegmentedProgress } from "../components/Overlays";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

export const IngredientsScene: React.FC<{
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
      <Grade scrim="full" />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 64,
          gap: 18,
        }}
      >
        <Rise>{scene.kicker ? <Kicker>{scene.kicker}</Kicker> : null}</Rise>
        {scene.title ? (
          <KineticTitle size={82} align="center" delay={4}>
            {scene.title}
          </KineticTitle>
        ) : null}
        <div
          style={{
            width: "100%",
            maxWidth: 880,
            background: "rgba(14,9,6,0.66)",
            backdropFilter: "blur(6px)",
            borderRadius: 26,
            padding: "24px 34px",
            boxShadow: SHADOW.card,
            marginTop: 6,
          }}
        >
          {scene.list?.map((item, i) => (
            <Rise key={item.label} delay={10 + i * 4} distance={26}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "baseline",
                  padding: "13px 0",
                  borderBottom:
                    i < (scene.list?.length ?? 0) - 1
                      ? "1px solid rgba(255,255,255,0.12)"
                      : "none",
                  fontFamily: FONTS.body,
                }}
              >
                <span style={{ fontSize: 38, fontWeight: 700, color: COLORS.crema }}>
                  {item.label}
                </span>
                <span style={{ fontSize: 38, fontWeight: 800, color: COLORS.oroChiaro }}>
                  {item.value}
                </span>
              </div>
            </Rise>
          ))}
        </div>
        {scene.listFooter ? (
          <Rise delay={10 + (scene.list?.length ?? 0) * 4}>
            <div
              style={{
                fontFamily: FONTS.body,
                fontWeight: 700,
                fontSize: 30,
                color: COLORS.oroChiaro,
                textShadow: SHADOW.testo,
                textAlign: "center",
              }}
            >
              {scene.listFooter}
            </div>
          </Rise>
        ) : null}
      </AbsoluteFill>
      <SegmentedProgress
        count={count}
        index={index}
        sceneProgress={frame / durationInFrames}
      />
    </AbsoluteFill>
  );
};
