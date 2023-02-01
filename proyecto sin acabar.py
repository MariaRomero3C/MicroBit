# Imports go at the top
from microbit import *

i = 0
    lista = ["A", "B","C","D","E"]

while True:
    if button_a.was_pressed():
        i = i - 1
        sleep(500)
    elif button_b.was_pressed():
        i = 1 + 1
        sleep(500)
   if     
