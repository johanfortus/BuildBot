import pydirectinput
import time


class ActionController:
    def __init__(self):
        pydirectinput.FAILSAFE = False
        #pydirectinput.keyDown("w")
    
    def perform(self, action):
        if action == 0:
            pydirectinput.moveRel(-20, 0)
        elif action == 1:
            pydirectinput.moveRel(20, 0)
        elif action == 2:
            pydirectinput.moveRel(0, -15)
        elif action == 3:
            pydirectinput.moveRel(0, 15)
        """
        elif action == 4:
            pydirectinput.press("space")
        elif action == 5:
            pass
        """

    def _hold(self, key, t=2):
        pydirectinput.keyDown(key)
        time.sleep(t)
        pydirectinput.keyUp(key)
