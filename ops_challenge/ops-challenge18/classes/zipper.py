from zipfile import ZipFile
from time import sleep

class Zipper():
    # properties that will be set when object is instantiate.
    def __init__(self):
        self.zip_file = self.what_file()
        self.file = "./rockyou.txt"
    # This will ask what file user wants to extract
    def what_file(self):
        output = input("What file do you want to unzip? ")
        while(output == ""):
            output = input("Enter correct file name ")
        return output
    # The function that is used to crack the zip file
    def crack_pw(self):
        with ZipFile(self.zip_file) as zf:
            file = open(self.file, "r")
            readfile = file.read().splitlines()
            for line in readfile:
                try:
                    print(f"Testing: {line}")
                    zf.extractall(pwd=bytes(line, 'utf-8'))
                    print(f"Password was {line}")
                    break
                except:
                    print(f"Password: {line} wasn't the match")
                    sleep(2)
                    continue
        input("Enter any button to finish")