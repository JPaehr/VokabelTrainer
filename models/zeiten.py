__author__ = 'JPaehr'

import threading
import time

class Zeiten(threading.Thread):

    def __init__(self, widgetToUpdate=""):
        threading.Thread.__init__(self)
        self.widgetToUpdate = widgetToUpdate
        self.zeit = 0 #in seconds
        self.widgetToUpdate.setText("00:00:00")

    def run(self):
        while True:

            time.sleep(1)
            self.zeit += 1
            self.widgetToUpdate.setText(self.zeitRechner(self.zeit))

    def zeitRechner(self, inSekunden):
        stunden, rest = divmod(inSekunden, 3600)
        minuten, rest = divmod(rest, 60)
        sekunden = rest

        if stunden < 9:
            stunden = "0"+str(stunden)

        if minuten < 9:
            minuten = "0"+str(minuten)

        if sekunden < 9:
            sekunden = "0"+str(sekunden)


        return str(stunden)+":"+str(minuten)+":"+str(sekunden)

    def getTimeInSeconds(self):
        return self.zeit
    def setTimeInSecouds(self, time):
        self.zeit = time