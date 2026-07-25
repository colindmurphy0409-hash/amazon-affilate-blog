import React from "react";
import { Composition } from "remotion";
import { HookReel } from "./compositions/HookReel";
import { ProductMontage } from "./compositions/ProductMontage";
import { EducationStrip } from "./compositions/EducationStrip";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="HookReel"
        component={HookReel}
        durationInFrames={450}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          hook: "3pm and I'm done. Unless...",
          productImage: "energy-strips.png",
          captionLines: ["Clean lift", "Zero crash", "No water needed"],
          cta: "wellthlab.shop",
        }}
      />
      <Composition
        id="ProductMontage"
        component={ProductMontage}
        durationInFrames={600}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          productImage: "energy-strips.png",
          bullets: ["Dissolves on your tongue", "No water. No pills.", "Third-party tested"],
          cta: "Shop → wellthlab.shop",
        }}
      />
      <Composition
        id="EducationStrip"
        component={EducationStrip}
        durationInFrames={750}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Why strips beat pills",
          tips: [
            "No water needed — dissolve on your tongue",
            "Fits in a pocket tin",
            "Clean label, real doses",
          ],
          productImage: "energy-strips.png",
          cta: "wellthlab.shop",
        }}
      />
    </>
  );
};
