from PIL import Image, ImageDraw

im = Image.open("CheesecakePic.png").convert("RGBA") #Open "CheesecakePic.png" with alpha layer

sym = Image.new('RGBA', (980, 980), (0, 0, 0, 0)) #Create filter image with alpha layer
sd = ImageDraw.Draw(sym) #Convert to drawable image

#                                    R, G, B  , A
sd.ellipse((90,90,890,890), outline=(0, 0, 255, 20), width=20) #Draws a thick blue circle

sd.line((490,90,490,890), fill=(0, 0, 255, 20), width=20) #Draws a thick blue plus sign
sd.line((90,490,890,490), fill=(0, 0, 255, 20), width=20)

sym.save("WatermarkBASE.png")

Image.alpha_composite(im, sym).save("WatermarkedBLUE.png")