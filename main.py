from email.mime import image
from PIL import Image
import sys
import os

if len(sys.argv)<=1:    
    raise Exception("image name not provided in command line arguments ☹️")

imageName = sys.argv[1]

try:

    # defining flag colors of UKRAINE
    color_gold_yellow = (255, 215, 0, 255)
    color_string_azure = (0, 87, 183, 255)
    ####

    def rgbaBlank(i): return 0 if (i == 1) else (0,)*i
    def colorToFill(i, h): return color_gold_yellow if (
        i >= h/2) else color_string_azure

    with Image.open(imageName) as img:
        mode = img.mode
        w, h = img.size
        for j in range(h):
            c = colorToFill(j, h)
            for i in range(w):
                d = (i, j)
                if img.getpixel(d) > rgbaBlank(len(mode)):
                    img.putpixel(d, c)

        img.save(f"uk_{os.path.basename(imageName)}")
except Exception as e:
    print(e)
