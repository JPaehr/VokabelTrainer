# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowAbfrageEinstellungen import Ui_Form as WindowAbfrageEinstellungen
import Abfrage as Abfrage
import models.base as Datenbank
import models.ListModel as Markierung

class AbfrageEinstellungen(WindowAbfrageEinstellungen, QtGui.QWidget):
    def __init__(self, parent):
        super(AbfrageEinstellungen, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)   
        self.AbfrageEinstellung = 0
        self.lektionsListe = []
        
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.cbSprache, QtCore.SIGNAL("activated(int)"), self.BuchZeichnen)
        self.connect(self.cbSprache, QtCore.SIGNAL("activated(int)"), self.Abfragerichtung)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.LektionZeichnen)
        self.connect(self.btnLektionZuAbfrageHinzu, QtCore.SIGNAL("clicked()"), self.LektionZuAbfrageHinzu)
        self.connect(self.btnLektionLoeschen, QtCore.SIGNAL("clicked()"), self.LektionTrennen)
        self.connect(self.btnAbfrageStarten, QtCore.SIGNAL("clicked()"), self.AbfrageStarten)
        self.connect(self.tfHaeufigkeit, QtCore.SIGNAL("textChanged(QString)"), self.AnzahlAbfragenPaint)
        self.connect(self.btnBuchZuAbfrage, QtCore.SIGNAL("clicked()"), self.BuchZuAbfrageHinzu)
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")   
        
        Voreinstellungen = self.Datenbank.getDataAsList("select meintenSie, rgva, warteZeit, haeufigkeit, richtung, wiederholen, distanz from Einstellungen \
        where id like 1")
        
        if Voreinstellungen[0][0] == "True":
            self.chBMeintenSie.setChecked(True)
        else:
            self.chBMeintenSie.setChecked(False)
        
        if Voreinstellungen[0][1] == "True":
            self.chBRichtigGeschriebeneAnzeigen.setChecked(True)
        else:
            self.chBRichtigGeschriebeneAnzeigen.setChecked(False)
        
        self.tfZeitWarten.setText(str(Voreinstellungen[0][2]))
        self.tfHaeufigkeit.setText(str(Voreinstellungen[0][3]))
        self.tfDistanz.setText(str(Voreinstellungen[0][6]))
        
        self.richtung = Voreinstellungen[0][4]
        
        self.SpracheZeichnen()
        self.Abfragerichtung()
    def AbfrageStarten(self):
        #Einstellungen Speichern
        
        updateStatement = "update Einstellungen set \
        meintenSie='"+str(self.chBMeintenSie.isChecked())+"', \
        rgva = '"+str(self.chBRichtigGeschriebeneAnzeigen.isChecked())+"', \
        warteZeit = "+str(int(self.tfZeitWarten.text()))+", \
        haeufigkeit = "+str(int(self.tfHaeufigkeit.text()))+", \
        richtung = "+str(int(int(self.cBAbfragerichtung.currentIndex())+1))+", \
        distanz = "+str(int(self.tfDistanz.text()))+" \
        where id like 1"
        self.Datenbank.setData(updateStatement)
        
        
        test = Abfrage.Abfrage(self, self.lektionsListe, self.tfHaeufigkeit.text(), self.tfZeitWarten.text(), self.chBMeintenSie.isChecked(), 
                       self.chBRichtigGeschriebeneAnzeigen.isChecked(), self.cBAbfragerichtung.currentIndex()+1, self.tfDistanz.text())
        test.show()
    def Abfragerichtung(self):
        #1 ist von Deutsch nach Fremd, 2 von Fremd nach Deutsch
        daten = QtCore.QStringList()
        daten.append("Deutsch - "+str(self.cbSprache.currentText()))
        daten.append(str(self.cbSprache.currentText())+" - Deutsch")
        model = QtGui.QStringListModel(daten)
        self.cBAbfragerichtung.setModel(model)
        self.cBAbfragerichtung.setCurrentIndex(self.richtung-1)
    def SpracheZeichnen(self):
        selectSprache = "select fremdsprache, id from sprache"
        spracheDaten = self.Datenbank.getDataAsQStringList(selectSprache)
        modelSprache = QtGui.QStringListModel(spracheDaten)
        self.cbSprache.setModel(modelSprache)
        self.BuchZeichnen()
        
    def BuchZeichnen(self):
        selectBuch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"'"
        buchDaten = self.Datenbank.getDataAsQStringList(selectBuch)
        modelBuch = QtGui.QStringListModel(buchDaten)
        self.cBBuch.setModel(modelBuch)
        self.LektionZeichnen()
        
    def LektionZeichnen(self):
        selectLektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.Datenbank.getDataAsList(selectLektion)
        liste = []
        for i in daten:
            #Vokabeln dahinter schreiben
            selection = self.Datenbank.getDataAsList("select count(*) from vokabeln \
            join lektionen on (lektionen.id=vokabeln.idlektion)\
            where idlektion like "+str(i[1]))
            liste.append(i[0]+" - "+str(selection[0][0])+" Vokabeln")
        model = Markierung.Markierung(liste)
        self.lvLektionen.setModel(model) 
        self.lvLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        
    
    def getIdSprache(self):
        selectSprache = "select fremdsprache, id from sprache \
        limit '"+str(self.cbSprache.currentIndex())+"', '"+str(self.cbSprache.currentIndex()+1)+"'" 
        spracheId = self.Datenbank.getDataAsList(selectSprache)[0][1]
        return spracheId
    
    def getIdBuch(self):
        selectBuch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"' \
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'"
        return self.Datenbank.getDataAsList(selectBuch)[0][1]
    def getIdLektionen(self):
        selectLektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.Datenbank.getDataAsList(selectLektion)
        liste = []
        for i in self.lvLektionen.selectedIndexes():
            liste.append(daten[i.row()][1])
        return liste
    def LektionZuAbfrageHinzu(self):
        self.lektionsListe.extend(self.getIdLektionen())
        self.AbfrageNeuZeichen()
    def AbfrageNeuZeichen(self):
        #print self.lektionsListe
        datenliste = []
        for i in self.lektionsListe:
            daten = self.Datenbank.getDataAsList("select Buecher.name, lektionen.name from lektionen \
            join buecher on (buecher.id=lektionen.idbuch) \
            where lektionen.id like "+str(i))
            datenliste.append(str(daten[0][0])+" - "+str(daten[0][1]))
        
        model = Markierung.Markierung(datenliste)
        self.lvGewaehlteLektionen.setModel(model)
        self.lvGewaehlteLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.AnzahlVokabelnPaint()
    def BuchZuAbfrageHinzu(self):
        daten = self.Datenbank.getDataAsList("select lektionen.id from buecher \
        join Lektionen on (lektionen.idbuch = buecher.id) \
        where buecher.id like "+str(self.getIdBuch()))
        listeZumHinzufuegen = []
        for i in daten:
            listeZumHinzufuegen.append(i[0])
        
        self.lektionsListe.extend(listeZumHinzufuegen)
        #print self.lektionsListe
        
        self.AbfrageNeuZeichen()
        
    def ListeZuSql(self, liste, args):
        statement = "where "
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]
    def LektionTrennen(self):
        popListe = []
        for i in reversed(self.lvGewaehlteLektionen.selectedIndexes()):
            popListe.append(i.row())
        for i in popListe:
            self.lektionsListe.pop(i)
        
        self.AbfrageNeuZeichen()
    def AnzahlVokabelnPaint(self):
        counter = 0
        for i in self.lektionsListe:
            counter += self.Datenbank.getDataAsList("select count(*) from lektionen \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where lektionen.id like "+str(i))[0][0]
        self.labAnzahlVokabeln.setText(u"Anzahl Vokabeln:"+str(counter))
        self.AnzahlAbfragenPaint()
    def AnzahlAbfragenPaint(self):
        counter = 0
        for i in self.lektionsListe:
            counter += self.Datenbank.getDataAsList("select count(*) from lektionen \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where lektionen.id like "+str(i))[0][0]
            
        if self.tfHaeufigkeit.text() == '':
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: 0")
        else:
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: "+str(int(counter)*int(self.tfHaeufigkeit.text())))