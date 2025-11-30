import cv2
import numpy as np

# Adjust based on item color, hsv 
LOWER_COLOR = np.array([0, 26, 163])
UPPER_COLOR = np.array([100, 255, 255])

MIN_ITEM_AREA = 10

def detect_item(colorFrame):
    """
    frame: full-res BGR image
    Returns True if item is visible
    """


    hsv = cv2.cvtColor(colorFrame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)

    # Remove noise
    mask = cv2.medianBlur(mask, 5)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > MIN_ITEM_AREA:
            return True

    return False

def get_item_mask(colorFrame):
    hsv = cv2.cvtColor(colorFrame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)
    mask = cv2.medianBlur(mask, 5)
    return mask