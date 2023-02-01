# Imports go at the top
from microbit import *

for x in range (5):
    display.set_pixel(x,0,9)
    sleep(500)
    display.set_pixel(x,1,9)
    sleep(500)
    display.clear()
    sleep(500)
