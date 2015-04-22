'''
Created on 03.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QBrush, QColor


class Markierung(QtCore.QAbstractTableModel):

    def __init__(self, data, parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        
        
        self.data = data


    def rowCount(self, parent):
        return 1#len(self.data)

    def columnCount(self, parent):
        return 1
        
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.data[index.row()]
        if role == QtCore.Qt.BackgroundRole:
            return QBrush(QColor(255, 0, 0, 157))
            # if self.__daten[index.row()][4] > self.__daten[index.row()][5] and self.__daten[index.row()][4] >= 3 and \
            #         not self.__daten[index.row()][6] == 0:
            #     #green
            #     return QBrush(QColor(0, 255, 0, 127))
            #
            # if self.__daten[index.row()][6] == 0:
            #     #red
            #     return QBrush(QColor(255, 0, 0, 157))
            #
            # if self.__daten[index.row()][4] < 3:
            #     #yellow
            #     return QBrush(QColor(233, 200, 0, 157))
            #     #return self.__daten[index.row()][index.column()]
            #
            # if role == QtCore.Qt.CheckStateRole:
            #     return 0
            # if role == QtCore.Qt.ItemIsUserCheckable:
            #     return 0

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
    