__author__ = 'JPaehr'
from copy import deepcopy
from threading import Thread
from time import sleep

class DrawThread(Thread):
    def __init__(self, parent, lock):
        Thread.__init__(self)
        self.parent = parent
        self.simulationRunning = True
        self.lock = lock

    def run(self):

        sleepTime = 0.7


        zaehler = len(self.parent.drawList)
        with self.lock:
            self.parent.saveDrawList = deepcopy(self.parent.drawList)
        lenList = len(self.parent.saveDrawList)
        while self.simulationRunning:
            #print("thread rennt")
            if zaehler == 1:
                break

            #self.drawList = []
            with self.lock:
                self.parent.drawList = []
                for i in range(len(self.parent.saveDrawList)-zaehler+2):
                    try:
                        self.parent.drawList.append([self.parent.saveDrawList[i][0], self.parent.saveDrawList[i][1]])
                    except:
                        pass

            self.parent.update()

            sleep(0.006)
            zaehler -= 1

            if lenList == len(self.parent.drawList):
                self.simulationRunning = False
                print("breaking")
                break
        self.parent.drawList = deepcopy(self.parent.saveDrawList)
        self.parent.threadFinished = True
        self.parent.update()
        self.parent.pBSimulate.setText(self.parent.simulationText)

    def stop(self):
        self.simulationRunning = False