
import socket
from .colors import *


def bannergrab(host, port):
    timeout = 5
    sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockmod.connect((host, int(port)))
    sockmod.settimeout(timeout)
    print(sockmod.recv(1024))

def main_banner():
    try:
        host = input("What IP you want to grab banner? ")
        port = input("What port you want to grab banner? ")
        bannergrab(host, port)
    
    except ConnectionRefusedError as msg:
        print(colors.fg.red, msg, colors.reset)
        pass
