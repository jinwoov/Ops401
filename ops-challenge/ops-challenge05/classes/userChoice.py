from cryptography.fernet import Fernet
from helper_method import *

currentPath = "./"
listOfFiles = list()

# def filePassage(uc, key):
#     global listOfFiles
#     f = Fernet(key)
#     if(uc == "1"):
#         for (dirpath, dirnames, filenames) in os.walk(currentPath):
#             listOfFiles += [os.path.join(dirpath, file) for file in filenames]
#     if(uc == "2" and len(listOfFiles) <= 0):
#         print(colors.fg.red, "you have to encrypt file first !!!",colors.reset)
#     for elem in listOfFiles:
#         print(elem)
#         if(uc == "1"):
#             encryptFile(elem, key)
#         elif(uc == "2"):
#             decryptFile(elem, key)
#         animated_marker()
#     print(colors.fg.magenta, "Process Complete. Press any key to go to interface", colors.reset)
#     input()

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