# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowWoerterbuchBearbeiten import Ui_Form as WindowWoerterbuchBearbeiten
import models.base as Datenbank
import Woerterbuch as Woerterbuch
from models import WoerterbuchModel

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
        #self.connect(self.btnVokabelLoeschen, QtCore.SIGNAL("clicked()"), self.delWithoutClose)
        self.connect(self.btnVokabelLoeschenUSchliessen, QtCore.SIGNAL("clicked()"), self.delete_with_close)

        
        
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

    def delete_vocable(self, close=False):


        delVokStatement = "delete from vokabeln where id like "+str(self.vokabelid)

        box = QtGui.QMessageBox()
        #box.setText("")
        #print unicode(self.cbLektionAuswaehlen.currentText())
        vokabelText = unicode(self.tfDeutsch.text()) + u" - " +unicode(self.tfFremd.text())
        #print "lektionsName: "+str(lektionsText)

        box.setText(u"Soll die Vokabel '"+vokabelText+u"' wirklich gelöscht werden?")

        #box.setInformativeText(u"Es werden "+str(anzVok)+u" Vokabeln gelöscht!")

        #box.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        btnJa = box.addButton(QtCore.QString(u"Ja"), QtGui.QMessageBox.AcceptRole)
        btnNein = box.addButton(QtCore.QString(u"Nein"), QtGui.QMessageBox.RejectRole)
        box.exec_()

        if box.clickedButton() == btnJa:
            print u"loeschen"
            self.Datenbank.setData(delVokStatement)

            if close:
                self.close()
                self.parent.redraw_table()
        elif box.clickedButton() == btnNein:
            print u"nicht loeschen"


    def delete_with_close(self):
        self.delete_vocable(True)

    def SpracheMachen(self):
        statementSprache = "select Sprache.Fremdsprache from Sprache"
        daten = self.Datenbank.getDataAsQStringList(statementSprache)
        #print daten
        model = QtGui.QStringListModel(daten)
        self.cBSprache.setModel(model)
        if self.ersterDurchlauf:
            self.cBSprache.setCurrentIndex(self.find_index_language(self.SpracheID))
        
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
            self.cBBuch.setCurrentIndex(self.find_index_book(self.BuchID))
        
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
            self.cBLekion.setCurrentIndex(self.find_index_lection(self.LektionID))
            self.ersterDurchlauf = False

    def find_index_language(self, id):
        
        statementBuch = "select sprache.fremdsprache, sprache.id from Sprache"
        daten = self.Datenbank.getDataAsList(statementBuch)
        liste = []
        for i in daten:
            liste.append(i[1])
        return liste.index(id)

    def find_index_book(self, id):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        daten = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (buecher.id_sprache=sprache.id) \
        where sprache.id like "+str(datenidSprache[0][1]))
        liste = []
        for i in daten:
            liste.append(i[1])
        return liste.index(id)

    def find_index_lection(self, id):
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
        Deutsch='"+str(self.tfDeutsch.text().toUtf8()).strip()+"', Fremd='"+str(self.tfFremd.text().toUtf8()).strip()+"' \
        where id like "+str(self.VokabelID)
        self.Datenbank.setData(updateStatementVokabeln)
        
        Woerterbuch.Woerterbuch.redraw_table(self.parent)

        self.close()