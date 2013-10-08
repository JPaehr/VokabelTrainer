# -*- coding: utf-8 -*-
'''
Created on 25.09.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
import sys

from windows.MainWindow import Ui_MainWindow as MainWindow

import oberfaechen.NeueSprache as NeueSprache
import oberfaechen.NeuesBuch as NeuesBuch
import oberfaechen.NeueLektion as NeueLektion
import oberfaechen.Woerterbuch as Woerterbuch
import oberfaechen.NeueVokabel as NeueVokabel
import oberfaechen.AbfrageEinstellungen as AbfrageEinstellungen
import oberfaechen.LektionAendern as LektionAendern
import oberfaechen.BuchAendern as BuchAendern
import oberfaechen.SpracheAendern as SpracheAendern



import models.base as Datenbank


class Programm(MainWindow, QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.connect(self.btnNeueSprache, QtCore.SIGNAL("clicked()"), self.NeueSprache)
        self.connect(self.btnNeuesBuch, QtCore.SIGNAL("clicked()"), self.NeuesBuch)
        self.connect(self.btnNeueLektion, QtCore.SIGNAL("clicked()"), self.NeueLektion)
        self.connect(self.btnWoerterbuch, QtCore.SIGNAL("clicked()"), self.Woerterbuch)
        self.connect(self.btnNeueVok, QtCore.SIGNAL("clicked()"), self.NeueVokabel)
        self.connect(self.btnAbfrageStarten, QtCore.SIGNAL("clicked()"), self.AbfrageEinstellungen)
        self.connect(self.btnSpracheBeareiten, QtCore.SIGNAL("clicked()"), self.SpracheAendern)
        self.connect(self.btnBuecherBearbeiten, QtCore.SIGNAL("clicked()"), self.BuchAendern)
        self.connect(self.btnLektionbearbeiten, QtCore.SIGNAL("clicked()"), self.LektioenAendern)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
    def LektioenAendern(self):
        test = LektionAendern.LektionAendern(self)
        test.show()
    def BuchAendern(self):
        test = BuchAendern.BuchAendern(self)
        test.show()
    def SpracheAendern(self):
        test = SpracheAendern.SpracheAendern(self)
        test.show()
    def AbfrageEinstellungen(self):
        test = AbfrageEinstellungen.AbfrageEinstellungen(self)
        test.show()
    def NeueVokabel(self):
        test = NeueVokabel.NeueVokabelAnlegen(self)
        test.show()
    def NeuesBuch(self):
        test = NeuesBuch.NeuesBuch(self)
        test.show()
        
    def NeueSprache(self):
        test = NeueSprache.NeueSprache(self)
        test.show()
    def NeueLektion(self):
        test = NeueLektion.NeueLektion(self)
        test.show()
    def Woerterbuch(self):
        test = Woerterbuch.Woerterbuch(self)
        test.show()

app = QtGui.QApplication(sys.argv) 
dialog = Programm() 
dialog.show() 
sys.exit(app.exec_())
