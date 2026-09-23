from PIL import Image, ImageDraw, ImageFont

img_path = input("Enter your image path: ")
img = Image.open(img_path).convert("RGBA")

watermark_adder = input("Would you like to add a watermark? yes/no: ").strip().lower()
if watermark_adder == "yes":
    watermark_text = input("Please enter your watermark text: ")
    font_size = int(input("Please enter your desired font size: "))
    font = ImageFont.truetype("arial.ttf", font_size)

    # Create a transparent layer for the watermark
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(layer)

    #Measure text
    bbox = sd.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    #Draw watermark
    x = img.width - text_width - 10
    y = img.height - text_height - 10
    sd.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)

    #Transparency of watermark text
    transparency = int(input("Please enter the transparency level (0-255): "))
    for y in range(layer.height):
        for x in range(layer.width):
            r, g, b, a = layer.getpixel((x, y))
            if a > 0:
                layer.putpixel((x, y), (r, g, b, transparency))

    # Merge layers
    watermarked_img = Image.alpha_composite(img, layer)
    show = input("Do you want to see the watermarked image? yes/no: ").strip().lower()
    if show == "yes":
        watermarked_img.show()
else:
    print("No watermark added. Exiting...")
