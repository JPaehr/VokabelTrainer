# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\WindowAbfrageEinstellungen.ui'
#
# Created: Thu Nov 06 20:10:46 2014
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
        Form.resize(936, 511)
        self.verticalLayout_11 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.cbSprache = QtGui.QComboBox(self.groupBox)
        self.cbSprache.setObjectName(_fromUtf8("cbSprache"))
        self.verticalLayout_6.addWidget(self.cbSprache)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.cBBuch = QtGui.QComboBox(self.groupBox_2)
        self.cBBuch.setObjectName(_fromUtf8("cBBuch"))
        self.verticalLayout_7.addWidget(self.cBBuch)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.chBMeintenSie = QtGui.QCheckBox(Form)
        self.chBMeintenSie.setObjectName(_fromUtf8("chBMeintenSie"))
        self.verticalLayout_8.addWidget(self.chBMeintenSie)
        self.chBRichtigGeschriebeneAnzeigen = QtGui.QCheckBox(Form)
        self.chBRichtigGeschriebeneAnzeigen.setObjectName(_fromUtf8("chBRichtigGeschriebeneAnzeigen"))
        self.verticalLayout_8.addWidget(self.chBRichtigGeschriebeneAnzeigen)
        self.chShowTime = QtGui.QCheckBox(Form)
        self.chShowTime.setObjectName(_fromUtf8("chShowTime"))
        self.verticalLayout_8.addWidget(self.chShowTime)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.tfZeitWartenRichtig = QtGui.QLineEdit(Form)
        self.tfZeitWartenRichtig.setObjectName(_fromUtf8("tfZeitWartenRichtig"))
        self.horizontalLayout_8.addWidget(self.tfZeitWartenRichtig)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tfZeitWarten = QtGui.QLineEdit(Form)
        self.tfZeitWarten.setObjectName(_fromUtf8("tfZeitWarten"))
        self.horizontalLayout_3.addWidget(self.tfZeitWarten)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tfHaeufigkeit = QtGui.QLineEdit(Form)
        self.tfHaeufigkeit.setObjectName(_fromUtf8("tfHaeufigkeit"))
        self.horizontalLayout_4.addWidget(self.tfHaeufigkeit)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tfDistanz = QtGui.QLineEdit(Form)
        self.tfDistanz.setObjectName(_fromUtf8("tfDistanz"))
        self.horizontalLayout_5.addWidget(self.tfDistanz)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.cBAbfragerichtung = QtGui.QComboBox(self.groupBox_5)
        self.cBAbfragerichtung.setObjectName(_fromUtf8("cBAbfragerichtung"))
        self.verticalLayout_9.addWidget(self.cBAbfragerichtung)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lvLektionen = QtGui.QListView(self.groupBox_4)
        self.lvLektionen.setObjectName(_fromUtf8("lvLektionen"))
        self.verticalLayout_3.addWidget(self.lvLektionen)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnLektionZuAbfrageHinzu = QtGui.QPushButton(Form)
        self.btnLektionZuAbfrageHinzu.setMaximumSize(QtCore.QSize(23, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnLektionZuAbfrageHinzu.setFont(font)
        self.btnLektionZuAbfrageHinzu.setStyleSheet(_fromUtf8("color:rgb(0, 255, 0)"))
        self.btnLektionZuAbfrageHinzu.setObjectName(_fromUtf8("btnLektionZuAbfrageHinzu"))
        self.verticalLayout_2.addWidget(self.btnLektionZuAbfrageHinzu, QtCore.Qt.AlignBottom)
        self.btnLektionLoeschen = QtGui.QPushButton(Form)
        self.btnLektionLoeschen.setMaximumSize(QtCore.QSize(23, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnLektionLoeschen.setFont(font)
        self.btnLektionLoeschen.setStyleSheet(_fromUtf8("color: red\n"
""))
        self.btnLektionLoeschen.setObjectName(_fromUtf8("btnLektionLoeschen"))
        self.verticalLayout_2.addWidget(self.btnLektionLoeschen, QtCore.Qt.AlignTop)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lvGewaehlteLektionen = QtGui.QListView(self.groupBox_3)
        self.lvGewaehlteLektionen.setObjectName(_fromUtf8("lvGewaehlteLektionen"))
        self.verticalLayout_4.addWidget(self.lvGewaehlteLektionen)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.labAnzahlVokabeln = QtGui.QLabel(Form)
        self.labAnzahlVokabeln.setObjectName(_fromUtf8("labAnzahlVokabeln"))
        self.verticalLayout.addWidget(self.labAnzahlVokabeln, QtCore.Qt.AlignBottom)
        self.labAnzahlAbfragen = QtGui.QLabel(Form)
        self.labAnzahlAbfragen.setObjectName(_fromUtf8("labAnzahlAbfragen"))
        self.verticalLayout.addWidget(self.labAnzahlAbfragen)
        self.labEstTime = QtGui.QLabel(Form)
        self.labEstTime.setObjectName(_fromUtf8("labEstTime"))
        self.verticalLayout.addWidget(self.labEstTime)
        self.verticalLayout.setStretch(0, 8)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 5)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.labKeineLektionGewaehlt = QtGui.QLabel(Form)
        self.labKeineLektionGewaehlt.setObjectName(_fromUtf8("labKeineLektionGewaehlt"))
        self.verticalLayout_10.addWidget(self.labKeineLektionGewaehlt)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btnBuchZuAbfrage = QtGui.QPushButton(Form)
        self.btnBuchZuAbfrage.setObjectName(_fromUtf8("btnBuchZuAbfrage"))
        self.horizontalLayout_7.addWidget(self.btnBuchZuAbfrage)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAbbrechen = QtGui.QPushButton(Form)
        self.btnAbbrechen.setObjectName(_fromUtf8("btnAbbrechen"))
        self.horizontalLayout.addWidget(self.btnAbbrechen)
        self.btnAbfrageStarten = QtGui.QPushButton(Form)
        self.btnAbfrageStarten.setObjectName(_fromUtf8("btnAbfrageStarten"))
        self.horizontalLayout.addWidget(self.btnAbfrageStarten)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)

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
        self.chBMeintenSie.setText(_translate("Form", "\"Meinten Sie\" Hinweis einblenden", None))
        self.chBRichtigGeschriebeneAnzeigen.setText(_translate("Form", "richtig geschriebene Vokabeln anzeigen", None))
        self.chShowTime.setText(_translate("Form", "Zeit anzeigen", None))
        self.label_4.setText(_translate("Form", "Zeit in ms warten wenn Vokabel richtig", None))
        self.label.setText(_translate("Form", "Zeit in ms warten wenn Vokabel falsch", None))
        self.label_2.setText(_translate("Form", "Häufigkeit der Abfrage", None))
        self.label_3.setText(_translate("Form", "Fehlertoleranz beim Vergleich", None))
        self.groupBox_5.setTitle(_translate("Form", "Abfragerichtung", None))
        self.groupBox_4.setTitle(_translate("Form", "Lektionen", None))
        self.btnLektionZuAbfrageHinzu.setText(_translate("Form", ">", None))
        self.btnLektionLoeschen.setText(_translate("Form", "x", None))
        self.groupBox_3.setTitle(_translate("Form", "Gewählte Lektionen", None))
        self.labAnzahlVokabeln.setText(_translate("Form", "Anzahl Vokabeln: 0", None))
        self.labAnzahlAbfragen.setText(_translate("Form", "Anzahl Abfragen: 0", None))
        self.labEstTime.setText(_translate("Form", "erwartete Zeit:", None))
        self.labKeineLektionGewaehlt.setText(_translate("Form", "Es sind keine Lektionen gewählt worden. Bitte Lektion(en) hinzufügen um Abfrage starten zu können.", None))
        self.btnBuchZuAbfrage.setText(_translate("Form", "Buch zu Abfrage hinzufügen", None))
        self.btnAbbrechen.setText(_translate("Form", "Abbrechen", None))
        self.btnAbfrageStarten.setText(_translate("Form", "Abfrage starten", None))

