import gymnasium as gym
import numpy as np
from collections import deque
from gymnasium import spaces

from .capture import ScreenCapture
from .control import ActionController
from .reward_functions import compute_reward


class FortniteEnv(gym.Env):
    metadata = {"render_modes": []}

    def __init__(self):
        super().__init__()

        self.capture = ScreenCapture()
        self.controller = ActionController()

        # --- OBSERVATION SPACE ---
        self.frame_stack = 4
        self.frames = deque(maxlen=self.frame_stack)

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(self.frame_stack, 84, 84),
            dtype=np.uint8
        )

        # --- ACTION SPACE ---
        self.action_space = spaces.Discrete(4)

        self.steps = 0
        self.max_steps = 3000

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        colorFrame ,frame = self.capture.get_frame()
        for _ in range(self.frame_stack):
            self.frames.append(frame)

        self.steps = 0
        return np.array(self.frames), {}

    def step(self, action):
        self.controller.perform(action)

        colorFrame ,frame = self.capture.get_frame()
        self.frames.append(frame)

        reward, info = compute_reward(frame, colorFrame)

        self.steps += 1
        terminated = False
        if info.get("pickup", False):
            terminated = True
        
        truncated = self.steps >= self.max_steps

        return np.array(self.frames), reward, terminated, truncated, info
