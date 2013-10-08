# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowLektionAendern import Ui_Form as WindowLektionAendern
import models.base as Datenbank

class LektionAendern(WindowLektionAendern, QtGui.QWidget):
    def __init__(self, parent):
        super(LektionAendern, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        
       
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.BuecherNeuZeichen)
        self.connect(self.cbBuchAuswaehlen, QtCore.SIGNAL("activated(int)"), self.LektionNeuZeichen)
        self.connect(self.cbLektionAuswaehlen, QtCore.SIGNAL("activated(int)"), self.TextfeldNeuZeichen)
        self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.Speichern)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite") 
        
        self.SpracheNeuZeichnen()
        self.TextfeldNeuZeichen()
        self.tfNeuerName.setFocus()
    def SpracheNeuZeichnen(self):
        daten = self.Datenbank.getDataAsQStringList("select fremdsprache,id from Sprache")
        model = QtGui.QStringListModel(daten)
        self.cBSpracheAuswaehlen.setModel(model)
        
        
        self.BuecherNeuZeichen()
    def getIdSpracheAlt(self):
        daten = self.Datenbank.getDataAsList("select fremdsprache,id from Sprache \
        limit '"+str(self.cBSpracheAuswaehlen.currentIndex())+"', '"+str(self.cBSpracheAuswaehlen.currentIndex()+1)+"'")
        return daten[0][1]
    

    def BuecherNeuZeichen(self):
        
        daten = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"'")
        
        model = QtGui.QStringListModel(daten)
        self.cbBuchAuswaehlen.setModel(model)
        
        datenBuchNeu = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"'")
        
        modelBuchNeu = QtGui.QStringListModel(datenBuchNeu)
        self.cbNeuesBuch.setModel(modelBuchNeu)
        
        
        self.LektionNeuZeichen()

    def getIdBuchAlt(self):
        daten = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"' \
        limit '"+str(self.cbBuchAuswaehlen.currentIndex())+"', '"+str(self.cbBuchAuswaehlen.currentIndex()+1)+"'")
        
        return daten[0][1]
    
    def getIdBuchNeu(self):
        daten = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"' \
        limit '"+str(self.cbNeuesBuch.currentIndex())+"', '"+str(self.cbNeuesBuch.currentIndex()+1)+"'")
        
        return daten[0][1]
    def getIdLektion(self):
        daten = self.Datenbank.getDataAsList("select lektionen.name, lektionen.id from Lektionen \
        join Buecher on (Buecher.id = Lektionen.idBuch) \
        where Buecher.id like '"+str(self.getIdBuchAlt())+"' \
        limit '"+str(self.cbLektionAuswaehlen.currentIndex())+"', '"+str(self.cbLektionAuswaehlen.currentIndex()+1)+"'")
        
        return daten[0][1]
    def LektionNeuZeichen(self):
        #BuecherNeuZeichen
        self.cbNeuesBuch.setCurrentIndex(self.cbBuchAuswaehlen.currentIndex())
               
        daten = self.Datenbank.getDataAsQStringList("select lektionen.name, lektionen.id from Lektionen \
        join Buecher on (Buecher.id = Lektionen.idBuch) \
        where Buecher.id like '"+str(self.getIdBuchAlt())+"'")
        
        model = QtGui.QStringListModel(daten)
        self.cbLektionAuswaehlen.setModel(model)
        
        self.TextfeldNeuZeichen()
    def TextfeldNeuZeichen(self):
        self.tfNeuerName.setText(self.cbLektionAuswaehlen.currentText())
        self.tfNeuerName.setFocus()
    def Speichern(self):
        neuerName = str(self.tfNeuerName.text().toUtf8()).decode("utf-8")
                
        self.getIdLektion()
        statement = "update Lektionen set name='"+str(neuerName)+"', idBuch='"+str(self.getIdBuchNeu())+"' \
        where id like '"+str(self.getIdLektion())+"'"
        self.Datenbank.setData(statement)
        self.close()