'''
Created on 03.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore

class Markierung(QtCore.QAbstractTableModel):
    

    def __init__(self, data, parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        
        
        self.data = data


    def rowCount(self, parent):
        return len(self.data)
    def columnCount(self, parent):
        return 1
        
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.data[index.row()]
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
    