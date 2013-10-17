# -*- coding: utf-8 -*-
'''
Created on 08.10.2013

@author: Johannes
'''
from PyQt4 import QtGui, QtCore
from windows.WindowLektionAnlegen import Ui_LektionAnlegen as WindowLektionAnlegen
import models.base as Datenbank

class NeueLektion(WindowLektionAnlegen, QtGui.QWidget):
    def __init__(self, parent):
        super(NeueLektion, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent=None)
        self.setupUi(self)      
        self.Datenbank = Datenbank.base("VokabelDatenbank.sqlite")
         
        self.connect(self.btnAbbrechn, QtCore.SIGNAL("clicked()"), QtCore.SLOT("close()"))
        self.connect(self.btnAnwenden, QtCore.SIGNAL("clicked()"), self.LektionAnlegen)
        self.connect(self.btnAnwendenSchliessen, QtCore.SIGNAL("clicked()"), self.LektionAnlegenUndSchliessen)
        self.connect(self.cBSprache, QtCore.SIGNAL("activated(int)"), self.LektionenNeueSchreiben)

        datenSprache = self.Datenbank.getDataAsQStringList("select fremdsprache, id from SPRACHE")
        modelSprache = QtGui.QStringListModel(datenSprache)
        self.cBSprache.setModel(modelSprache)
        
        self.LektionenNeueSchreiben()
        
        
    def LektionenNeueSchreiben(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        datenBuch = self.Datenbank.getDataAsQStringList("select Buecher.name, Buecher.id from Buecher \
        join sprache on (sprache.id=Buecher.id_sprache) \
        where Sprache.id like "+str(datenidSprache[0][1]))
        modelBuch = QtGui.QStringListModel(datenBuch)
        self.cBBuch.setModel(modelBuch)
        
    def LektionAnlegen(self):
        datenidSprache = self.Datenbank.getDataAsList("select fremdsprache, id from SPRACHE \
        limit '"+str(self.cBSprache.currentIndex())+"', '"+str(self.cBSprache.currentIndex()+1)+"'") 
        
        datenidBuch =  self.Datenbank.getDataAsList("select Buecher.name, Buecher.id from Buecher \
        join sprache on (sprache.id=Buecher.id_sprache) where Sprache.id like "+str(datenidSprache[0][1])+"\
        limit '"+str(self.cBBuch.currentIndex())+"', '"+str(self.cBBuch.currentIndex()+1)+"'")
        idSprache = datenidSprache[0][1]
        idBuch = int(datenidBuch[0][1])
        
        self.Datenbank.setData(u"insert into Lektionen (name, idBuch) \
        values ('"+str(self.tfLektion.text().toUtf8()).decode('utf-8')+"', '"+str(idBuch)+"')")

        self.tfLektion.setText("")
        self.tfLektion.setFocus()
    
    def LektionAnlegenUndSchliessen(self):
        self.LektionAnlegen()
        self.close()