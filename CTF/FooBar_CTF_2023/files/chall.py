import time
import random

from PIL import Image


random.seed(time.time())

flag_matrix = (img := Image.open('flag.png')).load()
w, h = img.size

for i in range(w):
    for j in range(h):
        flag_matrix[i, j] = tuple(
            map(
                lambda x: x ^ random.randint(0, 255),
                flag_matrix[i, j]
            )
        )

img.save('pixelite.png')
