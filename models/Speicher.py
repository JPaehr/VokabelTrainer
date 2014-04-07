__author__ = 'JPaehr'


class Speicher(object):

    def __init__(self,pBFortschritt, distance, meintenSie, verzoegerung, id_aktuell, richtige_anzeigen,
                 richtung, labPunkte, vokIds, abfragenGesamt, lektionen_ids, lektion, vokabel_deutsch, vokabel_fremd, buch, zeit):
        self.lektion = lektion
        self.vokabel_deutsch = vokabel_deutsch
        self.vokabel_fremd = vokabel_fremd
        self.buch = buch
        self.zeit = zeit


        self.Fortschritt = pBFortschritt
        self.distance = distance

        self.id_aktuell = id_aktuell
        #print "Im Konstruktor: "+str(id_aktuell)
        self.meinten_sie = meintenSie
        self.verzoegerung = verzoegerung

        self.richtige_anzeigen = richtige_anzeigen
        self.richtung = richtung
        self.labPunkte = labPunkte
        self.vokabel_ids = vokIds
        self.abfragenGesamt = abfragenGesamt
        self.lektion_ids = lektionen_ids

    def Info(self):
        print "Lektion: ", self.lektion
        print "Vokabel_deutsch: ", self.vokabel_deutsch
        print "vokabel_fremd: ", self.vokabel_fremd
        print "Buch: ", self.buch
        print "Fortschritt: ", self.Fortschritt
        print "Distance: ", self.distance
        print "ID-Aktuell: ", self.id_aktuell
        print "MeintenSie: ", self.meinten_sie
        print "Verzoegerung: ", self.verzoegerung
