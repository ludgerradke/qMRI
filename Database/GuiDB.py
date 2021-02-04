import sqlite3
import numpy as np
from Database.utils import *


class GuiDB:

    def __init__(self):
        self.con = sqlite3.connect(r'\temp\gui.db')
        self.cur = self.con.cursor()
        self.__create()

    ####################################################################################################################
    # public methods
    ####################################################################################################################
    def add(self, key, arr):
        pass

    def get(self, key, pointer):
        pass

    ####################################################################################################################
    # private methods
    ####################################################################################################################

    def __create(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS `user_settings` '
            '(setting text, value any) '
        )