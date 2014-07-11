from PyQt4 import QtCore


class georef():
    def __init__(self,  layoutPipeline):
        self.layoutPipeline= layoutPipeline
        self.__activeCanvas = 0
        self.__inactiveCanvas = 0
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
        if self.layoutPipeline.currentIndex()== 0:
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
                print "error setcoords"
            self.gimmeDemPoints()

    def activeCanvas(self):
        return self.__activeCanvas

    def __del__(self):
        print "deleted"
        
    def gimmeDemPoints(self):
        return len(self.__data)/4
        
    def calculateSomething(self,sAM):
        print '# points: ', self.gimmeDemPoints()
        for i in range(self.gimmeDemPoints()):
            print i,': ',self.getPointPair(i)
        print 'selected area: ', sAM.getArea()
        

   

    def getPointPair(self,i):
        temp=(self.__data[4*i],self.__data[1+4*i],self.__data[2+4*i],self.__data[3+4*i])
        return temp
    
