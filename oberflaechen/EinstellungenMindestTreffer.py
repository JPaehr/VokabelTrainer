# -*- coding:utf-8 -*-
from __future__ import division
__author__ = 'Johannes'
from PyQt4 import QtCore, QtGui
from windows.WindowMindestTreffer import Ui_Form as WindowMindestTreffer
import models.base as Datenbank


class MindestTreffer(WindowMindestTreffer, QtGui.QWidget):

    def __init__(self, parent=None):
        super(MindestTreffer, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.connect(self.lENeuerWert, QtCore.SIGNAL("textChanged(QString)"), self.newPaint)
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), self.abbrechen)
        self.connect(self.btnSpeichernUSchliessen, QtCore.SIGNAL("clicked()"), self.speichernUSchiessen)

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        self.minTrefferAlt = self.datenbank.getDataAsList("select mindesttreffer from einstellungen")[0][0]

        self.lENeuerWert.setText(str(self.minTrefferAlt))
        self.lENeuerWert.selectAll()

        self.newPaint()
    def abbrechen(self):
        self.close()
    def speichernUSchiessen(self):
        try:

            new = int(round(int(self.lENeuerWert.text()), 0))
            self.datenbank.setData("update Einstellungen set mindestTreffer="+str(new)+" where id like 1")
            self.close()
        except:
            print "User zu doof um sinnvollen Wert einzugeben :P"




    def newPaint(self):
        text = "wer wie was der die das wieso weshalb warum wer nicht fragt bleibt dumm!"

        #print round(len(text)*self.minTrefferAlt/100, 0)
        teil1 = text[:int(round(len(text)*self.minTrefferAlt/100, 0))]
        teil2 = text[int(round(len(text)*self.minTrefferAlt/100, 0)):]
        #self.labText.setText("<font color='red'>Some text</font><font color='blue'>Some text</font>")
        first1 = "<font color='red'>"
        last1 = "</font>"

        first2 = "<font color='green'>"
        self.labTextAlt.setText(first1+teil1+last1+first2+teil2+last1)


        #print round(len(text)*self.minTrefferAlt/100, 0)
        teil1 = text[:int(round(len(text)*int(self.lENeuerWert.text())/100, 0))]
        teil2 = text[int(round(len(text)*int(self.lENeuerWert.text())/100, 0)):]
        #self.labText.setText("<font color='red'>Some text</font><font color='blue'>Some text</font>")
        first1 = "<font color='red'>"
        last1 = "</font>"

        first2 = "<font color='green'>"
        self.labTextNeu.setText(first1+teil1+last1+first2+teil2+last1)
