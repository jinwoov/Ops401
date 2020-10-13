#!/usr/bin/env python3
# Script Name: Ops Challenge 3
# Author: Jin Kim
# Date of last revision: 10/12/2020
# Description of purpose: Encrypting and decrypting the files and message

# Bringing the library
from cryptography.fernet import Fernet
import time, progressbar, os

# Declare variable
file = "./encrypt_text.txt"
output = ""


## Generating the key
def generageKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


## Loading the key
def loadKey():
    return open("key.key", "rb").read()

## User main interface where user will be given choices and take the input
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


## invoke the function of whichever user's choice is
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
## This is the fancy spinner
def animated_marker(): 
    widgets = ['Loading: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(15): 
        time.sleep(0.1) 
        bar.update(i)
    print("Finished")
## Class that will carry the color
class colors:
    reset='\033[0m'
    class fg:
        green='\033[32m'
        red='\033[0;31m'
        orange = '\033[33m'

## Validating if the text file is there, otherwise generate the file
def validatingFile():
    if(~os.path.exists(file)):
        line = open(file, "w")
        line.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis dictum nibh facilisis tellus malesuada, at aliquam diam bibendum. Praesent convallis euismod ligula eget faucibus. Integer sed leo arcu. Morbi eu efficitur orci. Curabitur tellus dolor, faucibus vel dui ac, tincidunt venenatis mi. Praesent scelerisque lectus ac leo vestibulum mattis. Sed sit amet felis elit. Cras in arcu eu odio sollicitudin ullamcorper sed in ipsum.

Nulla rhoncus, eros et pellentesque volutpat, odio velit dapibus tortor, vitae pellentesque lorem metus eget tellus. Cras ornare et nisl id vehicula. Donec auctor vitae ligula sed blandit. Vivamus pellentesque, lorem a eleifend vestibulum, augue turpis molestie sem, pellentesque tincidunt orci odio tempor velit. Quisque dignissim, ligula vel aliquam sagittis, ex felis eleifend lorem, ac pretium tortor libero sit amet ante. Nulla ut euismod est. Aliquam pretium dolor id mauris convallis, nec interdum dui porttitor. Aenean libero ex, tincidunt id scelerisque quis, lacinia ut libero. Nullam pellentesque tellus erat, eu scelerisque nibh vulputate sodales. Donec leo elit, consequat eu commodo sit amet, pretium sit amet nibh. Aliquam vitae ultrices nisl. Curabitur vulputate porta convallis. Suspendisse et elit a libero bibendum laoreet.

Donec quis nunc rutrum, mollis risus ac, mattis sapien. Suspendisse ut lacinia dolor. Sed vel eros arcu. Morbi lobortis sed lorem tempus viverra. Praesent molestie scelerisque lacus, nec semper est ornare quis. Nunc vulputate purus id ex aliquam, non iaculis mi ornare. Nunc non molestie leo. Etiam ornare leo urna, sed tristique turpis aliquet quis. In a mi a nulla mollis rutrum. Sed faucibus faucibus dui, vel gravida arcu pretium in.

Pellentesque non quam lacus. Mauris pretium nisl nibh, ac dictum augue viverra nec. Quisque placerat, est sed sollicitudin lacinia, elit arcu congue lorem, vitae hendrerit nunc turpis vitae orci. Donec iaculis sit amet tortor blandit volutpat. In ullamcorper accumsan eros eu hendrerit. Suspendisse nulla magna, ornare ut augue non, imperdiet efficitur ex. Morbi et quam quam. Curabitur accumsan eget ex sodales aliquet. Cras finibus risus urna, nec porta risus ultricies in. Suspendisse potenti. Curabitur varius dolor at urna mollis, at cursus magna maximus.

Phasellus ullamcorper lorem vel metus molestie, ac luctus dui vehicula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis imperdiet mi vel tortor semper, pellentesque efficitur leo venenatis. Ut sapien lectus, imperdiet nec tincidunt vel, euismod et elit. Donec laoreet sapien non massa auctor condimentum. Nullam sagittis convallis leo, nec consectetur justo rhoncus eget. Aliquam dolor lectus, eleifend sit amet nibh a, pretium ullamcorper nulla. Aliquam id eros nec sem finibus tempor. Mauris porttitor orci id ipsum egestas, nec luctus enim rhoncus. Integer egestas leo in neque iaculis finibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus consectetur metus sed dolor feugiat, malesuada laoreet est elementum. Fusce pellentesque ex et ante ullamcorper, in vulputate ex laoreet.
        """)
        line.close()

## Main functions
def main():
    if(~os.path.exists("./key.key")):
        generageKey()
    key = loadKey()
    
    validatingFile()

    while(True):
        mainMenu(key)

# MAIN

if __name__ == "__main__":
    main()


# END