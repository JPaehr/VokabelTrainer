__author__ = 'JPaehr'
from PyQt4 import QtCore
from time import sleep


class InfoThreadMainWindow(QtCore.QThread):
    endeSignal = QtCore.pyqtSignal()
    def __init__(self, parent):
        QtCore.QThread.__init__(self)
        self.parent = parent
        endeSignal = QtCore.pyqtSignal()
        self.endeSignal.connect(parent.setInfoInvisible)

    def run(self):
        sleep(4)
        self.endeSignal.emit()

