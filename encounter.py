import random
import sys

class Player:
    def __init__(self, name, max_hp, hp, mana, strength, spwr):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.spwr = spwr

class Enemy:
    def __init__(self, name, max_hp, hp, strength, spwr, des):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.spwr = spwr
        self.des = des

    def check_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

pname = input("What is your name, Guy? ")
player = Player(pname, 100, 100, 50, 20, 10)
current_enemy = Enemy("Henchman", 200, 200, 10, 3, "Not a very powerful enemy.")

heal_mana_cost = 20
spell_mana_cost = 25
player_base_attack = player.strength * .7
player_best_attack = player.strength * 1.2

while current_enemy.check_alive() == True:
    player_acted = False
    action = input("What would you like to do? ")
    action = action.lower()
    if action == "attack":
        crit = False
        player_attack_amount = random.randrange(player_base_attack, player_best_attack)
        player_acted = True
        if player_attack_amount == player.strength:
            player_attack_amount *= 2
            crit = True
            player_acted = True
        else:
            pass
        current_enemy.hp -= player_attack_amount
        if crit == True:
            print("Hot damn! A crit! You hit him for {}! He has {} left." .format(player_attack_amount, current_enemy.hp))
        else:
            print("You hit him for {}. He has {} hp left." .format(player_attack_amount, current_enemy.hp))
    elif action == "cast":
        print("cast")
    else:
        print("Invalid")
    if player_acted == True:
        print("Alright. It's his turn. He looks pretty pissed.")
        enemy_base_attack = current_enemy.strength * .5
        enemy_best_attack = current_enemy.strength * .9
        enemy_attack_amount = random.randrange(enemy_base_attack, enemy_best_attack)
        player.hp -= enemy_attack_amount
        print("Damn. He got you good. {} damage, leaving you with {} hp." .format(enemy_attack_amount, player.hp))
    if player.hp <= 0:
        print("He killed you. Sry.")
        sys.exit()
    else:
        pass
print("Enemy died. Nice.")
print("Peace.!")
