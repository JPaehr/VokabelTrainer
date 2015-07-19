# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowDrawQuery import Ui_MainWindow
import models.base as Datenbank
import threading
from math import sqrt
from models.DrawFadeInThread import DrawFadeIn
from time import sleep
from copy import deepcopy
from models.DrawThread import DrawThread


class DrawQuery(Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self, parent, vokabelId):
        super(DrawQuery, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)


        self.vokabelId = vokabelId
        self.threadFinished = True

        self.fade = False
        self.originalPen = QtGui.QPen(QtGui.QColor(0, 0, 0, 0))
        self.drawedPen = QtGui.QPen(QtGui.QColor(0, 0, 0, 255))
        self.originalPen.setWidth(5)
        self.drawedPen.setWidth(5)


        self.database = Datenbank.base("Zeichen.sqlite")

        # self.setupUi(self)
        # self.initUI()
        self.drawList = []
        self.lastDrawnLine = []

        self.lock = threading.Lock()
        statement = "select x, y from punkte where idvokabel like %d" % self.vokabelId
        self.originalList = self.database.getDataAsList(statement)
        #print(self.drawList)
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
        self.drawList.append([-1, -1])

        subdraw = self.cutLists(self.drawList)
        subOriginal = self.cutLists(self.originalList)

        dummyList = self.cutLists(self.drawList)
        self.lastDrawnLine = dummyList[len(dummyList)-1]
        dummyList2 = self.cutLists(self.originalList)
        self.lastDrawnLineOriginal = dummyList2[len(dummyList)-1]

        for i in range(len(subdraw)):
            try:
                if self.listmatch(subOriginal[i], subdraw[i]):
                    self.drawList = self.insertOnPosition(self.drawList, subOriginal[i], i)
                    #print("")
                    self.fadeInThread = DrawFadeIn(self, self.lock)
                    self.fadeInThread.start()
                    self.fade = True
                else:
                    self.fade = False
                    print("zu weit weg")
            except:
                pass
        self.update()

    def mouseMoveEvent(self, args):

        x = args.pos().x()
        y = args.pos().y()

        self.drawList.append([x, y])
        self.update()

    def paintEvent(self, e):
        #print(self.drawList)
        with self.lock:
            if self.fade:
                # fade out drawed line, fade in original line from database
                pen = QtGui.QPen()
                pen.setWidth(5)

                painter = QtGui.QPainter(self)
                painter.setRenderHint(QtGui.QPainter.Antialiasing)
                painter.setPen(pen)
                #with self.lock:

                masterListToDraw = self.cutLists(self.drawList)
                #print(masterListToDraw)

                for i in range(len(masterListToDraw)-1):

                    for j in range(len(masterListToDraw[i])):
                        if j == 0:
                            previous = 0
                        else:
                            previous = j-1
                        if i == len(masterListToDraw):
                            #letzter Strich
                            painter.setPen(self.originalPen)

                        painter.drawLine(int(masterListToDraw[i][previous][0]), int(masterListToDraw[i][previous][1]),
                                         int(masterListToDraw[i][j][0]), int(masterListToDraw[i][j][1]))

                        painter.drawPoint(int(masterListToDraw[i][j][0]), int(masterListToDraw[i][j][1]))


                #print last drawn line
                painter.setPen(self.drawedPen)
                #with self.lock:
                for i in range(len(self.lastDrawnLine)):
                    if i == 0:
                        previous = 0
                    else:
                        previous = i-1
                    if int(self.lastDrawnLine[previous][0]) == -1 or int(self.lastDrawnLine[previous][1]) == -1 or int(self.lastDrawnLine[i][0]) == -1:
                        #stift abgesetzt
                        pass
                    else:
                        painter.drawLine(int(self.lastDrawnLine[previous][0]), int(self.lastDrawnLine[previous][1]),
                                         int(self.lastDrawnLine[i][0]), int(self.lastDrawnLine[i][1]))

                        painter.drawPoint(int(self.lastDrawnLine[i][0]), int(self.lastDrawnLine[i][1]))

                #print original from last drawn line
                painter.setPen(self.originalPen)
                #with self.lock:
                for i in range(len(self.lastDrawnLineOriginal)):
                    if i == 0:
                        previous = 0
                    else:
                        previous = i-1
                    if int(self.lastDrawnLineOriginal[previous][0]) == -1 or int(self.lastDrawnLineOriginal[previous][1]) == -1 or int(self.lastDrawnLineOriginal[i][0]) == -1:
                        #stift abgesetzt
                        pass
                    else:
                        painter.drawLine(int(self.lastDrawnLineOriginal[previous][0]), int(self.lastDrawnLineOriginal[previous][1]),
                                         int(self.lastDrawnLineOriginal[i][0]), int(self.lastDrawnLineOriginal[i][1]))

                        painter.drawPoint(int(self.lastDrawnLineOriginal[i][0]), int(self.lastDrawnLineOriginal[i][1]))

            else: #kein fadein
                pen = QtGui.QPen()
                pen.setWidth(5)

                painter = QtGui.QPainter(self)
                painter.setRenderHint(QtGui.QPainter.Antialiasing)
                painter.setPen(pen)
                #with self.lock:
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


    def listmatch(self, listOrg, listDraw):
        match = True
        for draw in listDraw:
            newPoint = True
            pointMatch = False
            for orig in listOrg:
                if sqrt((draw[0]-orig[0])**2 + (draw[1]-orig[1])**2) <= 34 and newPoint:
                    pointMatch = True
                    break
            if pointMatch == False:
                match = False
                break
        firstPoint = listDraw[0]
        lastPoint = listDraw[len(listDraw)-1]

        pointMatch = False
        newPoint = True
        for i in range(len(listOrg)/5):
            if sqrt((firstPoint[0]-listOrg[i][0])**2 + (firstPoint[1]-listOrg[i][1])**2) <= 34 and newPoint:
                pointMatch = True
                break
        if pointMatch == False:
            match = False

        pointMatch = False
        newPoint = True
        for i in range(len(listOrg)-len(listOrg)/5, len(listOrg)):
            if sqrt((lastPoint[0]-listOrg[i][0])**2 + (lastPoint[1]-listOrg[i][1])**2) <= 34 and newPoint:
                pointMatch = True
                break
        if pointMatch == False:
            match = False

        return match

    def cutLists(self, liste):
        listToReturn = list()

        sublist = list()
        for i in liste:
            if not i[0] == -1 and not i[1] == -1:
                sublist.append(i)
            else:
                listToReturn.append(sublist)
                sublist = []

        return listToReturn

    def insertOnPosition(self, liste, listToInsert, pos):
        sublists = self.cutLists(liste)

        listToReturn = list()
        for i in range(len(sublists)):
            if i == pos:
                for add in listToInsert:
                    listToReturn.append(add)
            else:
                for add in sublists[i]:
                    listToReturn.append(add)

            listToReturn.append([-1, -1])
        return listToReturn