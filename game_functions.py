# game_functions.py
# by Travis Mix
# May 24, 2022
# contains all the game functionality of
# the game that currently doesn't fit elsewhere

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
        by typing in HELP.
        """
        print(tutorial_output)
        input("Press ENTER To get started")

def torch():
    print("You picked up the torch")

def chest():
    print("There is a chest")

def monster():
    print("there is a monster")

def boss():
    print("There is a boss monster")