from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *
from georef_hibo import georef
import os, subprocess
import reduce
import math



class clickingP(QgsMapToolEmitPoint):
    def __init__(self, ui, layoutPipeline):
        self.ui = ui
        self.canvas = ui.canvas
        self.layoutPipeline = layoutPipeline
        self.counter=1
        self.startendcounter=0
        self.startendarray=[]
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def reset(self):    
        pass

    def canvasPressEvent(self, e):
        print self.ui.ended
        print self.layoutPipeline.currentIndex()== 1 and self.ui.ended==False
        if self.layoutPipeline.currentIndex()== 1 and self.ui.ended==False:
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
            matlab.append('-') #filename
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
            qrt.initializeTransparentPixelList(255,255,255)
            self.rlayer2.renderer().setRasterTransparency(qrt)
            self.layerlistr = []
            self.layerlistr.append(self.rlayer2)
            QgsMapLayerRegistry.instance().addMapLayers(self.layerlistr, False) 
            self.old_layers=self.ui.vectorMapCanvasLayerList

            self.old_layers.reverse()
            if len(self.old_layers)>7:
                self.old_layers.pop()
                print('pop')
            self.old_layers.append(QgsMapCanvasLayer(self.rlayer2))
            self.old_layers.reverse()
            self.canvas.setLayerSet( self.old_layers )
            self.canvas.refresh()
        elif self.layoutPipeline.currentIndex()== 1 and self.ui.ended==True:
            self.startendcounter=self.startendcounter+1
            self.marker = QgsVertexMarker(self.canvas)
            self.marker.setCenter(self.marker.toMapCoordinates(e.pos()))
            print self.marker.toMapCoordinates(e.pos()).x()
            self.startendarray.append(self.marker.toMapCoordinates(e.pos()).x())
            print self.marker.toMapCoordinates(e.pos()).y()
            self.startendarray.append(self.marker.toMapCoordinates(e.pos()).y())
            print self.startendarray
            
            if self.startendcounter>=2:
                lines = [float(line.strip()) for line in open('C:/matlabPython/polyline.txt')]
                
                x1delta=self.startendarray[0]-lines[0]
                y1delta=self.startendarray[1]-lines[1]
                x2delta=self.startendarray[2]-lines[len(lines)-2]
                y2delta=self.startendarray[3]-lines[len(lines)-1]
                case1 = math.sqrt(abs(x1delta+y1delta))+math.sqrt(abs(x2delta+y2delta))
                
                _x1delta=self.startendarray[0]-lines[len(lines)-2]
                _y1delta=self.startendarray[1]-lines[len(lines)-1]
                _x2delta=self.startendarray[2]-lines[0]
                _y2delta=self.startendarray[3]-lines[1]
                case2= math.sqrt(abs(_x1delta+_y1delta))+math.sqrt(abs(_x2delta+_y2delta))
                                
                if case1<case2:
                    print "case 1"
                    for i in range(len(lines)/2):
                        v1=(len(lines)-i*2)/float(len(lines))
                        v2=1-v1
                        lines[i*2]+=v1*x1delta+v2*x2delta
                        lines[i*2+1]+=v1*y1delta+v2*y2delta
                else:
                    print "case 2"
                    for i in range(len(lines)/2):
                        v1=(len(lines)-i*2)/float(len(lines))
                        v2=1-v1
                        lines[i*2]+= v2*_x1delta+v1*_x2delta
                        lines[i*2+1]+= v2*_y1delta+v1*_y2delta               

                
                crsSrc = QgsCoordinateReferenceSystem(3857)
                crsDest = QgsCoordinateReferenceSystem(4326)  
                xform = QgsCoordinateTransform(crsSrc, crsDest)
                test_map=[]
                for i in range(len(lines)/2):
                    pt = xform.transform(QgsPoint(lines[2*i],lines[2*i+1]))
                    test_map.append([pt.x(),pt.y()])
                    
                fileName = QFileDialog.getSaveFileName(None, "border map", ".", "Geojson Files (*.geojson)")
                reduce.execute(test_map,fileName)
                fileInfo = QFileInfo(fileName)
                baseName = fileInfo.baseName()
                vlayer = QgsVectorLayer(fileName, baseName, "ogr")
                QgsMapLayerRegistry.instance().addMapLayer(vlayer)

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