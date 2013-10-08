# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowLektionAnlegen.ui'
#
# Created: Thu Sep 26 20:15:52 2013
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

class Ui_LektionAnlegen(object):
    def setupUi(self, LektionAnlegen):
        LektionAnlegen.setObjectName(_fromUtf8("LektionAnlegen"))
        LektionAnlegen.resize(400, 300)
        self.label = QtGui.QLabel(LektionAnlegen)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(LektionAnlegen)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 371, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setGeometry(QtCore.QRect(20, 20, 341, 22))
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.groupBox_2 = QtGui.QGroupBox(LektionAnlegen)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 371, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setGeometry(QtCore.QRect(20, 20, 341, 22))
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.groupBox_3 = QtGui.QGroupBox(LektionAnlegen)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 190, 371, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tfLektion = QtGui.QLineEdit(self.groupBox_3)
        self.tfLektion.setGeometry(QtCore.QRect(20, 20, 341, 20))
        self.tfLektion.setObjectName(_fromUtf8("tfLektion"))
        self.widget = QtGui.QWidget(LektionAnlegen)
        self.widget.setGeometry(QtCore.QRect(10, 250, 371, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechn = QtGui.QPushButton(self.widget)
        self.btnAbbrechn.setObjectName(_fromUtf8("btnAbbrechn"))
        self.horizontalLayout.addWidget(self.btnAbbrechn)
        self.btnAnwenden = QtGui.QPushButton(self.widget)
        self.btnAnwenden.setObjectName(_fromUtf8("btnAnwenden"))
        self.horizontalLayout.addWidget(self.btnAnwenden)
        self.btnAnwendenSchliessen = QtGui.QPushButton(self.widget)
        self.btnAnwendenSchliessen.setObjectName(_fromUtf8("btnAnwendenSchliessen"))
        self.horizontalLayout.addWidget(self.btnAnwendenSchliessen)

        self.retranslateUi(LektionAnlegen)
        QtCore.QMetaObject.connectSlotsByName(LektionAnlegen)
        LektionAnlegen.setTabOrder(self.cBSprache, self.cBBuch)
        LektionAnlegen.setTabOrder(self.cBBuch, self.tfLektion)
        LektionAnlegen.setTabOrder(self.tfLektion, self.btnAnwenden)
        LektionAnlegen.setTabOrder(self.btnAnwenden, self.btnAnwendenSchliessen)
        LektionAnlegen.setTabOrder(self.btnAnwendenSchliessen, self.btnAbbrechn)

    def retranslateUi(self, LektionAnlegen):
        LektionAnlegen.setWindowTitle(_translate("LektionAnlegen", "Lektion Anlegen", None))
        self.label.setText(_translate("LektionAnlegen", "Lektion anlegen", None))
        self.groupBox.setTitle(_translate("LektionAnlegen", "Sprache", None))
        self.groupBox_2.setTitle(_translate("LektionAnlegen", "Buch", None))
        self.groupBox_3.setTitle(_translate("LektionAnlegen", "Lektion", None))
        self.btnAbbrechn.setText(_translate("LektionAnlegen", "Abbrechen", None))
        self.btnAnwenden.setText(_translate("LektionAnlegen", "Anwenden", None))
        self.btnAnwendenSchliessen.setText(_translate("LektionAnlegen", "Anwenden und Schließen", None))

