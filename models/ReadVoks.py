#-*- coding: utf-8 -*-
from __future__ import division
__author__ = 'JPaehr'

import models.base as Datenbank
from PyQt4 import QtGui
import codecs


class ReadVoks(object):

    def __init__(self, parent, path, IdLektion):
        self.path = path
        self.parent = parent
        self.idLektion = IdLektion

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        text = open(self.path).readlines()

        gesamt = len(text)
        zeile = 0

        self.parent.setProgressBarVisible(True)

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
            self.parent.ProgressBarUpdate(prozent)

        self.parent.setProgressBarVisible(False)

#test = ReadVoks("D:\Downloads\\tilo\jay.txt", 1)

#deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()