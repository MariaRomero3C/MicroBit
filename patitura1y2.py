# Imports go at the top
from microbit import *
import music

texto = "Star Wars y los Simpsons"
Star_Wars = ['A4:4','A4:4','A4:4','F4:6','C5:4','A4:4','F4:6','C5:4','A4:8','E5:4','E5:4',
        'E5:4','F5:6','C5:4','A4b:4','F4:6','C5:4','A4:8','A5:4','A4:6','A4:4','A5:4',
         'G5#:6','G5:4','F5#:4','E5#:4','F5:4',' ','A4#:2','D5#:4']

Los_Simpsons = ['C4:4','F4:4','G4:8','C5:3','E5:2','F5:2','A5:1','G5:3',
         'E5:2','C5:2','A4:1','F4:2','F4:2','F4:2','G4:2',' ',' ',
         'F4:2','F4:2','F4:2','G4:1','B4b:3','B4:4',' ',' ','C5:3',
         'E5:2','F5:2','A5:2','G5:3','E5:2','C5:2','A4:2','F5','F5',
         'F5',' ',' ','G5']

display.scroll(texto, delay=60)
music.play(Star_Wars, wait=False)
music.play(Los_Simpsons, wait=False)
