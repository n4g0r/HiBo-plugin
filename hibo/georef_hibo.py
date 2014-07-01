from PyQt4 import QtCore


class georef():
    def __init__(self):
        self.__activeCanvas = 0
        self.__tmpRaster = QtCore.QPoint()
        self.__data = ()
        print "object created"

    def __flipCanvas(self):
        if self.__activeCanvas == 0:
            self.__activeCanvas = 1
        elif self.__activeCanvas == 1:
            self.__activeCanvas = 0
        else:
            print "error flip_canvas"

    def setCoords(self, point):
        if self.__activeCanvas == 0:
            print ('raster:',point.x(),point.y())
            self.__tmpRaster.setX(point.x())
            self.__tmpRaster.setY(point.y())
            self.__flipCanvas()
        elif self.__activeCanvas == 1:
            print ('vector:',point.x(),point.y())
            self.__data = self.__data+(self.__tmpRaster.x(),self.__tmpRaster.y(),point.x(),point.y())
            self.__tmpRaster.isNull()
            self.__flipCanvas()
        else:
            print "error setoords"
        self.gimmeDemPoints()

    def activeCanvas(self):
        return self.__activeCanvas

    def __del__(self):
        print "deleted"
        
    def gimmeDemPoints(self):
        print len(self.__data)
        print self.__data
