# Player class
# by Travis Mix
# May 12, 2022

class Player():

    def __init__(self, max_hp, damage, healing_potions, level):
        """
        max_hp = players maximum hitpoints which they start with (int)
        damage the player does on start (int)
        healing_potion = how many potions to start (int)
        """
        self.hp = max_hp
        self.max_hp = max_hp
        self.damage = damage
        self.healing_potions = healing_potions
        self.level = level
        self.blocking = False
        self.attacking = False
        self.charging = False
        self.charging_amount = 1
        self.torch = False
        self.chest_count = 0
        self.sword = False
        self.shield = False
    
    # player combat actions
    def block(self):
        self.blocking = True
        self.charging = False
        self.charging_amount = 1

    def attack(self):
        self.attacking = True
        self.charging = False
        self.charging_amount = 1

    def charging(self):
        self.charging_amount += 1
        self.blocking = False
        self.attacking = False

    # this will need tweaking
    def player_reset(self):
        self.attacking = False
        self.blocking = False

    def player_level_up(self):
        self.level += 1
        self.damage += 3
        self.max_hp += 5
        self.hp = self.max_hp
    
    def pickup_torch(self):
        self.torch = True

    def open_chest(self, healing_potions, sword, shield):
        self.healing_potions += healing_potions
        self.sword = sword
        self.shield = shield


    def report_player_stats(self):
        player_stats = f"HP: {self.hp}\tPotions: {self.healing_potions}\tCharges: {self.charging_amount}\tTorch: {self.torch}\tSword: {self.sword}\tShield: {self.shield}"
        print(player_stats)