import os, getpass
from decouple import config
from .hashes import *
def query_virusTotal():
    hashcode = get_hashCode()
    path = os.path.dirname(__file__)
    api = input("Whats your API key? ")
    if(api == ""):
        api = config('vtkey')
    username = getpass.getuser()
    query = f"python {path}/virustotal-search.py -k " + api + " -m " + hashcode
    os.system(query)

def get_hashCode():
    target_file = input("whats the target file? ")
    target_file = os.path.abspath(target_file)
    return hash_co(target_file)