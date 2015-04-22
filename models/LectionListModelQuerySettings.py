'''
Created on 03.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QBrush, QColor
import datetime


class Markierung(QtCore.QAbstractTableModel):

    def __init__(self, data, datesList, parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        
        self.datesList = datesList
        self.data = data


    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return 1
        
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.data[index.row()]
        if role == QtCore.Qt.BackgroundRole:

            if self.datesList[index.row()] == None or self.datesList[index.row()] == '':
                #red
                return QBrush(QColor(255, 0, 0, 157))

            date = self.datesList[index.row()].split('-')

            t = datetime.datetime.now()-datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

            if t.days <= 7:
                #green
                return QBrush(QColor(0, 255, 0, 127))

            if t.days <= 30:
                #yellow
                return QBrush(QColor(233, 200, 0, 157))

            if t.days > 30:
                #red
                return QBrush(QColor(255, 0, 0, 157))

            if role == QtCore.Qt.CheckStateRole:
                return 0
            if role == QtCore.Qt.ItemIsUserCheckable:
                return 0

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            self.data[index.row()] = value

    def flags(self, index):
        
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled



    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                
                if section < len(self.header):
                    return self.header[section]
                else:
                    return "not implemented"  
    