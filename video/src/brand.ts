export const BRAND = {
  ink: "#0f172a",
  inkSoft: "#475569",
  cream: "#fafaf8",
  surface: "#f1f5f9",
  primary: "#0d9488",
  primaryDark: "#0f766e",
  border: "#e2e8f0",
};

export type HookReelProps = {
  hook: string;
  productImage: string;
  captionLines: string[];
  cta: string;
};

export type ProductMontageProps = {
  productImage: string;
  bullets: string[];
  cta: string;
};

export type EducationStripProps = {
  title: string;
  tips: string[];
  productImage: string;
  cta: string;
};
