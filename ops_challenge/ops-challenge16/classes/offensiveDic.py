import os
from time import sleep

class OffensiveDic:
    
    def __init__(self):
        self.dirPath = self.directoryPath()

    ## Asking user which text file do they want to analyze
    def directoryPath(self):
        userOutcome = input("Whats the directory this word list? (default will be rockyou.txt)")
        if(userOutcome == ""):
            userOutcome = "./rockyou.txt"
        return userOutcome
    
    ## printing the content in the text file
    def printToScreen(self):
        textFile = os.path.abspath(self.dirPath)
        file = open(textFile, "r")
        readfile = file.readlines()
        for line in readfile:
            print(line)
            sleep(.5)
        input("Complete. Press any key to contine")