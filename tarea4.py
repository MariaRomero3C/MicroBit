from microbit import *

dibujo1 = Image("90909:09090:00900:09090:90909")
dibujo2 = Image("90909:90909:09090:00900:09090")
dibujo3 = Image("09090:90909:90909:09090:00900")
dibujo4 = Image("00900:09090:90909:90909:09090")
dibujo5 = Image("09090:00900:09090:90909:90909")

while True:
    display.show(dibujo1)
    sleep(500)
    display.show(dibujo2)
    sleep(500)
    display.show(dibujo3)
    sleep(500)
    display.show(dibujo4)
    sleep(500)
    display.show(dibujo5)
    sleep(500)
