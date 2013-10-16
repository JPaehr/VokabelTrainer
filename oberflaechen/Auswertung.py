# -*- coding:utf-8 -*-
from __future__ import division
__author__ = 'Johannes'
from PyQt4 import QtCore, QtGui
from windows.WindowAuswertung import Ui_Form as WindowAuswertung
import models.base as Datenbank
import datetime as Datum
from oberflaechen.Statistik import Statistik

class Auswertung(WindowAuswertung, QtGui.QWidget):
    """
    Fenster für die Abfrage
    """
    def __init__(self, parent, float_richtige, int_gesamtanzahl, int_liste_lektionen):
        super(Auswertung, self).__init__(parent)
        self.parent = parent
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.connect(self.PbSchliessen, QtCore.SIGNAL("clicked()"), self.fenster_schliessen)
        self.connect(self.pbStatistik, QtCore.SIGNAL("clicked()"), self.statistik_aufrufen)

        self.labRichtigBeantwortete.setText(str(float_richtige)+" von "+str(int_gesamtanzahl)+" richtig beantwortet")
        if float_richtige == 0:
            self.labInProz.setText("Das entspricht 0%")
        else:
            float_anzahl_richtiger_prozent = round(float(float_richtige)/int_gesamtanzahl*100, 2)
            self.labInProz.setText("Das entspricht "+str(float_anzahl_richtiger_prozent)+"%")

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        insert = "insert into Statistik (datum, richtig, gesamt, lektionen) \
        values ('"+str(Datum.date.today())+"', '"+str(float_richtige)+"',  '"+str(int_gesamtanzahl)+"',  \
        '"+str(self.__liste_to_string(int_liste_lektionen))+"')"

        self.datenbank.setData(insert)

    def statistik_aufrufen(self):
        self.close()
        self.parent.close()
        test = Statistik(self)
        test.show()

    def fenster_schliessen(self):
        self.parent.close()
        self.close()
    def __liste_to_string(self, liste):
        string = ""
        for i in liste:
            string = string +str(i)+", "

        return string[:-2]