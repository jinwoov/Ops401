import subprocess, os
from time import sleep
from .colors import *

# Declare variables



# querying the functions to check if the file exists.
def search_file():
    try:
        # prompting user with different option
        user_file = input("What file name do you want to search? ")
        dir_location = input("What directory do you want to search in? ")
        path_way = os.path.abspath(dir_location)

        # Printing out to check with the user if they are satisfied with their answer
        print(colors.fg.green, path_way , f"File Name: {user_file}", colors.reset)
        user_choice = input("Is this where and what you want to search? (y/n) ")

        # while loop to check if the answer was y if not it will run continuous loop to get yes as a output.
        while (user_choice != "y"):
            dir_location = input("What directory do you want to search in? ")
            path_way = os.path.abspath(dir_location)
            print(colors.fg.green, path_way , f"File Name: {user_file}", colors.reset)
            user_choice = input("Is this where and what you want to search? (y/n) ")
                
        counter = output_search(user_file, path_way)

        if(counter == 0):
            print(colors.fg.red, "No result found", colors.reset)
        else:
            print(colors.fg.green, f"{counter} out of {total_files} files were matched", colors.reset)
        input("Search complete")

    except Exception as msg:
        print(msg)
        exit(1)

# universal file finder
def output_search(sf, pt):
    count = 0
    global total_files
    total_files = 0
    for root, dirs, files in os.walk(pt):
            for file in files:
                if(file.lower().__contains__(sf)):
                    print(os.path.join(root, file))
                    sleep(1.5)
                    count += 1
                total_files += 1
    return count