import sys

from PyQt5 import QtWidgets

from GUI.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Breeze')
    window = MainWindow()
    app.exec_()