#https://www.youtube.com/watch?v=6Qs3wObeWwc

from PIL import Image
import os

image1 = Image.open("CheesecakePic.jpg")

#image1.show()  <-- Show Image
#image1.save("CheesecakePic.png")   <-- Save as .png

for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("test-jpgs/{}.jpg".format(fn))