# Imports go at the top
from microbit import *

lista_vocales = ["A","E","I","O","U"]

for i in lista_vocales:
    display.scroll(i)
    sleep(700)
