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
        header = ['datum', 'Richtige', 'Gesamt', 'lektionen']
        model = StatistikModel.ModelListe(daten, header)
        self.tvStatistik.setModel(model)
        self.tvStatistik.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        """
        TODO
        Id von den Lektionen zu dem Lektionsnamen machen
        """
