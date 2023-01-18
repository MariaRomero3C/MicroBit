from microbit import *

n = 1
borde = Image("09990:09990:00900:09990:59095")
interior = Image("59095:09990:00900:09990:09990")
while n<= 6:
    if n %2 == 0:
        display.show(borde)
    else:
        display.show(interior)
    sleep(600)
    n += 1

display.show(Image.HAPPY)
