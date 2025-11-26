import pydirectinput
import time


class ActionController:
    def __init__(self):
        pydirectinput.FAILSAFE = False

    def perform(self, action):
        if action == 0:
            return
        elif action == 1:
            self._hold("w")
        elif action == 2:
            self._hold("s")
        elif action == 3:
            self._hold("a")
        elif action == 4:
            self._hold("d")
        elif action == 5:
            pydirectinput.press("space")
        elif action == 6:
            pydirectinput.click()
        elif action == 7:
            pydirectinput.moveRel(-15, 0)
        elif action == 8:
            pydirectinput.moveRel(15, 0)

    def _hold(self, key, t=2):
        pydirectinput.keyDown(key)
        time.sleep(t)
        pydirectinput.keyUp(key)
