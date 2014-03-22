# -*- coding: utf-8 -*-
"""
Created on 25.09.2013

@author: Johannes
"""
from PyQt4 import QtGui, QtCore
import sys
import os


from windows.MainWindow import Ui_MainWindow as MainWindow

import oberflaechen.NeueSprache as NeueSprache
import oberflaechen.NeuesBuch as NeuesBuch
import oberflaechen.NeueLektion as NeueLektion
import oberflaechen.Woerterbuch as Woerterbuch
import oberflaechen.NeueVokabel as NeueVokabel
import oberflaechen.AbfrageEinstellungen as AbfrageEinstellungen
import oberflaechen.LektionAendern as LektionAendern
import oberflaechen.BuchAendern as BuchAendern
import oberflaechen.SpracheAendern as SpracheAendern
import oberflaechen.Vorsichtig as Vorsichtig
import oberflaechen.Statistik as Statistik
import models.base as Datenbank
import oberflaechen.Abfrage as Abfrage
import models.base as Datenbank


class Programm(MainWindow, QtGui.QMainWindow):
    """MainKlasse"""
    def __init__(self):
        #self.r
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.connect(self.btnNeueSprache, QtCore.SIGNAL("clicked()"), self.neue_sprache)
        self.connect(self.btnNeuesBuch, QtCore.SIGNAL("clicked()"), self.neues_buch)
        self.connect(self.btnNeueLektion, QtCore.SIGNAL("clicked()"), self.neue_lektion)
        self.connect(self.btnWoerterbuch, QtCore.SIGNAL("clicked()"), self.woerterbuch)
        self.connect(self.btnNeueVok, QtCore.SIGNAL("clicked()"), self.neue_vokabel)
        self.connect(self.btnAbfrageStarten, QtCore.SIGNAL("clicked()"), self.abfrage_einstellungen)
        self.connect(self.btnSpracheBeareiten, QtCore.SIGNAL("clicked()"), self.sprache_aendern)
        self.connect(self.btnBuecherBearbeiten, QtCore.SIGNAL("clicked()"), self.buch_aendern)
        self.connect(self.btnLektionbearbeiten, QtCore.SIGNAL("clicked()"), self.lektioen_aendern)
        self.connect(self.btnStatistik, QtCore.SIGNAL("clicked()"), self.statistik_oeffnen)
        self.connect(self.btnFortsetzen, QtCore.SIGNAL("clicked()"), self.AbfrageFortsetzen)

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")


        if os.stat('zwischenSpeicher.fs').st_size == 0:
            self.FortsetzenDisable()
        else:
            self.FortsetzenEnable()

        
        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")



    def statistik_oeffnen(self):
        """
        öffnet die Statistik
        """
        test = Statistik.Statistik(self)
        test.show()

    def lektioen_aendern(self):
        """soll Fenster für Lektion ändern anzeigen
        """
        test = LektionAendern.LektionAendern(self)
        test.show()
    def AbfrageFortsetzen(self):

        test = Abfrage.Abfrage(self, '', '', '', '', '', '', '', '1')
        test.show()
        
    def vorsichtig_sein(self):
        """Fenster für Vorsichtig sein"""
        test = Vorsichtig.VorsichtigSein(self)
        test.show()

    def buch_aendern(self):
        """Fenster für Buch ändern"""
        test = BuchAendern.BuchAendern(self)
        test.show()

    def sprache_aendern(self):
        """Fenster für Sprache ändern"""
        test = SpracheAendern.SpracheAendern(self)
        test.show()

    def abfrage_einstellungen(self):
        """Fenster für Abfrage Einstellungen"""
        test = AbfrageEinstellungen.AbfrageEinstellungen(self)
        test.show()

    def neue_vokabel(self):
        """Fenster für neue Vokabel"""
        test = NeueVokabel.NeueVokabelAnlegen(self)
        test.show()

    def neues_buch(self):
        """Fenster für neue Buch"""
        test = NeuesBuch.NeuesBuch(self)
        test.show()
        
    def neue_sprache(self):
        """Fenster für neue Sprache"""
        test = NeueSprache.NeueSprache(self)
        test.show()

    def neue_lektion(self):
        """"Fenster für neue Lektion"""
        test = NeueLektion.NeueLektion(self)
        test.show()

    def woerterbuch(self):
        """fenster für Wörterbuch"""
        test = Woerterbuch.Woerterbuch(self)
        test.show()

    def FortsetzenDisable(self):
        self.btnFortsetzen.setEnabled(False)
        self.btnFortsetzen.setToolTip('')

    def FortsetzenEnable(self):
        self.btnFortsetzen.setEnabled(True)
        text = self.datenbank.getDataAsList('select datum from AbfrageFortsetzen where id like 1')
        self.btnFortsetzen.setToolTip(text[0][0])

app = QtGui.QApplication(sys.argv) 
dialog = Programm() 
dialog.show() 
sys.exit(app.exec_())
