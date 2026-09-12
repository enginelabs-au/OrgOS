#!/usr/bin/env python3
"""Build Papership app/tab icons from the owner source render."""

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
    "icon2-63a104f3-e32e-4941-bfa5-a8eecc2e9072-ba6e1cf4-7c4a-49ef-992f-faebd1847cd7.jpg"
)
IOS_FILL = (22, 8, 46, 255)  # #16082e — opaque for Apple touch icons


def is_outer_black(r: int, g: int, b: int) -> bool:
    return max(r, g, b) < 22


def is_purple_field(r: int, g: int, b: int) -> bool:
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    hue = h * 360.0
    if s < 0.22 or v < 0.08:
        return False
    if 185 <= hue <= 255 and v > 0.28:
        return False
    if 30 <= hue <= 85 and s > 0.25:
        return False
    if (hue <= 25 or hue >= 335) and s > 0.28 and v > 0.35:
        return False
    return 255 <= hue <= 335 or (hue >= 250 and s > 0.35 and v < 0.72)


def crop_to_mark(im: Image.Image, pad_ratio: float = 0.06) -> Image.Image:
    bbox = im.getbbox()
    if not bbox:
        return im
    left, top, right, bottom = bbox
    pad = int(max(right - left, bottom - top) * pad_ratio)
    left = max(0, left - pad)
    top = max(0, top - pad)
    right = min(im.width, right + pad)
    bottom = min(im.height, bottom + pad)
    cropped = im.crop((left, top, right, bottom))
    side = max(cropped.width, cropped.height)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(cropped, ((side - cropped.width) // 2, (side - cropped.height) // 2), cropped)
    return canvas


def _flood(px, w: int, h: int, seeds: list[tuple[int, int]], accept) -> set[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    q: deque[tuple[int, int]] = deque()
    for x, y in seeds:
        if (x, y) in seen:
            continue
        r, g, b, _ = px[x, y]
        if accept(r, g, b):
            seen.add((x, y))
            q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen:
                r, g, b, _ = px[nx, ny]
                if accept(r, g, b):
                    seen.add((nx, ny))
                    q.append((nx, ny))
    return seen


def is_mark(r: int, g: int, b: int) -> bool:
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    hue = h * 360.0
    if v > 0.62 and s < 0.28:
        return True
    if 185 <= hue <= 255 and v > 0.22:
        return True
    if 25 <= hue <= 80 and s > 0.28 and v > 0.35:
        return True
    if (hue <= 25 or hue >= 335) and s > 0.28 and v > 0.35:
        return True
    if 80 <= hue <= 170 and s > 0.28 and v > 0.3:
        return True
    return False


def cut_field(im: Image.Image) -> Image.Image:
    src = im.convert("RGBA")
    rgba = src.copy()
    w, h = rgba.size
    px = rgba.load()
    src_px = src.load()
    edge = [(x, 0) for x in range(w)] + [(x, h - 1) for x in range(w)]
    edge += [(0, y) for y in range(h)] + [(w - 1, y) for y in range(h)]
    black = _flood(px, w, h, edge, is_outer_black)
    purple_seeds = list(black)
    for x, y in edge:
        r, g, b, _ = px[x, y]
        if is_purple_field(r, g, b):
            purple_seeds.append((x, y))
    for x, y in list(black):
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h:
                purple_seeds.append((nx, ny))
    purple = _flood(px, w, h, purple_seeds, is_purple_field)
    for x, y in black | purple:
        px[x, y] = (0, 0, 0, 0)
    for y in range(h):
        for x in range(w):
            r, g, b, a = src_px[x, y]
            if a and is_mark(r, g, b):
                px[x, y] = (r, g, b, 255)
    return rgba


def fit(im: Image.Image, size: int, *, opaque: bool = False, content: float = 1.0) -> Image.Image:
    box = max(1, int(size * content))
    out = im.copy()
    out.thumbnail((box, box), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), IOS_FILL if opaque else (0, 0, 0, 0))
    x = (size - out.width) // 2
    y = (size - out.height) // 2
    canvas.paste(out, (x, y), out)
    return canvas


def write_png(path: Path, im: Image.Image) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)


def main() -> None:
    master = crop_to_mark(cut_field(Image.open(SRC)))
    brand = ROOT / "brand" / "papership-icon.png"
    write_png(brand, master)

    web = ROOT / "apps" / "web" / "public"
    desktop_pub = ROOT / "apps" / "desktop" / "public"
    tauri = ROOT / "apps" / "desktop" / "src-tauri" / "icons"
    blueprint = ROOT / "docs" / "ui-blueprint" / "blueprint-2" / "assets"

    write_png(web / "papership-icon.png", master)
    write_png(desktop_pub / "papership-icon.png", master)
    write_png(blueprint / "papership-icon.png", fit(master, 1024, opaque=True))
    write_png(tauri / "icon.png", fit(master, 512, opaque=True))

    write_png(web / "favicon-16.png", fit(master, 16, opaque=True))
    write_png(web / "favicon-32.png", fit(master, 32, opaque=True))
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

    stale = [
        ROOT / "brand" / "orgos-icon.png",
        web / "orgos-icon.png",
        desktop_pub / "orgos-icon.png",
        blueprint / "orgos-icon.png",
        ROOT / "docs" / "ui-blueprint" / "blueprint-2" / "uploads" / "icon-1789127412584-udcn.png",
    ]
    for path in stale:
        if path.exists():
            path.unlink()

    print("wrote", brand, "size", master.size)


if __name__ == "__main__":
    main()
