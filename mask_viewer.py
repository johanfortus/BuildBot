import cv2
from agent.env.capture import ScreenCapture
from agent.env.item_detector import detect_item, get_item_mask

from agent.env.reward_functions import detect_green_flash
import numpy as np
scoreCooldown = False

def main():
    cap = ScreenCapture()
    cv2.namedWindow("Frame")
    cv2.namedWindow("Frame2")
    cv2.namedWindow("Item Mask")
    global scoreCooldown
    while True:
        obs, colorFrame = cap.get_frame()

        mask = get_item_mask(obs)

        cv2.imshow("Frame", obs)
        cv2.imshow("Frame2", colorFrame)
        cv2.imshow("Item Mask", mask)

        
        if detect_green_flash(obs): # Detect if green takes up most of screen
            if not scoreCooldown:
                print("Score detected reward")
                scoreCooldown = True  
        else:
            scoreCooldown = False
        
        if detect_item(obs):
            print("ITEM DETECTED")
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

if __name__ == "__main__":
    main()