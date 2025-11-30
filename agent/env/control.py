import pydirectinput
import time
import vgamepad as vg
gamepad = vg.VX360Gamepad()



class ActionController:
    def __init__(self):
        pydirectinput.FAILSAFE = False
        pydirectinput.keyDown("w")
        #pydirectinput.keyDown("4")
    

    def perform(self, action):
        right_thumb_x = 0
        right_thumb_y = 0
        pydirectinput.keyDown("4")
        if action == 0:
            right_thumb_x = -1 # look to the left
        elif action == 1:
            right_thumb_x = 0 # look straight
        elif action == 2:
            right_thumb_x = 1 # look to the right
        
        gamepad.right_joystick_float(x_value_float=right_thumb_x, y_value_float=right_thumb_y)
        gamepad.update()

