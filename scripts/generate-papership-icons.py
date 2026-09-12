#!/usr/bin/env python3
"""Build Papership app/tab icons from the owner rounded-square render.

Keeps the purple icon plate. Only the pixels *outside* that plate (black
corners left after the owner cut, plus optional red fringe) become transparent.
"""

from __future__ import annotations

import colorsys
import shutil
import subprocess
from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(
    "/Users/camdouglas/.cursor/projects/Users-camdouglas-papership/assets/"
    "icon2-802a18f2-7307-41f8-9d29-230e46ba9cea.jpg"
)


def is_outside(r: int, g: int, b: int) -> bool:
    if max(r, g, b) < 24:
        return True
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    hue = h * 360.0
    if (hue <= 18 or hue >= 342) and s > 0.35 and v < 0.42 and r > g + 12 and r > b:
        return True
    return False


def _flood(px, w: int, h: int, seeds: list[tuple[int, int]]) -> set[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    q: deque[tuple[int, int]] = deque()
    for x, y in seeds:
        if (x, y) in seen:
            continue
        r, g, b, _ = px[x, y]
        if is_outside(r, g, b):
            seen.add((x, y))
            q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen:
                r, g, b, _ = px[nx, ny]
                if is_outside(r, g, b):
                    seen.add((nx, ny))
                    q.append((nx, ny))
    return seen


def clear_outside(im: Image.Image) -> Image.Image:
    rgba = im.convert("RGBA")
    w, h = rgba.size
    px = rgba.load()
    edge = [(x, 0) for x in range(w)] + [(x, h - 1) for x in range(w)]
    edge += [(0, y) for y in range(h)] + [(w - 1, y) for y in range(h)]
    for x, y in _flood(px, w, h, edge):
        px[x, y] = (0, 0, 0, 0)
    return rgba


def fit(im: Image.Image, size: int, *, opaque: bool = False, content: float = 1.0) -> Image.Image:
    box = max(1, int(size * content))
    out = im.copy()
    out.thumbnail((box, box), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 255) if opaque else (0, 0, 0, 0))
    x = (size - out.width) // 2
    y = (size - out.height) // 2
    canvas.paste(out, (x, y), out)
    return canvas


def write_png(path: Path, im: Image.Image) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)


def main() -> None:
    master = clear_outside(Image.open(SRC))
    brand = ROOT / "brand" / "papership-icon.png"
    write_png(brand, master)

    web = ROOT / "apps" / "web" / "public"
    desktop_pub = ROOT / "apps" / "desktop" / "public"
    tauri = ROOT / "apps" / "desktop" / "src-tauri" / "icons"
    blueprint = ROOT / "docs" / "ui-blueprint" / "blueprint-2" / "assets"

    write_png(web / "papership-icon.png", master)
    write_png(desktop_pub / "papership-icon.png", master)
    write_png(blueprint / "papership-icon.png", fit(master, 1024))
    write_png(tauri / "icon.png", fit(master, 512, opaque=True))

    write_png(web / "favicon-16.png", fit(master, 16))
    write_png(web / "favicon-32.png", fit(master, 32))
    write_png(web / "icon-192.png", fit(master, 192, opaque=True))
    write_png(web / "icon-512.png", fit(master, 512, opaque=True))
    write_png(web / "icon-512-maskable.png", fit(master, 512, opaque=True, content=0.8))
    write_png(web / "apple-touch-icon.png", fit(master, 180, opaque=True))
    fit(master, 32, opaque=True).save(web / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    write_png(desktop_pub / "favicon-32.png", fit(master, 32, opaque=True))
    fit(master, 32, opaque=True).save(
        desktop_pub / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)]
    )
    write_png(desktop_pub / "apple-touch-icon.png", fit(master, 180, opaque=True))

    write_png(tauri / "32x32.png", fit(master, 32, opaque=True))
    write_png(tauri / "128x128.png", fit(master, 128, opaque=True))
    write_png(tauri / "128x128@2x.png", fit(master, 256, opaque=True))
    fit(master, 256, opaque=True).save(
        tauri / "icon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (256, 256)]
    )

    iconset = Path("/tmp/papership.iconset")
    if iconset.exists():
        shutil.rmtree(iconset)
    iconset.mkdir(parents=True)
    mapping = {
        "icon_16x16.png": 16,
        "icon_16x16@2x.png": 32,
        "icon_32x32.png": 32,
        "icon_32x32@2x.png": 64,
        "icon_128x128.png": 128,
        "icon_128x128@2x.png": 256,
        "icon_256x256.png": 256,
        "icon_256x256@2x.png": 512,
        "icon_512x512.png": 512,
        "icon_512x512@2x.png": 1024,
    }
    for name, size in mapping.items():
        write_png(iconset / name, fit(master, size, opaque=True))
    subprocess.run(["iconutil", "-c", "icns", "-o", str(tauri / "icon.icns"), str(iconset)], check=True)

    print("wrote", brand, "size", master.size, "transparent", sum(
        1 for p in master.getdata() if p[3] == 0
    ))


if __name__ == "__main__":
    main()
