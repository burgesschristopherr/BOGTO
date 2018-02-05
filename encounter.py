import random
import sys
import time

class Player:
    def __init__(self, name, max_hp, hp, armor, max_mana, mana, strength, spwr):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.spwr = spwr
        self.armor = armor
        self.max_mana = max_mana
        self.mana = mana

class Enemy:
    def __init__(self, name, max_hp, hp, armor, strength, spwr, des):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.spwr = spwr
        self.des = des
        self.armor = armor

    def check_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

def display_status():
    print("Here's what the fight looks like: ")
    print("\n{}: " .format(player.name))
    print("    hp: {} / {} \n    mana: {} / {} \n    Str: {} \n    Armor: {} \n    Spell Power: {} \n" .format(player.hp, player.max_hp, player.mana, player.max_mana, player.strength, player.armor, player.spwr))
    print("\n{}:" .format(current_enemy.name))
    print("    hp: {} / {} \n    Note: {}    \n" .format(current_enemy.hp, current_enemy.max_hp, current_enemy.des))
pname = input("What is your name, Guy? ")
player = Player(pname, 100, 100, 10, 50, 50, 20, 10)
current_enemy = Enemy("Henchman", 200, 200, 5, 10, 3, "Not a very powerful enemy.")

heal_mana_cost = 20
spell_mana_cost = 25
player_base_attack = player.strength * .7
player_best_attack = player.strength * 1.2
player_base_spell = player.spwr * 1
player_best_spell = player. spwr * 2

while current_enemy.check_alive() == True:
    player_acted = False
    action = input("\nWhat would you like to do? ")
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
        player_attack_amount -= current_enemy.armor
        current_enemy.hp -= player_attack_amount
        if crit == True:
            time.sleep(1)
            print("\nHot damn! A crit! You hit him for {}! He has {} left." .format(player_attack_amount, current_enemy.hp))
        else:
            time.sleep(1)
            print("\nYou hit him for {}. He has {} hp left." .format(player_attack_amount, current_enemy.hp))
    elif action == "cast":
        time.sleep(1)
        if player.mana - spell_mana_cost >= 0:
            player_attack_amount = random.randrange(player_base_spell, player_best_spell)
            current_enemy.hp -= player_attack_amount
            print("\nYou cast a mighty spell! You hit the enemy for {}. He has {} hp lef!" .format(player_attack_amount, current_enemy.hp))
            player_acted = True
            player.mana -= spell_mana_cost
        else:
            print("Not enough mana!")
            player_acted = False
    elif action == "heal":
        time.sleep(1)
        if player.mana - heal_mana_cost >= 0:
            player_attack_amount = random.randrange(player_base_spell, player_best_spell)
            player.hp += player_attack_amount
            print("\nYou heal yourself for {}" .format(player_attack_amount))
            player_acted = True
        else:
            print("Not enough mana!")
            player_acted = False
    elif action == "status":
        time.sleep(1)
        display_status()
        player_acted = False
    else:
        time.sleep(1)
        print("\nInvalid")
    if player_acted == True:
        time.sleep(2)
        print("\nAlright. It's his turn. He looks pretty pissed.")
        enemy_base_attack = current_enemy.strength * .5
        enemy_best_attack = current_enemy.strength * .9
        enemy_attack_amount = random.randrange(enemy_base_attack, enemy_best_attack)
        if enemy_attack_amount - player.armor < 0:
            enemy_attack_amount -= 0
        else:
            enemy_attack_amount -= player.armor
        player.hp -= enemy_attack_amount
        time.sleep(1)
        print("\nDamn. He got you good. {} damage, leaving you with {} hp." .format(enemy_attack_amount, player.hp))
    if player.hp <= 0:
        time.sleep(1)
        print("\nHe killed you. Sry.")
        sys.exit()
    else:
        pass
print("\nEnemy died. Nice.")
print("\nPeace.!")
