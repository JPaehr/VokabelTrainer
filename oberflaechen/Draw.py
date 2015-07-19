# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowDraw import Ui_MainWindow
import models.base as Datenbank
import threading
from time import sleep
from copy import deepcopy
from models.DrawThread import DrawThread


class Draw(Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self, parent, vokabelId):
        super(Draw, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)


        #self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), QtCore.SLOT('close()'))
        self.connect(self.pBLoeschen, QtCore.SIGNAL("clicked()"), self.delCanvas)
        self.connect(self.pBSave, QtCore.SIGNAL("clicked()"), self.save)
        self.connect(self.pBSimulate, QtCore.SIGNAL("clicked()"), self.simulate)

        self.vokabelId = vokabelId
        self.threadFinished = True
        self.simulationText = self.pBSimulate.text()

        self.database = Datenbank.base("Zeichen.sqlite")

        # self.setupUi(self)
        # self.initUI()
        self.drawList = list()
        self.lock = threading.Lock()
        statement = "select x, y from punkte where idvokabel like %d" % self.vokabelId
        self.drawList = self.database.getDataAsList(statement)
        #print(self.drawList)
        self.update()


    def simulate(self):
        if self.threadFinished:

            self.threadFinished = False
            self.pBSimulate.setText("simulation stoppen")

            self.simlation = DrawThread(self, self.lock)
            self.simlation.start()
        else:
            self.pBSimulate.setText(self.simulationText)
            self.simlation.stop()

    def save(self):
        statement = "delete from punkte where idvokabel like "+str(self.vokabelId)
        self.database.setData(statement)

        with self.lock:
            for i in self.drawList:

                statement = "insert into punkte (x, y, idvokabel) values (%d, %d, %d)" % (int(i[0]), int(i[1]), int(self.vokabelId))
                #print(statement)
                self.database.setDataWithoutCommit(statement)
            self.database.commit()

    def delCanvas(self):
        self.drawList = []
        self.update()

    def initUI(self):

        self.setGeometry(50, 50, 1000, 1000)
        self.setWindowTitle('Points')
        self.show()

    def mousePressEvent(self, event):
        # print(event.pos())
        self.x = event.pos().x()
        self.y = event.pos().y()

    def mouseReleaseEvent(self, e):
        self.drawList.append(["-1", "-1"])
        #print(len(self.drawList))

    def mouseMoveEvent(self, args):

        #line = QtCore.QLine(0, 0, x2, 30)

        x = args.pos().x()
        y = args.pos().y()
        self.drawList.append([x, y])
        #print("listOrg.append([%d, %d])" % (x, y))


        self.update()
        #print(args.pos())

    def paintEvent(self, e):

        pen = QtGui.QPen()
        pen.setWidth(5)

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(pen)
        with self.lock:
            for i in range(len(self.drawList)):
                if i == 0:
                    previous = 0
                else:
                    previous = i-1
                if int(self.drawList[previous][0]) == -1 or int(self.drawList[previous][1]) == -1 or int(self.drawList[i][0]) == -1:
                    #stift abgesetzt
                    pass
                else:
                    painter.drawLine(int(self.drawList[previous][0]), int(self.drawList[previous][1]),
                                     int(self.drawList[i][0]), int(self.drawList[i][1]))

                    painter.drawPoint(int(self.drawList[i][0]), int(self.drawList[i][1]))

        # painter.setPen(QtGui.QColor(168, 34, 3))
        # painter.drawLine(20, 20, 100, 100)