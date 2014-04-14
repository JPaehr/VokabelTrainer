__author__ = 'JPaehr'

from PyQt4 import QtGui
class CLabel(QtGui.QLabel):
    def __init__(self, Form):
        QtGui.QLabel.__init__(self, Form)

    def mousePressEvent(self, QMouseEvent):
        self.parent.labZeit.hide()

    def setParent(self, parent):
        self.parent = parent