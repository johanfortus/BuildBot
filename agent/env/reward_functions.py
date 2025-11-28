import numpy as np
import cv2
from agent.env.item_detector import detect_item

prev_frame = None

def compute_reward(frame, colorFrame):
    global prev_frame

    hsv = cv2.cvtColor(colorFrame, cv2.COLOR_BGR2HSV) # Convert for easier color detection
    info = {}
    # RGB range
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green) # How many green pixels in frame
    green_ratio = np.sum(mask > 0) / (mask.shape[0] * mask.shape[1]) # ratio of green pixels on frame

    reward = 0.01  # survival reward

    if prev_frame is not None:
        movement = np.mean(np.abs(frame - prev_frame))
        reward += movement * 0.1  # encourage motion

    if green_ratio > 0.80: # Detect if green takes up most of screen
        reward += 10.0  

    if detect_item(colorFrame):
        reward += 0.02  # small shaping reward
        info["item_visible"] = True
        print("ITEM DETECTED")

    prev_frame = frame.copy()

    
    return reward, info
