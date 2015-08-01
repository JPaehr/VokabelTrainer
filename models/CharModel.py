__author__ = 'Johannes'


class Char(object):
    def __init__(self):
        self.data = []

    def delData(self):
        self.data = []

    def setData(self, dataStream):
        #stream format [[x, y], [x, y], [-1, -1]]
        sublist = []

        for i in dataStream:
            if not i[0] == -1 and not i[1] == -1:
                sublist.append(i)
            else:
                self.data.append(sublist)
                sublist = []

    def getSegment(self, index):
        return self.data[index]

    def getSegments(self):
        return self.data

    def insertSegment(self, index, liste):
        self.data.insert(index, liste)

    def appendItemToLastSegment(self, item):
        self.data[len(self.data)-1].append(item)

    def appendItemToNewSegment(self, item):
        self.data.append([item])

    def appendSegment(self, liste):
        self.data.append(liste)

    def getRawData(self):
        biglist = []
        for seg in self.data:
            for subseg in seg:
                biglist.append(subseg)
            biglist.append([-1, -1])

        return biglist

    def numberOfElements(self):
        return len(self.data)

    def delElement(self, index):
        return self.data.pop(index)

    def getNumberOfItems(self):
        ctr = 0
        for i in self.data:
            ctr += len(i)
        return ctr

    def info(self, raw=False):
        if raw:
            print(self.getRawData())
        else:
            print(self.data)
