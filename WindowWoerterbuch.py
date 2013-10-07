# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowWoerterbuch.ui'
#
# Created: Fri Sep 27 19:26:55 2013
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
        Form.resize(821, 482)
        self.tVWoerterbuch = QtGui.QTableView(Form)
        self.tVWoerterbuch.setGeometry(QtCore.QRect(20, 90, 781, 331))
        self.tVWoerterbuch.setObjectName(_fromUtf8("tVWoerterbuch"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 171, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 20, 261, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setGeometry(QtCore.QRect(30, 20, 221, 22))
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.chBBuch = QtGui.QCheckBox(self.groupBox_2)
        self.chBBuch.setGeometry(QtCore.QRect(10, 20, 16, 17))
        self.chBBuch.setText(_fromUtf8(""))
        self.chBBuch.setObjectName(_fromUtf8("chBBuch"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 20, 331, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tfSuche = QtGui.QLineEdit(self.groupBox_3)
        self.tfSuche.setGeometry(QtCore.QRect(10, 20, 311, 20))
        self.tfSuche.setObjectName(_fromUtf8("tfSuche"))
        self.btnBearbeiten = QtGui.QPushButton(Form)
        self.btnBearbeiten.setGeometry(QtCore.QRect(710, 440, 75, 23))
        self.btnBearbeiten.setObjectName(_fromUtf8("btnBearbeiten"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cBSprache, self.chBBuch)
        Form.setTabOrder(self.chBBuch, self.cBBuch)
        Form.setTabOrder(self.cBBuch, self.tfSuche)
        Form.setTabOrder(self.tfSuche, self.tVWoerterbuch)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Wörterbuch", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_2.setTitle(_translate("Form", "Buch", None))
        self.groupBox_3.setTitle(_translate("Form", "Suche", None))
        self.btnBearbeiten.setText(_translate("Form", "Bearbeiten", None))

