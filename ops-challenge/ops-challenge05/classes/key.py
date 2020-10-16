from cryptography.fernet import Fernet
import os

class Key:

    def __init__(self):
        self.generateKey()
        self.gkey = self.loadKey()

    ## Generating the key
    def generateKey(self):
        keydir = "../../key.key"
        key = Fernet.generate_key()
        if(os.path.exists(keydir) is False):
            with open(keydir, "wb") as key_file:
                key_file.write(key)


    ## Loading the key
    def loadKey(self):
        keydir = "../../key.key"
        return open(keydir, "rb").read()