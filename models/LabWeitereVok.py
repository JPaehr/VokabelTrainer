__author__ = 'JPaehr'
from PyQt4 import QtGui

class LabWeitereVok(QtGui.QLabel):

    def __init__(self,Form):
        QtGui.QLabel.__init__(self, Form)

    def mousePressEvent(self, event):
        self.hide()
        self.widget.setVisible(True)
        self.hilfs1.setVisible(True)
        self.hilfs2.setVisible(True)

    def addWidgetToShow(self, widget, hilfsW1, hilfsW2):
        self.widget = widget
        self.hilfs1 = hilfsW1
        self.hilfs2 = hilfsW2
