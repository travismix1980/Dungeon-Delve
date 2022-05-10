# ascii art title from https://patorjk.com/software/taag/#p=display&f=Bloody&t=Dungeon%20%0ADelve

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