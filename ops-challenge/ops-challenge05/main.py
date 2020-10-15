from classes.key import *
from classes.helper_method import *
from classes.userChoice import *

## interface screen
def interface(key):
    print(f"""


     ______                             _   _             _             
    |  ____|                           | | (_)           | |            
    | |__   _ __   ___ _ __ _   _ _ __ | |_ _ _ __   __ _| |_ ___  _ __ 
    |  __| | '_ \ / __| '__| | | | '_ \| __| | '_ \ / _' | __/ _ \| '__|
    | |____| | | | (__| |  | |_| | |_) | |_| | | | | (_| | || (_) | |   
    |______|_| |_|\___|_|   \__, | .__/ \__|_|_| |_|\__,_|\__\___/|_|   
                             __/ | |                                    
                            |___/|_|                     
                                                        
                              {colors.fg.orange} by Jin Kim{colors.reset}                       

    1) Encrypt File
    2) Decrypt File
    3) Encrypt a Message
    4) Decrypt a Message
    5) Encrypt the current folder
    6) Decrypt the current folder
    {colors.fg.red}7) Initiate RANSOMEWARE{colors.reset}
    8) Exit
    """)
    userChoice = input("Choice ? ")
    if(userChoice == "8" or userChoice == None):
        print(colors.fg.green, "Thanks for playing", colors.reset)
        exit(0)
    choiceMenu(userChoice,key)


## Create a main function to execute following functions
def main():
    keyring = Key()
    interface(keyring.gkey)
    
    



# MAIN
if __name__ == "__main__":
    while True:
        main()

# END