# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowVokabelAnlegen.ui'
#
# Created: Mon Oct 14 20:43:29 2013
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
        Form.resize(679, 438)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.verticalLayout_3.addWidget(self.cBSprache)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.verticalLayout_4.addWidget(self.cBBuch)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.cBLekion = QtGui.QComboBox(self.groupBox_3)
        self.cBLekion.setObjectName(_fromUtf8("cBLekion"))
        self.verticalLayout_5.addWidget(self.cBLekion)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.lbAnzVokabeln = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbAnzVokabeln.setFont(font)
        self.lbAnzVokabeln.setObjectName(_fromUtf8("lbAnzVokabeln"))
        self.horizontalLayout_3.addWidget(self.lbAnzVokabeln)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tfDeutsch = QtGui.QLineEdit(self.groupBox_4)
        self.tfDeutsch.setObjectName(_fromUtf8("tfDeutsch"))
        self.verticalLayout_6.addWidget(self.tfDeutsch)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.tfFremd = QtGui.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tfFremd.setFont(font)
        self.tfFremd.setObjectName(_fromUtf8("tfFremd"))
        self.verticalLayout_7.addWidget(self.tfFremd)
        self.horizontalLayout_4.addWidget(self.groupBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.labFelderAusfuellen = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labFelderAusfuellen.setFont(font)
        self.labFelderAusfuellen.setObjectName(_fromUtf8("labFelderAusfuellen"))
        self.verticalLayout.addWidget(self.labFelderAusfuellen)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout_2.addWidget(self.btnAbbrechen)
        self.btnAnwenden = QtGui.QPushButton(Form)
        self.btnAnwenden.setObjectName(_fromUtf8("btnAnwenden"))
        self.horizontalLayout_2.addWidget(self.btnAnwenden)
        self.btnAnwendenUndSchliessen = QtGui.QPushButton(Form)
        self.btnAnwendenUndSchliessen.setObjectName(_fromUtf8("btnAnwendenUndSchliessen"))
        self.horizontalLayout_2.addWidget(self.btnAnwendenUndSchliessen)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cBSprache, self.cBBuch)
        Form.setTabOrder(self.cBBuch, self.cBLekion)
        Form.setTabOrder(self.cBLekion, self.tfDeutsch)
        Form.setTabOrder(self.tfDeutsch, self.tfFremd)
        Form.setTabOrder(self.tfFremd, self.btnAbbrechen)
        Form.setTabOrder(self.btnAbbrechen, self.btnAnwenden)
        Form.setTabOrder(self.btnAnwenden, self.btnAnwendenUndSchliessen)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Vokabel anlegen", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_2.setTitle(_translate("Form", "Buch", None))
        self.groupBox_3.setTitle(_translate("Form", "Lektion", None))
        self.lbAnzVokabeln.setText(_translate("Form", "TextLabel", None))
        self.groupBox_4.setTitle(_translate("Form", "Deutsch", None))
        self.groupBox_5.setTitle(_translate("Form", "Fremdsprache", None))
        self.labFelderAusfuellen.setText(_translate("Form", "Bitte alle Felder ausfüllen", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnAnwenden.setText(_translate("Form", "Anwenden", None))
        self.btnAnwendenUndSchliessen.setText(_translate("Form", "Anwenden und Schließen", None))

