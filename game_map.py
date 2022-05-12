#-----------------------------------------------------------
# |1player exit   7walled  13empty   19empty   25monster2   |
# |2boss          8empty   14empty   20walled  26empty      |
# |3walled        9walled  15walled  21chest2  27empty      |
# |4player start  10walled 16chest1  22walled  28monster1   |
# |5empty         11walled 17empty   23empty   29empty      |  
# |6empty         12empty  18empty   24walled  30walled     |
#------------------------------------------------------------

room_one = {
    "move_options": ["south", "exit"],
    "contains": "exit"
}

room_two = {
    "move_options": ["north", "east"],
    "contains": "boss"
}

room_three = {
    "move_options": ["none"],
    "contains": "wall"
}

room_four = {
    "move_options": ["south"],
    "contains": "start"
}

room_five = {
    "move_options": ["north", "south"],
    "contains": "empty"
}

room_six = {
    "move_options": ["north", "east"],
    "contains": "empty"
}

room_seven = {
    "move_options": ["none"],
    "contains": "wall"
}

room_eight = {
    "move_options": ["west", "east"],
    "contains": "empty"
}

room_nine = {
    "move_options": ["none"],
    "contains": "wall"
}

room_ten = {
    "move_options": ["none"],
    "contains": "wall"
}

room_eleven = {
    "move_options": ["none"],
    "contains": "wall"
}

room_twelve = {
    "move_options": ["west", "east"],
    "contains": "empty"
}

room_thirteen = {
    "move_options": ["south", "east"],
    "contains": "empty"
}

room_fourteen = {
    "move_options": ["north", "west"],
    "contains": "empty"
}

room_fifteen = {
    "move_options": ["none"],
    "contains": "wall"
}

room_sixteen = {
    "move_options": ["south"],
    "contains": "chest1"
}

room_seventeen = {
    "move_options": ["north", "south", "east"],
    "contains": "empty"
}

room_eighteen = {
    "move_options": ["north", "west"],
    "contains": "empty"
}

room_ninteen = {
    "move_options": ["west", "east"],
    "contains": "empty"
}

room_twenty = {
    "move_options": ["none"],
    "contains": "wall"
}

room_twentyone = {
    "move_options": ["east"],
    "contains": "chest2"
}

room_twentytwo = {
    "move_options": ["none"],
    "contains": "wall"
}

room_twentythree = {
    "move_options": ["west", "east"],
    "contains": "empty"
}

room_twentyfour = {
    "move_options": ["none"],
    "contains": "wall"
}

room_twentyfive = {
    "move_options": ["south", "west"],
    "contains": "monster2"
}

room_twentysix = {
    "move_options": ["north", "south"],
    "contains": "empty"
}

room_twentyseven = {
    "move_options": ["north", "south", "west"],
    "contains": "empty"
}

room_twentyeight = {
    "move_options": ["north", "south"],
    "contains": "monster1"
}

room_twentynine = {
    "move_options": ["north", "west"],
    "contains": "empty"
}

room_thirty = {
    "move_options": ["none"],
    "contains": "wall"
}

class GameMap():
    """
    Handles our game map
    """

    def __init__(self):
        pass
