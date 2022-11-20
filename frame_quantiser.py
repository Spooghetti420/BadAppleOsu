from pathlib import Path
from PIL import Image
from common import FRAMES, QUANTISED

def quantise(im: Image.Image):
    pixels = [ ((255,255,255) if (pixel[0]+pixel[1]+pixel[2])/3 > 127 else (0,0,0)) for pixel in list(im.getdata()) ]
    im.putdata(pixels)

def main():
    for path in FRAMES.iterdir():
        num = path.stem + ".bmp"
        if (QUANTISED / num).exists():
            continue
        i = Image.open(str(path))
        quantise(i)
        i.save(QUANTISED / num)
        print(f"Finished processing file {num}")
        i.close()


if __name__ == "__main__":
    main()