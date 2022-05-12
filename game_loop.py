# this class contains our game loop
# by Travis Mix
# May 11, 2022

from monster import *
import os
import platform

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

    while keep_running:
        monster_one.attack()
        
        player_quit = input("wanna quit? ('y/n') ")
        clear_screen()

        if player_quit.lower() == 'y':
            keep_running = False
        
