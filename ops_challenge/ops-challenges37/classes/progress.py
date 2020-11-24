import progressbar, time
from .colors import *
def animated_marker(): 
    widgets = ['In Process: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
    for i in range(17): 
        time.sleep(0.1) 
        bar.update(i)
    print ("\033[A                             \033[A")
    print(colors.fg.green, "Finished!",colors.reset)