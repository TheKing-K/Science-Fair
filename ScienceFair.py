#https://www.youtube.com/watch?v=6Qs3wObeWwc

from PIL import Image, ImageFilter  #<--Module for blurring

image1 = Image.open("CheesecakePic.png")

#Blur with input for radius (defualt = 2)
image1.filter(ImageFilter.GaussianBlur(15)).save("BlurryCheesecake1.png")

#Basic Blurring
image1.filter(ImageFilter.BLUR()).save("BlurryCheesecake2.png")