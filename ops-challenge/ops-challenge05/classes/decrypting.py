from cryptography.fernet import Fernet
from .helper_method import *

## Decrypting the files 
def decryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as lines:
        encrypted_data = lines.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file, "wb") as lines:
        lines.write(decrypted_data)
    

def decryptMessage(key, msg):
    f = Fernet(key)
    decryptMessage = f.decrypt(msg)
    print("Decrypting message")
    animated_marker()
    print(colors.fg.green, str(decryptMessage), colors.reset)