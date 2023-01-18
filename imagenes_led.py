from microbit import *

n = 1
borde = Image("56789:45678:34567:23456:12345")
interior = Image("54321:65432:76543:87654:98765")
while n<= 10:
    if n %2 == 0:
        display.show(borde)
    else:
        display.show(interior)
    sleep(500)
    n += 1

display.scroll("FIN")
