import sqlite3
from PyQt4 import QtCore
class base:

	def __init__(self, dataBaseName):
		self.connection = sqlite3.connect(dataBaseName)
		self.cursor = self.connection.cursor()
			
	def create(self, statement):
		self.cursor.execute(statement)

		print "DB create: ", statement
	def getDataAsTupel(self, statement):
	
		return self.cursor.execute(statement)
		
	def getDataAsList(self, statement):
		#print statement
		self.cursor.execute(statement)
		#print self.cursor.fetchall()
		return self.cursor.fetchall()
		
	
	def setData(self, statement):
		#print "setData empfaegt: ", statement
		self.cursor.execute(statement)
		self.connection.commit()
		#print "setDataFunkt: ", statement
	
	def delData(self, statement):
		self.cursor.execute(statement)
		self.connection.commit()		
		#print "delData: ", statement, " successfully"
	
	def getDataAsQStringList(self, statement):
		liste = QtCore.QStringList()
		Tupels = self.getDataAsList(statement)
		
		for i in Tupels:
			liste.append(i[0])
			
		return liste