# ascii art title from https://patorjk.com/software/taag/#p=display&f=Bloody&t=Dungeon%20%0ADelve
# Our main code file.  It mainly runs the game loop
# by Travis Mix
# May 09, 2022

from game_loop import *




title = """
▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █    
▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █    
░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒   
░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒   
░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░   
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    
 ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   
 ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░    
   ░       ░              ░       ░    ░  ░    ░ ░           ░    
 ░                                                                
▓█████▄ ▓█████  ██▓  ██▒   █▓▓█████                               
▒██▀ ██▌▓█   ▀ ▓██▒ ▓██░   █▒▓█   ▀                               
░██   █▌▒███   ▒██░  ▓██  █▒░▒███                                 
░▓█▄   ▌▒▓█  ▄ ▒██░   ▒██ █░░▒▓█  ▄                               
░▒████▓ ░▒████▒░██████▒▒▀█░  ░▒████▒                              
 ▒▒▓  ▒ ░░ ▒░ ░░ ▒░▓  ░░ ▐░  ░░ ▒░ ░                              
 ░ ▒  ▒  ░ ░  ░░ ░ ▒  ░░ ░░   ░ ░  ░                              
 ░ ░  ░    ░     ░ ░     ░░     ░                                 
   ░       ░  ░    ░  ░   ░     ░  ░                              
 ░                       ░                 
"""

input("Please Maximize your console window then press ENTER...")
clear_screen()

print(title)

# start game loop
game_loop()

# prevent closing on end
print() # spacing
input("Thanks for playing Dungeon Delve! Press ENTER to close")
