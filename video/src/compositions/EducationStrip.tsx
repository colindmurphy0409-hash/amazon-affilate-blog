import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { BRAND, EducationStripProps } from "../brand";

export const EducationStrip: React.FC<EducationStripProps> = ({
  title,
  tips,
  productImage,
  cta,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleSpring = spring({ frame, fps, config: { damping: 14 } });

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.cream, fontFamily: "sans-serif" }}>
      <AbsoluteFill style={{ padding: 56, paddingTop: 100 }}>
        <div
          style={{
            color: BRAND.primaryDark,
            fontSize: 28,
            fontWeight: 700,
            letterSpacing: 2,
            textTransform: "uppercase",
            marginBottom: 16,
          }}
        >
          Did you know?
        </div>
        <div
          style={{
            color: BRAND.ink,
            fontSize: 52,
            fontWeight: 800,
            lineHeight: 1.15,
            opacity: interpolate(titleSpring, [0, 1], [0, 1]),
          }}
        >
          {title}
        </div>
      </AbsoluteFill>

      <AbsoluteFill style={{ justifyContent: "center", padding: 56, paddingTop: 280, gap: 24 }}>
        {tips.map((tip, i) => {
          const start = Math.round((i + 1) * 1.5 * fps);
          const s = spring({ frame: frame - start, fps, config: { damping: 14 } });
          return (
            <div
              key={tip}
              style={{
                color: BRAND.inkSoft,
                fontSize: 32,
                fontWeight: 600,
                opacity: interpolate(s, [0, 1], [0, 1]),
              }}
            >
              {i + 1}. {tip}
            </div>
          );
        })}
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: 80,
          flexDirection: "row",
          gap: 32,
        }}
      >
        <Img
          src={staticFile(`assets/products/${productImage}`)}
          style={{ width: 120, height: 120, objectFit: "contain" }}
        />
        <div style={{ color: BRAND.primaryDark, fontSize: 28, fontWeight: 700 }}>{cta}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
