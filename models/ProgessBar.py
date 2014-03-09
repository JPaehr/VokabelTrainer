__author__ = 'JPaehr'
from PyQt4 import QtGui

class Progessbar(QtGui.QProgressBar):

    def __init__(self, Form):
        QtGui.QProgressBar.__init__(self, Form)

    def mousePressEvent(self, event):
        self.hide()
        self.w1.hide()
        self.w2.hide()
        self.widget.setVisible(True)

    def hilfsWidgets(self, w1, w2):
        self.w1 = w1
        self.w2 = w2

    def addWidgetToShow(self, widget):
        self.widget = widget