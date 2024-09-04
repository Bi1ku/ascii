import os
import time
from image import Image
import simpleaudio as sa
import cv2 as cv


class Video:
    def __init__(self, name, fps=60):
        self.frame = 0
        self.name = name
        self.audio = sa.WaveObject.from_wave_file(
            f"../videos/{name}/audio.wav")
        self.fps = fps
        self.frames_path = f"../videos/{self.name}/frames"

    def create_frames(self):
        for f in os.listdir(self.frames_path):
            if os.path.isfile(os.path.join(self.frames_path, f)):
                print(f)
                return

        vidcap = cv.VideoCapture(f"../videos/{self.name}/video.mp4")
        exists, image = vidcap.read()
        count = 0

        while exists:
            cv.imwrite(f"{self.frames_path}/frame%d.jpg" % count, image)
            exists, image = vidcap.read()

            if exists:
                print(f"Created frame #{count}")
                count += 1

    def play(self):
        self.audio.play()

        count = 0
        while 1:
            if not os.path.isfile(os.path.join(self.frames_path, f"frame{count}.jpg")):
                return

            frame = Image(f"{self.frames_path}/frame{self.frame}.jpg")
            frame.generate()
            self.frame += 1
            time.sleep(1 / self.fps)
            os.system("cls" if os.name == "nt" else "clear")
            count += 1
