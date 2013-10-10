# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowMeintenSie.ui'
#
# Created: Thu Oct 10 21:19:04 2013
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
        Form.resize(467, 210)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lvMeintenSieSatz = QtGui.QListView(Form)
        self.lvMeintenSieSatz.setMinimumSize(QtCore.QSize(256, 192))
        self.lvMeintenSieSatz.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lvMeintenSieSatz.setLayoutMode(QtGui.QListView.SinglePass)
        self.lvMeintenSieSatz.setObjectName(_fromUtf8("lvMeintenSieSatz"))
        self.horizontalLayout.addWidget(self.lvMeintenSieSatz)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "MeintenSie", None))

