# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowLektionAendern.ui'
#
# Created: Mon Apr 14 17:32:41 2014
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
        Form.resize(777, 278)
        self.verticalLayout_8 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.cBSpracheAuswaehlen = QtGui.QComboBox(self.groupBox)
        self.cBSpracheAuswaehlen.setObjectName(_fromUtf8("cBSpracheAuswaehlen"))
        self.verticalLayout_7.addWidget(self.cBSpracheAuswaehlen)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.cbBuchAuswaehlen = QtGui.QComboBox(self.groupBox_3)
        self.cbBuchAuswaehlen.setObjectName(_fromUtf8("cbBuchAuswaehlen"))
        self.verticalLayout_6.addWidget(self.cbBuchAuswaehlen)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cbNeuesBuch = QtGui.QComboBox(self.groupBox_4)
        self.cbNeuesBuch.setObjectName(_fromUtf8("cbNeuesBuch"))
        self.verticalLayout_3.addWidget(self.cbNeuesBuch)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.cbLektionAuswaehlen = QtGui.QComboBox(self.groupBox_5)
        self.cbLektionAuswaehlen.setObjectName(_fromUtf8("cbLektionAuswaehlen"))
        self.verticalLayout_5.addWidget(self.cbLektionAuswaehlen)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tfNeuerName = QtGui.QLineEdit(self.groupBox_2)
        self.tfNeuerName.setObjectName(_fromUtf8("tfNeuerName"))
        self.verticalLayout_2.addWidget(self.tfNeuerName)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnLektionLoeschen = QtGui.QPushButton(Form)
        self.btnLektionLoeschen.setObjectName(_fromUtf8("btnLektionLoeschen"))
        self.horizontalLayout.addWidget(self.btnLektionLoeschen)
        self.btnSpeichernUndSchliessen = QtGui.QPushButton(Form)
        self.btnSpeichernUndSchliessen.setObjectName(_fromUtf8("btnSpeichernUndSchliessen"))
        self.horizontalLayout.addWidget(self.btnSpeichernUndSchliessen)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Lektion Ändern", None))
        self.groupBox.setTitle(_translate("Form", "Sprache auswählen", None))
        self.groupBox_3.setTitle(_translate("Form", "Buch auswählen", None))
        self.groupBox_4.setTitle(_translate("Form", "Neues Buch", None))
        self.groupBox_5.setTitle(_translate("Form", "Lektion auswählen", None))
        self.groupBox_2.setTitle(_translate("Form", "Neuer Lektionsname", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnLektionLoeschen.setText(_translate("Form", "Lektion löschen", None))
        self.btnSpeichernUndSchliessen.setText(_translate("Form", "Speichern und Schließen", None))

