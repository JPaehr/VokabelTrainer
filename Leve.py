#-*- coding:utf-8 -*-
'''
Created on 07.10.2013

@author: Johannes
'''
import Levenshtein as leve
import base as Datenbank


class Treffer(object):
    def __init__(self):
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
    
    def setAktVergleich(self, liste, wort):
        #liste vokabeln und id
        self.liste = liste
        self.wort = wort
        
    def getTreffer(self): 
        #liste von ids wird zurückgegeben
        rueckgabe = []
        for i in self.liste:
            #print "Aktueller vergleich "+unicode(i[0]) +" und "+unicode(self.wort)
            if leve.distance(i[0], self.wort) <= 2:
                rueckgabe.append(i[1])
        return rueckgabe
                
                
