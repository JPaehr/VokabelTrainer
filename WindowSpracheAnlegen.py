# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowSpracheAnlegen.ui'
#
# Created: Thu Sep 26 20:24:46 2013
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
        self.label.setGeometry(QtCore.QRect(10, 20, 108, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 371, 65))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tfNeueSprache = QtGui.QLineEdit(self.groupBox)
        self.tfNeueSprache.setGeometry(QtCore.QRect(10, 30, 351, 20))
        self.tfNeueSprache.setObjectName(_fromUtf8("tfNeueSprache"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 250, 371, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(self.widget)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnAnlegen = QtGui.QPushButton(self.widget)
        self.btnAnlegen.setObjectName(_fromUtf8("btnAnlegen"))
        self.horizontalLayout.addWidget(self.btnAnlegen)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Neue Sprache anlegen", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnAnlegen.setText(_translate("Form", "Anlegen", None))

