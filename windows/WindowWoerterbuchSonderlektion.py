# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowWoerterbuchSonderlektion.ui'
#
# Created: Tue Nov 04 22:26:41 2014
#      by: PyQt4 UI code generator 4.11.2
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
        Form.resize(794, 450)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cBSprache = QtGui.QComboBox(self.groupBox)
        self.cBSprache.setObjectName(_fromUtf8("cBSprache"))
        self.verticalLayout.addWidget(self.cBSprache)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tfSuche = QtGui.QLineEdit(self.groupBox_3)
        self.tfSuche.setObjectName(_fromUtf8("tfSuche"))
        self.verticalLayout_4.addWidget(self.tfSuche)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tVWoerterbuch = QtGui.QTableView(Form)
        self.tVWoerterbuch.setObjectName(_fromUtf8("tVWoerterbuch"))
        self.verticalLayout_3.addWidget(self.tVWoerterbuch)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cBSprache, self.tfSuche)
        Form.setTabOrder(self.tfSuche, self.tVWoerterbuch)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sondervokabeln", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_3.setTitle(_translate("Form", "Suche", None))

