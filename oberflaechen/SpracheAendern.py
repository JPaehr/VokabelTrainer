# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowSpracheAendern import Ui_Form as WindowSpracheAendern
import models.base as Datenbank 

class SpracheAendern(WindowSpracheAendern, QtGui.QWidget):
    def __init__(self, parent):
        super(SpracheAendern, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.TextfeldNeuZeichen)
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.Speichern)

        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        
        daten = self.Datenbank.getDataAsQStringList("select fremdsprache, id from Sprache")
        model = QtGui.QStringListModel(daten)
        self.cBSpracheAuswaehlen.setModel(model)
        self.TextfeldNeuZeichen()
        self.tfNeuerName.setFocus()
    def TextfeldNeuZeichen(self):
        self.tfNeuerName.setText(self.cBSpracheAuswaehlen.currentText())
        self.tfNeuerName.setFocus()

    def Speichern(self):
        neuerName = str(self.tfNeuerName.text().toUtf8()).decode("utf-8")
        #print neuerName
        daten = self.Datenbank.getDataAsList("select fremdsprache, id from Sprache \
        limit '"+str(self.cBSpracheAuswaehlen.currentIndex())+"', '"+str(self.cBSpracheAuswaehlen.currentIndex()+1)+"'")
        id = daten[0][1]
        
        statement = "update sprache set fremdsprache='"+str(neuerName)+"' where id like '"+str(id)+"'"
        self.Datenbank.setData(statement)
        self.close()