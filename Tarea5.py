# Imports go at the top
from microbit import *

i=0
nombres=["Alicia", "Maria", "Lucas", "Esteban", "Pepe"]

while True:
    if button_a.was_pressed():
        i=i-1
        sleep(500)
    elif button_b.was_pressed():
        i=i+1
        sleep(500)
    if i>len(nombres)-1:
        i=0
    elif i<0:
        i=len(nombres)-1
    else:
        display.scroll(nombres[i])
        sleep(500)
