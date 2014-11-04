#-*- coding: utf-8 -*-
__author__ = 'JPaehr'
import models.base as Datenbank

class SonderFall(object):

    def __init__(self, vokabelId, debug=False):
        self.vokabelId = vokabelId
        if debug == 0:
            self.debug = False
        else:
            self.debug = True

        if self.debug:
            print "Vokabelid: " +str(self.vokabelId)

        self.datenbank = Datenbank.base("VokabelDatenbank.sqlite")

        #sprache finden

        statement = "select sprache.id from sprache " \
                    "join buecher on (buecher.id_sprache=sprache.id) " \
                    "join lektionen on (lektionen.idbuch=buecher.id) " \
                    "join vokabeln on (vokabeln.idlektion=lektionen.id) " \
                    "where vokabeln.id like "+str(vokabelId)
        self.spracheId = self.datenbank.getDataAsList(statement)[0][0]

        #self.lekionsId = lektionsId



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
        statement = "select status from vokabeln where id like "+str(self.vokabelId)
        if self.debug:
            print statement
        status = self.datenbank.getDataAsList(statement)[0][0]

        if status == 5:
            self.setNewStatus(3)
        elif status == 4:
            self.setNewStatus(3)
        elif status == 3:
            self.setNewStatus(3)
        elif status == 2:
            self.setNewStatus(3)
            self.insertIntoSonderVokabeln()
        elif status == 1:
            self.setNewStatus(2)
        elif status == 0:
            self.setNewStatus(1)


    def richtig(self):
        if self.debug:
            print "richtig aufgerufen"
        status = self.datenbank.getDataAsList("select status from vokabeln where id like "+str(self.vokabelId))[0][0]
        if self.debug:
            print "Richtig: Status: "+str(status)
        if status == 0:
            if self.debug:
                print "status 0"
            self.setNewStatus(0)
        elif status == 1:
            if self.debug:
                print "status 1"
            self.setNewStatus(0)
        elif status == 2:
            if self.debug:
                print "status 2"
            self.setNewStatus(0)
        elif status == 5:
            if self.debug:
                print "status 3"
            self.setNewStatus(0)
            #delete sondervokabel
            statement = "update sondervokabeln set show='0' where idvokabeln like "+str(self.vokabelId)
            self.datenbank.setData(statement)
        elif status == 4:
            if self.debug:
                print "status 4"
            self.setNewStatus(5)
        elif status == 3:
            if self.debug:
                print "status 3"
            self.setNewStatus(4)




    def setNewStatus(self, status):
        if self.debug:
            print "setNewStatus aufgerufen"
            print "alter status: "+str(status)
        statement = "update vokabeln set status = "+str(status)+" where id like "+str(self.vokabelId)
        self.datenbank.setData(statement)

    def insertIntoSonderVokabeln(self):
        if self.debug:
            print "insertIntoSonderVokabeln aufgerufen"
        lookup = "select count(*) from sondervokabeln where idVokabeln like "+str(self.vokabelId)
        if self.datenbank.getDataAsList(lookup)[0][0] == 1:
            self.datenbank.setData("update sondervokabeln set show=1 where idvokabeln like "+str(self.vokabelId))
        else:
            statement = "insert into sondervokabeln (idvokabeln, idsonderlektion) " \
                        "values ("+str(self.vokabelId)+", "+str(self.getLektion())+")"
            print statement
            self.datenbank.setData(statement)

    def getLektion(self):
        statement = "select count(*) from lektionen " \
                    "join sondervokabeln on (lektionen.id=sondervokabeln.idsonderlektion) " \
                    "where sondervokabeln.idvokabeln like "+str(self.vokabelId)
        #print statement
        if self.datenbank.getDataAsList(statement)[0][0] == 0:
            #-> vokabel neu

            #vokabel muss lektion zugeordnet werden
            #lektion suchen die noch platz hat
            """statement = "select count(idsonderlektion), idsonderlektion " \
                        "from sondervokabeln  " \
                        "group by idsonderlektion " \
                        "order by count(idsonderlektion) limit 1"
            """
            statement = "select count(idsonderlektion), sondervokabeln.idsonderlektion " \
                        "from sondervokabeln " \
                        "join lektionen on (lektionen.id= sondervokabeln.idsonderlektion) " \
                        "join buecher on (buecher.id=lektionen.idbuch) " \
                        "join sprache on (sprache.id=buecher.id_sprache) " \
                        "where sprache.id like "+str(self.spracheId)+ \
                        " group by sondervokabeln.idsonderlektion " \
                        "order by count(idsonderlektion) " \
                        "limit 1"
            if self.debug:
                print statement
            result = self.datenbank.getDataAsList(statement)
            if self.debug:
                print result

            if len(result) > 0 and result[0][0] < 10:
                return result[0][1]
            else:
                #lektion muss geschaffen werden


                #create Sonderlektion
                #SonderBuch finden
                statement = "select sprache.id as SpracheId from sprache " \
                            "join buecher on (buecher.id_sprache=sprache.id) " \
                            "join lektionen on (lektionen.idbuch=buecher.id) " \
                            "join vokabeln on (vokabeln.idlektion = lektionen.id) " \
                            "where vokabeln.id like " +str(self.vokabelId)
                if self.debug:
                    print "sprache:id "+str(statement)

                spracheId = self.datenbank.getDataAsList(statement)[0][0]

                #buch finden
                statement = "select buecher.id as BuchId from sprache " \
                            "join buecher on (buecher.id_sprache=sprache.id) " \
                            "where buecher.name like 'sonder%' and buecher.id_Sprache like " +str(spracheId)
                if self.debug:
                    print statement

                if len(self.datenbank.getDataAsList(statement)) == 0:
                    # gibt noch kein Sonderbuch => erstellen
                    insertStatement = "insert into Buecher ('name', id_sprache) \
                    values ('Sonderbuch', "+str(spracheId)+")"
                    self.datenbank.setData(insertStatement)

                buchid = self.datenbank.getDataAsList(statement)[0][0]

                #anzahl vorhandener lektionen checken
                statement = "select count(*) from lektionen " \
                            "join buecher on (buecher.id= lektionen.idbuch) " \
                            "where lektionen.name like 'sonderlektion%' " \
                            "and buecher.id like "+str(buchid)

                anzahlSonderLektionen = self.datenbank.getDataAsList(statement)[0][0]

                name = "Sonderlektion"+str(anzahlSonderLektionen+1)



                statement = "insert into lektionen ('name', 'idbuch') values ('"+str(name)+"', "+str(buchid)+")"
                if self.debug:
                    print statement
                self.datenbank.setData(statement)

                #lektionid finden
                statement = "select id from lektionen where idbuch like "+str(buchid)+" and " \
                            " name like '"+str(name)+"'"
                if self.debug:
                    print statement
                idLektion = self.datenbank.getDataAsList(statement)[0][0]
                return idLektion
        else:
            statement = "select lektionen.id from lektionen " \
                        "join sondervokabeln on (lektionen.id= sondervokabeln.idsonderlektion) " \
                        "where sondervokabeln.idvokabeln like "+str(self.vokabelId)
            idLektion = self.datenbank.getDataAsList(statement)[0][0]
            return idLektion
