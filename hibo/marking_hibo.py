from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *

class marking(QgsMapToolEmitPoint):
	def __init__(self, canvas, georef):
		self.canvas = canvas.canvasVector
		self.georef = georef
		QgsMapToolEmitPoint.__init__(self, self.canvas)

	def reset(self):	
		pass

	def canvasPressEvent(self, e):
		self.marker = QgsVertexMarker(self.canvas)	
		self.marker.setCenter(self.marker.toMapCoordinates(e.pos()))

	def canvasReleaseEvent(self, e):
		pass

	def canvasMoveEvent(self, e):
		pass

	def showRect(self, startPoint, endPoint):
		pass

	def deactivate(self):
		QgsMapTool.deactivate(self)
		self.emit(SIGNAL("deactivated()"))
