# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowAbfrage.ui'
#
# Created: Mon Apr 14 08:44:19 2014
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
        Form.resize(881, 408)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.labZeit = CLabel(Form)
        self.labZeit.setObjectName(_fromUtf8("labZeit"))
        self.verticalLayout_9.addWidget(self.labZeit)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.hilfsWidget1 = QtGui.QWidget(Form)
        self.hilfsWidget1.setObjectName(_fromUtf8("hilfsWidget1"))
        self.verticalLayout_11.addWidget(self.hilfsWidget1)
        self.pBFortschritt = Progressbar(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBFortschritt.sizePolicy().hasHeightForWidth())
        self.pBFortschritt.setSizePolicy(sizePolicy)
        self.pBFortschritt.setMinimumSize(QtCore.QSize(0, 0))
        self.pBFortschritt.setProperty("value", 24)
        self.pBFortschritt.setObjectName(_fromUtf8("pBFortschritt"))
        self.verticalLayout_11.addWidget(self.pBFortschritt)
        self.hilfsWidget2 = QtGui.QWidget(Form)
        self.hilfsWidget2.setObjectName(_fromUtf8("hilfsWidget2"))
        self.verticalLayout_11.addWidget(self.hilfsWidget2)
        self.verticalLayout_9.addLayout(self.verticalLayout_11)
        self.labWeitereVokabeln = LabWeitereVok(Form)
        self.labWeitereVokabeln.setObjectName(_fromUtf8("labWeitereVokabeln"))
        self.verticalLayout_9.addWidget(self.labWeitereVokabeln)
        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_9.setStretch(2, 1)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.widgetWeitereVok = QtGui.QWidget(Form)
        self.widgetWeitereVok.setMinimumSize(QtCore.QSize(0, 0))
        self.widgetWeitereVok.setObjectName(_fromUtf8("widgetWeitereVok"))
        self.verticalLayout.addWidget(self.widgetWeitereVok)
        self.labBitteEingeben = QtGui.QLabel(Form)
        self.labBitteEingeben.setObjectName(_fromUtf8("labBitteEingeben"))
        self.verticalLayout.addWidget(self.labBitteEingeben)
        self.labVokabelMeintenSie = QtGui.QLabel(Form)
        self.labVokabelMeintenSie.setObjectName(_fromUtf8("labVokabelMeintenSie"))
        self.verticalLayout.addWidget(self.labVokabelMeintenSie)
        self.labMeintenSie = QtGui.QLabel(Form)
        self.labMeintenSie.setObjectName(_fromUtf8("labMeintenSie"))
        self.verticalLayout.addWidget(self.labMeintenSie)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tfInput = QtGui.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tfInput.setFont(font)
        self.tfInput.setObjectName(_fromUtf8("tfInput"))
        self.verticalLayout_2.addWidget(self.tfInput)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.labRichtigFalsch = QtGui.QLabel(Form)
        self.labRichtigFalsch.setObjectName(_fromUtf8("labRichtigFalsch"))
        self.verticalLayout.addWidget(self.labRichtigFalsch)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(6, 5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cBPunkte = QtGui.QCheckBox(self.groupBox)
        self.cBPunkte.setMinimumSize(QtCore.QSize(70, 30))
        self.cBPunkte.setObjectName(_fromUtf8("cBPunkte"))
        self.horizontalLayout_4.addWidget(self.cBPunkte)
        self.labPunkte = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labPunkte.setFont(font)
        self.labPunkte.setObjectName(_fromUtf8("labPunkte"))
        self.horizontalLayout_4.addWidget(self.labPunkte)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.labLektion = QtGui.QLabel(self.groupBox_2)
        self.labLektion.setObjectName(_fromUtf8("labLektion"))
        self.verticalLayout_5.addWidget(self.labLektion)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.labBuch = QtGui.QLabel(self.groupBox_3)
        self.labBuch.setObjectName(_fromUtf8("labBuch"))
        self.verticalLayout_7.addWidget(self.labBuch)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        self.btnSaveExit = QtGui.QPushButton(Form)
        self.btnSaveExit.setObjectName(_fromUtf8("btnSaveExit"))
        self.verticalLayout_3.addWidget(self.btnSaveExit)
        self.btnWeiter = QtGui.QPushButton(Form)
        self.btnWeiter.setObjectName(_fromUtf8("btnWeiter"))
        self.verticalLayout_3.addWidget(self.btnWeiter)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Abfrage", None))
        self.labZeit.setText(_translate("Form", "Zeit", None))
        self.labWeitereVokabeln.setText(_translate("Form", "weitere Vokabeln", None))
        self.labBitteEingeben.setText(_translate("Form", "Bitte eingeben", None))
        self.labVokabelMeintenSie.setText(_translate("Form", "Vokabel", None))
        self.labMeintenSie.setText(_translate("Form", "Meinten Sie", None))
        self.labRichtigFalsch.setText(_translate("Form", "Richtig Falsch", None))
        self.groupBox.setTitle(_translate("Form", "Punkte", None))
        self.cBPunkte.setText(_translate("Form", "Punkte", None))
        self.labPunkte.setText(_translate("Form", "PunkteStand", None))
        self.groupBox_2.setTitle(_translate("Form", "Lektion", None))
        self.labLektion.setText(_translate("Form", "vonWoHerLektion", None))
        self.groupBox_3.setTitle(_translate("Form", "Buch", None))
        self.labBuch.setText(_translate("Form", "vonWoBuch", None))
        self.btnSaveExit.setText(_translate("Form", "speichern und beenden", None))
        self.btnWeiter.setText(_translate("Form", "weiter", None))

from models.CLabel import CLabel
from models.LabWeitereVok import LabWeitereVok
from models.Progressbar import Progressbar
