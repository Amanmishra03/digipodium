import cv2
import numpy as np
import os
def load_video(camera_index):
    video = cv2.VideoCapture(camera_index)
    cv2.namedWindow("video")
    cv2.createTrackback
    while True:
        status, frame = video.read()
        height, width, _ = frame.shape
        if not status:
            print("camera data not read!!")
            break
        # operations
        # 1. resize
        # # # cv2.resize(frame,(640,480))
        frame = cv2.resize(frame,(None,None), fx=.5, fy=.5)    # half the size
        # 2. convert to grayscale
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 3. blur
        frame = cv2.GaussianBlur(frame,(5,5),0)
        # 4. add text
        cv2.putText()
        # 5. add graphics
        cv2.imshow("video",frame)
        if cv2.waitKey(1) == ord('q'):    # 1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam_idx = 0
    load_video(cam_idx)