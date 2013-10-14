# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowSpracheAendern.ui'
#
# Created: Mon Oct 14 22:16:59 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(382, 208)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cBSpracheAuswaehlen = QtGui.QComboBox(self.groupBox)
        self.cBSpracheAuswaehlen.setObjectName(_fromUtf8("cBSpracheAuswaehlen"))
        self.verticalLayout_3.addWidget(self.cBSpracheAuswaehlen)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tfNeuerName = QtGui.QLineEdit(self.groupBox_2)
        self.tfNeuerName.setObjectName(_fromUtf8("tfNeuerName"))
        self.verticalLayout_4.addWidget(self.tfNeuerName)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnSpeichernUndSchliessen = QtGui.QPushButton(Form)
        self.btnSpeichernUndSchliessen.setObjectName(_fromUtf8("btnSpeichernUndSchliessen"))
        self.horizontalLayout.addWidget(self.btnSpeichernUndSchliessen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sprache ändern", None))
        self.groupBox.setTitle(_translate("Form", "Sprache auswählen", None))
        self.groupBox_2.setTitle(_translate("Form", "Neuer Name", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnSpeichernUndSchliessen.setText(_translate("Form", "Speichern und Schließen", None))

