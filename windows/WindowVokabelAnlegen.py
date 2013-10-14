# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowVokabelAnlegen.ui'
#
# Created: Mon Oct 14 13:57:00 2013
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
        Form.resize(671, 370)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(343, 220, 311, 81))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.tfFremd = QtGui.QLineEdit(self.groupBox_5)
        self.tfFremd.setGeometry(QtCore.QRect(20, 30, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tfFremd.setFont(font)
        self.tfFremd.setObjectName(_fromUtf8("tfFremd"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(23, 130, 311, 81))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cBLekion = QtGui.QComboBox(self.groupBox_3)
        self.cBLekion.setGeometry(QtCore.QRect(20, 30, 271, 22))
        self.cBLekion.setObjectName(_fromUtf8("cBLekion"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(23, 220, 311, 81))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.tfDeutsch = QtGui.QLineEdit(self.groupBox_4)
        self.tfDeutsch.setGeometry(QtCore.QRect(20, 30, 271, 20))
        self.tfDeutsch.setObjectName(_fromUtf8("tfDeutsch"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(23, 40, 631, 81))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setGeometry(QtCore.QRect(20, 30, 271, 22))
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setGeometry(QtCore.QRect(20, 30, 271, 22))
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(340, 330, 311, 25))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAbbrechen = QtGui.QPushButton(self.layoutWidget_2)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout_2.addWidget(self.btnAbbrechen)
        self.btnAnwenden = QtGui.QPushButton(self.layoutWidget_2)
        self.btnAnwenden.setObjectName(_fromUtf8("btnAnwenden"))
        self.horizontalLayout_2.addWidget(self.btnAnwenden)
        self.btnAnwendenUndSchliessen = QtGui.QPushButton(self.layoutWidget_2)
        self.btnAnwendenUndSchliessen.setObjectName(_fromUtf8("btnAnwendenUndSchliessen"))
        self.horizontalLayout_2.addWidget(self.btnAnwendenUndSchliessen)
        self.lbAnzVokabeln = QtGui.QLabel(Form)
        self.lbAnzVokabeln.setGeometry(QtCore.QRect(360, 160, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbAnzVokabeln.setFont(font)
        self.lbAnzVokabeln.setObjectName(_fromUtf8("lbAnzVokabeln"))

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
        self.groupBox_5.setTitle(_translate("Form", "Fremdsprache", None))
        self.groupBox_3.setTitle(_translate("Form", "Lektion", None))
        self.groupBox_4.setTitle(_translate("Form", "Deutsch", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_2.setTitle(_translate("Form", "Buch", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnAnwenden.setText(_translate("Form", "Anwenden", None))
        self.btnAnwendenUndSchliessen.setText(_translate("Form", "Anwenden und Schließen", None))
        self.lbAnzVokabeln.setText(_translate("Form", "TextLabel", None))

