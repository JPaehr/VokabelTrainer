from PyQt4 import QtCore
from PyQt4.uic.Compiler.qtproxies import QtGui

class ModelListe(QtCore.QAbstractTableModel):
    def __init__(self, daten = [[]], headers = [],  parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__daten = daten
        self.__headers = headers
    def rowCount(self, parent):
        return len(self.__daten)
    def columnCount(self, parent):
        return len(self.__daten[0])
    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            return self.__daten[index.row()][index.column()]

        if role == QtCore.Qt.DisplayRole:

            return self.__daten[index.row()][index.column()]
        if role == QtCore.Qt.ToolTipRole:
            if len(self.__daten[index.row()][index.column()]) > 150:
                return self.__daten[index.row()][index.column()][:150]+"<br>"+ \
                       self.__daten[index.row()][index.column()][150:]
            else:
                return self.__daten[index.row()][index.column()]

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole:
            return False

        self.__daten[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def headerData(self, section, orientation, role):

        if role == QtCore.Qt.DisplayRole:

            if orientation == QtCore.Qt.Horizontal:

                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "not implemented"
