#-*- coding: utf-8 -*-
__author__ = 'JPaehr'

import models.base as Datenbank
from PyQt4 import QtGui


class ReadVoks(object):

    def __init__(self, path, IdLektion):
        self.path = path
        self.idLektion = IdLektion

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        text = open(self.path).readlines()

        #test = QtGui.QMessageBox()

        for lines in text:
            voks = lines.split("\t")
            if not voks[0] == "\n":

                statement = "insert into vokabeln ('deutsch', fremd, idlektion) values ('"+str((voks[len(voks)-1]).strip('\n')).decode('utf-8')+"', " \
                            "'"+str(voks[0]).decode('utf-8')+"', "+str(self.idLektion)+")"
                #print statement
                self.datenbank.setData(statement)

                #print voks[0].strip("\n"), voks[len(voks)-1].strip("\n")


#deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()