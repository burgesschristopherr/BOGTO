import map
import numpy

win = False


while win == False:
    map.print_map()
    map.move()
    if kc == len(map.map):
        win = True
print("Victory. Grats.")
