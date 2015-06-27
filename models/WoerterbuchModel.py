from PyQt4 import QtCore
from PyQt4.QtGui import QColor, QBrush
from PyQt4.uic.Compiler.qtproxies import QtGui


class ModelListe(QtCore.QAbstractTableModel):
    def __init__(self, daten=[[]], headers=[], colored=True, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        #dataformat 4 richtig, 5 falsch, 6 zuletzt
        self.__daten = daten
        self.__headers = headers
        self.colored = colored

    def rowCount(self, parent):
        return len(self.__daten)

    def columnCount(self, parent):
        if len(self.__daten) > 0:
            return 4
        else:
            return 0
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

        if self.colored:
            if role == QtCore.Qt.BackgroundRole:
                # Buecher.name [0], Lektionen.name [1], vokabeln.deutsch [2], vokabeln.fremd [3], vokabeln.richtig [4],
                # vokabeln.falsch [5], vokabeln.zuletztrichtig [6], vokabeln.id [7]

                if self.__daten[index.row()][4] > self.__daten[index.row()][5] and self.__daten[index.row()][4] >= 3 and \
                        not self.__daten[index.row()][6] == 0:
                    #green
                    return QBrush(QColor(0, 255, 0, 127))
                if self.__daten[index.row()][4] < 3:
                    #gray
                    return QBrush(QColor(129, 129, 129, 157))
                if self.__daten[index.row()][6] == 0 and self.__daten[index.row()][4] > self.__daten[index.row()][5]:
                    #yellow
                    return QBrush(QColor(233, 200, 0, 157))

                if self.__daten[index.row()][6] == 1 and self.__daten[index.row()][4] < self.__daten[index.row()][5]:
                    #orange
                    return QBrush(QColor(255, 153, 0, 200))

                if self.__daten[index.row()][6] == 0:
                    #red
                    return QBrush(QColor(255, 0, 0, 157))

                    #return self.__daten[index.row()][index.column()]
                if role == QtCore.Qt.CheckStateRole:
                    return 0
                if role == QtCore.Qt.ItemIsUserCheckable:
                    return 0

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





