#! python2.7
#  -*- coding: utf-8 -*-
"""
Created on 25.09.2013

@author: Johannes
"""
from time import sleep
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
import oberflaechen.SonderWoerterbuch as Sonderwoerterbuch
import oberflaechen.Abfrage as Abfrage
import models.base as Datenbank
import oberflaechen.EinstellungenMindestTreffer as EinstellungenMindestTreffer
from models.InfoThreadMainWindow import InfoThreadMainWindow


class Programm(MainWindow, QtGui.QMainWindow):
    """MainKlasse"""
    def __init__(self):
        #self.r
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        #self.connect(self.btnNeueSprache, QtCore.SIGNAL("clicked()"), self.neue_sprache)
        self.btnNeueSprache.clicked.connect(self.neue_sprache)
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
        self.connect(self.btnZuruecksetzen, QtCore.SIGNAL("clicked()"), self.databaseReseet)
        self.connect(self.pbSonderlektion, QtCore.SIGNAL("clicked()"), self.woerterbuechSonderlektion)
        self.infothread = InfoThreadMainWindow(self)

        self.actionMindestuebereinstimmung.triggered.connect(self.MinFit)
        self.actionSchliessen.triggered.connect(self.closeProgram)
        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        # Fehlerbekaempfung in Sonderlektion
        statement = "update vokabeln set status=0 where status > 6"
        self.datenbank.setData(statement)

        self.wStatistik = None
        self.wLektionAendern= None
        self.wAbfrageForsetzen= None
        self.wVorsichtigSein= None
        self.wBuch_aendern= None
        self.wSprache_aendern= None
        self.wAbfrage_einstellungen= None
        self.wNeue_vokabel= None
        self.wNeues_buch= None
        self.wNeue_sprache= None
        self.wNeue_lektion= None
        self.wWoerterbuch= None
        self.wMinFit= None
        self.wWoerterbuchSonder = None

        if os.stat('zwischenSpeicher.fs').st_size == 0:
            self.FortsetzenDisable()
        else:
            self.FortsetzenEnable()


        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")


        self.setInfoInvisible()
    def closeProgram(self):
        self.close()
    def setInfoVisible(self, text):
        self.labInfotext.setText(text)
        self.labInfotext.setVisible(True)
        self.hw1InfoText.setVisible(True)
        self.hw2InfoText.setVisible(True)
        self.hwInfotext.hide()

    def setInfoInvisible(self):
        self.labInfotext.hide()
        self.hw1InfoText.hide()
        self.hw2InfoText.hide()
        self.hwInfotext.setVisible(True)

    def databaseReseet(self):


        box = QtGui.QMessageBox()

        boxText = u"Wollen Sie die Datenbank wirklich zurücksetzen? <br> Es werden alle Daten gelöscht!"

        box.setText(boxText)

        btnJa = box.addButton(QtCore.QString(u"Ja"), QtGui.QMessageBox.AcceptRole)
        btnNein = box.addButton(QtCore.QString(u"Abbrechen"), QtGui.QMessageBox.RejectRole)
        box.exec_()

        if box.clickedButton() == btnJa:
            statement = "delete from Buecher"
            self.datenbank.delData(statement)

            statement = "delete from Lektionen"
            self.datenbank.delData(statement)
            statement = "delete from sprache"
            self.datenbank.delData(statement)
            statement = "delete from statistik"
            self.datenbank.delData(statement)
            statement = "delete from Vokabeln"
            self.datenbank.delData(statement)
            statement = "delete from sondervokabeln"
            self.datenbank.delData(statement)
            self.infothread.start()
            self.setInfoVisible(u"Datenbank wurde gelöscht")


        elif box.clickedButton() == btnNein:
            print(u"nein geklickt")


    def statistik_oeffnen(self):
        """
        öffnet die Statistik
        """
        self.wStatistik = Statistik.Statistik(self)
        self.wStatistik.show()

    def lektioen_aendern(self):
        """soll Fenster für Lektion ändern anzeigen
        """
        self.wLektionAendern = LektionAendern.LektionAendern(self)
        self.wLektionAendern.show()
    def AbfrageFortsetzen(self):

        self.wAbfrageForsetzen = Abfrage.Abfrage(self, '', '', '', '', '', '', '', '',  '1')
        self.wAbfrageForsetzen.show()
        
    def vorsichtig_sein(self):
        """Fenster für Vorsichtig sein"""
        self.wVorsichtigSein = Vorsichtig.VorsichtigSein(self)
        self.wVorsichtigSein.show()

    def buch_aendern(self):
        """Fenster für Buch ändern"""
        self.wBuch_aendern = BuchAendern.BuchAendern(self)
        self.wBuch_aendern.show()

    def sprache_aendern(self):
        """Fenster für Sprache ändern"""
        self.wSprache_aendern = SpracheAendern.SpracheAendern(self)
        self.wSprache_aendern.show()

    def abfrage_einstellungen(self):
        """Fenster für Abfrage Einstellungen"""
        self.wAbfrage_einstellungen = AbfrageEinstellungen.AbfrageEinstellungen(self)
        self.wAbfrage_einstellungen.show()

    def neue_vokabel(self):
        """Fenster für neue Vokabel"""
        self.wNeue_vokabel = NeueVokabel.NeueVokabelAnlegen(self)
        self.wNeue_vokabel.show()

    def neues_buch(self):
        """Fenster für neue Buch"""
        self.wNeues_buch = NeuesBuch.NeuesBuch(self)
        self.wNeues_buch.show()
        
    def neue_sprache(self):
        """Fenster für neue Sprache"""

        self.wNeue_sprache = NeueSprache.NeueSprache()
        self.wNeue_sprache.show()

    def woerterbuechSonderlektion(self):
        """Fenster für Sonderwoerterbuch"""
        self.wWoerterbuchSonder = Sonderwoerterbuch.SonderWoerterbuch(self)
        self.wWoerterbuchSonder.show()

    def neue_lektion(self):
        """"Fenster für neue Lektion"""
        self.wNeue_lektion = NeueLektion.NeueLektion(self)
        self.wNeue_lektion.show()

    def woerterbuch(self):
        """fenster für Wörterbuch"""
        self.wWoerterbuch = Woerterbuch.Woerterbuch(self)
        self.wWoerterbuch.show()

    def FortsetzenDisable(self):
        self.btnFortsetzen.setEnabled(False)
        self.btnFortsetzen.setToolTip('')

    def FortsetzenEnable(self):
        self.btnFortsetzen.setEnabled(True)
        text = self.datenbank.getDataAsList('select datum from AbfrageFortsetzen where id like 1')
        self.btnFortsetzen.setToolTip(str(text[0][0]))

    def MinFit(self):
        self.wMinFit = EinstellungenMindestTreffer.MindestTreffer(self)
        self.wMinFit.show()

app = QtGui.QApplication(sys.argv) 
dialog = Programm() 
dialog.show() 
sys.exit(app.exec_())
