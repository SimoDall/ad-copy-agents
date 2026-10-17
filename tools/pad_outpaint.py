"""Prepara una tela e una maschera per l'outpainting con openai/gpt-image-2/edit.

L'immagine originale viene ridimensionata in modo uniforme (senza stiramento)
in un quadrato di lato min(W, H) e centrata su una tela W x H. I bordi della
tela sono estesi e sfumati. La maschera ha alpha 0 (trasparente) dove il modello
deve generare, e alpha 255 sull'immagine originale.

Uso:
    python3 tools/pad_outpaint.py <immagine.png> <tela_out.png> <maschera_out.png> <W> <H>

Esempi: 1088 608 (16:9), 608 1088 (9:16).
"""
import sys

import numpy as np
from PIL import Image, ImageFilter


def main() -> None:
    src, out_img, out_mask = sys.argv[1], sys.argv[2], sys.argv[3]
    w, h = int(sys.argv[4]), int(sys.argv[5])

    im = Image.open(src).convert("RGB")
    side = min(w, h)
    im = im.resize((side, side), Image.LANCZOS)  # scala uniforme, nessuno stiramento
    pad_x, pad_y = (w - side) // 2, (h - side) // 2

    padded = np.pad(
        np.array(im),
        ((pad_y, h - side - pad_y), (pad_x, w - side - pad_x), (0, 0)),
        mode="edge",
    )
    canvas = Image.fromarray(padded).filter(ImageFilter.GaussianBlur(6))
    canvas.paste(im, (pad_x, pad_y))
    canvas.save(out_img)

    alpha = np.zeros((h, w), dtype=np.uint8)
    alpha[pad_y:pad_y + side, pad_x:pad_x + side] = 255
    mask = np.zeros((h, w, 4), dtype=np.uint8)
    mask[..., 3] = 255 - alpha  # trasparente = zona da generare
    Image.fromarray(mask, "RGBA").save(out_mask)

    print(f"tela {w}x{h} -> {out_img}; maschera -> {out_mask}; quadrato {side}px a ({pad_x},{pad_y})")


if __name__ == "__main__":
    main()
