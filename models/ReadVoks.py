#-*- coding: utf-8 -*-
from __future__ import division
__author__ = 'JPaehr'

import models.base as Datenbank
from PyQt4 import QtGui, QtCore
import models.tsvReader as Reader


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

        model = Reader.tsvReader(self.path)
        vokList = model.getList()
        zeile = 0
        gesamt = len(vokList)
        for i in vokList:
            zeile += 1
            fremd = i[0]
            deutsch = i[1]
            statement = "insert into vokabeln ('deutsch', fremd, idlektion) values ('"+deutsch+"', " \
                            "'"+fremd+"', "+str(self.idLektion)+")"

            self.datenbank.setDataWithoutCommit(statement)
            prozent = round((zeile / gesamt)*100, 0)
            self.emit(self.ProgressBarUpdate, prozent)
        self.datenbank.commit()
        self.emit(self.showBar, False)

        """
        text = open(self.path).readlines()

        ##self.emit(self.showBar, True)
        gesamt = len(text)
        zeile = 0

        for lines in text:
            zeile += 1
            voks = lines.split("\t")
            #print voks,
            if not voks[0] == "\n":
                #print voks,
                #print str(voks[0]).decode('utf-8').replace(u'\ufeff', "")
                fremd = str(voks[0]).decode('utf-8').replace(u'\ufeff', "")

                for i in range(1, len(voks)):
                    print "sch"
                    print voks
                    if str((voks[len(voks)-i]).strip('\n')).decode('utf-8') == '':
                        print "continued"
                        continue

                    deutsch = str((voks[len(voks)-i]).strip('\n')).decode('utf-8')
                    print deutsch

                statement = "insert into vokabeln ('deutsch', fremd, idlektion) values ('"+deutsch+"', " \
                            "'"+fremd+"', "+str(self.idLektion)+")"

                #print zeile, statement
                self.datenbank.setDataWithoutCommit(statement)
            prozent = round((zeile / gesamt)*100, 0)

            #print prozent
            self.emit(self.ProgressBarUpdate, prozent)
            #self.parent.ProgressBarUpdate(prozent)
        self.datenbank.commit()
        #self.parent.setProgressBarVisible(False)
        self.emit(self.showBar, False)
        """
#test = ReadVoks('', "D:/Mackenbekaempfung29.0.2014/testlade.txt", 1)
#test.run()
#deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()