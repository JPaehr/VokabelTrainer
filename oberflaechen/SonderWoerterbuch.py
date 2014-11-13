# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
import models.base as Datenbank
from models import WoerterbuchModel as WoerterbuchModel
from windows.WindowWoerterbuchSonderlektion import Ui_Form as WindowWoerterbuchSonderlektion

class SonderWoerterbuch(WindowWoerterbuchSonderlektion, QtGui.QWidget):
    def __init__(self, parent):
        super(SonderWoerterbuch, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        #self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.BuecherNeuSchreiben)
        # self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.TabelleNeuZeichnen)
        # self.connect(self.chBBuch, QtCore.SIGNAL("clicked()"), self.TabelleNeuZeichnen)
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.TabelleNeuZeichnen)
        self.connect(self.cBSprache, QtCore.SIGNAL("clicked()"), self.TabelleNeuZeichnen)
        self.connect(self.tfSuche, QtCore.SIGNAL("textChanged(QString)"), self.TabelleNeuZeichnen)
        # self.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.MarkierungBearbeiten)

        self.headerDaten = ['Buch', 'Lektion', 'Deutsch', 'Fremdsprache', 'Sonderlektion']

        datenSprache = self.Datenbank.getDataAsQStringList("select fremdsprache, id from SPRACHE")
        modelSprache = QtGui.QStringListModel(datenSprache)
        self.cBSprache.setModel(modelSprache)

        self.tVWoerterbuch.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tVWoerterbuch.setSelectionMode(QtGui.QTableView.SingleSelection)
        # self.tVWoerterbuch.doubleClicked.connect(self.MarkierungBearbeiten)
        self.EditWindow = None
        self.TabelleNeuZeichnen()
         
    def TabelleNeuZeichnen(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'")
        #print("Sprachid: "+str(datenidSprache))
        suchString = str(self.tfSuche.text().toUtf8()).decode("utf-8")


        self.statementId = "select Buecher.name, Lektionen.name,  vokabeln.deutsch, vokabeln.fremd, vokabeln.id from sprache \
        join buecher on (sprache.id=buecher.id_sprache) \
        join lektionen on (lektionen.idBuch = buecher.id) \
        join vokabeln on (vokabeln.idlektion=lektionen.id) \
        join sondervokabeln on (sondervokabeln.idVokabeln=vokabeln.id) \
        where (sprache.id like "+str(datenidSprache[0][1])+" \
        and (lektionen.name like '%"+suchString+"%' or \
        vokabeln.deutsch like '%"+suchString+"%' or \
        vokabeln.fremd like '%"+suchString+"%' or \
        Buecher.name like '%"+suchString+"%')) and " \
        "sondervokabeln.show like 1 " \
        "order by vokabeln.id"



        self.statement = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd from sprache \
        join buecher on (sprache.id=buecher.id_sprache) \
        join lektionen on (lektionen.idBuch = buecher.id) \
        join vokabeln on (vokabeln.idlektion=lektionen.id) \
        join sondervokabeln on (sondervokabeln.idVokabeln=vokabeln.id) \
        where ( sprache.id like "+str(datenidSprache[0][1])+" \
        and (lektionen.name like '%"+suchString+"%' or \
        vokabeln.deutsch like '%"+suchString+"%' or \
        vokabeln.fremd like '%"+suchString+"%' or \
        Buecher.name like '%"+suchString+"%')) and " \
        "sondervokabeln.show like 1 " \
        "order by vokabeln.id"


        IDListe = []
        for i in self.Datenbank.getDataAsList(self.statementId):
            IDListe.append(i[4])
        self.IndexIdZuordnung(IDListe)

        self.statementForSondername = "select Lektionen.name from sondervokabeln \
        join lektionen on (lektionen.id=sondervokabeln.idSonderlektion) " \
        +str(self.listeToSql(IDListe, "sondervokabeln.idVokabeln"))+ " " \
        "order by sondervokabeln.idVokabeln"

        self.sonderNamen = self.Datenbank.getDataAsList(self.statementForSondername)

        self.daten = self.Datenbank.getDataAsList(self.statement)
        self.datenMitSonderlektionsNamen = list()
        for i in range(len(self.daten)):
            liste = list()
            for k in range(len(self.daten[i])):
                liste.append(self.daten[i][k])
            liste.append(self.sonderNamen[i][0])
            self.datenMitSonderlektionsNamen.append(liste)
            liste = list()

        model = WoerterbuchModel.ModelListe(self.datenMitSonderlektionsNamen, self.headerDaten)


        self.tVWoerterbuch.setModel(model)
        #tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tVWoerterbuch.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def IndexIdZuordnung(self, ids):
        self.IndexListe = []
        for i in ids:
            self.IndexListe.append(i)

    def listeToSql(self, liste, column):
        string = "where "
        if len(liste) == 0:
            return ""
        else:
            for i in liste:
                string = string+" "+str(column)+" like "+str(i)+" or"
            return string[:-2]

