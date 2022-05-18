#-----------------------------------------------------------
# |1player exit   7walled  13empty   19empty   25monster2   |
# |2boss          8empty   14empty   20walled  26empty      |
# |3walled        9walled  15walled  21chest2  27empty      |
# |4player start  10walled 16chest1  22walled  28monster1   |
# |5empty         11walled 17empty   23empty   29empty      |
# |6empty         12empty  18empty   24walled  30walled     |
#------------------------------------------------------------

from asyncio.windows_events import NULL


room_zero = {
    id: 0,
    "move_options": ["none"],
    "contains": "game_over",
    "next_room": NULL
}

room_one = {
    id: 1,
    "move_options": ["south", "exit"],
    "contains": "exit",
    "next_room": 2 if "south" else 0
}

room_two = {
    id: 2,
    "move_options": ["north", "east"],
    "contains": "boss",
    "next_room": 1 if "north" else 8,
}

room_three = {
    id: 3,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_four = {
    id: 4,
    "move_options": ["south"],
    "contains": "start",
    "next_room": 5
}

room_five = {
    id: 5,
    "move_options": ["north", "south"],
    "contains": "empty",
    "next_room": 4 if "north" else 6
}

room_six = {
    id: 6,
    "move_options": ["north", "east"],
    "contains": "empty",
    "next_room": 5 if "north" else 12
}

room_seven = {
    id: 7,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_eight = {
    id: 8,
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": 2 if "west" else 14
}

room_nine = {
    id: 9,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_ten = {
    id: 10,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_eleven = {
    id: 11,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_twelve = {
    id: 12,
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": 6 if "west" else 18
}

room_thirteen = {
    id: 13,
    "move_options": ["south", "east"],
    "contains": "empty",
    "next_room": 14 if "south" else 19
}

room_fourteen = {
    id: 14,
    "move_options": ["north", "west"],
    "contains": "empty",  
    "next_room": 13 if "north" else 8
}

room_fifteen = {
    id: 15,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_sixteen = {
    id: 16,
    "move_options": ["south"],
    "contains": "chest1",
    "next_room": 17
}

room_seventeen = {
    id: 17,
    "move_options": ["north", "south", "east"],
    "contains": "empty",
    "next_room": 16 if "north" else 18 if "south" else 23
}

room_eighteen = {
    id: 18,
    "move_options": ["north", "west"],
    "contains": "empty",
    "next_room": 17 if "north" else 12
}

room_ninteen = {
    id: 19, 
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": 13 if "west" else 25
}

room_twenty = {
    id: 20,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_twentyone = {
    id: 21,
    "move_options": ["east"],
    "contains": "chest2",
    "next_room": 27
}

room_twentytwo = {
    id: 22,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_twentythree = {
    id: 23,
    "move_options": ["west", "east"],
    "contains": "empty",
    "next_room": 17 if "west" else 29
}

room_twentyfour = {
    id: 24,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

room_twentyfive = {
    id: 25,
    "move_options": ["south", "west"],
    "contains": "monster2",
    "next_room": 26 if "south" else 19
}

room_twentysix = {
    id: 26,
    "move_options": ["north", "south"],
    "contains": "empty",
    "next_room": 25 if "north" else 27
}

room_twentyseven = {
    id: 27,
    "move_options": ["north", "south", "west"],
    "contains": "empty",
    "next_room": 26 if "north" else 28 if "south" else 21
}

room_twentyeight = {
    id: 28,
    "move_options": ["north", "south"],
    "contains": "monster1",
    "next_room": 27 if "north" else 29
}

room_twentynine = {
    id: 29,
    "move_options": ["north", "west"],
    "contains": "empty",
    "next_room": 28 if "north" else 23
}

room_thirty = {
    id: 30,
    "move_options": ["none"],
    "contains": "wall",
    "next_room": NULL
}

class GameMap():
    """
    Handles our game map
    """

    def __init__(self):
        self.map = [room_zero, room_one, room_two, room_three, room_four, room_five, room_six, room_seven, room_eight, room_nine, room_ten, room_eleven, room_twelve, room_thirteen, room_fourteen, room_fifteen, room_sixteen, room_seventeen, room_eighteen, room_ninteen, room_twenty, room_twentyone, room_twentytwo, room_twentythree, room_twentyfour, room_twentyfive, room_twentysix, room_twentyseven, room_twentyeight, room_twentynine, room_thirty],
        self.start_location = 29 # player start on map

    def print_map(self):
        print("You are in the starting room of the dungeon")
        position = self.start_location
        print(f"You are in room: {self.start_location}")
        print(f"The room contains: {self.map[0][position]['contains']}")
        move_options_str = ""
        for i in range (len(self.map[0][position]['move_options'])):
            move_options_str += self.map[0][position]['move_options'][i] + ", "
        print(f"You can move {move_options_str}")
