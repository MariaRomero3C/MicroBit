# Imports go at the top
from microbit import *
import radio
import music

radio.on()
radio.config(channel=10)

notas = ['A4:4','A4:4','A4:4','F4:6','C5:4','A4:4','F4:6','C5:4','A4:8','E5:4','E5:4',
        'E5:4','F5:6']

def lista_texto(lista):
    mensaje = "Hola"
    for i in lista:
        mensaje += i + ","
    return mensaje

while True:
    if button_a.was_pressed():
        message = lista_texto(notas)
        radio.send(message)
        display.show("OK")
        sleep(1000)
    elif button_b.was_pressed():
        display.show("B")
        sleep(1000)
    else:
        display.show("?")
        sleep(1000)
   
