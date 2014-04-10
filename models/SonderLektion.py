#-*- coding: utf-8 -*-
__author__ = 'JPaehr'
import models.base as Datenbank

class SonderFall(object):

    def __init__(self, vokabelId, lektionsId):
        self.vokabelId = vokabelId
        self.lekionsId = lektionsId

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        """
        0 - nicht falsch
        1 - einmal falsch
        2 - zweimal falsch
        3 - dreimal falsch - >sonderlektion
        4 - sonderlektion + einmal richtig
        5 - sonderlektion + zweimal richtig
        6 - sonderlektion löschen -> neuer status 0 -> punkt 6 wird nie erreicht

        """

    def falsch(self):

        status = self.datenbank.getDataAsList("select status from vokabeln where id like "+str(self.vokabelId))[0][0]

        if status == 0:
            self.setNewStatus(1)
        elif status == 1:
            self.setNewStatus(2)
        elif status == 2:
            self.setNewStatus(3)
            self.insertIntoSonderVokabeln()

        elif status == 3:
            self.setNewStatus(3)
        elif status == 4:
            self.setNewStatus(3)
        elif status == 5:
            self.setNewStatus(3)

    def richtig(self):
        status = self.datenbank.getDataAsList("select status from vokabeln where id like "+str(self.vokabelId))[0][0]

        if status == 0:
            self.setNewStatus(0)
        elif status == 1:
            self.setNewStatus(0)
        elif status == 2:
            self.setNewStatus(0)

        elif status == 3:
            self.setNewStatus(4)
        elif status == 4:
            self.setNewStatus(5)
        elif status == 5:
            self.setNewStatus(0)
            #delete sondervokabel
            statement = "update sondervokabeln set show='False' where idvokabeln like "+str(self.vokabelId)
            self.datenbank.setData(statement)

    def setNewStatus(self, status):
        statement = "update vokabeln set status = "+str(status)+" where id like "+str(self.vokabelId)
        self.datenbank.setData(statement)

    def insertIntoSonderVokabeln(self):
        lookup = "select count(*) from sondervokabeln where idVokabeln like "+str(self.vokabelId)
        if self.datenbank.getDataAsList(lookup)[0][0] == 1:
            self.datenbank.setData("update sondervokabeln set show="+True+" where idvokabeln like "+str(self.vokabelId))
        else:
            statement = "insert sondervokabeln (idvokabeln, idsonderlektion) values ("+self.vokabelId+", "+str(self.getLektion())+")"
            self.datenbank.setData(statement)

    def getLektion(self):
        statement = "select count(*) from lektionen" \
                    "join sondervokabeln on (lektionen.id=sondervokabeln.idsonderlektion)" \
                    "where sondervokabeln.idvokabeln like "+str(self.vokabelId)
        if self.datenbank.getDataAsList(statement)[0][0] == 0:
            #vokabel muss lektion zugeordnet werden
            #lektion suchen die noch platz hat
            statement = "select count(idsonderlektion), idsonderlektion " \
                        "from sondervokabeln  " \
                        "group by idsonderlektion " \
                        "order by count(idsonderlektion) limit 1"
            result = self.datenbank.getDataAsList(statement)
            if result[0][0] < 10:
                return result[0][1]
            else:
                #lektion muss geschaffen werden
                #anzahl vorhandener lektionen checken
                statement = "select count(*) from lektionen where name like 'sonderlektion%'"
                anzahlSonderLektionen = self.datenbank.getDataAsList(statement)[0][0]

                #create Sonderlektion
                #SonderBuch finden
                statement = "select sprache.id as SpracheId from sprache " \
                            "join buecher on (buecher.id_sprache=sprache.id) " \
                            "join lektionen on (lektionen.idbuch=buecher.id) " \
                            "join vokabeln on (vokabeln.idlektion = lektionen.id) " \
                            "where vokabeln.id like " +str(self.vokabelId)
                spracheId = self.datenbank.getDataAsList(statement)[0][0]

                #buch finden
                statement = "select buecher.id as BuchId from sprache " \
                            "join buecher on (buecher.id_sprache=sprache.id) " \
                            "where buecher.name like 'sonder%' and idSprache like " +str(spracheId)
                buchid = self.datenbank.getDataAsList(statement)

                name = "Sonderlektion"+str(anzahlSonderLektionen+1)



                statement = "insert into lektionen ('name', 'idbuch') values ('"+str(name)+"', "+str(buchid)+")"
                self.datenbank.setData(statement)

                #lektionid finden
                statement = "select id from lektionen where buchid like "+str(buchid)+" and " \
                            " name like "+str(name)
                idLektion = self.datenbank.getDataAsList(statement)[0][0]
                return idLektion
        else:
            statement = "select lektionen.id from lektionen " \
                        "join sondervokabeln on (lektionen.id= sondervokabeln.idsonderlektion) " \
                        "where sondervokabeln.idvokabeln like "+str(self.vokabelId)
            idLektion = self.datenbank.getDataAsList(statement)[0][0]
            return idLektion

