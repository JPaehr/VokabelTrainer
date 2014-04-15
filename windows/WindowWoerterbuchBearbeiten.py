# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowWoerterbuchBearbeiten.ui'
#
# Created: Tue Apr 15 14:53:58 2014
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
        Form.resize(635, 396)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.verticalLayout_10.addWidget(self.cBSprache)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.verticalLayout_9.addWidget(self.cBBuch)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.cBLekion = QtGui.QComboBox(self.groupBox_3)
        self.cBLekion.setObjectName(_fromUtf8("cBLekion"))
        self.verticalLayout_8.addWidget(self.cBLekion)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.tfDeutsch = QtGui.QLineEdit(self.groupBox_4)
        self.tfDeutsch.setObjectName(_fromUtf8("tfDeutsch"))
        self.verticalLayout_7.addWidget(self.tfDeutsch)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tfFremd = QtGui.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tfFremd.setFont(font)
        self.tfFremd.setObjectName(_fromUtf8("tfFremd"))
        self.verticalLayout_6.addWidget(self.tfFremd)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout_2.addWidget(self.btnAbbrechen)
        self.btnVokabelLoeschenUSchliessen = QtGui.QPushButton(Form)
        self.btnVokabelLoeschenUSchliessen.setObjectName(_fromUtf8("btnVokabelLoeschenUSchliessen"))
        self.horizontalLayout_2.addWidget(self.btnVokabelLoeschenUSchliessen)
        self.btnAnwenden = QtGui.QPushButton(Form)
        self.btnAnwenden.setObjectName(_fromUtf8("btnAnwenden"))
        self.horizontalLayout_2.addWidget(self.btnAnwenden)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Wort bearbeiten", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_2.setTitle(_translate("Form", "Buch", None))
        self.groupBox_3.setTitle(_translate("Form", "Lektion", None))
        self.groupBox_4.setTitle(_translate("Form", "Deutsch", None))
        self.groupBox_5.setTitle(_translate("Form", "Fremdsprache", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnVokabelLoeschenUSchliessen.setText(_translate("Form", "Vokabeln löschen und schließen", None))
        self.btnAnwenden.setText(_translate("Form", "Anwenden", None))

