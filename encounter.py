import random

class Player:
    def __init__(self, name, max_hp, hp, strength, spwr):
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
player = Player(pname, 100, 100, 20, 10)
current_enemy = Enemy("Henchman", 200, 200, 10, 3, "Not a very powerful enemy.")

while current_enemy.check_alive() == True:
    action = input("What would you like to do? ")
    action = action.lower()
    if action == "attack":
        player_base_attack = player.strength * .7
        player_best_attack = player.strength * 1.2
        crit = False
        player_attack_amount = random.randrange(player_base_attack, player_best_attack)
        if player_attack_amount == player.strength:
            player_attack_amount *= 2
            crit = True
        else:
            pass
        current_enemy.hp -= player_attack_amount
        if crit == True:
            print("Hot damn! A crit! You hit him for {}! He has {} left." .format(player_attack_amount, current_enemy.hp))
        else:
            print("You hit him for {}. He has {} hp left." .format(player_attack_amount, current_enemy.hp))
    else:
        print("Invalid")

print("Enemy died. Nice.")
print("Peace.")
