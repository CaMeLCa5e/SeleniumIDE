#!/usr/bin/env python
#pymouse12.8.14.py

from pymouse import PyMouse
import time 

# mouse = pymouse.PyMouse()
# print mouse.position()
# print mouse.screen_size()

m = PyMouse()

m.move(200,200)

m.click(500, 300, 1) # 1 = left 2 = middle 3 = right click

m.screen_size()

m.position()


#hold and click-  m.press(x,y) m.release(x,y)

while True:
	print mouse.position()
	time.sleep(1)
	