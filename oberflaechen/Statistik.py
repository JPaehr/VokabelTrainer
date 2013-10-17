# -*- coding: utf-8 -*-
__author__ = 'Johannes'

from PyQt4 import QtGui, QtCore
from windows.WindowStatistik import Ui_Form as WindowStatistik
import models.base as Datenbank
import models.WoerterbuchModel as StatistikModel


class Statistik(WindowStatistik, QtGui.QWidget):
    """
    Fenster für die Abfrage Einstellungen
    """
    def __init__(self, parent):
        super(Statistik, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        statement = "select datum, richtig, gesamt, lektionen from statistik"
        daten = self.datenbank.getDataAsList(statement)
        #print daten
        header = ['datum', 'richtig/von', 'in Prozent', 'lektionen']

        datenZumAnzeigen = []
        for i in daten:
            datum = i[0]
            richtigVon = str(i[1])+"/"+str(i[2])
            inProzent = str(round(float(float(i[1])/int(i[2]))*100, 2))+"%"

            lektionen = ""
            listeLektionId = i[3].split(",")
            statement = "select lektionen.name from lektionen "+self.listeToSql(listeLektionId)
            lektionsAbfrage = self.datenbank.getDataAsList(statement)
            for teil in lektionsAbfrage:
                lektionen = lektionen+str(teil[0])+", "
            lektionen = lektionen[:-2]

            datenZumAnzeigen.append([datum, richtigVon, inProzent, lektionen])
            #print statement


        model = StatistikModel.ModelListe(datenZumAnzeigen, header)
        self.tvStatistik.setModel(model)
        self.tvStatistik.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        """
        TODO
        Id von den Lektionen zu dem Lektionsnamen machen
        """

    def listeToSql(self, liste):
        string = "where "
        for i in liste:
            string = string+" lektionen.id like "+str(i)+" or"
        return string[:-2]
