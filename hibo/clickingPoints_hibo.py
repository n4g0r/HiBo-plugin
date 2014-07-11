from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *
from georef_hibo import georef
import os, subprocess


class clickingP(QgsMapToolEmitPoint):
    def __init__(self, ui, layoutPipeline):
        self.ui = ui
        self.canvas = ui.canvas
        self.layoutPipeline = layoutPipeline
        self.counter=1
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def reset(self):    
        pass

    def canvasPressEvent(self, e):
        if self.layoutPipeline.currentIndex()== 1:
            self.marker = QgsVertexMarker(self.canvas)
            self.marker.setCenter(self.marker.toMapCoordinates(e.pos()))
            clicked_point=(self.marker.toMapCoordinates(e.pos()))
            matlab=['C:\\Users\\Freddy\\HiBo-plugin\\test1.exe']
            matlab.append(str(self.counter)) #0 for first step; 1 for first click and so on
            for i in range(4):
                matlab.append(str(0)) #xmin etc....
            matlab.append(str(clicked_point.x())) #xclick
            matlab.append(str(clicked_point.y())) #yclick
            for i in range(4):
                matlab.append(str(0))
                matlab.append(str(0))
                matlab.append(str(0))
                matlab.append(str(0))
            matlab=subprocess.Popen(matlab)
            matlab.wait()
            
            
            
            self.counter=self.counter+1

    def canvasReleaseEvent(self, e):
        pass

    def canvasMoveEvent(self, e):
        pass

    def showRect(self, startPoint, endPoint):
        pass

    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.emit(SIGNAL("deactivated()"))
