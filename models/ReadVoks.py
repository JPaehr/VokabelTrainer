#-*- coding: utf-8 -*-
__author__ = 'JPaehr'

import models.base as Datenbank
from PyQt4 import QtGui
import codecs


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
                #print str(voks[0]).decode('utf-8').replace(u'\ufeff', "")
                fremd = str(voks[0]).decode('utf-8').replace(u'\ufeff', "")


                statement = "insert into vokabeln ('deutsch', fremd, idlektion) values ('"+str((voks[len(voks)-1]).strip('\n')).decode('utf-8')+"', " \
                            "'"+fremd+"', "+str(self.idLektion)+")"

                #print statement
                self.datenbank.setData(statement)

#test = ReadVoks("D:\Downloads\\tilo\jay.txt", 1)

#deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()