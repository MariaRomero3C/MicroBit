# Imports go at the top
from microbit import *


while True:
    if button_a.is_pressed():
        display.show(Image.DIAMOND)
        sleep(1000)
    elif button_b.is_pressed():
        display.show(Image.HEART)
        sleep(1000)
    else:
        display.show(Image.ANGRY)
