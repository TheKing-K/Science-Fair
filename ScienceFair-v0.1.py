#https://www.youtube.com/watch?v=6Qs3wObeWwc

from PIL import Image
import os

#image1 = Image.open("CheesecakePic.jpg")  <-- Sets 'image1'

#image1.show()  <-- Show Image
#image1.save("CheesecakePic.png")   <-- Save as .png

size_300 = (300,300)  #<-- 300*300 px size set to 'size_300'
size_1080p = (1920, 1080)

for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_1080p)  #<-- Saves to '1080p' folder with size 1920*1080
        i.save("size-1080p-pics/{}-1080p{}".format(fn,fext))

        i.thumbnail(size_300)  #<-- Saves to 'size-300-pics' folder with size 300*300
        i.save("size-300-pics/{}-300{}".format(fn,fext))