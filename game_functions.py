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
        response = combat()
    else:
        response = sneak(map, player)

    return response

def boss():
    print("There is a boss monster")

# TODO: combat
def combat():
    print("You fight the monster")

# TODO: sneak
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