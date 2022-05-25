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
    monster_one = Monster(10, 5)
    monster_two = Monster(10, 5)
    player_one = Player(10, 5, 0, 1)
    map = GameMap()


    while keep_running:
        # choice = input(f"Type '{map.move_options_str.upper()}' to head to the next room: ")
        # map.position = int(map.map[0][map.position]["next_room"][choice.lower()])
        # print(map.position)
    
        if map.map[0][map.position]['contains'] == "tutorial":
            run_tutorial()
        elif map.map[0][map.position]['contains'] == "torch":
            print("You see a TORCH on the wall, and only darkness ahead.")
        elif map.map[0][map.position]['contains'] == "requires_torch":
            require_torch()
        elif map.map[0][map.position]['contains'].__contains__("chest"):
            chest()
        elif map.map[0][map.position]['contains'].__contains__("monster"):
            monster()
        elif map.map[0][map.position]['contains'] == "boss":
            boss()
        elif map.map[0][map.position]['contains'] == "game_over":
            break # end the game

        map.print_map()
        player_one.report_player_stats()
        print() # spacing

        choice = input("What would you like to do? ")
        if choice in map.map[0][map.position]["next_room"].keys():
            map.position = int(map.map[0][map.position]["next_room"][choice.lower()])
        elif choice.lower() == "torch" and choice.lower() == map.map[0][map.position] == 5:
            player_one.pickup_torch()
        elif choice.lower() == "help":
            run_tutorial()
        elif choice.lower() == "quit":
            break
        else:
            print("Not a valid choice please try again.")
            continue

        
        # player_quit = input("wanna quit? ('y/n') ")
        clear_screen()

        # if player_quit.lower() == 'y':
        #     keep_running = False
        
