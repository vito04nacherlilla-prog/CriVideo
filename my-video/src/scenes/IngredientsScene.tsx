import { AbsoluteFill } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Fade, Grade, Title } from "../components/Overlays";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

export const IngredientsScene: React.FC<{ scene: Scene }> = ({ scene }) => {
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
          padding: 70,
          gap: 20,
        }}
      >
        <Fade>
          {scene.title ? (
            <Title size={68} align="center">
              {scene.title}
            </Title>
          ) : null}
        </Fade>
        <div style={{ width: "100%", maxWidth: 820 }}>
          {scene.list?.map((item, i) => (
            <Fade key={item.label} delay={6 + i * 4} distance={18}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "baseline",
                  padding: "12px 4px",
                  borderBottom:
                    i < (scene.list?.length ?? 0) - 1
                      ? "1px solid rgba(255,255,255,0.15)"
                      : "none",
                  fontFamily: FONTS.body,
                }}
              >
                <span
                  style={{
                    fontSize: 40,
                    fontWeight: 700,
                    color: COLORS.bianco,
                    textShadow: SHADOW.testo,
                  }}
                >
                  {item.label}
                </span>
                <span
                  style={{
                    fontSize: 40,
                    fontWeight: 800,
                    color: COLORS.bianco,
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
                color: COLORS.crema,
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
