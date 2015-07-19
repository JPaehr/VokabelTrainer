# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowDraw.ui'
#
# Created: Thu Jul 16 20:58:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(318, 390)
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(300, 300))
        self.widget.setMaximumSize(QtCore.QSize(700, 700))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pBLoeschen = QtGui.QPushButton(self.centralwidget)
        self.pBLoeschen.setObjectName(_fromUtf8("pBLoeschen"))
        self.horizontalLayout.addWidget(self.pBLoeschen)
        self.pBSimulate = QtGui.QPushButton(self.centralwidget)
        self.pBSimulate.setObjectName(_fromUtf8("pBSimulate"))
        self.horizontalLayout.addWidget(self.pBSimulate)
        self.pBSave = QtGui.QPushButton(self.centralwidget)
        self.pBSave.setObjectName(_fromUtf8("pBSave"))
        self.horizontalLayout.addWidget(self.pBSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Zeichnen", None))
        self.pBLoeschen.setText(_translate("MainWindow", "löschen", None))
        self.pBSimulate.setText(_translate("MainWindow", "simulieren", None))
        self.pBSave.setText(_translate("MainWindow", "speichern", None))

