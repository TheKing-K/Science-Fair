from PIL import Image, ImageFilter

The_specified_image = input("Enter your image path: ")
img = Image.open(The_specified_image)

blur = input("Would you like to blur the image? yes/no: ").strip().lower()
if blur == "yes":
    value = int(input("Please enter your blur value: "))
    img = img.filter(ImageFilter.BoxBlur(value))
if blur == "no":
    print("No blur then. Moving on...")
Sizing = input("Size the image? yes/no:").strip().lower()
if Sizing == "yes":
    Your_width = int(input("Please enter your desired width: "))
    Your_height = int(input("Please enter your desired height: "))
    img = img.resize((Your_width, Your_height))
if Sizing == "no":
    print("Dude, you must edit SOMETHING.")

save = input("Do you want to save the image? yes/no: ").strip().lower()
if save == "yes":
    save_Location = input("Please enter your desired save location (including filename and extension): ")
    img.save(save_Location)
if save == "no":
    print("Tung Tung would be very SAD.")

print("Here is your majestic image.")
print("NOTE: You may see more than one image. This is the images that have been edited by each individual edit. Use the one you want.")
img.show()