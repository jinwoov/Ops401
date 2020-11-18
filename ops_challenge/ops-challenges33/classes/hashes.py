import hashlib,datetime, os, getpass
from .search import *
from .colors import *

### Getting the user input to search specified folder
def get_hashcode():
    folder_name = input("Enter the folder you want to scan? ")
    output_search(folder_name)
    input("Complete")

## Getting current time stamp
def get_time():
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%b-%d-%Y-%H:%M:%S")
    return timestampStr
    
# Outputting final results
def output_search(pt):
    user = getpass.getuser()
    abs_path= ""
    if(pt == "~/"):
        abs_path = f"C:/User/{user}"
    else:
        abs_path = os.path.abspath(pt)
    print(colors.fg.orange, "Timestamp            File-name            Hash-code             Size     File-path", colors.reset)
    for root, dirs, files in os.walk(abs_path):
            for filo in files:
                try:
                    full_path= os.path.join(root, filo)
                    hash_value = hash_co(full_path)
                    print(f"{get_time()} {filo} {hash_value}   {os.path.getsize(full_path)}   {full_path}")
                    sleep(1.5)
                except Exception as msg:
                    print(msg)
                    continue

## Getting the hash code.
def hash_co(fn):
    md_hash = hashlib.md5()
    with open(fn, "rb") as f:
        for byte_block in iter(lambda: f.read(4896),b""):
            md_hash.update(byte_block)
    f.close()
    return md_hash.hexdigest()
