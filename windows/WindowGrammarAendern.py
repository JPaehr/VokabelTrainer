# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowGrammarAendern.ui'
#
# Created: Wed Apr 29 14:45:11 2015
#      by: PyQt4 UI code generator 4.11.3
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
        Form.resize(774, 247)
        self.verticalLayout_6 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cBSpracheAuswaehlen = QtGui.QComboBox(self.groupBox)
        self.cBSpracheAuswaehlen.setObjectName(_fromUtf8("cBSpracheAuswaehlen"))
        self.verticalLayout.addWidget(self.cBSpracheAuswaehlen)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cBSpracheNeu = QtGui.QComboBox(self.groupBox_4)
        self.cBSpracheNeu.setObjectName(_fromUtf8("cBSpracheNeu"))
        self.verticalLayout_2.addWidget(self.cBSpracheNeu)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cbGrammarHint = QtGui.QComboBox(self.groupBox_3)
        self.cbGrammarHint.setObjectName(_fromUtf8("cbGrammarHint"))
        self.verticalLayout_4.addWidget(self.cbGrammarHint)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tfNeuerName = QtGui.QLineEdit(self.groupBox_2)
        self.tfNeuerName.setObjectName(_fromUtf8("tfNeuerName"))
        self.verticalLayout_3.addWidget(self.tfNeuerName)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnGrammarHintDel = QtGui.QPushButton(Form)
        self.btnGrammarHintDel.setObjectName(_fromUtf8("btnGrammarHintDel"))
        self.horizontalLayout.addWidget(self.btnGrammarHintDel)
        self.btnSpeichernUndSchliessen = QtGui.QPushButton(Form)
        self.btnSpeichernUndSchliessen.setObjectName(_fromUtf8("btnSpeichernUndSchliessen"))
        self.horizontalLayout.addWidget(self.btnSpeichernUndSchliessen)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Formhinweise ändern", None))
        self.groupBox.setTitle(_translate("Form", "Sprache auswählen", None))
        self.groupBox_4.setTitle(_translate("Form", "Neue Sprache", None))
        self.groupBox_3.setTitle(_translate("Form", "Formhinweis auswählen", None))
        self.groupBox_2.setTitle(_translate("Form", "Neuer Formhinweis", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnGrammarHintDel.setText(_translate("Form", "Formhinweis löschen", None))
        self.btnSpeichernUndSchliessen.setText(_translate("Form", "Speichern und Schließen", None))

