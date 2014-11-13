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
        self.connect(self.btnLoeschenUSchliessen, QtCore.SIGNAL("clicked()"), self.loeschenClicked)

        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        daten = self.Datenbank.getDataAsQStringList("select fremdsprache, id from Sprache")
        model = QtGui.QStringListModel(daten)
        self.cBSpracheAuswaehlen.setModel(model)
        self.TextfeldNeuZeichen()
        self.tfNeuerName.setFocus()

    def loeschenClicked(self):

        spracheId = self.getIdSprache()

        buecherIds = self.getIdsBuecher("sprache.id", spracheId)
        lektionenids = self.getIdsLektionen("sprache.id", spracheId)
        vokabelIds = self.getIdsVokabeln("sprache.id", spracheId)


        delVokStatement = "delete from vokabeln "+str(self.ListeZuSql(lektionenids, 'idlektion'))
        delLektion = "delete from lektionen "+str(self.ListeZuSql(lektionenids, 'id'))
        delBuch = "delete from buecher "+str(self.ListeZuSql(buecherIds, 'id'))
        delSprache = "delete from sprache where id like "+str(spracheId)

        #print anzVokStatement

        box = QtGui.QMessageBox()
        #box.setText("")
        sprachText = str(self.cBSpracheAuswaehlen.currentText()).decode('utf-8')

        box.setText(u"Soll die Sprache '"+sprachText+u"' wirklich gelöscht werden?")
        if len(buecherIds) > 1:
            buchformuliereung = len(buecherIds)
            buch = u"Bücher"
        else:
            buch = u"Buch"
            buchformuliereung = u"ein"
        box.setInformativeText(u"Es werden "+str(len(vokabelIds))+u" Vokabeln, "+str(len(lektionenids))+u" Lektionen"
                                u" und "+unicode(buchformuliereung)+u" "+unicode(buch)+u" gelöscht")

        #box.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        btnJa = box.addButton(QtCore.QString(u"Ja"), QtGui.QMessageBox.AcceptRole)
        btnNein = box.addButton(QtCore.QString(u"Nein"), QtGui.QMessageBox.RejectRole)
        box.exec_()

        if box.clickedButton() == btnJa:
            print u"loeschen"
            self.Datenbank.setData(delVokStatement)
            self.Datenbank.setData(delLektion)
            self.Datenbank.setData(delBuch)
            self.Datenbank.setData(delSprache)
            self.close()
        elif box.clickedButton() == btnNein:
            print u"nicht loeschen"

    def getIdsLektionen(self, feld, param):
        statement = "select lektionen.id " \
                    "from lektionen " \
                    "join buecher on (buecher.id = lektionen.idbuch) " \
                    "join sprache on (sprache.id = buecher.id_sprache)" \
                    "where "+str(feld)+" like "+str(param)
        daten = self.Datenbank.getDataAsList(statement)
        liste = list()
        for i in daten:
            liste.append(i[0])

        return liste

    def getIdsBuecher(self, feld, param):
        statement = "select buecher.id " \
                    "from buecher " \
                    "join sprache on (sprache.id = buecher.id_sprache)" \
                    "where "+str(feld)+" like "+str(param)
        daten = self.Datenbank.getDataAsList(statement)
        liste = list()
        for i in daten:
            liste.append(i[0])

        return liste

    def getIdsVokabeln(self, feld, param):
        statement = "select vokabeln.id " \
                    "from vokabeln " \
                    "join lektionen on (lektionen.id = vokabeln.idlektion) " \
                    "join buecher on (buecher.id = lektionen.idbuch) " \
                    "join sprache on (sprache.id = buecher.id_sprache) " \
                    "where "+str(feld)+" like "+str(param)
        daten = self.Datenbank.getDataAsList(statement)
        liste = list()
        for i in daten:
            liste.append(i[0])

        return liste

    def TextfeldNeuZeichen(self):
        self.tfNeuerName.setText(self.cBSpracheAuswaehlen.currentText())
        self.tfNeuerName.setFocus()

    def Speichern(self):
        neuerName = str(self.tfNeuerName.text().toUtf8()).decode("utf-8")
        #print neuerName

        id = self.getIdSprache()

        statement = "update sprache set fremdsprache='"+str(neuerName)+"' where id like '"+str(id)+"'"
        self.Datenbank.setData(statement)
        self.close()

    def getIdSprache(self):
        daten = self.Datenbank.getDataAsList("select fremdsprache, id from Sprache \
        limit '"+str(self.cBSpracheAuswaehlen.currentIndex())+"', '"+str(self.cBSpracheAuswaehlen.currentIndex()+1)+"'")
        id = daten[0][1]
        return id

    def ListeZuSql(self, liste, args):
        statement = "where "
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]