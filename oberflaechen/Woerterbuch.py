# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from windows.WindowWoerterbuch import Ui_Form as WindowWoerterbuch
import models.base as Datenbank

import WoerterbuchBearbeiten as WoerterbuchBearbeiten
from models import WoerterbuchModel as WoerterbuchModel


class Woerterbuch(WindowWoerterbuch, QtGui.QWidget):
    
    def __init__(self, parent):
        super(Woerterbuch, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.BuecherNeuSchreiben)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.TabelleNeuZeichnen)
        self.connect(self.chBBuch, QtCore.SIGNAL("clicked()"), self.TabelleNeuZeichnen)
        self.connect(self.tfSuche, QtCore.SIGNAL("textChanged(QString)"), self.TabelleNeuZeichnen)
        self.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.MarkierungBearbeiten)
        
        self.headerDaten =  [ 'Buch' , 'Lektion' , 'Deutsch' , 'Fremdsprache']
        
        datenSprache = self.Datenbank.getDataAsQStringList("select fremdsprache, id from SPRACHE")
        modelSprache = QtGui.QStringListModel(datenSprache)
        self.cBSprache.setModel(modelSprache)
        self.BuecherNeuSchreiben()
        self.tVWoerterbuch.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tVWoerterbuch.setSelectionMode(QtGui.QTableView.SingleSelection)
        
    def BuecherNeuSchreiben(self):
        
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        datenBuch = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join sprache on (sprache.id=Buecher.id_sprache) \
        where Sprache.id like "+str(datenidSprache[0][1]))
        modelBuch = QtGui.QStringListModel(datenBuch)
        self.cBBuch.setModel(modelBuch)
        self.TabelleNeuZeichnen()
  
    def TabelleNeuZeichnen(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        suchString = str(self.tfSuche.text().toUtf8()).decode("utf-8")
        
        if self.chBBuch.isChecked():
            datenidBuch =  self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
            join sprache on (sprache.id=Buecher.id_sprache) where Sprache.id like "+str(datenidSprache[0][1])+" \
            limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'")
            print datenidBuch
            
            self.statement = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where buecher.id like "+str(datenidBuch[0][1])+"\
            and sprache.id like "+str(datenidSprache[0][1])+"\
            and (lektionen.name like '%"+suchString+"%' or \
            vokabeln.deutsch like '%"+suchString+"%' or \
            vokabeln.fremd like '%"+suchString+"%')"
            
            self.statementId = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd,vokabeln.id from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where buecher.id like "+str(datenidBuch[0][1])+"\
            and sprache.id like "+str(datenidSprache[0][1])+"\
            and (lektionen.name like '%"+suchString+"%' or \
            vokabeln.deutsch like '%"+suchString+"%' or \
            vokabeln.fremd like '%"+suchString+"%')"
        else:
            self.statementId = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd, vokabeln.id from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where sprache.id like "+str(datenidSprache[0][1])+" \
            and (lektionen.name like '%"+suchString+"%' or \
            vokabeln.deutsch like '%"+suchString+"%' or \
            vokabeln.fremd like '%"+suchString+"%' or \
            Buecher.name like '%"+suchString+"%')"
            
            self.statement = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where sprache.id like "+str(datenidSprache[0][1])+" \
            and (lektionen.name like '%"+suchString+"%' or \
            vokabeln.deutsch like '%"+suchString+"%' or \
            vokabeln.fremd like '%"+suchString+"%' or \
            Buecher.name like '%"+suchString+"%')"
            
        
        IDListe = []
        for i in self.Datenbank.getDataAsList(self.statementId):
            IDListe.append(i[4])
        self.IndexIdZuordnung(IDListe)
        
        self.daten = self.Datenbank.getDataAsList(self.statement)
        model = WoerterbuchModel.ModelListe(self.daten, self.headerDaten)
        
        
        self.tVWoerterbuch.setModel(model)
        #tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tVWoerterbuch.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
    def IndexIdZuordnung(self, ids):
        self.IndexListe = []
        for i in ids:
            self.IndexListe.append(i)
    def MarkierungBearbeiten(self):
        
        daten = self.tVWoerterbuch.selectedIndexes()
        if len(daten) > 0:
            row = daten[0].row()
            VokabelId = self.IndexListe[row]
            test = WoerterbuchBearbeiten.WoerterbuchBearbeiten(self, VokabelId)
            test.show()
