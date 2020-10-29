#!/usr/bin/env python3
# Script Name: Ops Challenge 16 - Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author: Jin Kim
# Date of last revision: 10.26.2020
# Description of purpose: To see if the password is correctly protected and in a risk of vulnerability.

# This is the main file that will be executed when the application is ran.
# Importing python library

from classes.offensiveDic import *
from classes.defensivePW import *
from classes.zipper import *
from time import sleep
from classes.ssh import *

## Main interface outlook so when the application start it will trigger this.
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
    4) Authenticate to an SSH server
    5) Unzip my file
    6) Exit

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
    elif(userInput == "4"):
        user = AuthSSH()
        user.ssh_connection()
        input()
    elif(userInput == "5"):
        z = Zipper()
        z.crack_pw()
    else:
        print("Exiting......")
        sleep(1)
        exit()


while True:
    interface()
