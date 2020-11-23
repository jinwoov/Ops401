from classes.banner_grab import *
from time import sleep

def interface():
    try:
        print("""
        1) Banner Grabbing
        2) Exit
        """)
        user_answer = input("Whats your choice... ")

        if (user_answer == "1"):
            banner_grabbing()
        else:
            print("exiting.... ")
            sleep(1.5)
            exit(0)
    except Exception as msg:
        print(msg)
        exit(1)


if __name__ == "__main__":
    interface()
