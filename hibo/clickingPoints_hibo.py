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
            print self.marker.toMapCoordinates(e.pos()).x()
            print self.marker.toMapCoordinates(e.pos()).y()
            clicked_point=(self.marker.toMapCoordinates(e.pos()))
            matlab=['C:\\Users\\Freddy\\HiBo-plugin\\matlab\\test1.exe']
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
            
            ########PREVIEW
            fileName2Transform= 'C:/matlabPython/transformedBorder.bmp'
            lines = [float(line.strip()) for line in open('C:/matlabPython/coords.txt')]
            self.ui.transform(fileName2Transform,lines[0],lines[1],lines[2],lines[3])
            fileNameOut= os.path.dirname(__file__)+"/Maps/outputMap.GTiff"
            fileInfo = QFileInfo(fileNameOut)
            baseNameOut = fileInfo.baseName()
            self.rlayer2 = QgsRasterLayer(fileNameOut, baseNameOut)
            if not self.rlayer2.isValid():
                print "Layer failed to load!"
                return
            qrt=QgsRasterTransparency()
            qrt.initializeTransparentPixelList(255)
            self.rlayer2.renderer().setRasterTransparency(qrt)
            #self.rlayer2.renderer().setOpacity(0.5)
            self.layerlistr = []
            self.layerlistr.append(self.rlayer2)
            QgsMapLayerRegistry.instance().addMapLayers(self.layerlistr, False) 
            self.old_layers=self.ui.vectorMapCanvasLayerList
            self.old_layers.append(QgsMapCanvasLayer(self.rlayer2))
            self.canvas.setLayerSet( self.old_layers )
            self.canvas.setCurrentLayer(self.rlayer2)
            self.canvas.setVisible(True)
            self.canvas.refresh()

    def canvasReleaseEvent(self, e):
        pass

    def canvasMoveEvent(self, e):
        pass

    def showRect(self, startPoint, endPoint):
        pass

    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.emit(SIGNAL("deactivated()"))
        
    def getCounter(self):
       return self.counter