import socket
from .colors import *

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def main_port():
    timeout = 3000
    sockmod.settimeout(timeout)

    hostip = input("What Ip address? ")
    port = input("What Port? ")

    portScanner(hostip, port)

def portScanner(host_ip, portno):

    if sockmod.bind((host_ip, int(portno))): \
        print("Port closed")
    else:
        print("Port open")
