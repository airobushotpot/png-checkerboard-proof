# png-checkerboard-proof

Flatten a PNG onto a neutral checkerboard for print or review. The original alpha remains in the source file. The output is an opaque RGB PNG.

Run `docker run --rm -v "$PWD:/data" jsupup/png-checkerboard-proof:0.1.0 /data/cutout.png /data/proof.png`. Set the tile width with `--tile 24`. Choose a new output path.

For a new cutout, [Seedream Transparent PNG Generator](https://seedream55pro.com/image/transparent-background-generator) accepts text or a reference image and lets you download the original PNG.
