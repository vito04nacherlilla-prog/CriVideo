import { AbsoluteFill } from "remotion";
import { Scene } from "../lib/scenes";
import { ClipLayer } from "../components/ClipLayer";
import { Kicker, Rise, Scrim } from "../components/Overlays";
import { COLORS, FONTS, SHADOW } from "../lib/theme";

export const IngredientsScene: React.FC<{ scene: Scene }> = ({ scene }) => {
  return (
    <AbsoluteFill>
      <ClipLayer src={scene.src} label={scene.id} />
      <Scrim strength={1.3} />
      <AbsoluteFill
        style={{ justifyContent: "center", alignItems: "center", padding: 70 }}
      >
        <Rise>
          {scene.kicker ? <Kicker>{scene.kicker}</Kicker> : null}
        </Rise>
        <div style={{ height: 28 }} />
        <div
          style={{
            width: "100%",
            maxWidth: 860,
            background: "rgba(20,15,11,0.66)",
            backdropFilter: "blur(6px)",
            borderRadius: 28,
            padding: "28px 34px",
            boxShadow: SHADOW.card,
          }}
        >
          {scene.list?.map((item, i) => (
            <Rise key={item.label} delay={6 + i * 5} distance={30}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "baseline",
                  padding: "14px 0",
                  borderBottom:
                    i < (scene.list?.length ?? 0) - 1
                      ? "1px solid rgba(255,255,255,0.12)"
                      : "none",
                  fontFamily: FONTS.body,
                }}
              >
                <span
                  style={{ fontSize: 38, fontWeight: 600, color: COLORS.crema }}
                >
                  {item.label}
                </span>
                <span
                  style={{ fontSize: 36, fontWeight: 800, color: COLORS.oroForno }}
                >
                  {item.value}
                </span>
              </div>
            </Rise>
          ))}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
