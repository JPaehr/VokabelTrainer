# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowMindestTreffer.ui'
#
# Created: Thu Apr 17 10:24:57 2014
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
        Form.resize(553, 238)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lENeuerWert = QtGui.QLineEdit(Form)
        self.lENeuerWert.setObjectName(_fromUtf8("lENeuerWert"))
        self.horizontalLayout_2.addWidget(self.lENeuerWert)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.hSNeuerWert = QtGui.QSlider(Form)
        self.hSNeuerWert.setOrientation(QtCore.Qt.Horizontal)
        self.hSNeuerWert.setObjectName(_fromUtf8("hSNeuerWert"))
        self.verticalLayout.addWidget(self.hSNeuerWert)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.labTextNeu = QtGui.QLabel(self.groupBox_2)
        self.labTextNeu.setObjectName(_fromUtf8("labTextNeu"))
        self.verticalLayout_4.addWidget(self.labTextNeu)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.labTextAlt = QtGui.QLabel(self.groupBox_3)
        self.labTextAlt.setObjectName(_fromUtf8("labTextAlt"))
        self.verticalLayout_5.addWidget(self.labTextAlt)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnSpeichernUSchliessen = QtGui.QPushButton(Form)
        self.btnSpeichernUSchliessen.setObjectName(_fromUtf8("btnSpeichernUSchliessen"))
        self.horizontalLayout.addWidget(self.btnSpeichernUSchliessen)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Mindestübereinstimmung festlegen", None))
        self.label.setText(_translate("Form", "Neuer Wert (in Prozent)", None))
        self.groupBox.setTitle(_translate("Form", "Beispiel", None))
        self.groupBox_2.setTitle(_translate("Form", "Neu", None))
        self.labTextNeu.setText(_translate("Form", "Lorem ipsum dolor sit amet, consetetur", None))
        self.groupBox_3.setTitle(_translate("Form", "Alt", None))
        self.labTextAlt.setText(_translate("Form", "Lorem ipsum dolor sit amet, consetetur", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnSpeichernUSchliessen.setText(_translate("Form", "Speichern und Schließen", None))

