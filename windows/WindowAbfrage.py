# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowAbfrage.ui'
#
# Created: Sun Sep 29 12:36:24 2013
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
        Form.resize(669, 427)
        self.labWeitereVokabeln = QtGui.QLabel(Form)
        self.labWeitereVokabeln.setGeometry(QtCore.QRect(20, 20, 291, 16))
        self.labWeitereVokabeln.setObjectName(_fromUtf8("labWeitereVokabeln"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(460, 30, 101, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.labPunkte = QtGui.QLabel(self.groupBox)
        self.labPunkte.setGeometry(QtCore.QRect(20, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labPunkte.setFont(font)
        self.labPunkte.setObjectName(_fromUtf8("labPunkte"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 100, 191, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.labLektion = QtGui.QLabel(self.groupBox_2)
        self.labLektion.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.labLektion.setObjectName(_fromUtf8("labLektion"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 170, 191, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.labBuch = QtGui.QLabel(self.groupBox_3)
        self.labBuch.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.labBuch.setObjectName(_fromUtf8("labBuch"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 190, 431, 51))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.tfInput = QtGui.QLineEdit(self.groupBox_4)
        self.tfInput.setGeometry(QtCore.QRect(10, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tfInput.setFont(font)
        self.tfInput.setObjectName(_fromUtf8("tfInput"))
        self.labBitteEingeben = QtGui.QLabel(Form)
        self.labBitteEingeben.setGeometry(QtCore.QRect(20, 110, 421, 16))
        self.labBitteEingeben.setObjectName(_fromUtf8("labBitteEingeben"))
        self.labRichtigFalsch = QtGui.QLabel(Form)
        self.labRichtigFalsch.setGeometry(QtCore.QRect(20, 250, 421, 16))
        self.labRichtigFalsch.setObjectName(_fromUtf8("labRichtigFalsch"))
        self.labVokabelMeintenSie = QtGui.QLabel(Form)
        self.labVokabelMeintenSie.setGeometry(QtCore.QRect(20, 140, 421, 16))
        self.labVokabelMeintenSie.setObjectName(_fromUtf8("labVokabelMeintenSie"))
        self.btnWeiter = QtGui.QPushButton(Form)
        self.btnWeiter.setGeometry(QtCore.QRect(474, 380, 151, 23))
        self.btnWeiter.setObjectName(_fromUtf8("btnWeiter"))
        self.labMeintenSie = QtGui.QLabel(Form)
        self.labMeintenSie.setGeometry(QtCore.QRect(20, 170, 421, 16))
        self.labMeintenSie.setObjectName(_fromUtf8("labMeintenSie"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Abfrage", None))
        self.labWeitereVokabeln.setText(_translate("Form", "weitere Vokabeln", None))
        self.groupBox.setTitle(_translate("Form", "Punkte", None))
        self.labPunkte.setText(_translate("Form", "PunkteStand", None))
        self.groupBox_2.setTitle(_translate("Form", "Lektion", None))
        self.labLektion.setText(_translate("Form", "vonWoHerLektion", None))
        self.groupBox_3.setTitle(_translate("Form", "Buch", None))
        self.labBuch.setText(_translate("Form", "vonWoBuch", None))
        self.labBitteEingeben.setText(_translate("Form", "Bitte eingeben", None))
        self.labRichtigFalsch.setText(_translate("Form", "Richtig Falsch", None))
        self.labVokabelMeintenSie.setText(_translate("Form", "Vokabel", None))
        self.btnWeiter.setText(_translate("Form", "Weiter", None))
        self.labMeintenSie.setText(_translate("Form", "Meinten Sie", None))

