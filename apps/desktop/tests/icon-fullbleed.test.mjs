import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const icons = join(dirname(fileURLToPath(import.meta.url)), "../src-tauri/icons");

test("Tauri icons are full-bleed so the OS can apply its squircle", () => {
  const script = `
from PIL import Image
from pathlib import Path
root = Path(${JSON.stringify(icons)})
for name in ("32x32.png", "128x128.png", "128x128@2x.png", "icon.png"):
    im = Image.open(root / name).convert("RGBA")
    w, h = im.size
    corners = [im.getpixel((0, 0)), im.getpixel((w - 1, 0)), im.getpixel((0, h - 1)), im.getpixel((w - 1, h - 1))]
    assert all(p[3] == 255 for p in corners), f"{name} transparent corner {corners}"
    assert all(p[0] + p[1] + p[2] > 40 for p in corners), f"{name} dark gutter {corners}"
    cx, cy = w // 2, h // 2
    mid = im.getpixel((cx, cy))
    assert mid[3] == 255 and sum(mid[:3]) > 40, f"{name} empty center {mid}"
print("ok")
`;
  const out = execFileSync("python3", ["-c", script], { encoding: "utf8" });
  assert.match(out, /ok/);
});
