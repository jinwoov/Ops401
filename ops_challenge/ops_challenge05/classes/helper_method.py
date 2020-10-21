import time, progressbar, os

def animated_marker(): 
    widgets = ['In Process: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
    for i in range(17): 
        time.sleep(0.1) 
        bar.update(i)
    print ("\033[A                             \033[A")
    print("Finished!")

class colors:
    reset='\033[0m'
    class fg:
        magenta='\033[35m'
        green='\033[32m'
        red='\033[0;31m'
        orange = '\033[33m'