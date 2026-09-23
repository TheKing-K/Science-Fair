from PIL import Image, ImageDraw, ImageFont
im = Image.open("CheesecakePic.png").convert("RGBA") #Open "CheesecakePic.png" with alpha layer

sym = Image.new('RGBA', (980, 980), (0, 0, 0, 0)) #Create filter image with alpha layer
sd = ImageDraw.Draw(sym) #Convert to drawable image

#                                    R, G, B  , A
sd.ellipse((90,90,890,890), outline=(0, 0, 255, 10), width=20) #Draws a thick blue circle

sd.line((490,90,490,890), fill=(0, 0, 255, 10), width=20) #Draws a thick blue plus sign
sd.line((90,490,890,490), fill=(0, 0, 255, 10), width=20)

#Draws diagonal watermark text
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 30)
text = Image.new('RGBA', (sym.width * 2, sym.height * 2), (0, 0, 0, 0))
td = ImageDraw.Draw(text)
for y in range(0, text.height, 120):
	for x in range(0, text.width, 220):
		td.text((x, y), "SCIENCE FAIR", font=font, fill=(0, 0, 255, 20))
text = text.rotate(40)
text = text.crop(((text.width - sym.width) // 2, (text.height - sym.height) // 2,
				  (text.width + sym.width) // 2, (text.height + sym.height) // 2))
sym = Image.alpha_composite(sym, text)

sym.save("WatermarkBASE.png")

Image.alpha_composite(im, sym).save("WatermarkedBLUE.png")
Image.open("WatermarkedBLUE.png").show()