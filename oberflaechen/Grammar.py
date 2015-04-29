# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowGrammarAendern import Ui_Form as WindowGrammarChange
import models.base as Datenbank


class FormhinweiseAendern(WindowGrammarChange, QtGui.QWidget):
    def __init__(self, parent):
        super(FormhinweiseAendern, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      

        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        # self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        # self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.BuecherNeuZeichen)
        # self.connect(self.cbBuchAuswaehlen, QtCore.SIGNAL("activated(int)"), self.TextfeldNeuZeichen)
        # self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.Speichern)
        # self.connect(self.btnBuchLoeschen, QtCore.SIGNAL('clicked()'), self.loeschenClicked)
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.preSelectNewLanguage)
        self.connect(self.cBSpracheAuswaehlen, QtCore.SIGNAL("activated(int)"), self.paintHints)
        self.connect(self.cbGrammarHint, QtCore.SIGNAL("activated(int)"), self.preSelectTextfield)
        self.connect(self.btnSpeichernUndSchliessen, QtCore.SIGNAL("clicked()"), self.saveAndExit)


        self.paintLanguage()
        # self.TextfeldNeuZeichen()
        # self.tfNeuerName.setFocus()

        #self.getIdsLektionen()

    def ListeZuSql(self, liste, args):
        statement = "where "
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]

    def paintLanguage(self):
        statement = "select fremdsprache, id from sprache"
        data = self.Datenbank.getDataAsList(statement)
        self.langIdList = list()
        self.langNameList = QtCore.QStringList()

        for i in data:
            self.langIdList.append(i[1])
            self.langNameList.append(i[0])

        model = QtGui.QStringListModel(self.langNameList)
        self.cBSpracheAuswaehlen.setModel(model)
        self.cBSpracheNeu.setModel(model)

        self.paintHints()

    def preSelectNewLanguage(self):
        self.cBSpracheNeu.setCurrentIndex(self.cBSpracheAuswaehlen.currentIndex())

    def paintHints(self):
        statement = "select hint, id from formhinweise where idsprache like "+str(self.langIdList[self.cBSpracheAuswaehlen.currentIndex()])
        #print(statement)
        data = self.Datenbank.getDataAsList(statement)

        self.hintIdList = list()
        self.hintNameList = QtCore.QStringList()

        for i in data:
            self.hintIdList.append(i[1])
            self.hintNameList.append(i[0])

        model = QtGui.QStringListModel(self.hintNameList)
        self.cbGrammarHint.setModel(model)
        self.preSelectTextfield()

    def preSelectTextfield(self):
        self.tfNeuerName.setText(self.cbGrammarHint.currentText())

    def saveAndExit(self):
        idsprache = self.langIdList[self.cBSpracheNeu.currentIndex()]
        if len(self.hintIdList) < 1:
            statement = "insert into formhinweise (hint, idsprache) values ('"+str(self.tfNeuerName.text())+"', '"+str(idsprache)+"')"

        else:
            statement = "update formhinweise set hint='"+str(self.tfNeuerName.text())+"', idsprache='"+str(idsprache)+"' " \
                        " where id like "+str(self.hintIdList[self.cbGrammarHint.currentIndex()])
        #print(statement)
        self.Datenbank.setData(statement)
        self.close()
