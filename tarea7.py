# Imports go at the top
from microbit import *
import random
import music

vocales=["A","E","I","O","U"]
consonantes=["B","C","D","F","G","H","J","K","L","LL","M","N","P","Q","R","S","T","V","X","Y","Z"]
total_palabra = 2
cuenta = 21

while total_palabra>0:
    if button_a.was_pressed(): 
        vocal_aleatoria = vocales[random.randint(0,len(vocales)-1)]
        display.show(vocal_aleatoria)
        total_palabra = total_palabra-1
        sleep(1000)
    elif button_b.was_pressed():
        consonante_aleatoria = consonantes[random.randint(0,len(consonantes)-1)]
        display.show(consonante_aleatoria)
        total_palabra = total_palabra-1
        sleep(1000)
    else:
        display.show("?")

display.scroll("Fin")
while cuenta>0:
    cuenta = cuenta - 1
    display.scroll (cuenta, delay=40)
    sleep(500)

music.play('A4:8')
