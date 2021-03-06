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
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.rewrite_books)
        self.connect(self.cbColor, QtCore.SIGNAL("clicked()"), self.colorisedListener)
        self.connect(self.cbSolid, QtCore.SIGNAL("clicked()"), self.colorisedListener)
        self.connect(self.cbSufficient, QtCore.SIGNAL("clicked()"), self.colorisedListener)
        self.connect(self.cbMiserable, QtCore.SIGNAL("clicked()"), self.colorisedListener)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.redraw_table)
        self.connect(self.chBBuch, QtCore.SIGNAL("clicked()"), self.redraw_table)
        self.connect(self.tfSuche, QtCore.SIGNAL("textChanged(QString)"), self.redraw_table)
        self.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.edit_selection)

        self.headerDaten = ['Buch', 'Lektion', 'Deutsch', 'Fremdsprache']

        datenSprache = self.Datenbank.getDataAsQStringList("select fremdsprache, id from SPRACHE")
        modelSprache = QtGui.QStringListModel(datenSprache)
        self.cBSprache.setModel(modelSprache)
        self.rewrite_books()
        self.tVWoerterbuch.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tVWoerterbuch.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.tVWoerterbuch.doubleClicked.connect(self.edit_selection)
        self.EditWindow = None

    def colorisedListener(self):
        # print(self.createSearchStatementFlags())
        self.redraw_table()

    def createSearchStatementFlags(self):
        attach = ""
        if self.cbColor.isChecked():


            if self.cbSolid.isChecked():
                attach = attach + " (vokabeln.richtig > vokabeln.falsch and vokabeln.zuletztrichtig like 1) or"
            if self.cbSufficient.isChecked():
                attach = attach + " (vokabeln.richtig > vokabeln.falsch and vokabeln.zuletztrichtig like 0) or"
            if self.cbMiserable.isChecked():
                attach = attach + " (vokabeln.richtig <= vokabeln.falsch and vokabeln.zuletztrichtig like 0) or"
        if len(attach) > 0:
            attach = " ("+attach[:-2]+") "

        return attach

    def rewrite_books(self):

        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'")

        datenBuch = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join sprache on (sprache.id=Buecher.id_sprache) \
        where Sprache.id like "+str(datenidSprache[0][1])+" " \
                                                          "and Buecher.name not like 'Sonder%'")
        modelBuch = QtGui.QStringListModel(datenBuch)
        self.cBBuch.setModel(modelBuch)
        self.redraw_table()

    def redraw_table(self):
        statement = "select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'"
        #print(statement)
        datenidSprache = self.Datenbank.getDataAsList(statement)

        suchString = str(self.tfSuche.text().toUtf8()).decode("utf-8")

        if self.chBBuch.isChecked():
            datenidBuch =  self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
            join sprache on (sprache.id=Buecher.id_sprache) "
                                                        "where Sprache.id like "+str(datenidSprache[0][1])+" \
            and Buecher.name not like 'Sonder%' \
            limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'")
            # print datenidBuch

            self.statement = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd, vokabeln.richtig, " \
                             "vokabeln.falsch, vokabeln.zuletztrichtig, vokabeln.id from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where buecher.id like "+str(datenidBuch[0][1])+"\
            and sprache.id like "+str(datenidSprache[0][1])+"\
            and (lektionen.name like '%"+suchString+"%' or \
            vokabeln.deutsch like '%"+suchString+"%' or \
            vokabeln.fremd like '%"+suchString+"%')"

        else:
            self.statement = "select Buecher.name, Lektionen.name, vokabeln.deutsch, vokabeln.fremd, vokabeln.richtig, " \
                             "vokabeln.falsch, vokabeln.zuletztrichtig, vokabeln.id from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where sprache.id like "+str(datenidSprache[0][1])+" \
            and (lektionen.name like '%"+suchString+"%' or \
            vokabeln.deutsch like '%"+suchString+"%' or \
            vokabeln.fremd like '%"+suchString+"%' or \
            Buecher.name like '%"+suchString+"%')"
        #print(self.statement)
        #print self.statementId
        self.IndexListe = list()
        self.dataForModel = list()
        flags = self.createSearchStatementFlags()
        if len(flags) > 0:
            self.statement = self.statement+" and "+flags
        #print(self.statement)

        data = self.Datenbank.getDataAsList(self.statement)
        for i in data:
            self.IndexListe.append(i[7])
            # Buecher.name [0], Lektionen.name [1], vokabeln.deutsch [2], vokabeln.fremd [3], vokabeln.richtig [4],
            # vokabeln.falsch [5], vokabeln.zuletztrichtig [6], vokabeln.id [7]
            self.dataForModel.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])

        # self.index_id_allocate(IDListe)
        #print self.statement


        # self.daten = self.Datenbank.getDataAsList(self.statement)
        model = WoerterbuchModel.ModelListe(self.dataForModel, self.headerDaten, self.cbColor.isChecked())

        self.tVWoerterbuch.setModel(model)
        #tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tVWoerterbuch.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #self.tVWoerterbuch.setStyleSheet("background:red")

    def index_id_allocate(self, ids):
        self.IndexListe = []
        for i in ids:
            self.IndexListe.append(i)

    def edit_selection(self):

        data = self.tVWoerterbuch.selectedIndexes()
        if len(data) > 0:
            row = data[0].row()
            vocabulary_id = self.IndexListe[row]
            self.EditWindow = WoerterbuchBearbeiten.WoerterbuchBearbeiten(self, vocabulary_id)
            self.EditWindow.show()
