# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\MainWindow.ui'
#
# Created: Sat Mar 22 23:06:12 2014
#      by: PyQt4 UI code generator 4.9.6
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
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnNeueSprache = QtGui.QPushButton(self.centralwidget)
        self.btnNeueSprache.setObjectName(_fromUtf8("btnNeueSprache"))
        self.verticalLayout.addWidget(self.btnNeueSprache)
        self.btnNeuesBuch = QtGui.QPushButton(self.centralwidget)
        self.btnNeuesBuch.setObjectName(_fromUtf8("btnNeuesBuch"))
        self.verticalLayout.addWidget(self.btnNeuesBuch)
        self.btnNeueLektion = QtGui.QPushButton(self.centralwidget)
        self.btnNeueLektion.setObjectName(_fromUtf8("btnNeueLektion"))
        self.verticalLayout.addWidget(self.btnNeueLektion)
        self.btnNeueVok = QtGui.QPushButton(self.centralwidget)
        self.btnNeueVok.setObjectName(_fromUtf8("btnNeueVok"))
        self.verticalLayout.addWidget(self.btnNeueVok)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnFortsetzen = QtGui.QPushButton(self.centralwidget)
        self.btnFortsetzen.setObjectName(_fromUtf8("btnFortsetzen"))
        self.verticalLayout_2.addWidget(self.btnFortsetzen)
        self.btnAbfrageStarten = QtGui.QPushButton(self.centralwidget)
        self.btnAbfrageStarten.setObjectName(_fromUtf8("btnAbfrageStarten"))
        self.verticalLayout_2.addWidget(self.btnAbfrageStarten)
        self.btnZuruecksetzen = QtGui.QPushButton(self.centralwidget)
        self.btnZuruecksetzen.setObjectName(_fromUtf8("btnZuruecksetzen"))
        self.verticalLayout_2.addWidget(self.btnZuruecksetzen)
        self.btnWoerterbuch = QtGui.QPushButton(self.centralwidget)
        self.btnWoerterbuch.setObjectName(_fromUtf8("btnWoerterbuch"))
        self.verticalLayout_2.addWidget(self.btnWoerterbuch)
        self.btnStatistik = QtGui.QPushButton(self.centralwidget)
        self.btnStatistik.setObjectName(_fromUtf8("btnStatistik"))
        self.verticalLayout_2.addWidget(self.btnStatistik)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnSpracheBeareiten = QtGui.QPushButton(self.centralwidget)
        self.btnSpracheBeareiten.setObjectName(_fromUtf8("btnSpracheBeareiten"))
        self.verticalLayout_3.addWidget(self.btnSpracheBeareiten)
        self.btnLektionbearbeiten = QtGui.QPushButton(self.centralwidget)
        self.btnLektionbearbeiten.setObjectName(_fromUtf8("btnLektionbearbeiten"))
        self.verticalLayout_3.addWidget(self.btnLektionbearbeiten)
        self.btnBuecherBearbeiten = QtGui.QPushButton(self.centralwidget)
        self.btnBuecherBearbeiten.setObjectName(_fromUtf8("btnBuecherBearbeiten"))
        self.verticalLayout_3.addWidget(self.btnBuecherBearbeiten)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_3.addWidget(self.widget_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
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
        self.actionStatistik = QtGui.QAction(MainWindow)
        self.actionStatistik.setObjectName(_fromUtf8("actionStatistik"))
        self.menubar.addAction(self.menuDateu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnNeueSprache.setText(_translate("MainWindow", "Neue Sprache anlegen", None))
        self.btnNeuesBuch.setText(_translate("MainWindow", "Neues Buch anlegen", None))
        self.btnNeueLektion.setText(_translate("MainWindow", "Neue Lektion anlegen", None))
        self.btnNeueVok.setText(_translate("MainWindow", "Neue Vokabeln eingeben", None))
        self.btnFortsetzen.setText(_translate("MainWindow", "letzte Abfrage fortsetzen", None))
        self.btnAbfrageStarten.setText(_translate("MainWindow", "Abfrage starten", None))
        self.btnZuruecksetzen.setText(_translate("MainWindow", "Zurücksetzen", None))
        self.btnWoerterbuch.setText(_translate("MainWindow", "Wörterbuch", None))
        self.btnStatistik.setText(_translate("MainWindow", "Statistik", None))
        self.btnSpracheBeareiten.setText(_translate("MainWindow", "Sprachen bearbeiten", None))
        self.btnLektionbearbeiten.setText(_translate("MainWindow", "Lektionen bearbeiten", None))
        self.btnBuecherBearbeiten.setText(_translate("MainWindow", "Bücher bearbeiten", None))
        self.menuDateu.setTitle(_translate("MainWindow", "Datei", None))
        self.actionStatistik.setText(_translate("MainWindow", "Statistik", None))

