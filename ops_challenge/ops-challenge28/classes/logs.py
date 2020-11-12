import logging
import logging.config
class Logs:

    def __init__(self, fname, lvls):
        self.logger = logging.getLogger(__name__)
        self.c_handler = logging.StreamHandler()
        self.f_handler = logging.FileHandler(fname)
        self.setting_lvl(lvls)
        self.format_log()

    def setting_lvl(self, lvl):
        if(lvl == "i"):
            self.c_handler.setLevel(logging.INFO)
            self.f_handler.setLevel(logging.INFO)
        elif(lvl == "w"):
            self.c_handler.setLevel(logging.WARNING)
            self.f_handler.setLevel(logging.WARNING)
        elif(lvl == "e"):
            self.c_handler.setLevel(logging.ERROR)
            self.f_handler.setLevel(logging.ERROR)

    def format_log(self):
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.f_handler.setFormatter(f_format)
        self.c_handler.setFormatter(f_format)
        self.logger.addHandler(self.f_handler)
        self.logger.addHandler(self.c_handler)

        