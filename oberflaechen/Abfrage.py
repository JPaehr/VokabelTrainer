# -*- coding: utf-8 -*-
from __future__ import division
"""
Created on 08.10.2013

@author: Johannes
"""
from PyQt4 import QtGui, QtCore
from windows.WindowAbfrage import Ui_Form as WindowAbfrage
import models.base as Datenbank
import models.Leve as leve
from time import sleep
from random import shuffle as zufall
from oberflaechen.MeintenSie import MeintenSie
from oberflaechen.Auswertung import Auswertung
import oberflaechen.AbfrageEinstellungen

from models.Speicher import Speicher
import pickle


class ZeitThread(QtCore.QThread):
    def __init__(self, zeit):
        QtCore.QThread.__init__(self)
        self.zeit = zeit
        
    def run(self):
        """
        überschrieben runMethode aus QThread
        """
        sleep(self.zeit)
        #print "Thread ist fertig"
        return  
 

class Abfrage(WindowAbfrage, QtGui.QWidget):
    """
    Fenster für die Abfrage
    """
    def __init__(self, parent, lektionen_ids, abfrage_haeufigkeit, verzoegerung, meintenSie, RichtigeAnzeigen, Richtung, distanz, speicher='None'):
        super(Abfrage, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        self.pBFortschritt.hilfsWidgets(self.hilfsWidget1, self.hilfsWidget2)

        self.cBPunkte.setCheckState(QtCore.Qt.Checked)

        self.labWeitereVokabeln.addWidgetToShow(self.pBFortschritt, self.hilfsWidget1, self.hilfsWidget2)

        self.labWeitereVokabeln.hide()
        self.pBFortschritt.addWidgetToShow(self.labWeitereVokabeln)


        self.cBPunkte.stateChanged.connect(self.sichtbarPunkte)

        self.font_dick = QtGui.QFont()
        self.font_dick.setBold(True)
        self.font_normal = QtGui.QFont()


        if speicher is 'None':
            open('zwischenSpeicher.fs', 'w').close()
            self.pBFortschritt.setValue(0)
            self.distance = distanz
            self.treffer = leve.Treffer(distanz)
            zeit = float(verzoegerung)*10**(-3)
            self.thread = ZeitThread(zeit)
            self.meinten_sie = meintenSie
            self.lektionsliste = []
            self.verzoegerung = verzoegerung
            self.id_aktuell = 0
            self.vokabel_fremd = ""
            self.richtige_anzeigen = RichtigeAnzeigen
            self.richtung = Richtung
            self.labPunkte.setText('0')
            self.lektion = ""
            self.buch = ""
            self.vokabel_deutsch = ""
            self.vokabel_ids = self.lektionsid_to_vokid(lektionen_ids, int(abfrage_haeufigkeit))
            #self.abfragenGesamt = int(len(self.vokabel_ids)*int(abfrage_haeufigkeit))
            self.abfragenGesamt = len(self.vokabel_ids)
            self.lektion_ids = lektionen_ids
        else:
            file = open('zwischenSpeicher.fs', 'r')
            speicher = pickle.load(file)
            file.close()

            self.pBFortschritt.setValue(speicher.Fortschritt)
            self.distance = speicher.distance
            self.treffer = leve.Treffer(speicher.distance)
            zeit = float(speicher.verzoegerung)*10**(-3)
            self.thread = ZeitThread(zeit)
            self.meinten_sie = speicher.meinten_sie
            self.lektionsliste = []
            self.verzoegerung = speicher.verzoegerung
            self.id_aktuell = speicher.id_aktuell
            #print "danach: "+str(speicher.id_aktuell)
            self.vokabel_fremd = ""
            self.richtige_anzeigen = speicher.richtige_anzeigen
            self.richtung = speicher.richtung
            self.labPunkte.setText(speicher.labPunkte)
            self.lektion = ""
            self.buch = ""
            self.vokabel_deutsch = ""
            self.vokabel_ids = speicher.vokabel_ids
            self.abfragenGesamt = speicher.abfragenGesamt
            self.lektion_ids = speicher.lektion_ids
            self.vokabel_fremd = speicher.vokabel_fremd
            self.vokabel_deutsch = speicher.vokabel_deutsch
            self.buch = speicher.buch
            self.lektion = speicher.lektion

            self.labLektion.setText(unicode(self.lektion))
            self.labBuch.setText(str(self.buch))
            self.labRichtigFalsch.setText("")
            self.labBitteEingeben.setText("Bitte eingeben")
            self.labWeitereVokabeln.setText("Noch "+str(len(self.vokabel_ids)-self.id_aktuell-1)+" weitere Vokabeln")

            if self.richtung == 1:
                self.labVokabelMeintenSie.setText(self.vokabel_deutsch)
            else:
                self.labVokabelMeintenSie.setText(self.vokabel_fremd)
            self.labMeintenSie.setText("")
            self.labMeintenSie.setText("")

            #speicher.Info()
        spracheid_statement = "select sprache.id from sprache \
            join buecher on (sprache.id=buecher.id_sprache) \
            join lektionen on (lektionen.idBuch = buecher.id) \
            join vokabeln on (vokabeln.idlektion=lektionen.id) where vokabeln.id like " +str(self.vokabel_ids[0]) +" limit 1"
        #print self.spracheid_statement

        self.spracheid = self.datenbank.getDataAsList(spracheid_statement)[0][0]

        self.parent = parent

        self.connect(self.btnSaveExit, QtCore.SIGNAL("clicked()"), self.SaveAndExit)
        self.connect(self.thread, QtCore.SIGNAL("finished()"), self.weitere_vokabel)
        self.connect(self.btnWeiter, QtCore.SIGNAL("clicked()"), self.weitereVokabelKlick)
        self.btnWeiter.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return))


        if speicher is 'None':
            self.weitere_vokabel()

    def sichtbarBar(self):
        if self.cBBar.checkState():
            self.pBFortschritt.setVisible(1)
        else:
            self.pBFortschritt.hide()

    def SaveAndExit(self):
        #self,pBFortschritt, distance, meintenSie, verzoegerung, id_aktuell, richtige_anzeigen, richtung, labPunkte, vokIds, abfragenGesamt, lektionen_ids, lektion, vokabel_deutsch, vokabel_fremd, buch
        print type(self.distance)
        meinSpeicher = Speicher(self.pBFortschritt.value(), str(self.distance), str(self.meinten_sie), self.verzoegerung, self.id_aktuell, self.richtige_anzeigen, self.richtung,
                                self.labPunkte.text(), self.vokabel_ids, self.abfragenGesamt, self.lektion_ids, self.lektion, self.vokabel_deutsch, self.vokabel_fremd, self.buch)

        f = open("zwischenSpeicher.fs", 'w')
        pickle.dump(meinSpeicher, f)
        f.close()
        print "Dumped"

        self.datenbank.setData("update AbfrageFortsetzen set datum = datetime() where id like 1")

        self.FortsetzenEnable()
        #self.parent.btnFortsetzen.setVisible(True)

        #self.parent.hide()
        self.close()

    def sichtbarPunkte(self):
        if self.cBPunkte.checkState():
            self.labPunkte.setVisible(1)
        else:
            self.labPunkte.hide()


    def weitere_vokabel(self):
        """
        weitere Vokabel ziehen
        """
        if self.id_aktuell < len(self.vokabel_ids):

            daten = self.datenbank.getDataAsList("select lektionen.name, vokabeln.deutsch, vokabeln.fremd, buecher.name from vokabeln\
            join lektionen on (lektionen.id=vokabeln.idlektion) \
            join buecher on (buecher.id=lektionen.idBuch) \
            where vokabeln.id like "+str(self.vokabel_ids[self.id_aktuell]))
            self.lektion = daten[0][0]
            self.vokabel_deutsch = unicode(daten[0][1])
            self.vokabel_fremd = daten[0][2]
            self.buch = daten[0][3]

            if self.richtung == 1:
                self.labVokabelMeintenSie.setText(self.vokabel_deutsch)
            else:
                self.labVokabelMeintenSie.setText(self.vokabel_fremd)
            
            self.labLektion.setText(unicode(self.lektion))
            self.labBuch.setText(str(self.buch))
            self.labRichtigFalsch.setText("")
            self.labBitteEingeben.setText("Bitte eingeben")
            self.labWeitereVokabeln.setText("Noch "+str(len(self.vokabel_ids)-self.id_aktuell-1)+" weitere Vokabeln")

            print str((self.abfragenGesamt-(len(self.vokabel_ids)-self.id_aktuell)) / self.abfragenGesamt*100)
            print "AbfrgaenGesamt: "+ str(self.abfragenGesamt)
            print "id_aktuell: "+ str(self.id_aktuell)
            print "Vokabelids: "+ str(self.vokabel_ids)

            print "progressbar wird gesetzt auf:", int(round(float(str((self.abfragenGesamt-(len(self.vokabel_ids)-self.id_aktuell)) / self.abfragenGesamt*100)), 0))
            self.pBFortschritt.setValue(int(round(float(str((self.abfragenGesamt-(len(self.vokabel_ids)-self.id_aktuell)) / self.abfragenGesamt*100)), 0)))

            self.tfInput.setText("")
            self.tfInput.setFocus()    
            self.labMeintenSie.setText("")
            
            self.id_aktuell += 1
        else:
            print "fertig mit Abfragen"
            self.FortsetzenDisable()
            open("zwischenSpeicher.fs", 'w').close()


            self.close()
            test = Auswertung(self, self.labPunkte.text(), len(self.vokabel_ids), self.lektion_ids)
            test.show()

    def lektionsid_to_vokid(self, idliste, haeufigkeit):
        """
        zu lektions id gibts die Vokabelid
        """
        vokabelIds = []    
        for i in idliste:
            daten = self.datenbank.getDataAsList("select vokabeln.id from vokabeln \
            join lektionen on (vokabeln.idlektion=lektionen.id) where lektionen.id like "+str(i))
            for n in daten:
                for k in range(haeufigkeit):
                    vokabelIds.append(n[0])

        zufall(vokabelIds)
        print vokabelIds
        return vokabelIds

    def FortsetzenDisable(self):
        self.parent.FortsetzenDisable()
    def FortsetzenEnable(self):
        self.parent.FortsetzenEnable()
    def weitereVokabelKlick(self):
        
        self.thread.start()
        if self.richtung == 1:
            #print type(self.vokabelFremd)
            #print type(str(self.tfInput.text().toUtf8()).decode("utf-8"))
            if self.vokabel_fremd == str(self.tfInput.text().toUtf8()).decode("utf-8"):
                self.labRichtigFalsch.setText("Richtig")
                self.labPunkte.setText(str(float(self.labPunkte.text()) + 1))
            else:
                self.labRichtigFalsch.setText("Falsch")
                if self.richtige_anzeigen:
                    self.labBitteEingeben.setText(u"Richtig wäre: "+self.vokabel_fremd)
                if self.meinten_sie:

                    statement = "select vokabeln.fremd, vokabeln.id from sprache \
                                join buecher on (sprache.id=buecher.id_sprache) \
                                join lektionen on (lektionen.idBuch = buecher.id) \
                                join vokabeln on (vokabeln.idlektion=lektionen.id) where sprache.id like " +str(self.spracheid)
                    liste = self.datenbank.getDataAsList(statement)
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.treffer.setAktVergleich(liste, unicode(self.tfInput.text()), self.vokabel_ids[self.id_aktuell-1], 1)

                    daten = self.datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+self.ListeZuSql(self.treffer.getTreffer(), " id "))

                    if self.treffer.directStrike():
                        #print "direkterTreffer"
                        self.labRichtigFalsch.setText("fast richtig")
                        self.labPunkte.setText(str(float(self.labPunkte.text()) + 0.5))

                    else:
                        """if(len(daten) == 1):
                            self.labMeintenSie.setText("Meinten Sie: "+unicode(daten[0][1])+" - "+unicode(daten[0][0]))
                        """    
                        liste = []
                        for i in daten:
                            liste.append(unicode(i[1])+" - "+unicode(i[0]))
                        #print "Fenster auf"
                        
                        if len(liste) > 1:
                            test = MeintenSie(self, liste)
                            test.show()
                        if len(liste) == 1:
                            self.labMeintenSie.setText("Meinten Sie: "+unicode(liste[0]))
                        
                    """
                    daten = self.Datenbank.getDataAsList(u"select fremd, deutsch from vokabeln \
                    where fremd like '"+str(self.tfInput.text().toUtf8).decode('utf-8')+"' or deutsch like '"+str(self.tfInput.text().toUtf8()).decode("utf-8")+"'")
                    if(len(daten) > 0):
                        self.labMeintenSie.setText(u"Meinten Sie: "+daten[0][1]+" - "+daten[0][0])
                        """
        else:
            #print "vergleich zwischen " + self.Vergeleichsfaehigkeit(self.vokabelDeutsch)
            #print self.Vergeleichsfaehigkeit(str(self.tfInput.text().toUtf8()).decode('utf-8'))
            if self.Vergeleichsfaehigkeit(self.vokabel_deutsch) == self.Vergeleichsfaehigkeit(str(self.tfInput.text().toUtf8()).decode('utf-8')):
                self.labRichtigFalsch.setText("Richtig")
                self.labPunkte.setText(str(float(self.labPunkte.text()) + 1))
            else:
                self.labRichtigFalsch.setText("Falsch")
                if self.richtige_anzeigen:
                    self.labBitteEingeben.setText(unicode(u"Richtig wäre: ")+str(self.vokabel_deutsch))
                if self.meinten_sie:
                    #print "meintenSie Aktiv"
                    statement = "select vokabeln.deutsch, vokabeln.id from sprache \
                                join buecher on (sprache.id=buecher.id_sprache) \
                                join lektionen on (lektionen.idBuch = buecher.id) \
                                join vokabeln on (vokabeln.idlektion=lektionen.id) where sprache.id like " +str(self.spracheid)
                    liste = self.datenbank.getDataAsList(statement)# \
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.treffer.setAktVergleich(liste, unicode(self.tfInput.text()), self.vokabel_ids[self.id_aktuell-1], 2)
                    
                
                    
                
                    daten = self.datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+ self.ListeZuSql(self.treffer.getTreffer(), " id "))
                    
                    """
                    if(len(daten) > 0):
                        self.labMeintenSie.setText("Meinten Sie: "+unicode(daten[0][0])+" - "+unicode(daten[0][1]))
                    """
                    if self.treffer.directStrike():
                        #print "direkter treffer"
                        self.labRichtigFalsch.setText("fast richtig")
                        self.labPunkte.setText(str(float(self.labPunkte.text()) + 0.5))
                    else:
                        #print "das Fensterding"
        
                        liste = []
                        for i in daten:
                            liste.append(unicode(i[1])+" - "+unicode(i[0]))
                        #print "Fenster auf"
                        if len(liste) > 1:
                            test = MeintenSie(self, liste)
                            test.show()
                        if len(liste) == 1:
                            self.labMeintenSie.setText("Meinten Sie: "+unicode(liste[0]))
                            
    def Vergeleichsfaehigkeit(self, kette):
        
        #print "typen type:" + str(type(kette))
        
        if "(" in kette:
            kette = kette[:kette.find("(")]
        kette = kette.replace(",", "")
        kette = kette.replace(".", "")
        kette = kette.replace("!", "")
        kette = kette.replace("?", "")
        kette = kette.lower()
        kette = kette.strip()
        
        return kette
         
    def ListeZuSql(self, liste, args, where=True):
        if where:
            statement = "where "
        else:
            statement = ""
            
        if len(liste) < 1:
            statement += args+" like 'nix'   "
        for i in liste:
            statement += args+" like "+str(i)+" or "
        return statement[:-3]    