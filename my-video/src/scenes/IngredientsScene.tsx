import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Fade, Grade, Title } from "../components/Overlays";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

export const IngredientsScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const scale = interpolate(frame, [0, durationInFrames], [1.04, 1.12], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill>
      {scene.bgImage ? (
        <AbsoluteFill style={{ transform: `scale(${scale})` }}>
          <Img
            src={staticFile(scene.bgImage)}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </AbsoluteFill>
      ) : (
        <ClipLayer
          src={scene.src}
          clipDurationInSeconds={scene.clipDurationInSeconds}
          sceneDurationInSeconds={scene.durationInSeconds}
          label={scene.id}
        />
      )}
      <Grade scrim="center" />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 64,
          gap: 18,
        }}
      >
        <Fade>
          <div style={{ textAlign: "center" }}>
            {scene.emoji ? (
              <div style={{ fontSize: 60, lineHeight: 1, marginBottom: 6 }}>
                {scene.emoji}
              </div>
            ) : null}
            {scene.title ? (
              <Title size={72} align="center">
                {scene.title}
              </Title>
            ) : null}
          </div>
        </Fade>
        <div
          style={{
            width: "100%",
            maxWidth: 840,
            background:
              "linear-gradient(180deg, rgba(18,12,8,0.6), rgba(10,7,4,0.7))",
            backdropFilter: "blur(7px)",
            WebkitBackdropFilter: "blur(7px)",
            borderRadius: 24,
            padding: "22px 34px",
            boxShadow: SHADOW.card,
          }}
        >
          {scene.list?.map((item, i) => (
            <Fade key={item.label} delay={6 + i * 4} distance={20}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "baseline",
                  padding: "12px 2px",
                  borderBottom:
                    i < (scene.list?.length ?? 0) - 1
                      ? "1px solid rgba(255,255,255,0.13)"
                      : "none",
                  fontFamily: FONTS.body,
                }}
              >
                <span
                  style={{
                    fontSize: 40,
                    fontWeight: 700,
                    color: COLORS.crema,
                    textShadow: SHADOW.testo,
                  }}
                >
                  {item.label}
                </span>
                <span
                  style={{
                    fontFamily: FONTS.display,
                    fontSize: 42,
                    color: COLORS.oroChiaro,
                    textShadow: SHADOW.testo,
                  }}
                >
                  {item.value}
                </span>
              </div>
            </Fade>
          ))}
        </div>
        {scene.listFooter ? (
          <Fade delay={6 + (scene.list?.length ?? 0) * 4}>
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
          </Fade>
        ) : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
