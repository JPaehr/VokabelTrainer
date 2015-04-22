# -*- coding: utf-8 -*-
"""
Created on 08.10.2013

@author: Johannes
"""
from Tix import Select
from PyQt4 import QtGui, QtCore
from windows.WindowAbfrageEinstellungen import Ui_Form as WindowAbfrageEinstellungen
import Abfrage as Abfrage
import models.base as Datenbank
import models.ListModel as Markierung
import models.LectionListModelQuerySettings as LectionsListModerQuerySettings
import time
import thread


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
        self.labKeineLektionGewaehlt.hide()
        
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

        self.sonderCheck = False #keine Sondervokabeln dabei
        self.normalCheck = False #keine normalen Vokabeln dabei

        statement = "select meintenSie, rgva, warteZeit, haeufigkeit, richtung, wiederholen, " \
                    "distanz, zeitZeigen, warteZeitRichtig from Einstellungen where id like 1"
        voreinstellungen = self.datenbank.getDataAsList(statement)

        self.zeitPro10Voks = self.datenbank.getDataAsList("select secPro10Vok from zeit")[0][0]
        #print self.zeitPro10Voks
        
        if voreinstellungen[0][0] == "True":
            self.chBMeintenSie.setChecked(True)
        else:
            self.chBMeintenSie.setChecked(False)
        
        if voreinstellungen[0][1] == "True":
            self.chBRichtigGeschriebeneAnzeigen.setChecked(True)
        else:
            self.chBRichtigGeschriebeneAnzeigen.setChecked(False)

        if voreinstellungen[0][7] == "True":
            self.chShowTime.setChecked(True)
        else:
            self.chShowTime.setChecked(False)

        self.tfZeitWarten.setText(str(voreinstellungen[0][2]))
        self.tfHaeufigkeit.setText(str(voreinstellungen[0][3]))
        self.tfDistanz.setText(str(voreinstellungen[0][6]))
        self.tfZeitWartenRichtig.setText(str(voreinstellungen[0][8]))
        
        self.richtung = voreinstellungen[0][4]
        self.labEstTime.setWordWrap(True)


        self.SpracheZeichnen()
        self.Abfragerichtung()
        self.windowAbfrage = None

    def showBottomWidget(self):

        time.sleep(5)
        self.labKeineLektionGewaehlt.hide()

    def FortsetzenDisable(self):
        self.parent.FortsetzenDisable()

    def FortsetzenEnable(self):
        self.parent.FortsetzenEnable()

    def AbfrageStarten(self):
        #Einstellungen Speichern
        if len(self.lektions_liste) > 0:
            updateStatement = "update Einstellungen set \
                                meintenSie='"+str(self.chBMeintenSie.isChecked())+"', \
                                rgva = '"+str(self.chBRichtigGeschriebeneAnzeigen.isChecked())+"', \
                                warteZeit = "+str(int(self.tfZeitWarten.text()))+", \
                                haeufigkeit = "+str(int(self.tfHaeufigkeit.text()))+", \
                                richtung = "+str(int(int(self.cBAbfragerichtung.currentIndex())+1))+", \
                                distanz = "+str(int(self.tfDistanz.text()))+",  \
                                warteZeitRichtig = "+str(int(self.tfZeitWartenRichtig.text()))+",  \
                                zeitZeigen = '"+str(self.chShowTime.isChecked())+"' \
                                where id like 1"
            self.datenbank.setData(updateStatement)
            self.close()

            self.windowAbfrage = Abfrage.Abfrage(self, self.lektions_liste, self.tfHaeufigkeit.text(),
                                    self.tfZeitWarten.text(), self.tfZeitWartenRichtig.text(),
                                    self.chBMeintenSie.isChecked(), self.chBRichtigGeschriebeneAnzeigen.isChecked(),
                                    self.cBAbfragerichtung.currentIndex()+1, self.tfDistanz.text(), self.sonderCheck)
            self.windowAbfrage.show()
        else:
            self.labKeineLektionGewaehlt.setVisible(True)
            self.labKeineLektionGewaehlt.setText(u"Es sind keine Lektionen gewählt worden. Bitte Lektion(en) hinzufügen um Abfrage starten zu können.")
            thread.start_new(self.showBottomWidget, ())

    def Abfragerichtung(self):
        #1 ist von Deutsch nach Fremd, 2 von Fremd nach Deutsch
        daten = QtCore.QStringList()
        sprachenR1 = QtCore.QString("Deutsch - "+self.cbSprache.currentText())
        #daten.append("Deutsch - "+str(self.cbSprache.currentText()))
        daten.append(sprachenR1)
        sprachenR2 = QtCore.QString(self.cbSprache.currentText()+" - Deutsch")
        #daten.append(str(self.cbSprache.currentText())+" - Deutsch")
        daten.append(sprachenR2)
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
        select_lektion = "select lektionen.name, lektionen.id, lektionen.zuletztAbgefragt from lektionen \
        join Buecher on (Buecher.id = lektionen.idBuch) \
        join Sprache on (sprache.id = buecher.id_sprache) \
        where buecher.id like "+str(self.getIdBuch())
        daten = self.datenbank.getDataAsList(select_lektion)
        liste = []
        dateList = list()
        for i in daten:
            #Vokabeln dahinter schreiben

            statement = "select count(*) from vokabeln " \
                        "join lektionen on (lektionen.id=vokabeln.idlektion) " \
                        "where idlektion like "+str(i[1])

            selection = self.datenbank.getDataAsList(statement)
            if not self.querySonderlektion(i[1]):
                if selection[0][0] > 0:
                    liste.append(i[0]+" - "+str(selection[0][0])+" Vokabeln")
                    try:
                        dateList.append(i[2])
                        #datetime.date.today()
                    except:
                        print("Datumsliste konnte nicht angelegt werden")
            else:
                statement = "select count(*) from sondervokabeln " \
                        "join lektionen on (lektionen.id=sondervokabeln.idsonderlektion) " \
                        "where lektionen.id like "+str(i[1])+" " \
                        " and lektionen.name like 'sonder%' " \
                        "and sondervokabeln.show like 1"
                selection = self.datenbank.getDataAsList(statement)
                if selection[0][0] > 0:
                    liste.append(i[0]+" - "+str(selection[0][0])+" Vokabeln")

        model = LectionsListModerQuerySettings.Markierung(liste, dateList)
        self.lvLektionen.setModel(model)
        self.lvLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)

    def querySonderlektion(self, id):
        statement = "select name from lektionen where id like "+str(id)
        data = self.datenbank.getDataAsList(statement)
        if str("sonder") in unicode(data[0][0]).lower():
            return True
        else:
            return False
    
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
        #print self.getIdLektionen()
        for i in self.getIdLektionen():
            if not self.querySonderlektion(i):
                self.normalCheck = True
            else:
                self.sonderCheck = True

        if (self.normalCheck and not self.sonderCheck) or self.sonderCheck and not self.normalCheck:
            self.lektions_liste.extend(self.getIdLektionen())
            #print self.lektions_liste
            self.AbfrageNeuZeichen()
            self.lvLektionen.clearSelection()
        else:
            self.labKeineLektionGewaehlt.setVisible(True)
            self.labKeineLektionGewaehlt.setText(u"Sonderlektionen können nicht mit normalen Lektionen vermischt werden!")
            thread.start_new(self.showBottomWidget, ())
        print("lektionslisteStop")

    def AbfrageNeuZeichen(self):
        #print self.lektionsListe
        datenliste = []
        zuletztAbgefragt = []
        for i in self.lektions_liste:
            daten = self.datenbank.getDataAsList("select Buecher.name, lektionen.name, lektionen.zuletztAbgefragt from lektionen "
                                                 "join buecher on (buecher.id=lektionen.idbuch) "
                                                 "where lektionen.id like "+str(i))
            #deutsch = str(self.tfDeutsch.text().toUtf8()).decode("utf-8").strip()
            #print daten[0][0], daten[0][1]
            datenliste.append(unicode(daten[0][0])+" - "+unicode(daten[0][1]))
            zuletztAbgefragt.append(daten[0][2])
        #Checks neu lesen
        self.sonderCheck = False
        self.normalCheck = False
        for i in self.getIdLektionen():
            if not self.querySonderlektion(i):
                self.normalCheck = True
            else:
                self.sonderCheck = True

        model = LectionsListModerQuerySettings.Markierung(datenliste, zuletztAbgefragt)
        self.lvGewaehlteLektionen.setModel(model)
        self.lvGewaehlteLektionen.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.AnzahlVokabelnPaint()

    def BuchZuAbfrageHinzu(self):
        daten = self.datenbank.getDataAsList("select lektionen.id from buecher "
                                             "join Lektionen on (lektionen.idbuch = buecher.id) "
                                             "where buecher.id like "+str(self.getIdBuch()))
        liste_zum_hinzufuegen = list()

        statement = "select buecher.name from buecher " \
                    "where id like "+str(self.getIdBuch())
        buchname = self.datenbank.getDataAsList(statement)[0][0]
        try:
            if str(buchname).lower()[:6] == "sonder":

                sonderbuch = True
            else:
                sonderbuch = False
        except:
            sonderbuch = False

        print "sondercheck: "+str(self.sonderCheck)
        print "sonderbuch: "+str(sonderbuch)
        print "normalCheck: "+str(self.normalCheck)

        if not self.sonderCheck and not sonderbuch:

            for i in daten:
                liste_zum_hinzufuegen.append(i[0])

            self.lektions_liste.extend(liste_zum_hinzufuegen)
            #print self.lektionsListe

            self.AbfrageNeuZeichen()
            self.normalCheck = True
        elif not self.normalCheck and sonderbuch:
            for i in daten:
                liste_zum_hinzufuegen.append(i[0])

            self.lektions_liste.extend(liste_zum_hinzufuegen)
            #print self.lektionsListe

            self.AbfrageNeuZeichen()
            self.sonderCheck = True
        else:
            self.labKeineLektionGewaehlt.setVisible(True)
            self.labKeineLektionGewaehlt.setText(u"Sonderlektionen können nicht mit normalen Lektionen vermischt werden!")
            thread.start_new(self.showBottomWidget, ())

    def ListeZuSql(self, liste, args):
        statement = "where "
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]

    def LektionTrennen(self):
        pop_liste = []

        for i in self.lvGewaehlteLektionen.selectedIndexes():

            pop_liste.append(i.row())

        pop_liste = sorted(pop_liste, reverse=True)
        for i in pop_liste:
            self.lektions_liste.pop(i)

        self.AbfrageNeuZeichen()

    def anzVokabeln(self):
        counter = 0
        for i in self.lektions_liste:
            if not self.querySonderlektion(i):
                statement = "select count(*) from lektionen " \
                            "join vokabeln on (vokabeln.idlektion=lektionen.id) " \
                            "where lektionen.id like "+str(i)
            else:
                statement = "select count(*) from lektionen " \
                            "join sondervokabeln on (sondervokabeln.idsonderlektion=lektionen.id) " \
                            "where lektionen.id like "+str(i)+" " \
                            " and sondervokabeln.show like 1"
                #print statement


            counter += self.datenbank.getDataAsList(statement)[0][0]
        return counter

    def AnzahlVokabelnPaint(self):
        counter = self.anzVokabeln()
        self.labAnzahlVokabeln.setText(u"Anzahl Vokabeln:"+str(counter))
        self.AnzahlAbfragenPaint()

    def AnzahlAbfragenPaint(self):
        counter = self.anzVokabeln()
            
        if self.tfHaeufigkeit.text() == '':
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: 0")
        else:
            mal = int(counter)*int(self.tfHaeufigkeit.text())
            self.labAnzahlAbfragen.setText("Anzahl Abfragen: "+str(mal))
            AbfrageZeit = mal * self.zeitPro10Voks/10
            #print AbfrageZeit
            text = self.zeitRechner(round(AbfrageZeit, 0))
            self.labEstTime.setText("erwartete Zeit: " +str(text))

    def zeitRechner(self, inSekunden):
        stunden, rest = divmod(inSekunden, 3600)
        minuten, rest = divmod(rest, 60)
        sekunden = rest

        if stunden <= 9:
            stunden = "0"+str(int(stunden))
        else:
            stunden = int(stunden)

        if minuten <= 9:
            minuten = "0"+str(int(minuten))
        else:
            minuten = int(minuten)

        if sekunden <= 9:
            sekunden = "0"+str(int(sekunden))
        else:
            sekunden = int(sekunden)
        #print str(stunden)+":"+str(minuten)+":"+str(sekunden)
        return str((stunden))+":"+str((minuten))+":"+str((sekunden))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Right:
            self.LektionZuAbfrageHinzu()