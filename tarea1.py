# Imports go at the top
from microbit import *

# Variable nombre
nombre = "Maria"
apellido = "Romero"

while True:
    if button_a.was_pressed():
        nombre
        display.scroll(nombre)
    if button_b.was_pressed():
        apellido     
        display.scroll(apellido)       
