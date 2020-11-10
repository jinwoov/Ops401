import os
from time import sleep

class DefensivePW:

    def __init__(self):
        self.userInput = input("What password do you want to look up? ")
        self.filePath = self.directoryInput()

    ## Taking user input to get the directory path
    def directoryInput(self):
        uPath = input("What's the file path for the text file? (default will be from rockyou.txt)")
        if(uPath == ""):
            uPath = "./rockyou.txt"
        return uPath

    ## Taking the path and user's input to check if it is in the text file.
    def searchInText(self):
        textFile = os.path.abspath(self.filePath)
        file = open(textFile, "r")
        readfile = file.read().splitlines()
        if(readfile.__contains__(self.userInput)):
            print(f"There is a password matches the {self.userInput} !!")
        else:
            print(f"There is no matching {self.userInput}")
        input("Complete. Press any key to contine")