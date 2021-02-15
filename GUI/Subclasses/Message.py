from PyQt5 import QtWidgets, QtCore


def errorMessage(message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(message)
    # msg.setInformativeText("More Information")
    msg.setWindowTitle("ERROR")
    msg.exec()


def completedMessage(message):
    msg = QtWidgets.QMessageBox()
    msg.setText(message)
    #msg.setIconPixmap(QPixmap(r'Images\Accepted.png').scaled(64, 64, QtCore.Qt.KeepAspectRatio))
    msg.setWindowTitle("Completed")
    msg.exec()