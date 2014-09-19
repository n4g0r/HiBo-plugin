from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *
from georef_hibo import georef


class markingR(QgsMapToolEmitPoint):
    def __init__(self, ui, georef):
        self.ui = ui
        self.canvasRaster = ui.canvasRaster
        self.canvasVector = ui.canvasVector
        self.georef = georef
        QgsMapToolEmitPoint.__init__(self, self.canvasRaster)

    def reset(self):    
        pass

    def canvasPressEvent(self, e):
        if self.georef.activeCanvas() == 0:
            self.marker = QgsVertexMarker(self.canvasRaster)
            self.marker.setCenter(self.marker.toMapCoordinates(e.pos()))
            self.georef.setCoords(self.marker.toMapCoordinates(e.pos()))
        elif self.georef.activeCanvas() == 1:
            QtGui.QMessageBox.information(self.ui, "Information", "Please select a point on the left side first.")

    def canvasReleaseEvent(self, e):
        pass

    def canvasMoveEvent(self, e): 
        self.markerR = QgsVertexMarker(self.canvasRaster)
        self.markerV = QgsVertexMarker(self.canvasVector)
        self.markerV.setColor(QtGui.QColor(0, 255, 0, 127))
        value = self.georef.checkCoordsR(self.markerR.toMapCoordinates(e.pos()))
        if value != QgsPoint(0,0):
             self.markerV.setCenter(value)

    def showRect(self, startPoint, endPoint):
        pass

    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.emit(SIGNAL("deactivated()"))
