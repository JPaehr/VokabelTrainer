# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowBuchAnlegen.ui'
#
# Created: Thu Sep 26 20:24:05 2013
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
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 371, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setGeometry(QtCore.QRect(10, 30, 351, 22))
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 371, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tfBuchtitel = QtGui.QLineEdit(self.groupBox_2)
        self.tfBuchtitel.setGeometry(QtCore.QRect(10, 30, 351, 20))
        self.tfBuchtitel.setObjectName(_fromUtf8("tfBuchtitel"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 250, 371, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(self.layoutWidget)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnAnlegen = QtGui.QPushButton(self.layoutWidget)
        self.btnAnlegen.setObjectName(_fromUtf8("btnAnlegen"))
        self.horizontalLayout.addWidget(self.btnAnlegen)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Neues Buch anlegen", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_2.setTitle(_translate("Form", "Buchtitel", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnAnlegen.setText(_translate("Form", "Anlegen", None))

