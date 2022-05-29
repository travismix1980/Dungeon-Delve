# game_functions.py
# by Travis Mix
# May 24, 2022
# contains all the game functionality of
# the game that currently doesn't fit elsewhere

from random import randint
from game_map import *

def run_tutorial():
    tutorial_output = """
    Welcome to the tutorial!  
    While exploring you will see many words that are capitalized.
    If you type in the capitalized word it will allow you to do that
    action.  You will also see on the screen at all times various bits 
    of information such as how many hitpoints listed as 'HP' you have 
    or how many health potions you have.  You can also see how charged
    up your attack level is which will increase damage the more charged 
    your attack is.  You can take another look at this message anytime
    by typing in HELP.  You can quit anytime by typing QUIT as well.

    Helpful Tip: Get a pencil and paper and map out your journey
    """
    print(tutorial_output)
    input("Press ENTER To get started")

def run_died():
    print("You were unsuccessful and have died.  Try again!")
    print("We will let you keep the torch!")
    input("Press ENTER To continue")


def chest(player, map):
    print(map.map[0][map.position]['message'])
    if player.chest_count == 0:
        player.open_chest(0, True, True)
        map.map[0][map.position]['message'] = "You found a sword and a shield!"
        player.chest_count += 1
    else:
        player.open_chest(2, True, True)
        map.map[0][map.position]['message'] = "Looks like you found 2 health potions!"

    map.map[0][map.position].pop("actions")

def monster(player, monster, map):
    response = ""
    print("Before you there is a monster")
    if player.sword == True: # if they have a sword then they have a shield
        response = combat(map, player, monster)
    else:
        # no weapons at this point so you try to sneak past
        response = sneak(map, player)

    return response

def boss():
    print("There is a boss monster")

# TODO: combat
def combat(map, player, monster):
    print("The monster sees you and starts to run towards you raising its weapon")
    player.monsters_fought += 1
    response = ""
    while player.hp > 0 and monster.hp > 0:
        
        if player.hp > 0 or monster.hp > 0:
            # combat happens player first followed by monster
            player_choice = input("ATTACK, BLOCK, CHARGE attack, or use health POTION? ")
            if player_choice.lower() == "attack":
                player.attack()
                print(f"You hit the monster for {player.damage * player.charging_amount} damage!")
                monster.hp -= (player.damage * player.charging_amount)
                # we have to reset player attacking / charging / blocking after attacks or blocks
                player.player_reset() 
            elif player_choice.lower() == "charge":
                player.player_charging()
                print("You spend your turn charging up your attack")
            elif player_choice.lower() == "potion":
                player.player_heal()
            else:
                # block automatically if spelling error
                player.block()
                print("You prepare for the enemies attack by boosting your defenses")
                # we have to reset player attacking / charging / blocking after attacks or blocks
                player.player_charging()

            # if player killed monster
            if monster.hp <= 0:
                map.map[0][map.position]['contains'] == ""
                # for now to turn it in move player to room 0 to end game          
                response = "player_win"
                break
            else:
                # monsters turn
                monster_choice = monster.attack()
                if monster_choice == "charge": 
                    print("The monster spends its turn buffing its offense!")
                else:
                    # calculate the monsters damage
                    if player.blocking:
                        monster_damage = 0
                    else:
                        monster_damage = (monster.damage * monster.charge_counter)

                    print(f"The monster swings its weapon at you hitting you for {monster_damage} damage")
                    player.hp -= monster_damage
        elif player.hp <= 0:
            response = "died"
            map.map[0][map.position]['contains'] = ""
            break
        player.report_player_stats()
    return response
    

# only happens if there is no weapon.  It is based on a dice roll system    
def sneak(map, player):
    response = input("Would you like to turn BACK or SNEAK past the monster? ")
    if response.lower() == "back":
        return response
    else:
        sneak_success = randint(1, 20)
        if sneak_success > 12: # only a 40% chance reset to 12
            return response
        else:
            return "died"


def pickup_torch(player, map):
    print(map.map[0][map.position]['message'])
    player.pickup_torch()
    map.map[0][map.position].pop("actions")
    map.map[0][map.position]["message"] = "You have picked up the torch illuminating your way!"
    print(map.map[0][map.position])

def require_torch(player, map):
    if player.torch == True:
        #stop east from being added over and over
        if map.map[0][map.position]["move_options"].__contains__("east"):
            pass
        else:
            map.map[0][map.position]["move_options"].append("east")
            map.map[0][map.position]["next_room"]["east"] = 12
    else:
        print("After stumbling around in the dark you are only able to go back from where you came")