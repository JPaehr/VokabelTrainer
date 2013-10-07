# -*- coding: utf-8 -*-
'''
Created on 25.09.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
import sys
from time import sleep
from MainWindow import Ui_MainWindow as MainWindow
from WindowSpracheAnlegen import Ui_Form as WindowSpracheAnlgen
from WindowBuchAnlegen import Ui_Form as WindowBuchAnlegen
from WindowLektionAnlegen import Ui_LektionAnlegen as WindowLektionAnlegen
from WindowWoerterbuch import Ui_Form as WindowWoerterbuch
from WindowAbfrageEinstellungen import Ui_Form as WindowAbfrageEinstellungen
from WindowWoerterbuchBearbeiten import Ui_Form as WindowWoerterbuchBearbeiten
from WindowVokabelAnlegen import Ui_Form as WindowVokabelAnlegen
from WindowAbfrage import Ui_Form as WindowAbfrage
from WindowSpracheAendern import Ui_Form as WindowSpracheAendern
from WindowBuchAendern import Ui_Form as WindowBuchAendern
from WindowLektionAendern import  Ui_Form as WindowLektionAendern


from ListModel import Markierung
from random import shuffle as zufall
import thread
import Leve as leve
import base as Datenbank
import WoerterbuchModel as WoerterbuchModel
from dummy_thread import start_new_thread

class Programm(MainWindow, QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.connect(self.btnNeueSprache, QtCore.SIGNAL("clicked()"), self.NeueSprache)
        self.connect(self.btnNeuesBuch, QtCore.SIGNAL("clicked()"), self.NeuesBuch)
        self.connect(self.btnNeueLektion, QtCore.SIGNAL("clicked()"), self.NeueLektion)
        self.connect(self.btnWoerterbuch, QtCore.SIGNAL("clicked()"), self.Woerterbuch)
        self.connect(self.btnNeueVok, QtCore.SIGNAL("clicked()"), self.NeueVokabel)
        self.connect(self.btnAbfrageStarten, QtCore.SIGNAL("clicked()"), self.AbfrageEinstellungen)
        self.connect(self.btnSpracheBeareiten, QtCore.SIGNAL("clicked()"), self.SpracheAendern)
        self.connect(self.btnBuecherBearbeiten, QtCore.SIGNAL("clicked()"), self.BuchAendern)
        self.connect(self.btnLektionbearbeiten, QtCore.SIGNAL("clicked()"), self.LektioenAendern)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
    def LektioenAendern(self):
        test = LektionAendern(self)
        test.show()
    def BuchAendern(self):
        test = BuchAendern(self)
        test.show()
    def SpracheAendern(self):
        test = SpracheAendern(self)
        test.show()
    def AbfrageEinstellungen(self):
        test = AbfrageEinstellungen(self)
        test.show()
    def NeueVokabel(self):
        test = NeueVokabelAnlegen(self)
        test.show()
    def NeuesBuch(self):
        test = NeuesBuch(self)
        test.show()
        
    def NeueSprache(self):
        test = NeueSprache(self)
        test.show()
    def NeueLektion(self):
        test = NeueLektion(self)
        test.show()
    def Woerterbuch(self):
        test = Woerterbuch(self)
        test.show()
     

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
 
class NeueLektion(WindowLektionAnlegen, QtGui.QWidget):
    def __init__(self, parent):
        super(NeueLektion, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
         
        self.connect(self.btnAbbrechn, QtCore.SIGNAL("clicked()"), QtCore.SLOT("close()"))
        self.connect(self.btnAnwenden, QtCore.SIGNAL("clicked()"), self.LektionAnlegen)
        self.connect(self.btnAnwendenSchliessen, QtCore.SIGNAL("clicked()"), self.LektionAnlegenUndSchliessen)
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.LektionenNeueSchreiben)

        datenSprache = self.Datenbank.getDataAsQStringList("select fremdsprache, id from SPRACHE")
        modelSprache = QtGui.QStringListModel(datenSprache)
        self.cBSprache.setModel(modelSprache)
        
        self.LektionenNeueSchreiben()
        
        
    def LektionenNeueSchreiben(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        datenBuch = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join sprache on (sprache.id=Buecher.id_sprache) \
        where Sprache.id like "+str(datenidSprache[0][1]))
        modelBuch = QtGui.QStringListModel(datenBuch)
        self.cBBuch.setModel(modelBuch)
        
    def LektionAnlegen(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        datenidBuch =  self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join sprache on (sprache.id=Buecher.id_sprache) where Sprache.id like "+str(datenidSprache[0][1])+"\
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'")
        idSprache = datenidSprache[0][1]
        idBuch = int(datenidBuch[0][1])
        
        self.Datenbank.setData(u"insert into Lektionen (name, idBuch) \
        values ('"+str(self.tfLektion.text().toUtf8()).decode('utf-8')+"', '"+str(idBuch)+"')")
    
    def LektionAnlegenUndSchliessen(self):
        self.LektionAnlegen()
        self.close()

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
    def IndexIdZuordnung(self, ids):
        self.IndexListe = []
        for i in ids:
            self.IndexListe.append(i)
    def MarkierungBearbeiten(self):
        
        daten = self.tVWoerterbuch.selectedIndexes()
        if len(daten) > 0:
            row = daten[0].row()
            VokabelId = self.IndexListe[row]
            test = WoerterbuchBearbeiten(self, VokabelId)
            test.show()
            

class WoerterbuchBearbeiten(WindowWoerterbuchBearbeiten, QtGui.QWidget):
    def __init__(self, parent, VokabelId):
        super(WoerterbuchBearbeiten, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        self.parent = parent
        self.ersterDurchlauf = True
        self.vokabelid = VokabelId
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.BuchMachen)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.LektionMachen)
        self.connect(self.btnAnwenden, QtCore.SIGNAL("clicked()"), self.neuenSatzSpeichern)
        
        
        statement = "select Buecher.id, Lektionen.id, vokabeln.id, sprache.id from sprache \
        join buecher on (sprache.id=buecher.id_sprache) \
        join lektionen on (lektionen.idBuch = buecher.id) \
        join vokabeln on (vokabeln.idlektion=lektionen.id) \
        where vokabeln.id like "+str(self.vokabelid)
        
        daten = self.Datenbank.getDataAsList(statement)
        self.BuchID = daten[0][0]
        self.LektionID = daten[0][1]
        self.VokabelID = daten[0][2]
        self.SpracheID = daten[0][3]
        
        self.SpracheMachen()
        vokabeln = self.Datenbank.getDataAsList("select deutsch, fremd from vokabeln where id like "+str(self.VokabelID))
        self.tfDeutsch.setText(vokabeln[0][0])
        self.tfFremd.setText(vokabeln[0][1])
    def SpracheMachen(self):
        statementSprache = "select Sprache.Fremdsprache from Sprache"
        daten = self.Datenbank.getDataAsQStringList(statementSprache)
        #print daten
        model = QtGui.QStringListModel(daten)
        self.cBSprache.setModel(model)
        if self.ersterDurchlauf:
            self.cBSprache.setCurrentIndex(self.IndexSpracheFinden(self.SpracheID))
        
        self.BuchMachen()
        
    def BuchMachen(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        statementBuch = "select Buecher.name from Buecher join Sprache on (buecher.id_sprache=sprache.id) \
        where sprache.id like "+str(datenidSprache[0][1])
        
        datenBuch = self.Datenbank.getDataAsQStringList(statementBuch)
        model = QtGui.QStringListModel(datenBuch)
        self.cBBuch.setModel(model)
        if self.ersterDurchlauf:
            self.cBBuch.setCurrentIndex(self.IndexBuchFinden(self.BuchID))        
        
        self.LektionMachen()
        
    def LektionMachen(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        statementBuch = "select Buecher.name, Buecher.id from Buecher join Sprache on (buecher.id_sprache=sprache.id) \
        where sprache.id like "+str(datenidSprache[0][1])+"\
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'" 
        
        datenidBuch = self.Datenbank.getDataAsList(statementBuch)
        statementLektion = "select lektionen.name, lektionen.id from Lektionen\
        join buecher on (buecher.id=lektionen.idBuch) \
        join Sprache on (sprache.id=buecher.id_sprache) where buecher.id like "+str(datenidBuch[0][1])
        datenLektionen = self.Datenbank.getDataAsQStringList(statementLektion)
        model = QtGui.QStringListModel(datenLektionen)
        self.cBLekion.setModel(model)
        if self.ersterDurchlauf:
            self.cBLekion.setCurrentIndex(self.IndexLektionFinden(self.LektionID))        
            self.ersterDurchlauf = False
        
        
    def IndexSpracheFinden(self, id):
        
        statementBuch = "select sprache.fremdsprache, sprache.id from Sprache"
        daten = self.Datenbank.getDataAsList(statementBuch)
        liste = []
        for i in daten:
            liste.append(i[1])
        return liste.index(id) 
    def IndexBuchFinden(self, id):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        daten = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (buecher.id_sprache=sprache.id) \
        where sprache.id like "+str(datenidSprache[0][1]))
        liste = []
        for i in daten:
            liste.append(i[1])
        return liste.index(id)  
    def IndexLektionFinden(self, id):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        datenidBuch = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (buecher.id_sprache=sprache.id) \
        where sprache.id like "+str(datenidSprache[0][1])+"\
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'")
        daten = self.Datenbank.getDataAsList("select Lektionen.name, lektionen.id from Buecher \
        join Sprache on (buecher.id_sprache=sprache.id) \
        join Lektionen on (lektionen.idBuch=Buecher.id) \
        where sprache.id like "+str(datenidSprache[0][1])+" and buecher.id like "+str(datenidBuch[0][1]) )
        liste = []
        for i in daten:
            liste.append(i[1])
        #print liste
        return liste.index(id)  
    def neuenSatzSpeichern(self):
        neueSpracheId = self.Datenbank.getDataAsList("select Fremdsprache, id from sprache \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'")[0][1]
        
        neuesBuchId = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (buecher.id_sprache=Sprache.id)\
        where sprache.id like "+str(neueSpracheId)+"  \
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'")[0][1]
        
        neueLektionId = self.Datenbank.getDataAsList("select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id=lektionen.idBuch)\
        join Sprache on (sprache.id=Buecher.id_sprache) \
        where buecher.id like "+str(neuesBuchId)+" \
        limit '"+str(self.cBLekion.currentIndex())+"', '"+str(self.cBLekion.currentIndex()+1)+"'")[0][1]
        
        updateStatementVokabeln = "update vokabeln set idlektion="+str(neueLektionId)+", \
        Deutsch='"+str(self.tfDeutsch.text())+"', Fremd='"+str(self.tfFremd.text())+"' \
        where id like "+str(self.VokabelID)
        self.Datenbank.setData(updateStatementVokabeln)
        
        Woerterbuch.TabelleNeuZeichnen(self.parent)
        self.close()
        
class NeueVokabelAnlegen(WindowVokabelAnlegen, QtGui.QWidget):
    def __init__(self, parent):
        super(NeueVokabelAnlegen, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)  
        
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.BuchZeichnen)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.LektionZeichnen)
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.btnAnwendenUndSchliessen, QtCore.SIGNAL("clicked()"), self.speichernUndSchliessen)
        self.connect(self.btnAnwenden, QtCore.SIGNAL("clicked()"), self.speichern)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.SpracheZeichnen()
    def speichern(self):
        deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()
        
        fremd = str(self.tfFremd.text().toUtf8()).decode("utf-8").strip()
         
        #deutsch = str(self.tfDeutsch.text())
        #fremd = str(self.tfFremd.text())       
        
        insertVokabel = "insert into vokabeln (deutsch, fremd, idlektion) values ('"+deutsch+"', '"+fremd+"', '"+str(self.getIdLektion())+"')"
        print type(insertVokabel)
        self.Datenbank.setData(insertVokabel)
        self.tfDeutsch.setText("")
        self.tfFremd.setText("")
        self.tfDeutsch.setFocus()
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
class AbfrageEinstellungen(WindowAbfrageEinstellungen, QtGui.QWidget):
    def __init__(self, parent):
        super(AbfrageEinstellungen, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)   
        self.AbfrageEinstellung = 0
        self.lektionsListe = []
        
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.cbSprache, QtCore.SIGNAL("activated(int)"), self.BuchZeichnen)
        self.connect(self.cbSprache, QtCore.SIGNAL("activated(int)"), self.Abfragerichtung)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.LektionZeichnen)
        self.connect(self.btnLektionZuAbfrageHinzu, QtCore.SIGNAL("clicked()"), self.LektionZuAbfrageHinzu)
        self.connect(self.btnLektionLoeschen, QtCore.SIGNAL("clicked()"), self.LektionTrennen)
        self.connect(self.btnAbfrageStarten, QtCore.SIGNAL("clicked()"), self.AbfrageStarten)
        self.connect(self.tfHaeufigkeit, QtCore.SIGNAL("textChanged(QString)"), self.AnzahlAbfragenPaint)
        self.connect(self.btnBuchZuAbfrage, QtCore.SIGNAL("clicked()"), self.BuchZuAbfrageHinzu)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")   
        
        Voreinstellungen = self.Datenbank.getDataAsList("select meintenSie, rgva, warteZeit, haeufigkeit, richtung, wiederholen from Einstellungen \
        where id like 1")
        
        if Voreinstellungen[0][0] == "True":
            self.chBMeintenSie.setChecked(True)
        else:
            self.chBMeintenSie.setChecked(False)
        
        if Voreinstellungen[0][1] == "True":
            self.chBRichtigGeschriebeneAnzeigen.setChecked(True)
        else:
            self.chBRichtigGeschriebeneAnzeigen.setChecked(False)
        
        self.tfZeitWarten.setText(str(Voreinstellungen[0][2]))
        self.tfHaeufigkeit.setText(str(Voreinstellungen[0][3]))
        
        self.richtung = Voreinstellungen[0][4]
        
        self.SpracheZeichnen()
        self.Abfragerichtung()
    def AbfrageStarten(self):
        #Einstellungen Speichern
        
        updateStatement = "update Einstellungen set \
        meintenSie='"+str(self.chBMeintenSie.isChecked())+"', \
        rgva = '"+str(self.chBRichtigGeschriebeneAnzeigen.isChecked())+"', \
        warteZeit = "+str(int(self.tfZeitWarten.text()))+", \
        haeufigkeit = "+str(int(self.tfHaeufigkeit.text()))+", \
        richtung = "+str(int(int(self.cBAbfragerichtung.currentIndex())+1))+" \
        where id like 1"
        self.Datenbank.setData(updateStatement)
        
        
        test = Abfrage(self, self.lektionsListe, self.tfHaeufigkeit.text(), self.tfZeitWarten.text(), self.chBMeintenSie.isChecked(), 
                       self.chBRichtigGeschriebeneAnzeigen.isChecked(), self.cBAbfragerichtung.currentIndex()+1)
        test.show()
    def Abfragerichtung(self):
        #1 ist von Deutsch nach Fremd, 2 von Fremd nach Deutsch
        daten = QtCore.QStringList()
        daten.append("Deutsch - "+str(self.cbSprache.currentText()))
        daten.append(str(self.cbSprache.currentText())+" - Deutsch")
        model = QtGui.QStringListModel(daten)
        self.cBAbfragerichtung.setModel(model)
        self.cBAbfragerichtung.setCurrentIndex(self.richtung-1)
    def SpracheZeichnen(self):
        selectSprache = "select fremdsprache, id from sprache"
        spracheDaten = self.Datenbank.getDataAsQStringList(selectSprache)
        modelSprache = QtGui.QStringListModel(spracheDaten)
        self.cbSprache.setModel(modelSprache)
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
        daten = self.Datenbank.getDataAsList(selectLektion)
        liste = []
        for i in daten:
            liste.append(i[0])
        model = Markierung(liste)
        self.lvLektionen.setModel(model) 
        self.lvLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        
    
    def getIdSprache(self):
        selectSprache = "select fremdsprache, id from sprache \
        limit '"+str(self.cbSprache.currentIndex())+"', '"+str(self.cbSprache.currentIndex()+1)+"'" 
        spracheId = self.Datenbank.getDataAsList(selectSprache)[0][1]
        return spracheId
    
    def getIdBuch(self):
        selectBuch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"' \
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'"
        return self.Datenbank.getDataAsList(selectBuch)[0][1]
    def getIdLektionen(self):
        selectLektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.Datenbank.getDataAsList(selectLektion)
        liste = []
        for i in self.lvLektionen.selectedIndexes():
            liste.append(daten[i.row()][1])
        return liste
    def LektionZuAbfrageHinzu(self):
        self.lektionsListe.extend(self.getIdLektionen())
        self.AbfrageNeuZeichen()
    def AbfrageNeuZeichen(self):
        #print self.lektionsListe
        datenliste = []
        for i in self.lektionsListe:
            daten = self.Datenbank.getDataAsList("select Buecher.name, lektionen.name from lektionen \
            join buecher on (buecher.id=lektionen.idbuch) \
            where lektionen.id like "+str(i))
            datenliste.append(str(daten[0][0])+" - "+str(daten[0][1]))
        
        model = Markierung(datenliste)
        self.lvGewaehlteLektionen.setModel(model)
        self.lvGewaehlteLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.AnzahlVokabelnPaint()
    def BuchZuAbfrageHinzu(self):
        daten = self.Datenbank.getDataAsList("select lektionen.id from buecher \
        join Lektionen on (lektionen.idbuch = buecher.id) \
        where buecher.id like "+str(self.getIdBuch()))
        listeZumHinzufuegen = []
        for i in daten:
            listeZumHinzufuegen.append(i[0])
        
        self.lektionsListe.extend(listeZumHinzufuegen)
        #print self.lektionsListe
        
        self.AbfrageNeuZeichen()
        
    def ListeZuSql(self, liste, args):
        statement = "where "
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]
    def LektionTrennen(self):
        popListe = []
        for i in reversed(self.lvGewaehlteLektionen.selectedIndexes()):
            popListe.append(i.row())
        for i in popListe:
            self.lektionsListe.pop(i)
        
        self.AbfrageNeuZeichen()
    def AnzahlVokabelnPaint(self):
        counter = 0
        for i in self.lektionsListe:
            counter += self.Datenbank.getDataAsList("select count(*) from lektionen \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where lektionen.id like "+str(i))[0][0]
        self.labAnzahlVokabeln.setText(u"Anzahl Vokabeln:"+str(counter))
        self.AnzahlAbfragenPaint()
    def AnzahlAbfragenPaint(self):
        counter = 0
        for i in self.lektionsListe:
            counter += self.Datenbank.getDataAsList("select count(*) from lektionen \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where lektionen.id like "+str(i))[0][0]
            
        if self.tfHaeufigkeit.text() == '':
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: 0")
        else:
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: "+str(int(counter)*int(self.tfHaeufigkeit.text())))
class Abfrage(WindowAbfrage, QtGui.QWidget):
    def __init__(self, parent, lektionenIds, AbfrageHaeufigkeit, verzoegerung, meintenSie, RichtigeAnzeigen, Richtung):
        super(Abfrage, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        
        self.Treffer = leve.Treffer()
           
        zeit = float(verzoegerung)*10**(-3)  
        self.thread = ZeitThread(zeit)
        
        self.parent = parent
        
        self.connect(self.thread, QtCore.SIGNAL("finished()"), self.weitereVokabel)
        self.connect(self.btnWeiter, QtCore.SIGNAL("clicked()"), self.weitereVokabelKlick)
        
        self.meintenSie = meintenSie
        self.Lektionsliste = []
        self.verzoegerung = verzoegerung
        self.idAktuell = 0
        self.RichtigeAnzeigen = RichtigeAnzeigen
        self.Richtung = Richtung
        self.labPunkte.setText('0')
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite") 
        
        self.vokabelIds = self.LektionsIdToVokId(lektionenIds, int(AbfrageHaeufigkeit))
        
        self.weitereVokabel()
        
    def weitereVokabel(self):
        if self.idAktuell < len(self.vokabelIds):
            
        
            daten = self.Datenbank.getDataAsList("select lektionen.name, vokabeln.deutsch, vokabeln.fremd, buecher.name from vokabeln\
            join lektionen on (lektionen.id=vokabeln.idlektion) \
            join buecher on (buecher.id=lektionen.idBuch) \
            where vokabeln.id like "+str(self.vokabelIds[self.idAktuell]))
            self.lektion = daten[0][0]
            self.vokabelDeutsch = daten[0][1]
            self.vokabelFremd = daten[0][2]
            self.Buch = daten[0][3]
            
            print "Richtung: ", self.Richtung
            
            if self.Richtung == 1:
                self.labVokabelMeintenSie.setText(self.vokabelDeutsch)
            else:
                self.labVokabelMeintenSie.setText(self.vokabelFremd)
            
            self.labLektion.setText(str(self.lektion))
            self.labBuch.setText(str(self.Buch))
            self.labRichtigFalsch.setText("")
            self.labBitteEingeben.setText("Bitte eingeben")
            self.labWeitereVokabeln.setText("Noch "+str(len(self.vokabelIds)-self.idAktuell-1)+" weitere Vokabeln")
            self.tfInput.setText("")
            self.tfInput.setFocus()    
            self.labMeintenSie.setText("")
            
            self.idAktuell +=1
        else:
            print "fertig mit Abfragen"
    def LektionsIdToVokId(self, idliste, haeufigkeit):
            
        vokabelIds = []    
        for i in idliste:
            daten = self.Datenbank.getDataAsList("select vokabeln.id from vokabeln \
            join lektionen on (vokabeln.idlektion=lektionen.id) where lektionen.id like "+str(i))
            for n in daten:
                for k in range(haeufigkeit):
                    vokabelIds.append(n[0])
             
            
        zufall(vokabelIds)
        print vokabelIds
        return vokabelIds
    def weitereVokabelKlick(self):
        
        self.thread.start()
        if self.Richtung == 1:
            #print type(self.vokabelFremd)
            #print type(str(self.tfInput.text().toUtf8()).decode("utf-8"))
            if self.vokabelFremd == str(self.tfInput.text().toUtf8()).decode("utf-8"):
                self.labRichtigFalsch.setText("Richtig")
                self.labPunkte.setText(str(int(self.labPunkte.text()) + 1))
            else:
                self.labRichtigFalsch.setText("Falsch")
                if self.RichtigeAnzeigen:
                    self.labBitteEingeben.setText(u"Richtig währe: "+self.vokabelFremd)
                if self.meintenSie:
                    liste = self.Datenbank.getDataAsList("select fremd, id from vokabeln")# \
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.Treffer.setAktVergleich(liste, unicode(self.tfInput.text()))
                    
                    #print self.Treffer.getTreffer()
                    
                    daten = self.Datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+ self.ListeZuSql(self.Treffer.getTreffer(), " id "))
                    
                    
                    if(len(daten) > 0):
                        self.labMeintenSie.setText("Meinten Sie: "+unicode(daten[0][1])+" - "+unicode(daten[0][0]))
        
                    """
                    daten = self.Datenbank.getDataAsList(u"select fremd, deutsch from vokabeln \
                    where fremd like '"+str(self.tfInput.text().toUtf8).decode('utf-8')+"' or deutsch like '"+str(self.tfInput.text().toUtf8()).decode("utf-8")+"'")
                    if(len(daten) > 0):
                        self.labMeintenSie.setText(u"Meinten Sie: "+daten[0][1]+" - "+daten[0][0])
                        """
        else:
            if self.vokabelDeutsch == self.tfInput.text():
                self.labRichtigFalsch.setText("Richtig")
                self.labPunkte.setText(str(int(self.labPunkte.text()) + 1))
            else:
                self.labRichtigFalsch.setText("Falsch")
                if self.RichtigeAnzeigen:
                    self.labBitteEingeben.setText(unicode("Richtig währe: ")+str(self.vokabelDeutsch))
                if self.meintenSie:
                    #print "meintenSie Aktiv"
                    liste = self.Datenbank.getDataAsList("select deutsch, id from vokabeln")# \
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.Treffer.setAktVergleich(liste, unicode(self.tfInput.text()))
                    
                    #print self.Treffer.getTreffer()
                    
                    daten = self.Datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+ self.ListeZuSql(self.Treffer.getTreffer(), " id "))
                    
                    
                    if(len(daten) > 0):
                        self.labMeintenSie.setText("Meinten Sie: "+unicode(daten[0][0])+" - "+unicode(daten[0][1]))
        
        
        
        
    def ListeZuSql(self, liste, args, where=True):
        if where:
            statement = "where "
        else:
            statement = ""
            
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]    
class ZeitThread(QtCore.QThread):
    def __init__(self, zeit):
        QtCore.QThread.__init__(self)
        self.zeit = zeit
        
    def run(self):
        sleep(self.zeit)
        print "Thread ist fertig"
        return  
      
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
class BuchAendern(WindowBuchAendern, QtGui.QWidget):
    def __init__(self, parent):
        super(BuchAendern, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        
       
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.BuecherNeuZeichen)
        self.connect(self.cbBuchAuswaehlen, QtCore.SIGNAL("activated(int)"), self.TextfeldNeuZeichen)
        self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.Speichern)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite") 
        
        self.SpracheNeuZeichnen()
        self.TextfeldNeuZeichen()
        self.tfNeuerName.setFocus()
    def SpracheNeuZeichnen(self):
        daten = self.Datenbank.getDataAsQStringList("select fremdsprache,id from Sprache")
        model = QtGui.QStringListModel(daten)
        self.cBSpracheAuswaehlen.setModel(model)
        
        datenSpracheNeu = self.Datenbank.getDataAsQStringList("select fremdsprache,id from Sprache")
        modelSpracheNeu = QtGui.QStringListModel(datenSpracheNeu)
        self.cBSpracheNeu.setModel(modelSpracheNeu)
        self.BuecherNeuZeichen()
    def getIdSpracheAlt(self):
        daten = self.Datenbank.getDataAsList("select fremdsprache,id from Sprache \
        limit '"+str(self.cBSpracheAuswaehlen.currentIndex())+"', '"+str(self.cBSpracheAuswaehlen.currentIndex()+1)+"'")
        return daten[0][1]
    
    def getIdSpracheNeu(self):
        daten = self.Datenbank.getDataAsList("select fremdsprache,id from Sprache \
        limit '"+str(self.cBSpracheNeu.currentIndex())+"', '"+str(self.cBSpracheNeu.currentIndex()+1)+"'")
        return daten[0][1]
    
    def BuecherNeuZeichen(self):
        #SpracheNeu setzten
        self.cBSpracheNeu.setCurrentIndex(self.cBSpracheAuswaehlen.currentIndex())
        
        daten = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"'")
        
        model = QtGui.QStringListModel(daten)
        self.cbBuchAuswaehlen.setModel(model)
        self.TextfeldNeuZeichen()
    def getIdBuch(self):
        daten = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"' \
        limit '"+str(self.cbBuchAuswaehlen.currentIndex())+"', '"+str(self.cbBuchAuswaehlen.currentIndex()+1)+"'")
        
        return daten[0][1]
        
    def TextfeldNeuZeichen(self):
        self.tfNeuerName.setText(self.cbBuchAuswaehlen.currentText())
        self.tfNeuerName.setFocus()
    def Speichern(self):
        neuerName = str(self.tfNeuerName.text().toUtf8()).decode("utf-8")
                
        statement = "update Buecher set name='"+str(neuerName)+"', id_sprache='"+str(self.getIdSpracheNeu())+"' where id like '"+str(self.getIdBuch())+"'"
        self.Datenbank.setData(statement)
        self.close()
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
app = QtGui.QApplication(sys.argv) 
dialog = Programm() 
dialog.show() 
sys.exit(app.exec_())
