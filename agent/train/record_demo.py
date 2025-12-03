import numpy as np
from agent.env.fortnite_env import FortniteEnv
from collections import deque
from datetime import datetime
import keyboard
import mouse
import os
import time


def capture_player_action():

    time.sleep(0.01)

    mouse_pos = mouse.get_position()
    x_value = mouse_pos[0]

    SCREEN_WIDTH = 1920

    if x_value < SCREEN_WIDTH /3:
        action = 0
        #print("Left")
    elif x_value > 2 * SCREEN_WIDTH / 3:
        action = 2
        #print("Right")
    else:
        action = 1
        #print("Straight")

    

    return action


def record_demo():

    os.makedirs('./logs_bc', exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M%p")

    save_folder = os.path.join('./logs_bc', timestamp)

    os.makedirs(save_folder, exist_ok=True)

    print(f"Creating demo folder to : {save_folder}")

    env = FortniteEnv(manual_control=True)

    states = []
    actions = []

    frame_stack = deque(maxlen=4)
    obs, _ = env.reset()

    while True:
        action = capture_player_action()

        frames, reward, terminated, truncated, info = env.step(action)

        frame_stack.append(frames)

        if len(frame_stack) == 4:
            states.append(np.array(frame_stack))

        actions.append(action)

        if terminated or truncated:
            obs, _ = env.reset()

        if keyboard.is_pressed("esc"):
            print("Escape key detected, stopping recording")
            break

    np.save(os.path.join(save_folder, 'states.npy'), np.array(states))
    np.save(os.path.join(save_folder, 'actions.npy'), np.array(actions))
    
    print(f"Demo saved to {save_folder}")


if __name__ == "__main__":
    record_demo()