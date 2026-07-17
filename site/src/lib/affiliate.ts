import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';

export interface AffiliateConfig {
  associate_tag: string;
  store_id?: string;
  site_url: string;
  site_name: string;
  site_tagline: string;
  disclosure_short: string;
  disclosure_full: string;
}

export interface AsinData {
  asin: string;
  title: string;
  niche?: 'beauty' | 'fitness' | 'home' | string;
  price_band?: string;
  rating?: number;
  review_count?: number;
  affiliate_url?: string;
  image_url?: string;
  pros?: string[];
  cons?: string[];
  best_for?: string;
}

const siteRoot = path.resolve(import.meta.dirname, '../..');
const repoRoot = path.resolve(siteRoot, '..');

function readYamlFile<T>(filePath: string): T | null {
  if (!fs.existsSync(filePath)) return null;
  return parseYaml(fs.readFileSync(filePath, 'utf8')) as T;
}

export function getAffiliateConfig(): AffiliateConfig {
  const paths = [
    path.join(siteRoot, 'data', 'affiliate-config.yaml'),
    path.join(repoRoot, 'affiliate', 'config.yaml'),
    path.join(repoRoot, 'affiliate', 'config.example.yaml'),
  ];

  for (const configPath of paths) {
    const config = readYamlFile<AffiliateConfig>(configPath);
    if (config) {
      return {
        site_name: 'Wellth Lab',
        site_tagline: 'Research-backed product guides you can trust',
        ...config,
      };
    }
  }

  throw new Error('Missing affiliate config (site/data/affiliate-config.yaml)');
}

export function getAssociateTag(): string {
  const config = getAffiliateConfig();
  return config.associate_tag || config.store_id || 'wellthlab-20';
}

export function buildAmazonUrl(asin: string, tag?: string): string {
  const associateTag = tag ?? getAssociateTag();
  return `https://www.amazon.com/dp/${asin}?tag=${associateTag}`;
}

export function buildAmazonImageUrl(asin: string): string {
  return `/images/products/${asin}.jpg`;
}

export function buildAmazonImageFallbackUrl(asin: string, size = 500): string {
  return `https://images-na.ssl-images-amazon.com/images/P/${asin}.01._SL${size}_.jpg`;
}

export function resolveProductImageSrc(data: Pick<AsinData, 'asin' | 'image_url'>): {
  primary: string;
  fallback: string;
} {
  return {
    primary: buildAmazonImageUrl(data.asin),
    fallback: data.image_url ?? buildAmazonImageFallbackUrl(data.asin),
  };
}

export function getAsinData(asin: string): AsinData | null {
  const paths = [
    path.join(siteRoot, 'data', 'asins', `${asin}.yaml`),
    path.join(repoRoot, 'affiliate', 'asins', `${asin}.yaml`),
  ];

  let data: AsinData | null = null;
  for (const asinPath of paths) {
    data = readYamlFile<AsinData>(asinPath);
    if (data) break;
  }

  if (!data) return null;

  const tag = getAssociateTag();
  if (!data.affiliate_url || !data.affiliate_url.includes(`tag=${tag}`)) {
    data.affiliate_url = buildAmazonUrl(asin, tag);
  }

  return data;
}

export function getAsinDataList(asins: string[]): AsinData[] {
  return asins
    .map((asin) => getAsinData(asin))
    .filter((item): item is AsinData => item !== null);
}

export function nicheLabel(niche?: string): string {
  switch (niche) {
    case 'beauty':
      return 'Beauty';
    case 'fitness':
      return 'Fitness';
    case 'home':
      return 'Home';
    default:
      return 'Guide';
  }
}

export function nicheBadgeClass(niche?: string): string {
  switch (niche) {
    case 'beauty':
      return 'badge-beauty';
    case 'fitness':
      return 'badge-fitness';
    case 'home':
      return 'badge-home';
    default:
      return 'badge-type';
  }
}

export function nicheStripClass(niche?: string): string {
  switch (niche) {
    case 'beauty':
      return 'card-strip-beauty';
    case 'fitness':
      return 'card-strip-fitness';
    case 'home':
      return 'card-strip-home';
    default:
      return 'card-strip-default';
  }
}
