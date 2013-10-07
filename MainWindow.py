# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\MainWindow.ui'
#
# Created: Thu Sep 26 21:29:39 2013
#      by: PyQt4 UI code generator 4.10.3
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 40, 87, 83))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnAbfrageStarten = QtGui.QPushButton(self.layoutWidget)
        self.btnAbfrageStarten.setObjectName(_fromUtf8("btnAbfrageStarten"))
        self.verticalLayout_2.addWidget(self.btnAbfrageStarten)
        self.btnZuruecksetzen = QtGui.QPushButton(self.layoutWidget)
        self.btnZuruecksetzen.setObjectName(_fromUtf8("btnZuruecksetzen"))
        self.verticalLayout_2.addWidget(self.btnZuruecksetzen)
        self.btnWoerterbuch = QtGui.QPushButton(self.layoutWidget)
        self.btnWoerterbuch.setObjectName(_fromUtf8("btnWoerterbuch"))
        self.verticalLayout_2.addWidget(self.btnWoerterbuch)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(41, 21, 127, 112))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnNeueSprache = QtGui.QPushButton(self.layoutWidget1)
        self.btnNeueSprache.setObjectName(_fromUtf8("btnNeueSprache"))
        self.verticalLayout.addWidget(self.btnNeueSprache)
        self.btnNeuesBuch = QtGui.QPushButton(self.layoutWidget1)
        self.btnNeuesBuch.setObjectName(_fromUtf8("btnNeuesBuch"))
        self.verticalLayout.addWidget(self.btnNeuesBuch)
        self.btnNeueLektion = QtGui.QPushButton(self.layoutWidget1)
        self.btnNeueLektion.setObjectName(_fromUtf8("btnNeueLektion"))
        self.verticalLayout.addWidget(self.btnNeueLektion)
        self.btnNeueVok = QtGui.QPushButton(self.layoutWidget1)
        self.btnNeueVok.setObjectName(_fromUtf8("btnNeueVok"))
        self.verticalLayout.addWidget(self.btnNeueVok)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(490, 32, 111, 83))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnSpracheBeareiten = QtGui.QPushButton(self.layoutWidget2)
        self.btnSpracheBeareiten.setObjectName(_fromUtf8("btnSpracheBeareiten"))
        self.verticalLayout_3.addWidget(self.btnSpracheBeareiten)
        self.btnLektionbearbeiten = QtGui.QPushButton(self.layoutWidget2)
        self.btnLektionbearbeiten.setObjectName(_fromUtf8("btnLektionbearbeiten"))
        self.verticalLayout_3.addWidget(self.btnLektionbearbeiten)
        self.btnBuecherBearbeiten = QtGui.QPushButton(self.layoutWidget2)
        self.btnBuecherBearbeiten.setObjectName(_fromUtf8("btnBuecherBearbeiten"))
        self.verticalLayout_3.addWidget(self.btnBuecherBearbeiten)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDateu = QtGui.QMenu(self.menubar)
        self.menuDateu.setObjectName(_fromUtf8("menuDateu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDateu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnAbfrageStarten.setText(_translate("MainWindow", "Abfrage starten", None))
        self.btnZuruecksetzen.setText(_translate("MainWindow", "Zurücksetzen", None))
        self.btnWoerterbuch.setText(_translate("MainWindow", "Wörterbuch", None))
        self.btnNeueSprache.setText(_translate("MainWindow", "Neue Sprache anlegen", None))
        self.btnNeuesBuch.setText(_translate("MainWindow", "Neues Buch anlegen", None))
        self.btnNeueLektion.setText(_translate("MainWindow", "Neue Lektion anlegen", None))
        self.btnNeueVok.setText(_translate("MainWindow", "Neue Vokabeln eingeben", None))
        self.btnSpracheBeareiten.setText(_translate("MainWindow", "Sprachen bearbeiten", None))
        self.btnLektionbearbeiten.setText(_translate("MainWindow", "Lektionen bearbeiten", None))
        self.btnBuecherBearbeiten.setText(_translate("MainWindow", "Bücher bearbeiten", None))
        self.menuDateu.setTitle(_translate("MainWindow", "Datei", None))

