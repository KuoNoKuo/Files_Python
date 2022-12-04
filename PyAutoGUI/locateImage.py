import pyautogui as _
import time 
_.FAILSAFE = True 
_.PAUSE = 0.01
time.sleep(4,)
while True:
    a = _.locateCenterOnScreen(r'Icon2.png', confidence=0.8)
    print(a)
    if a is not None:
        _.click(a)