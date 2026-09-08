from PIL import Image
import numpy as np

# Create a blue image
img = Image.new("RGB", (300, 300), "blue")

# Convert the image to a NumPy array so we can edit pixels
img_array = np.array(img)

# Change a square in the middle to white
img_array[100:200, 100:200] = [255, 255, 255]

# Convert the array back to an image
result = Image.fromarray(img_array)

# Save the result to a file
result.save("science_fair_result.png")

print("Image saved as science_fair_result.png")
print("Image shape:", img_array.shape)