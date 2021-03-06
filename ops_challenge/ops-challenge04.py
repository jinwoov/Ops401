#!/usr/bin/env python3
# Script Name: Ops Challenge 4
# Author: Jin Kim
# Date of last revision: 10/14/2020
# Description of purpose: Encrypt and decrypt the folder recursively.


# Library imports
from cryptography.fernet import Fernet
import time, progressbar, os

# Declare variables
currentPath = "./"
listOfFiles = list()
keyLocation = "../key.key"

# Declare functions
## interface where user will see
def interface(key):
    print("""


     ______                             _   _             _             
    |  ____|                           | | (_)           | |            
    | |__   _ __   ___ _ __ _   _ _ __ | |_ _ _ __   __ _| |_ ___  _ __ 
    |  __| | '_ \ / __| '__| | | | '_ \| __| | '_ \ / _' | __/ _ \| '__|
    | |____| | | | (__| |  | |_| | |_) | |_| | | | | (_| | || (_) | |   
    |______|_| |_|\___|_|   \__, | .__/ \__|_|_| |_|\__,_|\__\___/|_|   
                             __/ | |                                    
                            |___/|_|                     
                                                        
                               by Jin Kim                       


    1) Encrypt the current folder
    2) Decrypt the current folder
    3) Exit
    """)
    userChoice = input("Choice ? ")
    if(userChoice == "3" or userChoice == None):
        print(colors.fg.green, "Thanks for playing", colors.reset)
        exit(0)
    filePassage(userChoice,key)



## reading all of the file and encrypt it 
def filePassage(uc, key):
    global listOfFiles
    f = Fernet(key)
    if(uc == "1"):
        for (dirpath, dirnames, filenames) in os.walk(currentPath):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    if(uc == "2" and len(listOfFiles) <= 0):
        print(colors.fg.red, "you have to encrypt file first !!!",colors.reset)
    for elem in listOfFiles:
        print(elem)
        if(uc == "1"):
            encryptFile(elem, key)
        elif(uc == "2"):
            decryptFile(elem, key)
        animated_marker()
    print(colors.fg.magenta, "Process Complete. Press any key to go to interface", colors.reset)
    input()


## Encrypting the files
def encryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as fl:
        fl_data = fl.read()
        encrypt_data = f.encrypt(fl_data)
    with open(file, "wb") as fl:
        fl.write(encrypt_data)


## Decrypting the files 
def decryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as lines:
        encrypted_data = lines.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file, "wb") as lines:
        lines.write(decrypted_data)

### HELPER FUNCTIONS
## This is to generate the key
def generateKey():
    key = Fernet.generate_key()
    with open(keyLocation, "wb") as key_file:
        key_file.write(key)


## Loading the key
def loadKey():
    return open(keyLocation, "rb").read()

## Spinner
def animated_marker(): 
    widgets = ['In Process: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
    for i in range(17): 
        time.sleep(0.1) 
        bar.update(i)
    print ("\033[A                             \033[A")
    print("Finished!")

## Class of colors that will be used to show for the output
class colors:
    reset='\033[0m'
    class fg:
        magenta='\033[35m'
        green='\033[32m'
        red='\033[0;31m'
        orange = '\033[33m'

## MAIN function that will be ran when this is compiled
def main():
    if(os.path.exists(keyLocation) is False):
        generateKey()
    key = loadKey()
    while True:
        interface(key)


# MAIN
if __name__ == "__main__":
    main()

# END