# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowLektionAendern.ui'
#
# Created: Thu Oct 03 13:17:56 2013
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
        Form.resize(787, 326)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 361, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cBSpracheAuswaehlen = QtGui.QComboBox(self.groupBox)
        self.cBSpracheAuswaehlen.setGeometry(QtCore.QRect(10, 20, 341, 22))
        self.cBSpracheAuswaehlen.setObjectName(_fromUtf8("cBSpracheAuswaehlen"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 160, 361, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tfNeuerName = QtGui.QLineEdit(self.groupBox_2)
        self.tfNeuerName.setGeometry(QtCore.QRect(10, 20, 341, 20))
        self.tfNeuerName.setObjectName(_fromUtf8("tfNeuerName"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 90, 361, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cbBuchAuswaehlen = QtGui.QComboBox(self.groupBox_3)
        self.cbBuchAuswaehlen.setGeometry(QtCore.QRect(10, 20, 341, 22))
        self.cbBuchAuswaehlen.setObjectName(_fromUtf8("cbBuchAuswaehlen"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 290, 361, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(self.layoutWidget)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnSpeichernUndSchliessen = QtGui.QPushButton(self.layoutWidget)
        self.btnSpeichernUndSchliessen.setObjectName(_fromUtf8("btnSpeichernUndSchliessen"))
        self.horizontalLayout.addWidget(self.btnSpeichernUndSchliessen)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 90, 361, 61))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.cbNeuesBuch = QtGui.QComboBox(self.groupBox_4)
        self.cbNeuesBuch.setGeometry(QtCore.QRect(10, 20, 341, 22))
        self.cbNeuesBuch.setObjectName(_fromUtf8("cbNeuesBuch"))
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 160, 361, 61))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.cbLektionAuswaehlen = QtGui.QComboBox(self.groupBox_5)
        self.cbLektionAuswaehlen.setGeometry(QtCore.QRect(10, 20, 341, 22))
        self.cbLektionAuswaehlen.setObjectName(_fromUtf8("cbLektionAuswaehlen"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Lektion Ändern", None))
        self.groupBox.setTitle(_translate("Form", "Sprache auswählen", None))
        self.groupBox_2.setTitle(_translate("Form", "Neuer Lektionsname", None))
        self.groupBox_3.setTitle(_translate("Form", "Buch auswählen", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnSpeichernUndSchliessen.setText(_translate("Form", "Speichern und Schließen", None))
        self.groupBox_4.setTitle(_translate("Form", "Neues Buch", None))
        self.groupBox_5.setTitle(_translate("Form", "Lektion auswählen", None))

