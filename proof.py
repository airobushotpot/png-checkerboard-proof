import argparse
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser(description="Render a checkerboard alpha proof")
parser.add_argument("input")
parser.add_argument("output")
parser.add_argument("--tile", type=int, default=16)
args = parser.parse_args()
if args.tile < 1:
    parser.error("tile width must be positive")
with Image.open(args.input, formats=["PNG"]) as source:
    rgba = source.convert("RGBA")
tile = min(args.tile, max(rgba.size))
pattern = Image.new("RGB", (min(tile * 2, rgba.width), min(tile * 2, rgba.height)), "#eeeeee")
draw = ImageDraw.Draw(pattern)
for x, y in [(tile, 0), (0, tile)]:
    draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill="#aaaaaa")
background = Image.new("RGB", rgba.size)
for y in range(0, rgba.height, pattern.height):
    for x in range(0, rgba.width, pattern.width):
        background.paste(pattern, (x, y))
background.paste(rgba, (0, 0), rgba.getchannel("A"))
with open(args.output, "xb") as output:
    background.save(output, format="PNG")
