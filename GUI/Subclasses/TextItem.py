
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

_translate = QCoreApplication.translate


class TextItem(QLabel):

    def __init__(self, text, pointSize=9, textColor="black"):
        super(TextItem, self).__init__()
        self.setText(_translate("MainWindow", text))

        font = QFont()
        font.setPointSize(pointSize)

        #palette = QPalette()
        #palette.setColor(QPalette.Text, QColor)
        # FUNKTIONIERT NICHT !!!!!!

        #self.setPalette(palette)
        self.setFont(font)