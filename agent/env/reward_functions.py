import numpy as np
import cv2
from agent.env.item_detector import detect_item

prev_frame = None
scoreCooldown = False

def detect_green_flash(colorFrame):
    # colorFrame is BGR uint8
    b, g, r = cv2.split(colorFrame.astype(np.float32))
    total = r + g + b + 1e-6
    green_ratio = np.mean(g / total)
    return green_ratio > 0.35

def compute_reward(frame, colorFrame):
    global prev_frame
    global scoreCooldown

    reward = 0
    info = {}

    if detect_green_flash(colorFrame): # Detect if green takes up most of screen
        if not scoreCooldown:
            reward += 10.0
            info["pickup"] = True
            print(f"Score detected reward: {reward}")
            scoreCooldown = True  
    else:
        scoreCooldown = False
    
    
    
    if detect_item(colorFrame):
        # reward += .5  # small shaping reward
        # reward += .05  # small shaping reward
        reward += .01  # small shaping reward
        info["item_visible"] = True
        print("ITEM DETECTED")

    
    prev_frame = frame.copy()

    
    return reward, info