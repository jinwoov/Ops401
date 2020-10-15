from cryptography.fernet import Fernet
from .helper_method import *
from .encrypting import *
from .decrypting import *
from .recursion import *

currentPath = "./"
listOfFiles = list()
output = ""
text_file = "./encrypt_text.txt"

def choiceMenu(uc, key):
    global output
    if(uc == "1"):
        encryptFile(text_file, key)
        animated_marker()
        input("Process Complete! Please press any key!")
    elif(uc == "2"):
        decryptFile(text_file, key)
        animated_marker()
        input("Process Complete! Please press any key!")
    elif(uc == "3"):
        output = encryptMessage(key)
        input("Process Complete! Please press any key!")
    elif(uc == "4"):
        if(str(output) == ""):
            print(colors.fg.red, "You have to encrypt first!!!!!", colors.reset)
            input("Process Complete! Please press any key!")
            return
        else:
            decryptMessage(key,output)
        input("Process Complete! Please press any key!")
    elif(uc == "5"):
        filePassage(uc,key)
    elif(uc == "6"):
        filePassage(uc,key)
    elif(uc == "7"):
        
