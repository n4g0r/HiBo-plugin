from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *
from georef_hibo import georef


class markingV(QgsMapToolEmitPoint):
    def __init__(self, ui, georef):
        self.ui = ui
        self.canvasRaster = ui.canvasRaster
        self.canvasVector = ui.canvasVector
        self.georef = georef
        QgsMapToolEmitPoint.__init__(self, self.canvasVector)

    def reset(self):    
        pass

    def canvasPressEvent(self, e):
        if self.georef.activeCanvas() == 0:
            QtGui.QMessageBox.information(self.ui,"Information", "Please select a point on the right side first.")
        elif self.georef.activeCanvas() == 1:
            self.marker = QgsVertexMarker(self.canvasVector)    
            self.marker.setCenter(self.marker.toMapCoordinates(e.pos()))
            self.georef.setCoords(self.marker.toMapCoordinates(e.pos()))

    def canvasReleaseEvent(self, e):
        pass

    def canvasMoveEvent(self, e):
        self.markerV = QgsVertexMarker(self.canvasVector)
        self.markerR = QgsVertexMarker(self.canvasRaster)
        self.markerR.setColor(QtGui.QColor(0, 255, 0, 127))
        value = self.georef.checkCoordsV(self.markerV.toMapCoordinates(e.pos()))
        if value != QgsPoint(0,0):
             self.markerR.setCenter(value)

    def showRect(self, startPoint, endPoint):
        pass

    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.emit(SIGNAL("deactivated()"))
