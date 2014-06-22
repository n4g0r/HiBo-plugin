from PyQt4 import QtCore

class georef(object):

    def __init__(self):
        self.__activeCanvas = 0
        self.__tmpRaster = QtCore.QPoint()
        self.__data = dict()
        print "object created"

    def __del__(self):
        print "deleted"

    def __flipCanvas(self):
        if self.__activeCanvas == 0:
            self.__activeCanvas = 1
        elif self.__activeCanvas == 1:
            self.activeCanvas = 0
        else:
            print "error flip_canvas"

    def setCoords(self, point): 
        if self.__activeCanvas == 0:
            self.__tmpRaster = point
            flipCanvas()
        elif self.__activeCanvas == 1:
            self.__data = {self.__tmpRaster : point}
            self.__tmpRaster = 0
            flipCanvas()
        else:
            print "error setoords"
