# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowBuchAendern import Ui_Form as WindowBuchAendern
import models.base as Datenbank

class BuchAendern(WindowBuchAendern, QtGui.QWidget):
    def __init__(self, parent):
        super(BuchAendern, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        
       
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.BuecherNeuZeichen)
        self.connect(self.cbBuchAuswaehlen, QtCore.SIGNAL("activated(int)"), self.TextfeldNeuZeichen)
        self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.Speichern)
        self.connect(self.btnBuchLoeschen, QtCore.SIGNAL('clicked()'), self.loeschenClicked)

        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite") 
        
        self.SpracheNeuZeichnen()
        self.TextfeldNeuZeichen()
        self.tfNeuerName.setFocus()

        #self.getIdsLektionen()

    def ListeZuSql(self, liste, args):
        statement = "where "
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]

    def loeschenClicked(self):

        buchid = self.getIdBuch()
        lektionenids = self.getIdsLektionen()
        anzVokStatement = "select count(*) from vokabeln "+str(self.ListeZuSql(lektionenids, 'idlektion'))
        anzVok = self.Datenbank.getDataAsList(anzVokStatement)[0][0]
        #print anzVok
        delVokStatement = "delete from vokabeln "+str(self.ListeZuSql(lektionenids, 'idlektion'))
        delLektion = "delete from lektionen "+str(self.ListeZuSql(lektionenids, 'id'))
        delBuch = "delete from Buecher where id like "+str(buchid)

        #print anzVokStatement

        box = QtGui.QMessageBox()
        #box.setText("")
        buchtext = str(self.cbBuchAuswaehlen.currentText()).decode('utf-8')
        #print u"Soll das Buch "+str(str(self.cbBuchAuswaehlen.currentText()).decode('utf-8'))+u" wirklich gelöscht werden???"

        box.setText(u"Soll das Buch '"+buchtext+u"' wirklich gelöscht werden?")

        box.setInformativeText(u"Es werden "+str(anzVok)+u" Vokabeln gelöscht!")

        #box.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        btnJa = box.addButton(QtCore.QString(u"Ja"), QtGui.QMessageBox.AcceptRole)
        btnNein = box.addButton(QtCore.QString(u"Nein"), QtGui.QMessageBox.RejectRole)
        box.exec_()

        if box.clickedButton() == btnJa:
            print u"loeschen"
            self.Datenbank.setData(delVokStatement)
            self.Datenbank.setData(delLektion)
            self.Datenbank.setData(delBuch)
        elif box.clickedButton() == btnNein:
            print u"nicht loeschen"
        self.close()

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
        statement = "select Buecher.name, Buecher.id from Buecher \
        join Sprache on (sprache.id = Buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSpracheAlt())+"' \
        limit '"+str(self.cbBuchAuswaehlen.currentIndex())+"', '"+str(self.cbBuchAuswaehlen.currentIndex()+1)+"'"
        #print statement
        daten = self.Datenbank.getDataAsList(statement)

        if len(daten) > 0:
            return daten[0][1]
        else:
            return []
    def getIdsLektionen(self):
        statement = "select lektionen.id from lektionen where idBuch like "+str(self.getIdBuch())
        daten = self.Datenbank.getDataAsList(statement)
        liste = list()
        for i in daten:
            liste.append(i[0])

        return liste
        
    def TextfeldNeuZeichen(self):
        self.tfNeuerName.setText(self.cbBuchAuswaehlen.currentText())
        self.tfNeuerName.setFocus()
    def Speichern(self):
        neuerName = str(self.tfNeuerName.text().toUtf8()).decode("utf-8")
                
        statement = "update Buecher set name='"+str(neuerName)+"', id_sprache='"+str(self.getIdSpracheNeu())+"' where id like '"+str(self.getIdBuch())+"'"
        self.Datenbank.setData(statement)
        self.close()