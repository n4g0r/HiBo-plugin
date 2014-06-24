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
        self.georef = georef
        QgsMapToolEmitPoint.__init__(self, self.canvasRaster)

    def reset(self):    
        pass

    def canvasPressEvent(self, e):
        if self.georef.activeCanvas() == 0:
            self.marker = QgsVertexMarker(self.canvasRaster)
            self.marker.setCenter(self.marker.toMapCoordinates(e.pos()))
            self.georef.setCoords(e)
        elif self.georef.activeCanvas() == 1:
            QtGui.QMessageBox.information(self.ui, "Information", "Please select a point on the left side first.")

    def canvasReleaseEvent(self, e):
        pass

    def canvasMoveEvent(self, e):
        pass

    def showRect(self, startPoint, endPoint):
        pass

    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.emit(SIGNAL("deactivated()"))
