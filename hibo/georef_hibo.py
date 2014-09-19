from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *

class georef():
    def __init__(self,  layoutPipeline):
        self.layoutPipeline= layoutPipeline
        self.__activeCanvas = 0
        self.__inactiveCanvas = 0
        self.__tmpRasterX = 0.0
        self.__tmpRasterY = 0.0
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
                self.__tmpRasterX = point.x()
                self.__tmpRasterY = point.y()
                self.__flipCanvas()
            elif self.__activeCanvas == 1:
                print ('vector:',point.x(),point.y())
                self.__data = self.__data+(self.__tmpRasterX,self.__tmpRasterY,point.x(),point.y())
                self.__tmpRaster = 0.0
                self.__tmpRaster = 0.0
                self.__flipCanvas()
            else:
                print "error setcoords"
            self.gimmeDemPoints()
    
    def checkCoordsR(self, point):
        eps = 10
        print "length: ",len(self.__data)
        if len(self.__data) > 0:
            for i in range(len(self.__data)/4):
                print "data : ", self.__data[int(i*4)],"," ,self.__data[int(i*4+1)], " point:  ", point.x(),",",point.y()         
                if self.__data[int(i*4)] - eps <= point.x() and self.__data[int(i*4)] + eps >= point.x() and self.__data[int(i*4+1)] - eps <= point.y() and self.__data[int(i*4+1)] + eps >= point.y():
                   return QgsPoint(self.__data[int(i*4+2)],self.__data[int(i*4+3)])
                   print "treffer"
        return QgsPoint(0.0,0.0)

    def checkCoordsV(self, point):
        eps = 0.000001
        print "length: ",len(self.__data)
        if len(self.__data) > 0:
            for i in range(len(self.__data)/4):
                print "data : ", self.__data[int(i*4+2)],"," ,self.__data[int(i*4+3)], " point:  ", point.x(),",",point.y()         
                if self.__data[int(i*4+2)] - eps <= point.x() and self.__data[int(i*4+2)] + eps >= point.x() and self.__data[int(i*4+3)] - eps <= point.y() and self.__data[int(i*4+3)] + eps >= point.y():
                   return QgsPoint(self.__data[int(i*4)],self.__data[int(i*4+1)])
                   print "treffer"
        return QgsPoint(0.0,0.0)

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
    
