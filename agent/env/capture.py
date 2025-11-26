import mss
import numpy as np
import cv2


class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()
        self.region = {
            "top": 100,
            "left": 100,
            "width": 800,
            "height": 600
        }

    def get_frame(self):
        img = np.array(self.sct.grab(self.region))[:, :, :3]

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (84, 84), interpolation=cv2.INTER_AREA)

        return resized.astype(np.uint8)
