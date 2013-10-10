'''
Created on 10.10.2013

@author: Johannes
'''
from models import ListModel
from PyQt4 import QtCore, QtGui
from models.ListModel import Markierung

class ListModelMeintenSie(Markierung):
    
    def flags(self, index):
        
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled

    