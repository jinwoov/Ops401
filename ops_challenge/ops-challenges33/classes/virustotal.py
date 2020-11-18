import os, getpass
from decouple import config
from .hashes import *

## querying the virus total using virustotal-search.py and api
def query_virusTotal():
    ## getting the hash code of the file of choice
    hashcode = get_hashCode()
    path = os.path.dirname(__file__)
    api = input("Whats your API key? ")
    ## validation to check if the key is there
    if(api == ""):
        api = config('vtkey')
    username = getpass.getuser()
    ## calling the query
    query = f"python {path}/virustotal-search.py -k " + api + " -m " + hashcode
    os.system(query)

## getting the hashcode using the previous challenge
def get_hashCode():
    target_file = input("whats the target file? ")
    target_file = os.path.abspath(target_file)
    return hash_co(target_file)