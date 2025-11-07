import gymnasium as gym
import numpy as np


class BuildBotEnv(gym.Env):

    def __init__(self, max_steps=50):
        super().__init__()
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Box(
            low=0, high=1, shape=(4,), dtype=np.float32
        )
        self.max_steps = max_steps
        self.steps = 0

    def reset(self, *, seed=None, options=None):
        self.steps = 0
        obs = np.zeros(4, dtype=np.float32)
        return obs, {}


    def step(self, action):
        self.steps += 1
        obs = np.random.rand(4).astype(np.float32)
        reward = float(action == 1)
        terminated = False
        truncated = self.steps >= self.max_steps
        info = {}
        return obs, reward, terminated, truncated, info