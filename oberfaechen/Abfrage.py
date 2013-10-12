# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowAbfrage import Ui_Form as WindowAbfrage
import models.base as Datenbank
import models.Leve as leve
import thread
from time import sleep
from random import shuffle as zufall
from oberfaechen.MeintenSie import MeintenSie

class ZeitThread(QtCore.QThread):
    def __init__(self, zeit):
        QtCore.QThread.__init__(self)
        self.zeit = zeit
        
    def run(self):
        sleep(self.zeit)
        print "Thread ist fertig"
        return  
 

class Abfrage(WindowAbfrage, QtGui.QWidget):
    def __init__(self, parent, lektionenIds, AbfrageHaeufigkeit, verzoegerung, meintenSie, RichtigeAnzeigen, Richtung, distanz):
        super(Abfrage, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)
        
        self.Treffer = leve.Treffer(distanz)
           
        zeit = float(verzoegerung)*10**(-3)  
        self.thread = ZeitThread(zeit)
        
        self.parent = parent
        
        self.connect(self.thread, QtCore.SIGNAL("finished()"), self.weitereVokabel)
        self.connect(self.btnWeiter, QtCore.SIGNAL("clicked()"), self.weitereVokabelKlick)
        
        self.meintenSie = meintenSie
        self.Lektionsliste = []
        self.verzoegerung = verzoegerung
        self.idAktuell = 0
        self.RichtigeAnzeigen = RichtigeAnzeigen
        self.Richtung = Richtung
        self.labPunkte.setText('0')
        
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite") 
        
        self.vokabelIds = self.LektionsIdToVokId(lektionenIds, int(AbfrageHaeufigkeit))
        
        self.weitereVokabel()
        
    def weitereVokabel(self):
        if self.idAktuell < len(self.vokabelIds):
            
        
            daten = self.Datenbank.getDataAsList("select lektionen.name, vokabeln.deutsch, vokabeln.fremd, buecher.name from vokabeln\
            join lektionen on (lektionen.id=vokabeln.idlektion) \
            join buecher on (buecher.id=lektionen.idBuch) \
            where vokabeln.id like "+str(self.vokabelIds[self.idAktuell]))
            self.lektion = daten[0][0]
            self.vokabelDeutsch = unicode(daten[0][1])
            self.vokabelFremd = daten[0][2]
            self.Buch = daten[0][3]
            
            print "Richtung: ", self.Richtung
            
            if self.Richtung == 1:
                self.labVokabelMeintenSie.setText(self.vokabelDeutsch)
            else:
                self.labVokabelMeintenSie.setText(self.vokabelFremd)
            
            self.labLektion.setText(str(self.lektion))
            self.labBuch.setText(str(self.Buch))
            self.labRichtigFalsch.setText("")
            self.labBitteEingeben.setText("Bitte eingeben")
            self.labWeitereVokabeln.setText("Noch "+str(len(self.vokabelIds)-self.idAktuell-1)+" weitere Vokabeln")
            self.tfInput.setText("")
            self.tfInput.setFocus()    
            self.labMeintenSie.setText("")
            
            self.idAktuell +=1
        else:
            print "fertig mit Abfragen"
    def LektionsIdToVokId(self, idliste, haeufigkeit):
            
        vokabelIds = []    
        for i in idliste:
            daten = self.Datenbank.getDataAsList("select vokabeln.id from vokabeln \
            join lektionen on (vokabeln.idlektion=lektionen.id) where lektionen.id like "+str(i))
            for n in daten:
                for k in range(haeufigkeit):
                    vokabelIds.append(n[0])
             
            
        zufall(vokabelIds)
        print vokabelIds
        return vokabelIds
    def weitereVokabelKlick(self):
        
        self.thread.start()
        if self.Richtung == 1:
            #print type(self.vokabelFremd)
            #print type(str(self.tfInput.text().toUtf8()).decode("utf-8"))
            if self.vokabelFremd == str(self.tfInput.text().toUtf8()).decode("utf-8"):
                self.labRichtigFalsch.setText("Richtig")
                self.labPunkte.setText(str(float(self.labPunkte.text()) + 1))
            else:
                self.labRichtigFalsch.setText("Falsch")
                if self.RichtigeAnzeigen:
                    self.labBitteEingeben.setText(u"Richtig währe: "+self.vokabelFremd)
                if self.meintenSie:
                    liste = self.Datenbank.getDataAsList("select fremd, id from vokabeln")# \
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.Treffer.setAktVergleich(liste, unicode(self.tfInput.text()), self.vokabelIds[self.idAktuell-1], 1)
                    
                   
                    daten = self.Datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+ self.ListeZuSql(self.Treffer.getTreffer(), " id "))
                    
                    
                    if(len(daten) > 0):
                        self.labMeintenSie.setText("Meinten Sie: "+unicode(daten[0][1])+" - "+unicode(daten[0][0]))
                    
                    if self.Treffer.directStrike():
                        #print "direkterTreffer"
                        self.labRichtigFalsch.setText("fast richtig")
                        self.labPunkte.setText(str(float(self.labPunkte.text()) + 0.5))
                        
                    
                    else:
                        liste = []
                        for i in daten:
                            liste.append(str(i[1])+" - "+str(i[0]))
                        #print "Fenster auf"
                        test = MeintenSie(self, liste)
                        test.show()
                        
                    """
                    daten = self.Datenbank.getDataAsList(u"select fremd, deutsch from vokabeln \
                    where fremd like '"+str(self.tfInput.text().toUtf8).decode('utf-8')+"' or deutsch like '"+str(self.tfInput.text().toUtf8()).decode("utf-8")+"'")
                    if(len(daten) > 0):
                        self.labMeintenSie.setText(u"Meinten Sie: "+daten[0][1]+" - "+daten[0][0])
                        """
        else:
            print "vergleich zwischen " + self.Vergeleichsfaehigkeit(self.vokabelDeutsch)
            print self.Vergeleichsfaehigkeit(str(self.tfInput.text().toUtf8()).decode('utf-8'))
            if self.Vergeleichsfaehigkeit(self.vokabelDeutsch) == self.Vergeleichsfaehigkeit(str(self.tfInput.text().toUtf8()).decode('utf-8')):
                self.labRichtigFalsch.setText("Richtig")
                self.labPunkte.setText(str(float(self.labPunkte.text()) + 1))
            else:
                self.labRichtigFalsch.setText("Falsch")
                if self.RichtigeAnzeigen:
                    self.labBitteEingeben.setText(unicode("Richtig währe: ")+str(self.vokabelDeutsch))
                if self.meintenSie:
                    #print "meintenSie Aktiv"
                    liste = self.Datenbank.getDataAsList("select deutsch, id from vokabeln")# \
                    #where deutsch like '"+str(self.tfInput)+"'")
                    #print liste
                    self.Treffer.setAktVergleich(liste, unicode(self.tfInput.text()), self.vokabelIds[self.idAktuell-1], 2)
                    
                
                    
                
                    daten = self.Datenbank.getDataAsList("select fremd, deutsch from vokabeln \
                    "+ self.ListeZuSql(self.Treffer.getTreffer(), " id "))
                    
                    
                    if(len(daten) > 0):
                        self.labMeintenSie.setText("Meinten Sie: "+unicode(daten[0][0])+" - "+unicode(daten[0][1]))
    
                    if self.Treffer.directStrike():
                        #print "direkter treffer"
                        self.labRichtigFalsch.setText("fast richtig")
                        self.labPunkte.setText(str(float(self.labPunkte.text()) + 0.5))
                    else:
                        #print "das Fensterding"
        
                        liste = []
                        for i in daten:
                            liste.append(str(i[1])+" - "+str(i[0]))
                        #print "Fenster auf"
                        test = MeintenSie(self, liste)
                        test.show()
    def Vergeleichsfaehigkeit(self, kette):
        
        print "typen type:" + str(type(kette))
        
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