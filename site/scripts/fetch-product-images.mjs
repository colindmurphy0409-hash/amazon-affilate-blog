#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse as parseYaml } from 'yaml';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const siteRoot = path.resolve(__dirname, '..');
const asinDir = path.join(siteRoot, 'data', 'asins');
const outDir = path.join(siteRoot, 'public', 'images', 'products');

const MIN_BYTES = 500;

function amazonFallback(asin) {
  return `https://images-na.ssl-images-amazon.com/images/P/${asin}.01._SL500_.jpg`;
}

async function download(url, dest) {
  const res = await fetch(url, {
    headers: { 'User-Agent': 'WellthLabBuild/1.0' },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  if (buf.length < MIN_BYTES) throw new Error(`too small (${buf.length} bytes)`);
  fs.writeFileSync(dest, buf);
  return buf.length;
}

async function main() {
  fs.mkdirSync(outDir, { recursive: true });
  const files = fs.readdirSync(asinDir).filter((f) => f.endsWith('.yaml'));

  for (const file of files) {
    const data = parseYaml(fs.readFileSync(path.join(asinDir, file), 'utf8'));
    const asin = data.asin;
    if (!asin) continue;

    const dest = path.join(outDir, `${asin}.jpg`);
    const sources = [data.image_url, amazonFallback(asin)].filter(Boolean);

    for (const url of sources) {
      try {
        const size = await download(url, dest);
        console.log(`✓ ${asin} (${size} bytes) ← ${url}`);
        break;
      } catch (err) {
        console.warn(`✗ ${asin} failed ${url}: ${err.message}`);
      }
    }
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
