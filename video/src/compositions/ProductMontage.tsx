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
import { BRAND, ProductMontageProps } from "../brand";

export const ProductMontage: React.FC<ProductMontageProps> = ({
  productImage,
  bullets,
  cta,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.surface, fontFamily: "sans-serif" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", paddingTop: 40 }}>
        <Img
          src={staticFile(`assets/products/${productImage}`)}
          style={{ width: 520, height: 520, objectFit: "contain" }}
        />
      </AbsoluteFill>
      <AbsoluteFill style={{ justifyContent: "flex-end", padding: 56, paddingBottom: 90, gap: 20 }}>
        {bullets.map((bullet, i) => {
          const start = Math.round((i + 1) * 1.2 * fps);
          const s = spring({ frame: frame - start, fps, config: { damping: 14 } });
          const opacity = interpolate(s, [0, 1], [0, 1]);
          return (
            <div
              key={bullet}
              style={{
                color: BRAND.ink,
                fontSize: 34,
                fontWeight: 600,
                opacity,
                borderLeft: `6px solid ${BRAND.primary}`,
                paddingLeft: 20,
              }}
            >
              {bullet}
            </div>
          );
        })}
        <div style={{ color: BRAND.primaryDark, fontSize: 30, fontWeight: 700, marginTop: 16 }}>
          {cta}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
