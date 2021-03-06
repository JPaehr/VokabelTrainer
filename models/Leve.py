#-*- coding:utf-8 -*-
'''
Created on 07.10.2013

@author: Johannes
'''
import Levenshtein as leve
import base as Datenbank


class Treffer(object):
    def __init__(self, distanz):
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
        self.distanz = distanz
        self.minTreffer = self.Datenbank.getDataAsList("select mindesttreffer from Einstellungen")[0][0]
    def setAktVergleich(self, liste, wort, ids, richtung):
        #print "Akutelle id "+str(ids)
        #liste vokabeln und id
        self.ids = ids
        self.richtung = richtung
        self.liste = liste
        self.wort = wort
        self.direktTreffer = False
    def directStrike(self):
        if self.direktTreffer:
            #print "directStrike gemacht"
            return True
        else:
            #print "directStrike gefailt"
            return False
        
    def getTreffer(self): 
        #liste von ids wird zurückgegeben
        #print "get Treffer"
        
        daten = self.Datenbank.getDataAsList("select deutsch, fremd from vokabeln where id like "+ str(self.ids))
        
        #print "vergleich zwischen "+str(daten[0][1]) +" und "+str(self.wort)
        
        if self.richtung == 1:
            if leve.distance(daten[0][1], self.wort) <= int(self.distanz) and leve.jaro(daten[0][1], self.wort) > round((self.minTreffer/100), 2):
                self.direktTreffer = True
                #print self.ids
                return [self.ids]
        else:
            if leve.distance(self.Vergeleichsfaehigkeit(daten[0][0]), self.Vergeleichsfaehigkeit(self.wort)) <= int(self.distanz) \
                    and leve.jaro(self.Vergeleichsfaehigkeit(daten[0][0]), self.Vergeleichsfaehigkeit(self.wort)) > round((self.minTreffer/100), 2):
                #print "Leven Vergleich zwischen "+ str(daten[0][0])+ " und "+ str(self.wort)
                self.direktTreffer = True
                #print self.id
                return [self.ids] 

       
        rueckgabe = []
        for i in self.liste:
            #print "Aktueller vergleich "+unicode(i[0]) +" und "+unicode(self.wort)
            if leve.distance(i[0], self.wort) <= int(self.distanz) and leve.jaro(i[0], self.wort) > 0.7:
                rueckgabe.append(i[1])
        return rueckgabe
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