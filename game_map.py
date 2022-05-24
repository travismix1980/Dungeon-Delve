#-----------------------------------------------------------
# |1player exit   7walled  13empty   19empty   25monster2   |
# |2boss          8empty   14empty   20walled  26empty      |
# |3walled        9walled  15walled  21chest2  27empty      |
# |4player start  10walled 16chest1  22walled  28monster1   |
# |5empty         11walled 17empty   23empty   29empty      |
# |6empty         12empty  18empty   24walled  30walled     |
#------------------------------------------------------------

room_zero = {
    id: 0,
    "move_options": ["none"],
    "contains": "game_over",
    "next_room": None
}

room_one = {
    id: 1,
    "move_options": ["south", "exit"],
    "contains": "exit",
    "next_room": {"south": 2, "exit": 0}
}

room_two = {
    id: 2,
    "move_options": ["north", "east"],
    "contains": "boss",
    "next_room": {"north": 1, "east": 8}
}

room_three = {
    id: 3,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_four = {
    id: 4,
    "move_options": ["south"],
    "contains": "tutorial",
    "next_room": {"south": 5}
}

room_five = {
    id: 5,
    "move_options": ["north", "south"],
    "contains": "torch",
    "next_room": {"north": 4, "south": 6}
}

room_six = {
    id: 6,
    "move_options": ["north", "east"],
    "contains": "empty",
    "next_room": {"north": 5, "east": 12}
}

room_seven = {
    id: 7,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_eight = {
    id: 8,
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": {"west": 2, "east": 14}
}

room_nine = {
    id: 9,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_ten = {
    id: 10,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_eleven = {
    id: 11,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_twelve = {
    id: 12,
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": {"west": 6, "east": 18}
}

room_thirteen = {
    id: 13,
    "move_options": ["south", "east"],
    "contains": "empty",
    "next_room": {"south": 14, "east": 19}
}

room_fourteen = {
    id: 14,
    "move_options": ["north", "west"],
    "contains": "empty",  
    "next_room": {"north": 13, "west": 8}
}

room_fifteen = {
    id: 15,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_sixteen = {
    id: 16,
    "move_options": ["south"],
    "contains": "chest1",
    "next_room": {"south": 17}
}

room_seventeen = {
    id: 17,
    "move_options": ["north", "south", "east"],
    "contains": "empty",
    "next_room": {"north": 16, "south": 18, "east": 23}
}

room_eighteen = {
    id: 18,
    "move_options": ["north", "west"],
    "contains": "empty",
    "next_room": {"north": 17, "west": 12}
}

room_ninteen = {
    id: 19, 
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": {"west": 13, "east": 25}
}

room_twenty = {
    id: 20,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_twentyone = {
    id: 21,
    "move_options": ["east"],
    "contains": "chest2",
    "next_room": {"east": 27}
}

room_twentytwo = {
    id: 22,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_twentythree = {
    id: 23,
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": {"west": 17, "east": 29}
}

room_twentyfour = {
    id: 24,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

room_twentyfive = {
    id: 25,
    "move_options": ["south", "west"],
    "contains": "monster2",
    "next_room": {"south": 26, "west": 19}
}

room_twentysix = {
    id: 26,
    "move_options": ["north", "south"],
    "contains": "empty",
    "next_room": {"north": 25, "south": 27}
}

room_twentyseven = {
    id: 27,
    "move_options": ["north", "south", "west"],
    "contains": "empty",
    "next_room": {"north": 26, "south": 28, "west": 21}
}

room_twentyeight = {
    id: 28,
    "move_options": ["north", "south"],
    "contains": "monster1",
    "next_room": {"north": 27, "south": 29}
}

room_twentynine = {
    id: 29,
    "move_options": ["north", "west"],
    "contains": "empty",
    "next_room": {"north": 28, "west": 23}
}

room_thirty = {
    id: 30,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": None
}

class GameMap():
    """
    Handles our game map
    """

    def __init__(self):
        self.map = [room_zero, room_one, room_two, room_three, room_four, room_five, room_six, room_seven, room_eight, room_nine, room_ten, room_eleven, room_twelve, room_thirteen, room_fourteen, room_fifteen, room_sixteen, room_seventeen, room_eighteen, room_ninteen, room_twenty, room_twentyone, room_twentytwo, room_twentythree, room_twentyfour, room_twentyfive, room_twentysix, room_twentyseven, room_twentyeight, room_twentynine, room_thirty],
        self.start_location = 4 # player start on map
        self.position = self.start_location
        self.move_options_str = ""

    def print_map(self):
        self.move_options_str = ""
        print(f"You are in room: {self.position}")
        print(f"The room contains: {self.map[0][self.position]['contains']}")
        for i in range (len(self.map[0][self.position]['move_options'])):
            self.move_options_str += self.map[0][self.position]['move_options'][i] + ", "
        print(f"You can move {self.move_options_str.upper()}")
        
