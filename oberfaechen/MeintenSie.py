#-*- coding:utf-8 -*-
'''
Created on 10.10.2013

@author: Johannes
'''

from PyQt4 import QtGui, QtCore
from windows.WindowMeintenSie import Ui_Form as WindowMeintenSie
from models import ListModelMeintenSie



class MeintenSie(WindowMeintenSie, QtGui.QWidget):
    def __init__(self, parent, daten):
        super(MeintenSie, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        self.setMouseTracking(True)
        self.lvMeintenSieSatz.setMouseTracking(True)
        print daten
        
        model = ListModelMeintenSie.ListModelMeintenSie(daten)
        self.lvMeintenSieSatz.setModel(model)
        
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()
        
    """def mouseMoveEvent(self, event):
        self.close()
        return QtGui.QWidget.mouseMoveEvent(self, event)
    """      