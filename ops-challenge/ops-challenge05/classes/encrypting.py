from cryptography.fernet import Fernet
from .helper_method import *


## Encrypting the files
def encryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as fl:
        fl_data = fl.read()
        encrypt_data = f.encrypt(fl_data)
    with open(file, "wb") as fl:
        fl.write(encrypt_data)

## Do the encrypt a message
def encryptMessage(key):
    f = Fernet(key)
    userMsg = input("What do you want to encrypt? ").encode()
    encryptMessage = f.encrypt(userMsg)
    print("Encrypting message")
    animated_marker()
    print("Here is the encrypted message")
    print(colors.fg.green, str(encryptMessage), colors.reset)
    return encryptMessage