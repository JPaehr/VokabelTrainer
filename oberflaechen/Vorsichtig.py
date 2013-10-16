# -*- coding: utf-8 -*-
'''
Created on 14.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowVorsichtig import Ui_Form as WindowVorsichtig
import oberflaechen.NeueVokabel as NeueVokabel

class VorsichtigSein(WindowVorsichtig, QtGui.QWidget):
    def __init__(self, parent):
        super(VorsichtigSein, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)  
        self.parent = parent
        self.connect(self.btnVerstanden, QtCore.SIGNAL("clicked()"), self.EingabeOeffnen)
        self.connect(self.btnZurueck, QtCore.SIGNAL("clicked()"), self.close)
        
    def EingabeOeffnen(self):
        test = NeueVokabel.NeueVokabelAnlegen(self.parent)
        test.show()
        self.close()
    