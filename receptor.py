# Imports go at the top
from microbit import *
import radio
import music

radio.on()
radio.config(channel=10)

def texto_lista(texto):
    return texto.split(",")

while True:
    message = radio.receive()
    sleep(20)
    if message is not None:
        try:
            notas = texto_lista(message)
            music.play (notas)
        except:
            display.scroll(message)
