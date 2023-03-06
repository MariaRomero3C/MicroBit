# Imports go at the top
from microbit import *

i = 0
imagenes = [Image.ARROW_E,Image.ARROW_N,Image.ARROW_NE,Image.ARROW_NW]

while True:
    if button_a.get_presses():
        i = i+1
    elif button_b.get_presses():
        i = i-1
    if i>len(imagenes):
        i = 0
    elif i<0:
        i = len(imagenes)-1
    else:
        display.show(imagenes[i])
