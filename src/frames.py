import cv2 as cv

name = "spiral"
vidcap = cv.VideoCapture(f"../videos/{name}/video.mp4")
exists, image = vidcap.read()
count = 0

while exists:
    cv.imwrite(f"../videos/{name}/frames/frame%d.jpg" % count, image)
    exists, image = vidcap.read()

    if exists:
        print(f"Created frame #{count}")
        count += 1
