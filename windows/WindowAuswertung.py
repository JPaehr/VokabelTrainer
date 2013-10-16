# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowAuswertung.ui'
#
# Created: Wed Oct 16 17:17:43 2013
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
        Form.resize(403, 197)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labZusammenfassung = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labZusammenfassung.setFont(font)
        self.labZusammenfassung.setObjectName(_fromUtf8("labZusammenfassung"))
        self.verticalLayout.addWidget(self.labZusammenfassung)
        self.labRichtigBeantwortete = QtGui.QLabel(Form)
        self.labRichtigBeantwortete.setObjectName(_fromUtf8("labRichtigBeantwortete"))
        self.verticalLayout.addWidget(self.labRichtigBeantwortete)
        self.labInProz = QtGui.QLabel(Form)
        self.labInProz.setObjectName(_fromUtf8("labInProz"))
        self.verticalLayout.addWidget(self.labInProz)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PbSchliessen = QtGui.QPushButton(Form)
        self.PbSchliessen.setObjectName(_fromUtf8("PbSchliessen"))
        self.horizontalLayout.addWidget(self.PbSchliessen)
        self.pbStatistik = QtGui.QPushButton(Form)
        self.pbStatistik.setObjectName(_fromUtf8("pbStatistik"))
        self.horizontalLayout.addWidget(self.pbStatistik)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Auswertung", None))
        self.labZusammenfassung.setText(_translate("Form", "Zusammenfassung", None))
        self.labRichtigBeantwortete.setText(_translate("Form", "von richtig beanwortet", None))
        self.labInProz.setText(_translate("Form", "das entspricht in proz", None))
        self.PbSchliessen.setText(_translate("Form", "Schließen", None))
        self.pbStatistik.setText(_translate("Form", "zur Statistik", None))

