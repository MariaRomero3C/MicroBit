# Imports go at the top
from microbit import *


def suma (x,y,z):
    resul=x+y+z
    return resul

display.scroll(suma(3,5,4), delay=60,loop=True)
