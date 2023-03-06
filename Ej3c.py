# Imports go at the top
from microbit import *
import music

i = 0
sonidos = ['b7:20','a7:20','g7:20','f7:20','e7:20','d7:20','c7:20']

while True:
    if button_a.get_presses():
        i = i+1
    elif button_b.get_presses():
        i = i-1
    if i>len(sonidos):
        i = 1
    elif i<0:
        i = len(sonidos)-1
    else:
        music.play(sonidos[i])
        sleep(500)
