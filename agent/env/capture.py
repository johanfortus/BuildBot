import mss
import numpy as np
import cv2


class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()
        self.region = {
            "top": 100,
            "left": 100,
            "width": 1600,
            "height": 800
        }

    def get_frame(self):
        img = np.array(self.sct.grab(self.region))[:, :, :3]

        resized_color = cv2.resize(img, (84, 84), interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (84, 84), interpolation=cv2.INTER_AREA)

        return resized_color.astype(np.uint8), resized.astype(np.uint8) # Returning color frame for reward
