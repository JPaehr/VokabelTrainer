# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs\WindowAbfrage.ui'
#
# Created: Tue Mar 04 19:52:31 2014
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
        self.labWeitereVokabeln = QtGui.QLabel(Form)
        self.labWeitereVokabeln.setObjectName(_fromUtf8("labWeitereVokabeln"))
        self.verticalLayout.addWidget(self.labWeitereVokabeln)
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
        self.verticalLayout.setStretch(5, 5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cBBar = QtGui.QCheckBox(self.groupBox)
        self.cBBar.setObjectName(_fromUtf8("cBBar"))
        self.horizontalLayout_3.addWidget(self.cBBar)
        self.pBFortschritt = QtGui.QProgressBar(self.groupBox)
        self.pBFortschritt.setMinimumSize(QtCore.QSize(166, 21))
        self.pBFortschritt.setProperty("value", 24)
        self.pBFortschritt.setObjectName(_fromUtf8("pBFortschritt"))
        self.horizontalLayout_3.addWidget(self.pBFortschritt)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cBPunkte = QtGui.QCheckBox(self.groupBox)
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
        self.btnWeiter = QtGui.QPushButton(Form)
        self.btnWeiter.setObjectName(_fromUtf8("btnWeiter"))
        self.verticalLayout_3.addWidget(self.btnWeiter)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Abfrage", None))
        self.labWeitereVokabeln.setText(_translate("Form", "weitere Vokabeln", None))
        self.labBitteEingeben.setText(_translate("Form", "Bitte eingeben", None))
        self.labVokabelMeintenSie.setText(_translate("Form", "Vokabel", None))
        self.labMeintenSie.setText(_translate("Form", "Meinten Sie", None))
        self.labRichtigFalsch.setText(_translate("Form", "Richtig Falsch", None))
        self.groupBox.setTitle(_translate("Form", "Punkte", None))
        self.cBBar.setText(_translate("Form", "Bar", None))
        self.cBPunkte.setText(_translate("Form", "Punkte", None))
        self.labPunkte.setText(_translate("Form", "PunkteStand", None))
        self.groupBox_2.setTitle(_translate("Form", "Lektion", None))
        self.labLektion.setText(_translate("Form", "vonWoHerLektion", None))
        self.groupBox_3.setTitle(_translate("Form", "Buch", None))
        self.labBuch.setText(_translate("Form", "vonWoBuch", None))
        self.btnWeiter.setText(_translate("Form", "Weiter", None))

