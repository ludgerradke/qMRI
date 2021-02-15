from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from win32api import GetMonitorInfo, MonitorFromPoint
from GUI.Menubar.Menubar import MenuBar
_translate = QCoreApplication.translate


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # check workspace
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        workspace = monitor_info.get("Work")

        self.setMenuBar(MenuBar(self))

        self.show()


class Version(QLabel):

    def __init__(self):
        super(Version, self).__init__()
        self.setText(_translate("MainWindow", 'Version 0.0 (15.2.2021) \n'
                                              'From: ludger.radke@med.uni-duesseldorf.de'))
