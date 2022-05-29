# this class contains our game loop
# by Travis Mix
# May 11, 2022

import os
import platform
from monster import *
from player import *
from game_map import *
from game_functions import *

os_name = platform.system()
clear = ""

# clear console based on operating system
if os_name == "Windows":
    clear = "cls"
else:
    # mac or linux
    clear = "clear"


def clear_screen():
    os.system(clear)


def game_loop():
    """
    runs our main game loop
    """
    keep_running = True
    monster_response = ""
    choice = ""
    monster_one = Monster(10, 5)
    monster_two = Monster(10, 5)
    player_one = Player(10, 5, 0, 1)
    map = GameMap()

    while keep_running:
        if map.map[0][map.position]['contains'] == "tutorial":
            run_tutorial()
            map.map[0][map.position]['contains'] = "empty"
        elif map.map[0][map.position]['contains'] == "player_died":
            run_died()
            map.map[0][map.position]['contains'] = "empty"
        elif map.map[0][map.position]['contains'] == "gained_xp":
            print("You defeated the monster and gained some experience!")
            map.map[0][map.position]['contains'] = "empty"
        elif map.map[0][map.position]['contains'] == "leveled_up":
            map.map[0][map.position]['contains'] = "empty"
            print("You gained enough experience to level up, boosting health, and damage!!!")
            player_one.player_level_up()
        elif map.map[0][map.position]['contains'] == "torch":
            if map.map[0][map.position]['message'] != "":
                print(map.map[0][map.position]['message'])
        elif map.map[0][map.position]['contains'] == "requires_torch":
            require_torch(player_one, map)
        elif map.map[0][map.position]['contains'] == "chest":
            if map.map[0][map.position]['message'] != "":
                print(map.map[0][map.position]['message'])
        elif map.map[0][map.position]['contains'] == "monster":
            if player_one.monsters_fought == 0:
                monster_response = monster(player_one, monster_one, map)
                if monster_response == "player_win":
                    map.map[0][map.position]['contains'] = "player_win"
                    map.map[0][map.position]['move_options'].extend(["north", "south"])
                else: # player died
                    map.map[0][map.position]['contains'] = "died"
            else:
                monster_response = monster(player_one, monster_two, map)
        elif map.map[0][map.position]['contains'] == "boss":
            boss()
        elif map.map[0][map.position]['contains'] == "game_over":
            break # end the game

        map.print_map()
        player_one.report_player_stats()
        print() # spacing
        
        if map.map[0][map.position]['contains'] == "monster":
            choice = monster_response
        else:
            choice = input("What would you like to do? ")
        if choice in map.map[0][map.position]["next_room"].keys():
            map.position = int(map.map[0][map.position]["next_room"][choice.lower()])
        elif choice.lower() == "torch" and map.map[0][map.position]["contains"] == "torch":
            pickup_torch(player_one, map)
        elif choice.lower() == "chest" and map.map[0][map.position]["contains"] == "chest":
            chest(player_one, map)
        elif choice.lower() == "died" and map.map[0][map.position]['contains'] == "monster":
            # reset player
            map.position = map.start_location
            player_one.player_died()
            map.map[0][map.position]['contains'] = "player_died"
        elif choice.lower() == "player_win":
            if player_one.monsters_fought < 2:
                map.map[0][map.position]['contains'] = "gained_xp"
                map.map[0][map.position]['move_options'] = ["north", "south"]
            else:
                map.map[0][map.position]['contains'] = "leveled_up"
                player_one.player_level_up()
        elif choice.lower() == "potion":
            player_one.player_heal()
        elif choice.lower() == "help":
            run_tutorial()
        elif choice.lower() == "quit":
            break
        else:
            print("Not a valid choice please try again.")
            continue

        clear_screen()
        
