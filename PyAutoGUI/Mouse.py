import pyautogui as _
import time 
#get screen size 
ss = _.size()
#cursor position
cp = _.position()
'''
#move cursor and duration to specific value
_.moveTo(ss[0]/2,ss[1]/2, duration = 0)

#move cursor relative (where the cursor is)

_.moveRel(100,100, duration = 0)


#---------------Clicks
#left click:
_.click()
_.click(button='left')

#right click:
_.click(button="right")
_.rightClick()

#double click:
_.doubleClick()
_.doubleClick(button="left")
_.doubleClick(button="right")

#middle click
_.middleClick()
_.click(button="middle")
'''
'''
#drag cursor
_.dragTo(100,200,button="left", duration =1) #Parameters = X,Y,BUTTON,DURATION
#drag relative (cursor position)
_.dragRel(-100,-100,button="left",duration=1) #Parameters = X,Y,BUTTON,DURATION

#scroll
_.scroll(200)
_.hscroll(200)

#key(cursor) down
_.mouseDown(button="left")
_.mouseUp(button="left")

'''



