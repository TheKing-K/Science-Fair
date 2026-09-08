from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.new("RGB", (300, 300), "blue")

arr = np.array(img)
print("Shape:", arr.shape)

plt.imshow(arr)
plt.title("Test Image")
plt.show()

img.save("test_image.png")
print("Done!")