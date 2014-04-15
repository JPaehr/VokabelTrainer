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

        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")

       
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.BuecherNeuZeichen)
        self.connect(self.cbBuchAuswaehlen, QtCore.SIGNAL("activated(int)"), self.LektionNeuZeichen)
        self.connect(self.cbLektionAuswaehlen, QtCore.SIGNAL("activated(int)"), self.TextfeldNeuZeichen)
        self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.Speichern)
        self.connect(self.btnLektionLoeschen, QtCore.SIGNAL("clicked()"), self.delWithoutClose)
        self.connect(self.btnLektionloeschenUSchliessen, QtCore.SIGNAL("clicked()"), self.delWithClose)


        self.SpracheNeuZeichnen()
        #self.BuecherNeuZeichen()
        #self.LektionNeuZeichen()
        self.tfNeuerName.setFocus()
    def SpracheNeuZeichnen(self):
        #print "Sprach wird gezeichnet"

        statement = "select fremdsprache,id from Sprache"
        #print "Sprache neu zeichnen:" +str(statement)
        daten = self.Datenbank.getDataAsQStringList(statement)
        model = QtGui.QStringListModel(daten)
        self.cBSpracheAuswaehlen.setModel(model)
        self.BuecherNeuZeichen()

    def loeschenClicked(self, close=False):

        lektionenid = self.getIdLektion()
        anzVokStatement = "select count(*) from vokabeln where idlektion like "+str(lektionenid)
        anzVok = self.Datenbank.getDataAsList(anzVokStatement)[0][0]
        #print anzVok
        delVokStatement = "delete from vokabeln where idlektion like "+str(lektionenid)
        delLektion = "delete from lektionen where id like "+str(lektionenid)

        box = QtGui.QMessageBox()
        #box.setText("")
        #print unicode(self.cbLektionAuswaehlen.currentText())
        lektionsText = unicode(self.cbLektionAuswaehlen.currentText())
        #print "lektionsName: "+str(lektionsText)

        box.setText(u"Soll das Buch '"+lektionsText+u"' wirklich gelöscht werden?")

        box.setInformativeText(u"Es werden "+str(anzVok)+u" Vokabeln gelöscht!")

        #box.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        btnJa = box.addButton(QtCore.QString(u"Ja"), QtGui.QMessageBox.AcceptRole)
        btnNein = box.addButton(QtCore.QString(u"Nein"), QtGui.QMessageBox.RejectRole)
        box.exec_()

        if box.clickedButton() == btnJa:
            print u"loeschen"
            self.Datenbank.setData(delVokStatement)
            self.Datenbank.setData(delLektion)
            if close:
                self.close()
        elif box.clickedButton() == btnNein:
            print u"nicht loeschen"

        self.LektionNeuZeichen()

    def delWithClose(self):
        self.loeschenClicked(True)
    def delWithoutClose(self):
        self.loeschenClicked()
    def getIdSpracheAlt(self):
        statement = "select fremdsprache,id from Sprache " \
                    "limit '"+str(self.cBSpracheAuswaehlen.currentIndex())+"', '"+str(self.cBSpracheAuswaehlen.currentIndex()+1)+"'"
        #print statement
        daten = self.Datenbank.getDataAsList(statement)

        try:
            return daten[0][1]
        except:
            print "Fehler in getIdSpracheAlt"

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
        statement = "select Buecher.name, Buecher.id from Buecher " \
                    "join Sprache on (sprache.id = Buecher.id_sprache) " \
                    "where sprache.id like '"+str(self.getIdSpracheAlt())+"' " \
                    "limit '"+str(self.cbBuchAuswaehlen.currentIndex())+"', '"+str(self.cbBuchAuswaehlen.currentIndex()+1)+"'"
        #print statement
        daten = self.Datenbank.getDataAsList(statement)
        try:
            return daten[0][1]
        except:
            print "Fehler in getIdBuchAlt"
    
    def getIdBuchNeu(self):
        daten = self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"' \
        limit '"+str(self.cbNeuesBuch.currentIndex())+"', '"+str(self.cbNeuesBuch.currentIndex()+1)+"'")
        
        return daten[0][1]
    def getIdLektion(self):
        daten = self.Datenbank.getDataAsList("select lektionen.name, lektionen.id from Lektionen "
                                             "join Buecher on (Buecher.id = Lektionen.idBuch) "
                                             "where Buecher.id like '"+str(self.getIdBuchAlt())+"' \
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