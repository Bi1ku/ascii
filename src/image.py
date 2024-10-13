from PIL import Image as PImage
import numpy as np
import math
import os
import matplotlib.pyplot as plt


density = " .:-=+*#%@"
width = os.get_terminal_size().columns
height_offset = (
    3.3  # Because in text, the height of a character is larger than the width
)


class Image:
    def __init__(self, path, reverse=False):
        self.path = path
        self.reverse = reverse

    def generate(self):
        img = plt.imread(self.path)
        inc = math.ceil(len(img[0]) / width)

        img_type = self.path.split("/")[-1].split(".")[1]
        if img_type == "jpg" or img_type == "jpeg":
            img = img[:, :, :] / 255  # Convert rgb to percentages

        row_idx = 0
        pixel_idx = 0

        while row_idx < len(img):
            ascii = ""
            pixel_idx = 0

            while pixel_idx < len(img[row_idx]):
                density_idx = round(
                    sum(img[row_idx][pixel_idx][:3]) / 3 * (len(density) - 1)
                )
                ascii += str(
                    density[::-1][density_idx] if self.reverse else density[density_idx]
                )

                pixel_idx += inc

            print(ascii)
            row_idx += round((inc * len(img)) / len(img[0]) * height_offset)
