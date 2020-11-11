import logging
import logging.config
class Logs:

    def __init__(self, fname, lvls):
        self.f_handler = logging.FileHandler(fname)
        self.setting_lvl(lvls)
        self.format_log()

    def setting_lvl(self, lvl):
        if(lvl == "i"):
            self.f_handler.setLevel(logging.INFO)
        elif(lvl == "w"):
            self.f_handler.setLevel(logging.WARNING)
        elif(lvl == "e"):
            self.f_handler.setLevel(logging.ERROR)

    def format_log(self):
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.f_handler.setFormatter(f_format)