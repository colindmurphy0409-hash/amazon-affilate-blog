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
import { BRAND, HookReelProps } from "./brand";

export const HookReel: React.FC<HookReelProps> = ({
  hook,
  productImage,
  captionLines,
  cta,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const hookSpring = spring({ frame, fps, config: { damping: 14 } });
  const hookY = interpolate(hookSpring, [0, 1], [40, 0]);
  const hookOpacity = interpolate(hookSpring, [0, 1], [0, 1]);

  const productStart = Math.round(2.5 * fps);
  const productSpring = spring({
    frame: frame - productStart,
    fps,
    config: { damping: 16 },
  });
  const productScale = interpolate(productSpring, [0, 1], [0.85, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.cream, fontFamily: "sans-serif" }}>
      <AbsoluteFill
        style={{
          justifyContent: "flex-start",
          padding: 64,
          paddingTop: 120,
        }}
      >
        <div
          style={{
            color: BRAND.ink,
            fontSize: 64,
            fontWeight: 800,
            lineHeight: 1.1,
            transform: `translateY(${hookY}px)`,
            opacity: hookOpacity,
          }}
        >
          {hook}
        </div>
      </AbsoluteFill>

      {frame >= productStart && (
        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            paddingTop: 80,
          }}
        >
          <Img
            src={staticFile(`assets/products/${productImage}`)}
            style={{
              width: 480,
              height: 480,
              objectFit: "contain",
              transform: `scale(${productScale})`,
            }}
          />
        </AbsoluteFill>
      )}

      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          padding: 64,
          paddingBottom: 100,
          gap: 16,
        }}
      >
        {captionLines.map((line, i) => {
          const lineStart = productStart + Math.round((i + 1) * 0.6 * fps);
          const visible = frame >= lineStart;
          return (
            <div
              key={line}
              style={{
                color: BRAND.inkSoft,
                fontSize: 36,
                fontWeight: 600,
                opacity: visible ? 1 : 0,
              }}
            >
              {line}
            </div>
          );
        })}
        <div
          style={{
            marginTop: 24,
            color: BRAND.primaryDark,
            fontSize: 32,
            fontWeight: 700,
            opacity: frame >= productStart + Math.round(2 * fps) ? 1 : 0,
          }}
        >
          {cta}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
