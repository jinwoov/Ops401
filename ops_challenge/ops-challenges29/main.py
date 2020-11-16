import sys
from classes.search import *


def interface():
    # operSys = sys.platform
    # if operSys.lower().__contains__("win"):
    #     search_windows()
    # # else:
    # #     search_linux()
    search_file()
    exit(0)


def main():
    interface()

if __name__ == "__main__":
    main()