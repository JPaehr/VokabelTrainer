#-*- coding: utf-8 -*-
from __future__ import division
__author__ = 'JPaehr'

import models.base as Datenbank
from PyQt4 import QtGui, QtCore
import codecs


class ReadVoks(QtCore.QThread):

    def __init__(self, parent, path, IdLektion):
        super(ReadVoks, self).__init__(parent)
        self.path = path
        #self.parent = parent
        self.idLektion = IdLektion

        self.showBar = QtCore.SIGNAL("signal")
        self.ProgressBarUpdate = QtCore.SIGNAL("signal")

    def run(self):
        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        text = open(self.path).readlines()

        self.emit(self.showBar, True)
        gesamt = len(text)
        zeile = 0

        #self.parent.setProgressBarVisible(True)

        print "bis hier ist es schnell"

        for lines in text:
            zeile += 1
            voks = lines.split("\t")
            if not voks[0] == "\n":
                #print str(voks[0]).decode('utf-8').replace(u'\ufeff', "")
                fremd = str(voks[0]).decode('utf-8').replace(u'\ufeff', "")


                statement = "insert into vokabeln ('deutsch', fremd, idlektion) values ('"+str((voks[len(voks)-1]).strip('\n')).decode('utf-8')+"', " \
                            "'"+fremd+"', "+str(self.idLektion)+")"

                #print statement
                self.datenbank.setData(statement)
            prozent = round((zeile / gesamt)*100, 0)

            #print prozent
            self.emit(self.ProgressBarUpdate, prozent)
            #self.parent.ProgressBarUpdate(prozent)

        #self.parent.setProgressBarVisible(False)
        self.emit(self.showBar, False)
#test = ReadVoks("D:\Downloads\\tilo\jay.txt", 1)

#deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()