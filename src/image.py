from PIL import Image as PImage
import numpy as np
import math
import os


width = os.get_terminal_size().columns
density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


class Image:
    def __init__(self, path):
        self.path = path

    def generate(self):
        with PImage.open(self.path) as img:
            data = np.asarray(img, dtype=np.float64)

            inc = math.ceil(len(data[0]) / width)
            row_idx = 0

            while row_idx < len(data):
                ascii = ""
                pixel_idx = 0

                while pixel_idx < len(data[round(row_idx)]):
                    ascii += str(
                        density[
                            round(
                                sum(data[round(row_idx)][pixel_idx][:3] / 3)
                                * ((len(density) - 1) / 255)
                            )
                        ]
                    )

                    pixel_idx += inc

                row_idx += inc * 2
                print(ascii)
