def move():
    global pX
    global pY
    map[pX][pY]=2
    action = input("WASD? ")
    action.lower()
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


##############

print("A {} appeared! Holy Shit!" .format(current_enemy.name))
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
    if player_acted == True and current_enemy.check_alive() == True:
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
    else:
        pass
    if player.hp <= 0:
        time.sleep(1)
        print("\nHe killed you. Sry.")
        sys.exit()
    else:
        pass
time.sleep(1)
print("\nEnemy died. Nice.")
time.sleep(1)
print("Let's keep going!")
time.sleep(.5)
