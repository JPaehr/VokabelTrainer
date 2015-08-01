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
from models.CharModel import Char


class Draw(Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self, parent, vokabelId):
        super(Draw, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.connect(self.pBLoeschen, QtCore.SIGNAL("clicked()"), self.delCanvas)
        self.connect(self.pBSave, QtCore.SIGNAL("clicked()"), self.save)
        self.connect(self.pBSimulate, QtCore.SIGNAL("clicked()"), self.simulate)

        self.vokabelId = vokabelId
        self.threadFinished = True
        self.simulationText = self.pBSimulate.text()

        self.database = Datenbank.base("Zeichen.sqlite")

        self.ctr = 0
        self.lock = threading.Lock()
        statement = "select x, y from punkte where idvokabel like %d" % self.vokabelId

        data = self.database.getDataAsList(statement)
        self.drawObj = Char()
        self.drawObj.setData(data)
        self.simulationRunning = False

        self.mousePressed = False
        self.update()

    def simulate(self):

        if self.simulationRunning:
            self.pBSimulate.setText(self.simulationText)
            self.simulation.stop()
            self.simulationRunning = False
            self.update()
        else:
            self.simulation = DrawThread(self.lock, self.drawObj.getNumberOfItems(), self)
            self.simulationRunning = True
            self.newestSegment = 1
            self.simulation.start()
            self.pBSimulate.setText("simulation stoppen")

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
        self.drawObj.delData()
        self.update()

    def initUI(self):

        self.setGeometry(50, 50, 1000, 1000)
        self.setWindowTitle('Points')
        self.show()

    def mousePressEvent(self, event):

        pass

    def mouseReleaseEvent(self, e):
        self.mousePressed = False

    def mouseMoveEvent(self, args):

        x = args.pos().x()
        y = args.pos().y()
        xOffset = self.drawWidget.pos().x()
        yOffset = self.drawWidget.pos().y()

        if self.mousePressed == False:
            self.drawObj.appendItemToNewSegment([-xOffset+x, -yOffset+y])
            self.mousePressed = True
        else:
            self.drawObj.appendItemToLastSegment([-xOffset+x, -yOffset+y])
        self.update()


    def paintEvent(self, e):

        xOffset = self.drawWidget.pos().x()
        yOffset = self.drawWidget.pos().y()


        #draw grid
        pen = QtGui.QPen()
        pen.setWidth(1)

        painterGrid = QtGui.QPainter(self)
        painterGrid.setRenderHint(QtGui.QPainter.Antialiasing)
        painterGrid.setPen(pen)
        width = self.drawWidget.width()
        height = self.drawWidget.height()

        horizontalLines = 4
        verticalLines = 4
        for i in range(verticalLines):
            painterGrid.drawLine(xOffset+width/(verticalLines+1)*(i+1), yOffset, xOffset+width/(verticalLines+1)*(i+1), yOffset+height)

        for i in range(horizontalLines):
            painterGrid.drawLine(xOffset, yOffset+height/(horizontalLines+1)*(i+1), xOffset+width, yOffset+height/(horizontalLines+1)*(i+1))

        if not self.simulationRunning:
            pen = QtGui.QPen()
            pen.setWidth(5)

            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(pen)


            xScale = float(self.drawWidget.width()) / 300
            yScale = float(self.drawWidget.height()) / 300


            previous = [-1, -1]
            for segment in self.drawObj.getSegments():
                for item in segment:
                    if previous[0] == -1:
                        previous[0] = item[0]
                        previous[1] = item[1]

                    painter.drawLine(xOffset + previous[0]*xScale, yOffset + previous[1]*yScale, xOffset + item[0]*xScale, yOffset + item[1]*yScale)
                    previous[0] = item[0]
                    previous[1] = item[1]

                previous[0] = -1
                previous[1] = -1
        else:

            pen = QtGui.QPen()
            pen.setWidth(5)

            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(pen)


            xScale = float(self.drawWidget.width()) / 300
            yScale = float(self.drawWidget.height()) / 300

            previous = [-1, -1]
            localctr = 0
            bigbrake = False

            segcounter = 0


            for segment in self.drawObj.getSegments():
                segcounter += 1
                if bigbrake:
                    break
                for item in segment:
                    with self.lock:
                        if localctr < self.ctr:
                            if previous[0] == -1:
                                previous[0] = item[0]
                                previous[1] = item[1]
                            if self.newestSegment == segcounter:
                                pen = QtGui.QPen()
                                pen.setWidth(5)
                                pen.setColor(QtGui.QColor(26, 132, 57, 157))

                                painter.setPen(pen)

                            painter.drawLine(xOffset + previous[0]*xScale, yOffset + previous[1]*yScale, xOffset + item[0]*xScale, yOffset + item[1]*yScale)
                            previous[0] = item[0]
                            previous[1] = item[1]
                            localctr += 1
                        else:
                            bigbrake = True
                            break
                if segcounter > self.newestSegment:
                    self.newestSegment = segcounter
                previous[0] = -1
                previous[1] = -1
