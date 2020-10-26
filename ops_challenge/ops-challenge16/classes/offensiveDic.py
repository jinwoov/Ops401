import os
from time import sleep

class OffensiveDic:
    
    def __init__(self):
        self.dirPath = self.directoryPath()

    def directoryPath(self):
        userOutcome = input("Whats the directory this word list? (default will be rockyou.txt)")
        if(userOutcome == ""):
            userOutcome = "./rockyou.txt"
        return userOutcome
    
    def printToScreen(self):
        textFile = os.path.abspath(self.dirPath)
        file = open(textFile, "r")
        readfile = file.readlines()
        for line in readfile:
            print(line)
            sleep(.5)
        input("Complete. Press any key to contine")