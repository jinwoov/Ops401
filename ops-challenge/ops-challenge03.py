#!/usr/bin/env python3

from cryptography.fernet import Fernet
import time, progressbar, os

# Declare variable
file = "./encrypt_text.txt"
output = ""

def generageKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
    return open("key.key", "rb").read()

def mainMenu(key):
    print("""

     _    _           _     ______ _                     
    | |  | |         | |   |  ____| |                    
    | |__| | __ _ ___| |__ | |__  | | _____      ___ __  
    |  __  |/ _` / __| '_ \|  __| | |/ _ \ \ /\ / / '_ \ 
    | |  | | (_| \__ \ | | | |    | | (_) \ V  V /| | | |
    |_|  |_|\__,_|___/_| |_|_|    |_|\___/ \_/\_/ |_| |_|
                                                        
                               by Jin Kim                       


    1) Encrypt File
    2) Decrypt File
    3) Encrypt a Message
    4) Decrypt a Message
    5) Exit
    """)
    userChoice = input("Choice ? ")
    if(userChoice == "5" or userChoice == None):
        print(colors.fg.green, "Thanks for playing", colors.reset)
        exit(0)
    choiceMenu(userChoice,key)

    
def choiceMenu(uc, key):
    global output
    if(uc == "1"):
        encryptFile(file, key)
    elif(uc == "2"):
        decryptFile(file, key)
    elif(uc == "3"):
        output = encryptMessage(key)
    else:
        if(str(output) == ""):
            print(colors.fg.red, "You have to encrypt first!!!!!", colors.reset)
            return
        else:
            decryptMessage(key,output)
            
## Do the encrypt file
def encryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as fl:
        fl_data = fl.read()
        encrypt_data = f.encrypt(fl_data)
    print("It is reading to the file")
    animated_marker()
    with open(file, "wb") as fl:
        fl.write(encrypt_data)
    print("It is writing to the file")
    animated_marker()

## Do the decrypt file
def decryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as lines:
        encrypted_data = lines.read()
    print("It is reading to the file")
    animated_marker()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file, "wb") as lines:
        lines.write(decrypted_data)

## Do the encrypt a message
def encryptMessage(key):
    f = Fernet(key)
    userMsg = input("What do you want to encrypt? ").encode()
    encryptMessage = f.encrypt(userMsg)
    print("Encrypting message")
    animated_marker()
    print("Here is the encrypted message")
    print(colors.fg.green, encryptMessage, colors.reset)
    input("Type anything to continue")
    return encryptMessage

## Do the decrypt a message
def decryptMessage(key, msg):
    f = Fernet(key)
    decryptMessage = f.decrypt(msg)
    print(colors.fg.green, decryptMessage, colors.reset)

## Helper Methods
## Source: https://www.geeksforgeeks.org/progress-bars-in-python/
def animated_marker(): 
    widgets = ['Loading: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(15): 
        time.sleep(0.1) 
        bar.update(i)
    print("Finished")

class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'
        red='\033[0;31m'
        orange = '\033[33m'

def main():
    if(os.path.exists("key.key")):
        key = loadKey()
    else:
        generageKey()
        

    while(True):
        mainMenu(key)

# MAIN

if __name__ == "__main__":
    main()


# END