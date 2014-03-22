# -*- coding: utf-8 -*-
"""
Created on 08.10.2013

@author: Johannes
"""
from PyQt4 import QtGui, QtCore
from windows.WindowAbfrageEinstellungen import Ui_Form as WindowAbfrageEinstellungen
import Abfrage as Abfrage
import models.base as Datenbank
import models.ListModel as Markierung


class AbfrageEinstellungen(WindowAbfrageEinstellungen, QtGui.QWidget):
    """
    Fenster für die Abfrage Einstellungen
    """
    def __init__(self, parent):
        super(AbfrageEinstellungen, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.abfrage_einstellung = 0
        self.lektions_liste = []
        
        self.connect(self.btnAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.cbSprache, QtCore.SIGNAL("activated(int)"), self.BuchZeichnen)
        self.connect(self.cbSprache, QtCore.SIGNAL("activated(int)"), self.Abfragerichtung)
        self.connect(self.cBBuch, QtCore.SIGNAL("activated(int)"), self.LektionZeichnen)
        self.connect(self.btnLektionZuAbfrageHinzu, QtCore.SIGNAL("clicked()"), self.LektionZuAbfrageHinzu)
        self.connect(self.btnLektionLoeschen, QtCore.SIGNAL("clicked()"), self.LektionTrennen)
        self.connect(self.btnAbfrageStarten, QtCore.SIGNAL("clicked()"), self.AbfrageStarten)
        self.connect(self.tfHaeufigkeit, QtCore.SIGNAL("textChanged(QString)"), self.AnzahlAbfragenPaint)
        self.connect(self.btnBuchZuAbfrage, QtCore.SIGNAL("clicked()"), self.BuchZuAbfrageHinzu)

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        
        voreinstellungen = self.datenbank.getDataAsList("select meintenSie, rgva, warteZeit, haeufigkeit, richtung, wiederholen, distanz from Einstellungen \
        where id like 1")
        
        if voreinstellungen[0][0] == "True":
            self.chBMeintenSie.setChecked(True)
        else:
            self.chBMeintenSie.setChecked(False)
        
        if voreinstellungen[0][1] == "True":
            self.chBRichtigGeschriebeneAnzeigen.setChecked(True)
        else:
            self.chBRichtigGeschriebeneAnzeigen.setChecked(False)
        
        self.tfZeitWarten.setText(str(voreinstellungen[0][2]))
        self.tfHaeufigkeit.setText(str(voreinstellungen[0][3]))
        self.tfDistanz.setText(str(voreinstellungen[0][6]))
        
        self.richtung = voreinstellungen[0][4]
        
        self.SpracheZeichnen()
        self.Abfragerichtung()
    def FortsetzenDisable(self):
        self.parent.FortsetzenDisable()
    def FortsetzenEnable(self):
        self.parent.FortsetzenEnable()
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
        self.datenbank.setData(updateStatement)
        self.close()

        test = Abfrage.Abfrage(self, self.lektions_liste, self.tfHaeufigkeit.text(), self.tfZeitWarten.text(),
                               self.chBMeintenSie.isChecked(), self.chBRichtigGeschriebeneAnzeigen.isChecked(),
                               self.cBAbfragerichtung.currentIndex()+1, self.tfDistanz.text())
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
        select_sprache = "select fremdsprache, id from sprache"
        sprache_daten = self.datenbank.getDataAsQStringList(select_sprache)
        model_sprache = QtGui.QStringListModel(sprache_daten)
        self.cbSprache.setModel(model_sprache)
        self.BuchZeichnen()
        
    def BuchZeichnen(self):
        select_buch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"'"
        buch_daten = self.datenbank.getDataAsQStringList(select_buch)
        model_buch = QtGui.QStringListModel(buch_daten)
        self.cBBuch.setModel(model_buch)
        self.LektionZeichnen()
        
    def LektionZeichnen(self):
        select_lektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.datenbank.getDataAsList(select_lektion)
        liste = []
        for i in daten:
            #Vokabeln dahinter schreiben
            selection = self.datenbank.getDataAsList("select count(*) from vokabeln \
            join lektionen on (lektionen.id=vokabeln.idlektion)\
            where idlektion like "+str(i[1]))
            liste.append(i[0]+" - "+str(selection[0][0])+" Vokabeln")
        model = Markierung.Markierung(liste)
        self.lvLektionen.setModel(model) 
        self.lvLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        
    
    def getIdSprache(self):
        select_sprache = "select fremdsprache, id from sprache \
        limit '"+str(self.cbSprache.currentIndex())+"', '"+str(self.cbSprache.currentIndex()+1)+"'" 
        sprache_id = self.datenbank.getDataAsList(select_sprache)[0][1]
        return sprache_id
    
    def getIdBuch(self):
        select_buch = "select buecher.name, buecher.id from buecher \
        join sprache on (sprache.id=buecher.id_sprache) \
        where sprache.id like '"+str(self.getIdSprache())+"' \
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'"
        return self.datenbank.getDataAsList(select_buch)[0][1]
    def getIdLektionen(self):
        select_lektion = "select lektionen.name, lektionen.id from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.datenbank.getDataAsList(select_lektion)
        liste = []
        for i in self.lvLektionen.selectedIndexes():
            liste.append(daten[i.row()][1])
        return liste
    def LektionZuAbfrageHinzu(self):
        self.lektions_liste.extend(self.getIdLektionen())
        self.AbfrageNeuZeichen()
    def AbfrageNeuZeichen(self):
        #print self.lektionsListe
        datenliste = []
        for i in self.lektions_liste:
            daten = self.datenbank.getDataAsList("select Buecher.name, lektionen.name from lektionen \
            join buecher on (buecher.id=lektionen.idbuch) \
            where lektionen.id like "+str(i))
            datenliste.append(str(daten[0][0])+" - "+str(daten[0][1]))
        
        model = Markierung.Markierung(datenliste)
        self.lvGewaehlteLektionen.setModel(model)
        self.lvGewaehlteLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.AnzahlVokabelnPaint()
    def BuchZuAbfrageHinzu(self):
        daten = self.datenbank.getDataAsList("select lektionen.id from buecher \
        join Lektionen on (lektionen.idbuch = buecher.id) \
        where buecher.id like "+str(self.getIdBuch()))
        liste_zum_hinzufuegen = []
        for i in daten:
            liste_zum_hinzufuegen.append(i[0])
        
        self.lektions_liste.extend(liste_zum_hinzufuegen)
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
        pop_liste = []
        for i in reversed(self.lvGewaehlteLektionen.selectedIndexes()):
            pop_liste.append(i.row())
        for i in pop_liste:
            self.lektions_liste.pop(i)
        
        self.AbfrageNeuZeichen()
    def AnzahlVokabelnPaint(self):
        counter = 0
        for i in self.lektions_liste:
            counter += self.datenbank.getDataAsList("select count(*) from lektionen \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where lektionen.id like "+str(i))[0][0]
        self.labAnzahlVokabeln.setText(u"Anzahl Vokabeln:"+str(counter))
        self.AnzahlAbfragenPaint()
    def AnzahlAbfragenPaint(self):
        counter = 0
        for i in self.lektions_liste:
            counter += self.datenbank.getDataAsList("select count(*) from lektionen \
            join vokabeln on (vokabeln.idlektion=lektionen.id) \
            where lektionen.id like "+str(i))[0][0]
            
        if self.tfHaeufigkeit.text() == '':
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: 0")
        else:
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: "+str(int(counter)*int(self.tfHaeufigkeit.text())))