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
    
    def setAktVergleich(self, liste, wort, id, richtung):
        #liste vokabeln und id
        self.id = id
        self.richtung = richtung
        self.liste = liste
        self.wort = wort
        self.direktTreffer = False
    def directStrike(self):
        print "directStrike gemacht"
        if self.direktTreffer:
            return True
        else:
            return False
        
    def getTreffer(self): 
        #liste von ids wird zurückgegeben
        print "get Treffer"
        
        daten = self.Datenbank.getDataAsList("select deutsch, fremd from vokabeln where id like "+ str(self.id))
        
        print "vergleich zwischen "+str(daten[0][1]) +" und "+str(self.wort)
        
        if self.richtung == 1:
            if leve.distance(daten[0][1], self.wort) <= self.distanz:
                self.direktTreffer = True
                print self.id
                return [self.id]
        else:
            if leve.distance(daten[0][0], self.wort) <= self.distanz:
                self.direktTreffer = True
                print self.id
                return [self.id] 

       
        rueckgabe = []
        for i in self.liste:
            #print "Aktueller vergleich "+unicode(i[0]) +" und "+unicode(self.wort)
            if leve.distance(i[0], self.wort) <= self.distanz:
                rueckgabe.append(i[1])
        return rueckgabe
                
   
   