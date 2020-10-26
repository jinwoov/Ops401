from classes.offensiveDic import *
from classes.defensivePW import *
from time import sleep

def interface():
    print("""


                          _     _           _       _ _   
                         | |   (_)         | |     (_) |  
     _ __ ___   ___   ___| |__  _ ___ _ __ | | ___  _| |_ 
    | '_ ' _ \ / _ \ / __| '_ \| / __| '_ \| |/ _ \| | __|
    | | | | | | (_) | (__| | | | \__ \ |_) | | (_) | | |_ 
    |_| |_| |_|\___/ \___|_| |_|_|___/ .__/|_|\___/|_|\__|
                                    | |                  
                                    |_|   
                                    by Jin Kim               

    Please enter what you would like to perform!!

    1) Offensive, Dictionary Iterator
    2) Defensive, Password Recognized
    3) Defensive; Password Complexity
    4) Exit

    """)

    userInput = input()

    if(userInput == "1"):
        oD = OffensiveDic()
        oD.printToScreen()
    elif(userInput == "2"):
        dD = DefensivePW()
        dD.searchInText()
    elif(userInput == "3"):
        # dP = DefensivePC()
        print("Not available yet. Coming soon!")
        input()
    else:
        print("Exiting......")
        sleep(1)
        exit()


while True:
    interface()
