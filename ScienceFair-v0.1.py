#https://www.youtube.com/watch?v=6Qs3wObeWwc

from PIL import Image
import os

for f in os.listdir("."):
    if os.path.splitext(f)[1].lower() == ".png":
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        #i.convert(mode="L").save(f"{fn}-grayscale{fext}")
        #i.convert(mode="P").save(f"{fn}-8bit{fext}")
        i.convert(mode="RGBA").save(f"{fn}-alpha{fext}")  #<-- Allows for transparency

image1 = Image.open('CheesecakePic.png')
image1.rotate(90).save('Cheesecake+90.png')

image1.convert("RGBA")
image1.putalpha(128)
image1.save("CheesecakeTRAN.png")