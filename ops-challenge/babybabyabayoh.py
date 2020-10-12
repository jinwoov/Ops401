
from cryptography.fernet import Fernet
import time

# Declaring variables
file = "ops06.txt"

# Declaring functions

## function to load interface
def interface():
    print("""
    What options do you wanna choose?

    1) Encrypt File
    2) Decrypt file
    3) Encrypt a message
    4) Decrypt a message
    5) exit
    """)
    userInput = input("options ? ")

    if(userInput == "1"):
        encryptFile()
    elif(userInput == "2"):
        ## Decrypt file here
        print("")
    elif(userInput == "3"):
        ## Encrypt a message
        print("")
    elif(userInput == "4"):
        ## Decrypt a message
        print("")
    elif(userInput == "5"):
        print("Thank you for using this application")
        exit(0)
    else:
        print("put right input here you")
        interface()


def encryptFile():
    f = Fernet(key)
    with open(file, "rb") as fileread:
        readfile = fileread.read()
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
    time.sleep(2)
    print("file has been encrypted")

## Generating the key to be used for hashing
def generageKey():
    key = Fernet.generate_key()
    with open("demo.key", "wb") as key_file:
        key_file.write(key)

## Getting the key from key file
def loadKey():
    return open("demo.key", "rb").read()







## main

generageKey()
key = loadKey()
while(True):
    interface()

## END 