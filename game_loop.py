# this class contains our game loop
# by Travis Mix
# May 11, 2022

import os
import platform
from monster import *
from player import *
from game_map import *

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
        map.print_map()
        monster_one.attack()
        player_one.report_player_stats()

        
        player_quit = input("wanna quit? ('y/n') ")
        clear_screen()

        if player_quit.lower() == 'y':
            keep_running = False
        
