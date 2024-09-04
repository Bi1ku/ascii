from PIL import Image as PImage
import numpy as np
import math
import os


density = " .:-=+*#%@"
width = os.get_terminal_size().columns


class Image:
    def __init__(self, path, reverse=False):
        self.path = path
        self.reverse = reverse

    def generate(self):
        with PImage.open(self.path) as img:
            data = np.asarray(img, dtype=np.float64)

            inc = math.ceil(len(data[0]) / width)
            row_idx = 0

            while row_idx < len(data):
                ascii = ""
                pixel_idx = 0

                while pixel_idx < len(data[round(row_idx)]):
                    density_idx = round(
                        sum(data[round(row_idx)][pixel_idx][:3] / 3)
                        * ((len(density) - 1) / 255)
                    )

                    ascii += str(
                        density[::-1][density_idx]
                        if self.reverse
                        else density[density_idx]
                    )

                    pixel_idx += inc

                row_idx += inc * 2.7
                print(ascii)
