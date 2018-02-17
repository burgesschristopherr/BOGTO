import map
import numpy
import sys

pX = 0
pY = 0

while True:
    map.map[pX][pY] = 1
    map.print_map()
    map.map[pX][pY] = 2
    if (map.map==2).all()==True:
        print("Victory. Grats.")
        sys.exit()
    else:
        pX, pY = map.move(pX, pY)
