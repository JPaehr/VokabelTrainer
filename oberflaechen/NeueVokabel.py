# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowVokabelAnlegen import Ui_Form as WindowVokabelAnlegen
import models.base as Datenbank
import models.ReadVoks as ReadVoks

class NeueVokabelAnlegen(WindowVokabelAnlegen, QtGui.QWidget):
    def __init__(self, parent):
        super(NeueVokabelAnlegen, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)  
        
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.BuchZeichnen)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.LektionZeichnen)
        self.connect(self.cBLekion, QtCore.SIGNAL("activated(int)"), self.AnzVokabelnZeichen)
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnAnwendenUndSchliessen, QtCore.SIGNAL("clicked()"), self.speichernUndSchliessen)
        self.connect(self.btnAnwenden, QtCore.SIGNAL("clicked()"), self.speichern)
        self.connect(self.pBFile, QtCore.SIGNAL("clicked()"), self.LoadFile)

        self.btnAnwenden.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return))
        self.labFelderAusfuellen.setText("")
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.SpracheZeichnen()

    def LoadFile(self):
        try:
            filepath = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')

            ReadVoks.ReadVoks(filepath, self.getIdLektion())
        except:
            print "Keine Datei geladen"


        self.AnzVokabelnZeichen()

    def speichern(self):
        deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()
        
        fremd = str(self.tfFremd.text().toUtf8()).decode("utf-8").strip()
        
        if len(fremd) < 1 or len(deutsch) < 1:
            self.labFelderAusfuellen.setText(u"Bitte alle Felder ausfüllen")
        else:
            self.labFelderAusfuellen.setText("")
            #deutsch = str(self.tfDeutsch.text())
            #fremd = str(self.tfFremd.text())       
            
            insertVokabel = "insert into vokabeln (deutsch, fremd, idlektion) values ('"+deutsch+"', '"+fremd+"', '"+str(self.getIdLektion())+"')"
            print type(insertVokabel)
            self.Datenbank.setData(insertVokabel)
            self.tfDeutsch.setText("")
            self.tfFremd.setText("")
            self.tfDeutsch.setFocus()
            
            self.AnzVokabelnZeichen()
            
    def speichernUndSchliessen(self):
        self.speichern()
        self.close()
        
    def SpracheZeichnen(self):
        selectSprache = "select fremdsprache, id from sprache"
        spracheDaten = self.Datenbank.getDataAsQStringList(selectSprache)
        modelSprache = QtGui.QStringListModel(spracheDaten)
        self.cBSprache.setModel(modelSprache)
        self.BuchZeichnen()
        
    def BuchZeichnen(self):
        selectBuch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"'"
        buchDaten = self.Datenbank.getDataAsQStringList(selectBuch)
        modelBuch = QtGui.QStringListModel(buchDaten)
        self.cBBuch.setModel(modelBuch)
        self.LektionZeichnen()
        
    def LektionZeichnen(self):
        selectLektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.Datenbank.getDataAsQStringList(selectLektion)
        model = QtGui.QStringListModel(daten)
        self.cBLekion.setModel(model) 
        self.AnzVokabelnZeichen()
        
    def AnzVokabelnZeichen(self):
        
        #Anzahl vokabeln berechen und zeichen
        
        daten = self.Datenbank.getDataAsList("select count(*) from vokabeln \
        join lektionen on (lektionen.id = vokabeln.idlektion) \
        where lektionen.id like "+str(self.getIdLektion()))
        if len(daten) < 1:
            self.lbAnzVokabeln.setText("0 Vokabeln in dieser Lektion")
        else:
            if int(daten[0][0]) == 1:
                self.lbAnzVokabeln.setText(str(daten[0][0])+" Vokabel in dieser Lektion")
            else:
                self.lbAnzVokabeln.setText(str(daten[0][0])+" Vokabeln in dieser Lektion")

    def getIdSprache(self):
        selectSprache = "select fremdsprache, id from sprache \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'" 
        spracheId = self.Datenbank.getDataAsList(selectSprache)[0][1]
        return spracheId
    
    def getIdBuch(self):
        selectBuch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"' \
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'"
        return self.Datenbank.getDataAsList(selectBuch)[0][1]
    def getIdLektion(self):
        selectLektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())+" \
        limit '"+str(self.cBLekion.currentIndex())+"', '"+str(self.cBLekion.currentIndex()+1)+"'"
        return self.Datenbank.getDataAsList(selectLektion)[0][1]
    
    """def enterEvent(self, event):
        self.speichern()
        return QtGui.QWidget.enterEvent(self, event)
    """