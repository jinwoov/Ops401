import os
from decouple import config
from .hashes import *
def query_virusTotal():
    hashcode = get_hashCode()
    api = input("Whats your API key? ")
    if(api == ""):
        api = config('vtkey')
    
    query = "python C:/Users/User/codefellows/Ops401/ops_challenge/ops-challenges33/classes/virustotal-search.py -k " + api + " -m " + hashcode
    os.system(query)

def get_hashCode():
    target_file = input("whats the target file? ")
    target_file = os.path.abspath(target_file)
    return hash_co(target_file)