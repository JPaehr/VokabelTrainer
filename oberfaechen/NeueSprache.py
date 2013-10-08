# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowSpracheAnlegen import Ui_Form as WindowSpracheAnlgen
import models.base as Datenbank

class NeueSprache(WindowSpracheAnlgen, QtGui.QWidget):
    def __init__(self, parent):
        super(NeueSprache, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.btnAnlegen, QtCore.SIGNAL("clicked()"), self.anlegen)

    def anlegen(self):
        sprache = str(self.tfNeueSprache.text().toUtf8()).decode('utf-8')
        self.Datenbank.setData("insert into sprache (Fremdsprache) values ('"+sprache+"')")
        self.close()
        