# -*- coding: utf-8 -*-
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
from oberfaechen.MeintenSie import MeintenSie


class ZeitThread(QtCore.QThread):
    def __init__(self, zeit):
        QtCore.QThread.__init__(self)
        self.zeit = zeit
        
    def run(self):
        """
        überschrieben runMethode aus QThread
        """
        sleep(self.zeit)
        print "Thread ist fertig"
        return  
 

class Abfrage(WindowAbfrage, QtGui.QWidget):
    """
    Fenster für die Abfrage
    """
    def __init__(self, parent, lektionen_ids, abfrage_haeufigkeit, verzoegerung, meintenSie, RichtigeAnzeigen, Richtung, distanz):
        super(Abfrage, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        
        self.font_dick = QtGui.QFont()
        self.font_dick.setBold(True)
        self.font_normal = QtGui.QFont()

        self.treffer = leve.Treffer(distanz)
           
        zeit = float(verzoegerung)*10**(-3)  
        self.thread = ZeitThread(zeit)
        
        self.parent = parent
        
        self.connect(self.thread, QtCore.SIGNAL("finished()"), self.weitere_vokabel)
        self.connect(self.btnWeiter, QtCore.SIGNAL("clicked()"), self.weitereVokabelKlick)
        self.btnWeiter.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return))
        
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
        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        
        self.vokabel_ids = self.lektionsid_to_vokid(lektionen_ids, int(abfrage_haeufigkeit))
        
        self.weitere_vokabel()
        
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
            
            #print "Richtung: ", self.Richtung
            
            if self.richtung == 1:
                self.labVokabelMeintenSie.setText(self.vokabel_deutsch)
            else:
                self.labVokabelMeintenSie.setText(self.vokabel_fremd)
            
            self.labLektion.setText(str(self.lektion))
            self.labBuch.setText(str(self.buch))
            self.labRichtigFalsch.setText("")
            self.labBitteEingeben.setText("Bitte eingeben")
            self.labWeitereVokabeln.setText("Noch "+str(len(self.vokabel_ids)-self.id_aktuell-1)+" weitere Vokabeln")
            self.tfInput.setText("")
            self.tfInput.setFocus()    
            self.labMeintenSie.setText("")
            
            self.id_aktuell +=1
        else:
            print "fertig mit Abfragen"

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
                    liste = self.datenbank.getDataAsList("select fremd, id from vokabeln")# \
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.treffer.setAktVergleich(liste, unicode(self.tfInput.text()), self.vokabel_ids[self.id_aktuell-1], 1)
                    
                   
                    daten = self.datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+ self.ListeZuSql(self.treffer.getTreffer(), " id "))
                    
                    
                    
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
                    liste = self.datenbank.getDataAsList("select deutsch, id from vokabeln")# \
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