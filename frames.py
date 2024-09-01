import cv2

video_name = "donut"
vidcap = cv2.VideoCapture(f"./videos/{video_name}/{video_name}.mp4")
success, image = vidcap.read()
count = 0

while success:
    cv2.imwrite(f"./videos/{video_name}/frames/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    print("Read a new frame: ", success)
    count += 1
