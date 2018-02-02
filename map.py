import numpy
import sys

map = numpy.zeros(shape=(4,4))
map[0,0] = 1
pX = 0
pY = 0


def print_map():
    x=0
    y=0
    while x < len(map):
        while y < len(map[0]):
            if map[x][y] == 1:
                sys.stdout.write ("P "),
            elif map[x][y] == 2:
                sys.stdout.write ("X "),
            else:
                sys.stdout.write ("[]"),
            y += 1
        print("\n")
        y = 0
        x += 1

def move():
    global pX
    global pY
    map[pX][pY]=2
    action = input("WASD? ")
    if action == "w" and pX > 0:
        pX -= 1
        map[pX][pY] = 1
    elif action == "a" and pY > 0:
        pY -= 1
        map[pX][pY] = 1
    elif action == "s" and pX < 3:
        pX += 1
        map[pX][pY] = 1
    elif action == "d" and pY < 3:
        pY +=1
        map[pX][pY] = 1
    else:
        print("Invalid Command. Try again.")
        move()
