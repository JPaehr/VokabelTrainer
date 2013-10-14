# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowLektionAnlegen.ui'
#
# Created: Mon Oct 14 23:08:47 2013
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(LektionAnlegen)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(LektionAnlegen)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(LektionAnlegen)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.verticalLayout_3.addWidget(self.cBSprache)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(LektionAnlegen)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.verticalLayout_4.addWidget(self.cBBuch)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(LektionAnlegen)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tfLektion = QtGui.QLineEdit(self.groupBox_3)
        self.tfLektion.setObjectName(_fromUtf8("tfLektion"))
        self.verticalLayout_5.addWidget(self.tfLektion)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechn = QtGui.QPushButton(LektionAnlegen)
        self.btnAbbrechn.setObjectName(_fromUtf8("btnAbbrechn"))
        self.horizontalLayout.addWidget(self.btnAbbrechn)
        self.btnAnwenden = QtGui.QPushButton(LektionAnlegen)
        self.btnAnwenden.setObjectName(_fromUtf8("btnAnwenden"))
        self.horizontalLayout.addWidget(self.btnAnwenden)
        self.btnAnwendenSchliessen = QtGui.QPushButton(LektionAnlegen)
        self.btnAnwendenSchliessen.setObjectName(_fromUtf8("btnAnwendenSchliessen"))
        self.horizontalLayout.addWidget(self.btnAnwendenSchliessen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

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

