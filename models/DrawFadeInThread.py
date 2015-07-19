__author__ = 'JPaehr'
from copy import deepcopy
from threading import Thread
from time import sleep
from PyQt4 import QtGui


class DrawFadeIn(Thread):
    def __init__(self, parent, lock):
        Thread.__init__(self)
        self.parent = parent

        self.lock = lock
        self.stop = False
        self.fadeTime = 0.5
        self.sleepTime = self.fadeTime/128


    def run(self):
        ctr = 0
        while not self.stop:
            if ctr < 128:
                self.parent.update()
                with self.lock:
                    self.parent.originalPen = QtGui.QPen(QtGui.QColor(0, 0, 0, ctr))
                    self.parent.drawedPen = QtGui.QPen(QtGui.QColor(0, 0, 0, 128-ctr))
                    self.parent.originalPen.setWidth(5)
                    self.parent.drawedPen.setWidth(5)
                sleep(self.sleepTime)
                ctr += 1
            else:
                self.parent.fade = False
                break

