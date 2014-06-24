#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis import core, gui
from qgis.core import *
from qgis.gui import *
from georef_hibo import georef
from markingVector_hibo import markingV
from markingRaster_hibo import markingR

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_hibo(QtGui.QDialog):
    def __init__(self): 
        QtGui.QDialog.__init__(self)
        self.setupUi()
        self.connect(self.loadRaster, QtCore.SIGNAL('triggered()'), self.loadRasterImage)
        self.connect(self.loadVector, QtCore.SIGNAL('triggered()'), self.loadVectorImage)
        self.connect(self.selectRaster, QtCore.SIGNAL('triggered()'), self.selectPoints)
        self.setWindowTitle(self.tr("HiBo"))

    def setupUi(self):
        """setup for toolbar"""
        self.toolbarVector  = QtGui.QToolBar('vector', self)
        self.toolbarRaster  = QtGui.QToolBar('raster', self)
        self.zoominVector   = QtGui.QAction(QtGui.QIcon("zoomin.png"), 'zoominVector', self)
        self.zoomoutVector  = QtGui.QAction(QtGui.QIcon("zoomout.png"), 'zoomoutVector', self)
        self.moveVector     = QtGui.QAction(QtGui.QIcon("move.png"), 'moveVector', self)
        self.loadVector     = QtGui.QAction(QtGui.QIcon("load.png"), 'loadVector', self)
        self.zoominRaster   = QtGui.QAction(QtGui.QIcon("zoomin.png"), 'zoominRaster', self)
        self.zoomoutRaster  = QtGui.QAction(QtGui.QIcon("zoomout.png"), 'zoomoutRaster', self)
        self.moveRaster     = QtGui.QAction(QtGui.QIcon("move.png"), 'moveRaster', self)
        self.loadRaster     = QtGui.QAction(QtGui.QIcon("load.png"), 'loadRaster', self)
        self.selectRaster   = QtGui.QAction(QtGui.QIcon("select.png"), 'selectRaster', self)    
        self.toolbarVector.addAction(self.loadVector)
        self.toolbarVector.addAction(self.zoominVector)
        self.toolbarVector.addAction(self.zoomoutVector)
        self.toolbarVector.addAction(self.moveVector)
        self.toolbarRaster.addAction(self.loadRaster)   
        self.toolbarRaster.addAction(self.zoominRaster)
        self.toolbarRaster.addAction(self.zoomoutRaster)
        self.toolbarRaster.addAction(self.moveRaster)
        self.toolbarRaster.addAction(self.selectRaster)
        """setup for canvas"""
        self.canvasVector   = QgsMapCanvas()
        self.canvasVector.setCanvasColor(Qt.white)
        self.canvasVector.enableAntiAliasing(True)
        self.canvasRaster   = QgsMapCanvas()
        self.canvasRaster.setCanvasColor(Qt.white)
        self.canvasRaster.enableAntiAliasing(True)
        """layout"""
        vectorarea  = QtGui.QWidget()
        rasterarea  = QtGui.QWidget()
        layoutVector    = QtGui.QVBoxLayout()
        layoutRaster    = QtGui.QVBoxLayout()
        vectorarea.setLayout(layoutVector)
        rasterarea.setLayout(layoutRaster)
        layoutVector.addWidget(self.toolbarVector)
        layoutVector.addWidget(self.canvasVector)
        layoutRaster.addWidget(self.toolbarRaster)
        layoutRaster.addWidget(self.canvasRaster)
        layoutCentral = QtGui.QHBoxLayout(self)
        layoutCentral.addWidget(vectorarea)
        layoutCentral.addWidget(rasterarea) 

    def retranslateUi(self):
        self.setWindowTitle(_translate("hibo", "hibo", None))

    @QtCore.pyqtSlot()
    def loadRasterImage(self):
        fileName = QFileDialog.getOpenFileName(None, "historical map", ".", "Image Files (*.png *.jpg *.bmp *.tiff)")
        fileInfo = QFileInfo(fileName)
        baseName = fileInfo.baseName()
        self.rlayer = QgsRasterLayer(fileName, baseName)
        if not self.rlayer.isValid():
            print "Layer failed to load!"
        self.rlayer.extent()
        layerlistr = []
        layerlistr.append(self.rlayer)
        QgsMapLayerRegistry.instance().addMapLayers(layerlistr, False) 
        self.canvasRaster.setExtent(self.rlayer.extent())
        self.canvasRaster.setLayerSet( [ QgsMapCanvasLayer(self.rlayer) ] )
        self.canvasRaster.setCurrentLayer(self.rlayer)
        self.canvasRaster.setVisible(True)
        self.canvasRaster.refresh()

    @QtCore.pyqtSlot()
    def loadVectorImage(self):
        layerlistv = []
        self.coastline_layer = QgsVectorLayer("ned/10m_physical/ne_10m_coastline.shp", "coastlines", "ogr")
        if not self.coastline_layer.isValid():
            print "Layer failed to load!"
        self.coastline_layer.extent()
        layerlistv.append(self.coastline_layer)
        self.admin0_layer = QgsVectorLayer("ned/ne_10m_admin_0_boundary_lines_land.shp", "admin0", "ogr")
        if not self.admin0_layer.isValid():
            print "Layer failed to load!"
        self.admin0_layer.extent()
        layerlistv.append(self.admin0_layer)
        self.admin1_layer = QgsVectorLayer("ned/ne_10m_admin_1_states_provinces_lines_shp.shp", "admin1", "ogr")
        if not self.admin1_layer.isValid():
            print "Layer failed to load!"
        self.admin1_layer.extent()
        layerlistv.append(self.admin1_layer)
        QgsMapLayerRegistry.instance().addMapLayers(layerlistv, False) 
        self.canvasVector.setExtent(self.coastline_layer.extent())
        self.canvasVector.setLayerSet( [ QgsMapCanvasLayer(self.coastline_layer), QgsMapCanvasLayer(self.admin0_layer), QgsMapCanvasLayer(self.admin1_layer)] )
        #self.canvasVector.setCurrentLayer(self.vlayer)
        self.canvasVector.setVisible(True)
        self.canvasVector.refresh()

    @QtCore.pyqtSlot()
    def selectPoints(self):
        self.georef = georef()
        print self.georef
        self.markRaster = markingR(self, self.georef)
        self.markVector = markingV(self, self.georef)
        self.canvasRaster.setMapTool(self.markRaster)
        self.canvasVector.setMapTool(self.markVector)
