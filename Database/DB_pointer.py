import sqlite3
import numpy as np
from Database.utils import *

class Connection:

    def __init__(self):
        # self.con = sqlite3.connect(':memory:')
        self.con = sqlite3.connect(r'\temp\guiDB.db')
        self.cur = self.con.cursor()
        self.__create_db()

    ####################################################################################################################
    # public methods
    ####################################################################################################################
    def add(self, key, arr):
        if key in ['d_array', 'm_array']:
            self.__add_array(key, arr)
        elif key in ["d_information"]:
            self.__add_information(key, arr)

    def get(self, key, pointer):
        if key in ['d_array', 'm_array']:
            return self.__get_array(key, pointer)
        elif key in ['d_information']:
            return self.__get_information(key, pointer)

    ####################################################################################################################
    # private methods
    ####################################################################################################################

    def __add_array(self, table_name: str, arr: np.ndarray):
        dtype = str(arr.dtype)
        shape = arr.shape
        if len(shape) == 3:
            slices = [i for i in range(shape[0])]
        elif len(shape) == 2:
            slices = [0]
            arr = np.resize(arr, (1, shape[-2], shape[-1]))
        else:
            return

        for slice_nr in slices:
            size_x = shape[-2]
            size_y = shape[-1]
            flatt_arr = bytes(arr[slice_nr].flatten())
            self.cur.execute(
                'INSERT INTO {} VALUES (?, ?, ?, ?, ?)'.format(table_name),
                (slice_nr, dtype, size_x, size_y, flatt_arr)
            )
            self.con.commit()

    def __add_information(self, key, arr):
        self.cur.execute(
            'INSERT INTO {} VALUES (?, ?)'.format(key),
            (arr[0], arr[1])
        )
        self.con.commit()

    def __get_array(self, key, slice_nr):

        cursor = self.cur.execute('SELECT * FROM {} WHERE slice=:slice'.format(key),
                                             {"slice": slice_nr})
        array_information = [info for info in cursor][0]
        array = np.frombuffer(array_information[-1], dtype=dtypes[array_information[1]]).reshape(
            (int(array_information[2]), int(array_information[3])))
        return array

    def __get_information(self, key, pointer):
        cursor = self.cur.execute('SELECT VALUE FROM {} WHERE information=:pointer'.format(key),
                                  {"pointer": pointer})
        info = [i for i in cursor]
        return info[0][0]

    def __create_db(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS `d_array` '
            '(slice text, dtype text, size_x text, size_y text, array bytes) '
        )
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS `m_array` '
            '(slice INT, dtype text, size_x INT, size_y INT, array bytes) '
        )
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS `d_information` '
            '(information text, value any) '
        )
