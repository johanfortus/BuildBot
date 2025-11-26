import numpy as np

prev_frame = None

def compute_reward(frame):
    global prev_frame

    reward = 0.01  # survival reward

    if prev_frame is not None:
        movement = np.mean(np.abs(frame - prev_frame))
        reward += movement * 0.1  # encourage motion

    prev_frame = frame.copy()

    info = {}
    return reward, info
