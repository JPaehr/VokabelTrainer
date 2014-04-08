__author__ = 'JPaehr'

import threading
import time
import models.base as Datenbank

class Zeiten(threading.Thread):

    def __init__(self, widgetToUpdate=""):
        threading.Thread.__init__(self)
        self.widgetToUpdate = widgetToUpdate
        self.zeit = 0 #in seconds
        self.widgetToUpdate.setText("00:00:00, verbleibende Zeit: 00:00:00")
        self.remainVoks = 5
        self.remainTime = ""

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.zeit10Vok = self.datenbank.getDataAsList("select secPro10Vok from zeit")[0][0]

        self.killFlag = False

    def run(self):
        while not self.killFlag:

            self.zeit += 1
            restZeit = self.remainVoks * self.zeit10Vok / 10
            self.remainTime = ", verbleibende Zeit: " +str(self.zeitRechner(restZeit))

            time.sleep(1)
            self.widgetToUpdate.setText(self.zeitRechner(self.zeit)+str(self.remainTime))

    def zeitRechner(self, inSekunden):
        stunden, rest = divmod(inSekunden, 3600)
        minuten, rest = divmod(rest, 60)
        sekunden = rest

        if stunden <= 9:
            stunden = "0"+str(int(stunden))
        else:
            stunden = int(stunden)

        if minuten <= 9:
            minuten = "0"+str(int(minuten))
        else:
            minuten = int(minuten)

        if sekunden <= 9:
            sekunden = "0"+str(int(sekunden))
        else:
            sekunden = int(sekunden)
        #print str(stunden)+":"+str(minuten)+":"+str(sekunden)
        return str((stunden))+":"+str((minuten))+":"+str((sekunden))

    def setRemainVok(self, remainVoks):
        self.remainVoks = remainVoks
    def getTimeInSeconds(self):
        return self.zeit
    def setTimeInSecouds(self, time):
        self.zeit = time
    def killThread(self):
        self.killFlag = True