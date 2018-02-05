import numpy
import sys
import encounter
import time

map = numpy.zeros(shape=(4,4))
map[0,0] = 1
pX = 0
pY = 0

def slow_elipse(direction):
    time.sleep(1)
    print("You move slowly to the {}" .format(direction))
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(". \n")
    sys.stdout.flush()
    time.sleep(1)

def print_map():
    x, y = 0
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

def check_square(x, y):
    pass

def move():
    global pX
    global pY
    map[pX][pY]=2 #Marking current square as vistied
    action = input("WASD? ")
    action.lower()
    if action == "w" and pX > 0: # Changing player position +- 1
        slow_elipse("North")
        if map[pX-1][pY] == 0:
            encounter.current_enemy.hp = encounter.current_enemy.max_hp
            encounter.fight()
        else:
            print("Phew. You've been here before. Nothing to see.")
        pX -= 1
    elif action == "a" and pY > 0: # Changing player position +- 1
        slow_elipse("West")
        if map[pX][pY-1] == 0:
            encounter.current_enemy.hp = encounter.current_enemy.max_hp
            encounter.fight()
        else:
            print("Phew. You've been here before. Nothing to see.")
        pY -= 1
    elif action == "s" and pX < 3: # Changing player position +- 1
        slow_elipse("South")
        if map[pX+1][pY] == 0:
            encounter.current_enemy.hp = encounter.current_enemy.max_hp
            encounter.fight()
        else:
            print("Phew. You've been here before. Nothing to see.")
        pX += 1
    elif action == "d" and pY < 3: # Changing player position +- 1
        slow_elipse("East")
        if map[pX][pY+1] == 0:
            encounter.current_enemy.hp = encounter.current_enemy.max_hp
            encounter.fight()
        else:
            print("Phew. You've been here before. Nothing to see.")
        pY +=1
    else:
        print("Invalid Command. Try again.")
        move()
    map[pX][pY] = 1 #marking new square as P
