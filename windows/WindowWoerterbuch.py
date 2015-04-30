# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowWoerterbuch.ui'
#
# Created: Thu Apr 30 07:50:51 2015
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
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chBBuch = QtGui.QCheckBox(self.groupBox_2)
        self.chBBuch.setText(_fromUtf8(""))
        self.chBBuch.setObjectName(_fromUtf8("chBBuch"))
        self.horizontalLayout_2.addWidget(self.chBBuch)
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.horizontalLayout_2.addWidget(self.cBBuch)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tfSuche = QtGui.QLineEdit(self.groupBox_3)
        self.tfSuche.setObjectName(_fromUtf8("tfSuche"))
        self.verticalLayout_4.addWidget(self.tfSuche)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbColor = QtGui.QCheckBox(Form)
        self.cbColor.setObjectName(_fromUtf8("cbColor"))
        self.horizontalLayout_3.addWidget(self.cbColor)
        self.cbSolid = QtGui.QCheckBox(Form)
        self.cbSolid.setObjectName(_fromUtf8("cbSolid"))
        self.horizontalLayout_3.addWidget(self.cbSolid)
        self.cbSufficient = QtGui.QCheckBox(Form)
        self.cbSufficient.setObjectName(_fromUtf8("cbSufficient"))
        self.horizontalLayout_3.addWidget(self.cbSufficient)
        self.cbMiserable = QtGui.QCheckBox(Form)
        self.cbMiserable.setObjectName(_fromUtf8("cbMiserable"))
        self.horizontalLayout_3.addWidget(self.cbMiserable)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tVWoerterbuch = QtGui.QTableView(Form)
        self.tVWoerterbuch.setObjectName(_fromUtf8("tVWoerterbuch"))
        self.verticalLayout_3.addWidget(self.tVWoerterbuch)
        self.btnBearbeiten = QtGui.QPushButton(Form)
        self.btnBearbeiten.setObjectName(_fromUtf8("btnBearbeiten"))
        self.verticalLayout_3.addWidget(self.btnBearbeiten)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cBSprache, self.cBBuch)
        Form.setTabOrder(self.cBBuch, self.tfSuche)
        Form.setTabOrder(self.tfSuche, self.tVWoerterbuch)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Wörterbuch", None))
        self.groupBox.setTitle(_translate("Form", "Sprache", None))
        self.groupBox_2.setTitle(_translate("Form", "Buch", None))
        self.groupBox_3.setTitle(_translate("Form", "Suche", None))
        self.cbColor.setText(_translate("Form", "Colorierung", None))
        self.cbSolid.setText(_translate("Form", "Solide", None))
        self.cbSufficient.setText(_translate("Form", "Ausreichend", None))
        self.cbMiserable.setText(_translate("Form", "Miserabel", None))
        self.btnBearbeiten.setText(_translate("Form", "Bearbeiten", None))

