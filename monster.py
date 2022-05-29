# Monster class

from random import choice


class Monster():
    """
    Controls the two monsters in the game and is the base class for the Boss
    """

    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
        self.charge_counter = 1 # we start at 1 to make it easier to do our attack damage math
        self.what_doing = ["charge", "attack"]

    def attack(self):
        """
        Monster decides to attack or charge attack.  Charging allows the monster to do 
        more damage when it decides to attack. 
        """
        monster_attack = choice(self.what_doing)
        if monster_attack == "attack":
            return "attack"
        else:
            self.charge_counter += 1
            return "charge"
