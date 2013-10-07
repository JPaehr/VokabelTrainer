# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Johannes\Documents\Python\VokabelTrainer\UIs\WindowAbfrageEinstellungen.ui'
#
# Created: Thu Oct 03 20:08:38 2013
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
        Form.resize(791, 656)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 281, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cbSprache = QtGui.QComboBox(self.groupBox)
        self.cbSprache.setGeometry(QtCore.QRect(20, 30, 231, 22))
        self.cbSprache.setObjectName(_fromUtf8("cbSprache"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 281, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setGeometry(QtCore.QRect(20, 30, 231, 22))
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(329, 219, 281, 221))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lvGewaehlteLektionen = QtGui.QListView(self.groupBox_3)
        self.lvGewaehlteLektionen.setGeometry(QtCore.QRect(10, 20, 261, 192))
        self.lvGewaehlteLektionen.setObjectName(_fromUtf8("lvGewaehlteLektionen"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 220, 281, 221))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.lvLektionen = QtGui.QListView(self.groupBox_4)
        self.lvLektionen.setGeometry(QtCore.QRect(10, 20, 261, 191))
        self.lvLektionen.setObjectName(_fromUtf8("lvLektionen"))
        self.chBMeintenSie = QtGui.QCheckBox(Form)
        self.chBMeintenSie.setGeometry(QtCore.QRect(330, 20, 180, 17))
        self.chBMeintenSie.setObjectName(_fromUtf8("chBMeintenSie"))
        self.chBRichtigGeschriebeneAnzeigen = QtGui.QCheckBox(Form)
        self.chBRichtigGeschriebeneAnzeigen.setGeometry(QtCore.QRect(330, 43, 210, 17))
        self.chBRichtigGeschriebeneAnzeigen.setObjectName(_fromUtf8("chBRichtigGeschriebeneAnzeigen"))
        self.tfZeitWarten = QtGui.QLineEdit(Form)
        self.tfZeitWarten.setGeometry(QtCore.QRect(331, 67, 51, 20))
        self.tfZeitWarten.setObjectName(_fromUtf8("tfZeitWarten"))
        self.tfHaeufigkeit = QtGui.QLineEdit(Form)
        self.tfHaeufigkeit.setGeometry(QtCore.QRect(331, 95, 51, 20))
        self.tfHaeufigkeit.setObjectName(_fromUtf8("tfHaeufigkeit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(389, 71, 140, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(389, 99, 109, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(329, 129, 251, 81))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.cBAbfragerichtung = QtGui.QComboBox(self.groupBox_5)
        self.cBAbfragerichtung.setGeometry(QtCore.QRect(10, 30, 221, 22))
        self.cBAbfragerichtung.setObjectName(_fromUtf8("cBAbfragerichtung"))
        self.btnLektionZuAbfrageHinzu = QtGui.QPushButton(Form)
        self.btnLektionZuAbfrageHinzu.setGeometry(QtCore.QRect(30, 520, 271, 23))
        self.btnLektionZuAbfrageHinzu.setObjectName(_fromUtf8("btnLektionZuAbfrageHinzu"))
        self.btnLektionLoeschen = QtGui.QPushButton(Form)
        self.btnLektionLoeschen.setGeometry(QtCore.QRect(30, 560, 271, 21))
        self.btnLektionLoeschen.setObjectName(_fromUtf8("btnLektionLoeschen"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(336, 479, 311, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(self.layoutWidget)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnAbfrageStarten = QtGui.QPushButton(self.layoutWidget)
        self.btnAbfrageStarten.setObjectName(_fromUtf8("btnAbfrageStarten"))
        self.horizontalLayout.addWidget(self.btnAbfrageStarten)
        self.btnBuchZuAbfrage = QtGui.QPushButton(Form)
        self.btnBuchZuAbfrage.setGeometry(QtCore.QRect(30, 480, 271, 23))
        self.btnBuchZuAbfrage.setObjectName(_fromUtf8("btnBuchZuAbfrage"))
        self.labAnzahlVokabeln = QtGui.QLabel(Form)
        self.labAnzahlVokabeln.setGeometry(QtCore.QRect(620, 400, 141, 16))
        self.labAnzahlVokabeln.setObjectName(_fromUtf8("labAnzahlVokabeln"))
        self.labAnzahlAbfragen = QtGui.QLabel(Form)
        self.labAnzahlAbfragen.setGeometry(QtCore.QRect(620, 420, 141, 16))
        self.labAnzahlAbfragen.setObjectName(_fromUtf8("labAnzahlAbfragen"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cbSprache, self.cBBuch)
        Form.setTabOrder(self.cBBuch, self.btnLektionZuAbfrageHinzu)
        Form.setTabOrder(self.btnLektionZuAbfrageHinzu, self.btnLektionLoeschen)
        Form.setTabOrder(self.btnLektionLoeschen, self.chBMeintenSie)
        Form.setTabOrder(self.chBMeintenSie, self.chBRichtigGeschriebeneAnzeigen)
        Form.setTabOrder(self.chBRichtigGeschriebeneAnzeigen, self.tfZeitWarten)
        Form.setTabOrder(self.tfZeitWarten, self.tfHaeufigkeit)
        Form.setTabOrder(self.tfHaeufigkeit, self.cBAbfragerichtung)
        Form.setTabOrder(self.cBAbfragerichtung, self.lvGewaehlteLektionen)
        Form.setTabOrder(self.lvGewaehlteLektionen, self.btnAbbrechen)
        Form.setTabOrder(self.btnAbbrechen, self.btnAbfrageStarten)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Abfrageeinstellungen", None))
        self.groupBox.setTitle(_translate("Form", "Sprache wählen", None))
        self.groupBox_2.setTitle(_translate("Form", "Buch", None))
        self.groupBox_3.setTitle(_translate("Form", "Gewählte Lektionen", None))
        self.groupBox_4.setTitle(_translate("Form", "Lektionen", None))
        self.chBMeintenSie.setText(_translate("Form", "\"Meinten Sie\" Hinweis einblenden", None))
        self.chBRichtigGeschriebeneAnzeigen.setText(_translate("Form", "richtig geschriebene Vokabeln anzeigen", None))
        self.label.setText(_translate("Form", "Zeit in ms warten pro Vokabel", None))
        self.label_2.setText(_translate("Form", "Häufigkeit der Abfrage", None))
        self.groupBox_5.setTitle(_translate("Form", "Abfragerichtung", None))
        self.btnLektionZuAbfrageHinzu.setText(_translate("Form", "Lektion zu Abfrage hinzufügen", None))
        self.btnLektionLoeschen.setText(_translate("Form", "markierte Lektion nicht abfragen", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnAbfrageStarten.setText(_translate("Form", "Abfrage starten", None))
        self.btnBuchZuAbfrage.setText(_translate("Form", "Buch zu Abfrage hinzufügen", None))
        self.labAnzahlVokabeln.setText(_translate("Form", "Anzahl Vokabeln: 0", None))
        self.labAnzahlAbfragen.setText(_translate("Form", "Anzahl Abfragen: 0", None))

