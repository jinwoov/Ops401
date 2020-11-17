# Script Name: Ops Challenge 29
# Author: Jin Kim
# Date of last revision: 11/16/2020
# Description of purpose: Finding the file using user input part 1/3


# importing library
import sys
from classes.search import *

## Declare functions
def interface():
    # operSys = sys.platform
    # if operSys.lower().__contains__("win"):
    #     search_windows()
    # # else:
    # #     search_linux()
    search_file()
    exit(0)

## Main
def main():
    interface()

if __name__ == "__main__":
    main()
## END