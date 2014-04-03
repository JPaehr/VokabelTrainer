#-*- coding: utf-8 -*-
__author__ = 'JPaehr'

import csv
import copy

class tsvReader(object):

    def __init__(self, path):

        filetsv = csv.reader(open(path, 'rb'), delimiter='\t')

        newlist = list()
        for row in filetsv:
            newlist.append(copy.deepcopy(row))
        newlist2 = list()
        for index in range(len(newlist)):
            zwlist = list()
            for i in newlist[index]:
                if not i == '':
                    zwlist.append(i)
            if len(zwlist) > 0:
                newlist2.append(zwlist)
        self.liste = newlist2

    def getList(self):
        return  self.liste