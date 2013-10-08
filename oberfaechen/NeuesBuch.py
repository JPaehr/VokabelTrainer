# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowBuchAnlegen import Ui_Form as WindowBuchAnlegen
import models.base as Datenbank

class NeuesBuch(WindowBuchAnlegen, QtGui.QWidget):
    def __init__(self, parent):
        super(NeuesBuch, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.btnAnlegen, QtCore.SIGNAL("clicked()"), self.anlegen)
        
        daten = self.Datenbank.getDataAsQStringList("select fremdsprache, id from SPRACHE")
        model = QtGui.QStringListModel(daten)
        self.cBSprache.setModel(model)
        
    def anlegen(self):
        print self.cBSprache.currentIndex()
        
        daten = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', \
        '"+str(self.cBSprache.currentIndex()+1)+"'") 
        self.Datenbank.setData("insert into Buecher (name, id_sprache) \
        values('"+str(self.tfBuchtitel.text())+"', '"+str(daten[0][1])+"')")
        self.close()