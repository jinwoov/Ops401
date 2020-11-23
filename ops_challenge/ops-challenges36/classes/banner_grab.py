import subprocess
from time import sleep
from .colors import *

def banner_grabbing():

    user_input = input("what ip/url address do you want to query? ")

    user_port = input("What port do you want to scan? ")
    print(colors.fg.green, "Net catting!", colors.reset)
    run_cmd("nc", user_input, user_port)
    print(colors.fg.green, "Telnetting~", colors.reset)
    run_cmd("telnet", user_input, user_port)
    print(colors.fg.green, "Nmapping!", colors.reset)
    nmaping(user_input)
    print(colors.fg.green, "Curlling!", colors.reset)
    curl_dest(user_input)
    print(colors.fg.green, "Whatweb!", colors.reset)
    what_web(user_input)

def what_web(dest):
    if(not "http" in dest):
        dest = f"http://{dest}"
    
    process_ww = subprocess.Popen(["whatweb", dest])
    try:
        process_ww.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process_ww.kill()
    sleep(1)
    print("Done")

def curl_dest(destIP):
    process2 = subprocess.Popen(["curl", "-s", "-I", destIP])
    try:
        process2.wait(timeout=5)
        if(process2.stdout == None):
            print("This IP doesn't have web server.")
        else:
            print(process2.stdout)
    except subprocess.TimeoutExpired:
        process2.kill()
    sleep(1)
    print("Done")

def run_cmd(cmd, dest, port):
    process = subprocess.Popen([cmd, dest, port])
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
    sleep(1)
    print("Done")

def nmaping(dest):
    process3 = subprocess.Popen(["nmap", "-sV", dest])
    try:
        process3.wait(timeout=2)
    except subprocess.TimeoutExpired:
        process3.kill()
    sleep(1)
    print("Done")