#!/usr/bin/env python3
"""Builds the page's pixel art from the game repository (next to this one, ../fisherman-charm):

  img/og.jpg        the 1200x630 link preview: the key art's sunset sky and sea run the full width,
                    the fisher, the dog and the pier on the right on the painting's own pixel grid
                    (8 screen pixels per art pixel), the game's logo (assets/art/logo.png) on the left
  img/icon.png      the app icon (icon.png)

    python3 tools/build_images.py [path/to/fisherman-charm]
"""
import shutil
import sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent.parent
GAME = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "fisherman-charm"
PAINTING = GAME / "assets/pixellab-generated/_raw/key_art/key_art_wide.png"   # 72x128, logo-free
S = 8                    # screen pixels per art pixel in the preview
OG_W, OG_H = 150, 79     # the preview in art pixels (x8 = 1200x632, cut to 630)
SCENE_TOP = 14           # the painting's row at the top of the preview
HORIZON = 30             # the painting's first row of sea


def og() -> Image.Image:
    paint = Image.open(PAINTING).convert("RGBA")
    rows = paint.crop((0, SCENE_TOP, paint.width, SCENE_TOP + OG_H))
    from collections import Counter
    sea = Counter(paint.crop((56, 90, 72, 128)).get_flattened_data()).most_common(1)[0][0]
    out = Image.new("RGBA", (OG_W, OG_H))
    for y in range(OG_H):   # the sky's bands carried across from the painting's left edge; the sea flat
        c = rows.getpixel((0, y)) if SCENE_TOP + y < HORIZON else sea
        for x in range(OG_W):
            out.putpixel((x, y), c)
    shades = {c for c in paint.get_flattened_data()   # the painting's water shades (its teals): all
              if c[1] > c[0] + 60 and c[2] > c[0] + 60}   # one sea, so there's no seam
    scene = rows.copy()
    for y in range(max(0, HORIZON - SCENE_TOP), OG_H):
        for x in range(scene.width):
            if scene.getpixel((x, y)) in shades:
                scene.putpixel((x, y), sea)
    out.alpha_composite(scene, (OG_W - paint.width, 0))   # the scene on the right
    big = out.resize((OG_W * S, OG_H * S), Image.NEAREST).crop((0, 0, 1200, 630))
    # the game's logo (painted, so scaled smoothly) over the open sea on the left
    lg = Image.open(GAME / "assets/art/logo.png").convert("RGBA")
    w = (OG_W - paint.width) * S - 40
    lg = lg.resize((w, round(w * lg.height / lg.width)), Image.LANCZOS)
    big.alpha_composite(lg, (20, (630 - lg.height) // 2 - 30))
    return big.convert("RGB")


def main() -> None:
    img = HERE / "img"
    og().save(img / "og.jpg", quality=92)
    shutil.copyfile(GAME / "icon.png", img / "icon.png")
    print("wrote img/og.jpg, img/icon.png")


if __name__ == "__main__":
    main()
