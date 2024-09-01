from PIL import Image
import simpleaudio as sa
import numpy as np
import math
import os
import time

width = os.get_terminal_size().columns
density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."
video = "donut"

frame = 0

# audio = sa.WaveObject.from_wave_file(f"./videos/{video}/audio.wav")


def generate_frame():
    with Image.open(f"videos/{video}/frames/frame{frame}.jpg") as img:
        data = np.asarray(img, dtype=np.float64)

        row_idx = 0
        inc = math.ceil(len(data[0]) / width)

        while row_idx < len(data):
            line = ""
            pixel_idx = 0

            while pixel_idx < len(data[round(row_idx)]):
                line += str(
                    density[
                        round(
                            sum(data[round(row_idx)][pixel_idx][:3] / 3)
                            * ((len(density) - 1) / 255)
                        )
                    ]
                )

                pixel_idx += inc

            row_idx += inc * 2
            print(line)


# audio.play()
while 1:
    try:
        generate_frame()
        frame += 1
        time.sleep(1 / 60)
        os.system("cls" if os.name == "nt" else "clear")
    except:
        print("END")
