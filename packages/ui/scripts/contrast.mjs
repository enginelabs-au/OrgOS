#!/usr/bin/env node
/**
 * Assert text tokens t1/t2/t3 meet WCAG AA (≥ 4.5:1) on canvas and surface.
 * t4 is decorative and is excluded from this assertion (decision: D-06 proposed).
 */
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const src = readFileSync(join(root, "../src/tokens.ts"), "utf8");

function parseThemes(text) {
  const themes = {};
  for (const key of ["light", "dark", "dimmed"]) {
    const m = text.match(new RegExp(`${key}:\\s*\\{([\\s\\S]*?)\\n  \\},`));
    if (!m) throw new Error(`theme block not found: ${key}`);
    const body = m[1];
    const get = (k) => {
      const hit = body.match(new RegExp(`${k}:\\s*"(#[0-9a-fA-F]{3,8})"`));
      if (!hit) throw new Error(`${key}.${k} hex not found`);
      return hit[1];
    };
    themes[key] = {
      canvas: get("canvas"),
      surface: get("surface"),
      t1: get("t1"),
      t2: get("t2"),
      t3: get("t3"),
    };
  }
  return themes;
}

function hexToRgb(hex) {
  let h = hex.replace("#", "");
  if (h.length === 3) h = h.split("").map((c) => c + c).join("");
  return {
    r: parseInt(h.slice(0, 2), 16),
    g: parseInt(h.slice(2, 4), 16),
    b: parseInt(h.slice(4, 6), 16),
  };
}

function channel(c) {
  const s = c / 255;
  return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
}

function luminance(hex) {
  const { r, g, b } = hexToRgb(hex);
  return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b);
}

export function contrastRatio(fg, bg) {
  const L1 = luminance(fg);
  const L2 = luminance(bg);
  const lighter = Math.max(L1, L2);
  const darker = Math.min(L1, L2);
  return (lighter + 0.05) / (darker + 0.05);
}

const themes = parseThemes(src);
const MIN = 4.5;
const failures = [];
const report = [];

for (const [name, theme] of Object.entries(themes)) {
  for (const token of ["t1", "t2", "t3"]) {
    for (const surface of ["canvas", "surface"]) {
      const ratio = contrastRatio(theme[token], theme[surface]);
      const line = `${name}.${token} on ${surface} (${theme[token]} / ${theme[surface]}) = ${ratio.toFixed(2)}:1`;
      report.push(line);
      if (ratio < MIN) failures.push(line);
    }
  }
}

console.log("Text-token contrast (t4 excluded, decorative-only):");
for (const line of report) console.log(`  ${line}`);

if (failures.length) {
  console.error("\nFAIL — below 4.5:1:");
  for (const line of failures) console.error(`  ${line}`);
  process.exit(1);
}

console.log("\nPASS — t1/t2/t3 ≥ 4.5:1 on canvas and surface for all themes.");
process.exit(0);
