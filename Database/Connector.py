from Database.DataDB import DataDB
from Database.GuiDB import GuiDB


def connect(key):
    if key == 'data':
        return DataDB()
    elif key == 'gui':
        return GuiDB()
    else:
        raise KeyError
