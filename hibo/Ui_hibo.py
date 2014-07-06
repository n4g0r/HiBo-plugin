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
from selectArea import RectangleMapTool
from functools import partial
from PIL import Image



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
        self.connect(self.loadVector, QtCore.SIGNAL('triggered()'), partial(self.loadVectorImage, self.canvasVector))
        self.connect(self.selectRaster, QtCore.SIGNAL('triggered()'), self.selectPoints)
        self.connect(self.calcRaster, QtCore.SIGNAL('triggered()'), self.calc)
        self.connect(self.back, QtCore.SIGNAL('triggered()'), self.backToSelection)
        self.connect(self.rectRaster, QtCore.SIGNAL('triggered()'), self.selectArea)
        self.connect(self.finish, QtCore.SIGNAL('triggered()'), self.end)
        self.setWindowTitle(self.tr("HiBo"))
        self.rlayer_temp = QgsRasterLayer()
        self.vlayer_temp = QgsVectorLayer()

    def setupUi(self):
        """toolbar step one"""
        self.toolbarVector  = QtGui.QToolBar('vector', self)
        self.toolbarRaster  = QtGui.QToolBar('raster', self)
        self.zoominVector   = QtGui.QAction(QtGui.QIcon(":/icons/zoomin.png"), 'zoominVector', self)
        self.zoomoutVector  = QtGui.QAction(QtGui.QIcon(":/icons/zoomout.png"), 'zoomoutVector', self)
        self.moveVector     = QtGui.QAction(QtGui.QIcon(":/icons/move.png"), 'moveVector', self)
        self.loadVector     = QtGui.QAction(QtGui.QIcon(":/icons/load.png"), 'loadVector', self)
        self.zoominRaster   = QtGui.QAction(QtGui.QIcon(":/icons/zoomin.png"), 'zoominRaster', self)
        self.zoomoutRaster  = QtGui.QAction(QtGui.QIcon(":/icons/zoomout.png"), 'zoomoutRaster', self)
        self.moveRaster     = QtGui.QAction(QtGui.QIcon(":/icons/move.png"), 'moveRaster', self)
        self.loadRaster     = QtGui.QAction(QtGui.QIcon(":/icons/load.png"), 'loadRaster', self)
        self.selectRaster   = QtGui.QAction(QtGui.QIcon(":/icons/select.png"), 'selectRaster', self)
        self.calcRaster     = QtGui.QAction(QtGui.QIcon(":/icons/calc.png"), 'calcRaster', self)
        self.rectRaster     = QtGui.QAction(QtGui.QIcon(":/icons/rectangle.png"), 'rect', self)
        
    
        self.toolbarVector.addAction(self.loadVector)
        self.toolbarVector.addAction(self.zoominVector)
        self.toolbarVector.addAction(self.zoomoutVector)
        self.toolbarVector.addAction(self.moveVector)
        self.toolbarRaster.addAction(self.loadRaster)   
        self.toolbarRaster.addAction(self.zoominRaster)
        self.toolbarRaster.addAction(self.zoomoutRaster)
        self.toolbarRaster.addAction(self.moveRaster)
        self.toolbarRaster.addAction(self.selectRaster)
        self.toolbarRaster.addAction(self.rectRaster)
        self.toolbarRaster.addAction(self.calcRaster)
        
        """canvas step one"""
        self.canvasVector   = QgsMapCanvas()
        self.canvasVector.setCanvasColor(Qt.white)
        self.canvasVector.enableAntiAliasing(True)
        self.canvasRaster   = QgsMapCanvas()
        self.canvasRaster.setCanvasColor(Qt.white)
        self.canvasRaster.enableAntiAliasing(True)

        """layout step one"""
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
        layoutCentral = QtGui.QHBoxLayout()
        layoutCentral.addWidget(vectorarea)
        layoutCentral.addWidget(rasterarea)

        """toolbar step two"""
        self.toolbar  = QtGui.QToolBar('toolbar', self)

        self.back        = QtGui.QAction(QtGui.QIcon(":/icons/back.png"), 'back', self)
        self.finish      = QtGui.QAction(QtGui.QIcon(":/icons/finish.png"), 'back', self)

        self.toolbar.addAction(self.back)
        self.toolbar.addAction(self.finish)
        
        """canvas step two"""
        self.canvas   = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)

        """layout step two"""
        layoutComputation = QtGui.QVBoxLayout()
        layoutComputation.addWidget(self.toolbar)
        layoutComputation.addWidget(self.canvas)

        """layout pipeline"""
        self.layoutPipeline = QtGui.QStackedLayout(self)
        step_one = QtGui.QWidget()
        step_one.setLayout(layoutCentral)
        self.layoutPipeline.addWidget(step_one)
        step_two = QtGui.QWidget()
        step_two.setLayout(layoutComputation)
        self.layoutPipeline.addWidget(step_two)

    def retranslateUi(self):
        self.setWindowTitle(_translate("hibo", "hibo", None))

    @QtCore.pyqtSlot()
    def loadRasterImage(self):
        #fileName = QFileDialog.getOpenFileName(None, "historical map", ".", "Image Files (*.png *.jpg *.bmp *.tiff)")
        fileName='C:/Users/Freddy/HiBo-plugin/hibo/map.jpg'
        fileInfo = QFileInfo(fileName)
        #baseName = fileInfo.baseName()
        baseName = 'map'
        self.rlayer_temp = QgsRasterLayer(fileName, baseName)
        if not self.rlayer_temp.isValid():
            print "Layer failed to load!"
            return  
        self.rlayer = self.rlayer_temp
        self.rlayer.extent()
        self.layerlistr = []
        self.layerlistr.append(self.rlayer)
        QgsMapLayerRegistry.instance().addMapLayers(self.layerlistr, False) 
        self.canvasRaster.setExtent(self.rlayer.extent())
        self.canvasRaster.setLayerSet( [ QgsMapCanvasLayer(self.rlayer) ] )
        self.canvasRaster.setCurrentLayer(self.rlayer)
        self.canvasRaster.setVisible(True)
        self.canvasRaster.refresh()
        self.selectArea()#################################NASTY

    @QtCore.pyqtSlot()
    def loadVectorImage(self,canvas):
        self.layerlistv = []
        self.coastline_layer = QgsVectorLayer(os.path.dirname(__file__)+"/ned/10m_physical/ne_10m_coastline.shp", "coastlines", "ogr")
        if not self.coastline_layer.isValid():
            print "Layer failed to load!"
        self.coastline_layer.extent()
        self.coastline_layer.Color = Qt.green
        self.layerlistv.append(self.coastline_layer)

        self.admin0_layer = QgsVectorLayer(os.path.dirname(__file__)+"/ned/ne_10m_admin_0_boundary_lines_land.shp", "admin0", "ogr")
        if not self.admin0_layer.isValid():
            print "Layer failed to load!"
        self.admin0_layer.extent()
        self.layerlistv.append(self.admin0_layer)

        self.admin1_layer = QgsVectorLayer(os.path.dirname(__file__)+"/ned/ne_10m_admin_1_states_provinces_lines_shp.shp", "admin1", "ogr")
        if not self.admin1_layer.isValid():
            print "Layer failed to load!"
        self.admin1_layer.extent()
        self.layerlistv.append(self.admin1_layer)

        self.lakes_layer = QgsVectorLayer(os.path.dirname(__file__)+"/ned/ne_10m_lakes.shp", "lakes", "ogr")
        if not self.lakes_layer.isValid():
            print "Layer failed to load!"
        self.lakes_layer.extent()
        self.layerlistv.append(self.lakes_layer)

        self.rivers_layer = QgsVectorLayer(os.path.dirname(__file__)+"/ned/ne_10m_rivers_lake_centerlines_scale_rank.shp", "rivers", "ogr")
        if not self.rivers_layer.isValid():
            print "Layer failed to load!"
        self.rivers_layer.extent()
        self.layerlistv.append(self.rivers_layer)

        self.coastline_layer.Color = Qt.green

        QgsMapLayerRegistry.instance().addMapLayers(self.layerlistv, False) 
        canvas.setLayerSet( [ QgsMapCanvasLayer(self.coastline_layer), QgsMapCanvasLayer(self.admin0_layer), QgsMapCanvasLayer(self.admin1_layer), QgsMapCanvasLayer(self.lakes_layer), QgsMapCanvasLayer(self.rivers_layer)] )
        canvas.setCurrentLayer(self.coastline_layer)
        canvas.setVisible(True)
        canvas.refresh()
        canvas.zoomToFullExtent()

    @QtCore.pyqtSlot()
    def selectPoints(self):
        self.georef = georef()
        print self.georef
        self.markRaster = markingR(self, self.georef)
        self.markVector = markingV(self, self.georef)
        self.canvasRaster.setMapTool(self.markRaster)
        self.canvasVector.setMapTool(self.markVector)

    @QtCore.pyqtSlot()
    def calc(self):
        #try:
            if self.georef.gimmeDemPoints()>=4:
                self.layoutPipeline.setCurrentIndex(1)
                self.georef.calculateSomething(self.selectAreaMT)
                self.loadVectorImage(self.canvas)
                
                #self.loadResultRasterImage(self.canvas)
            else:
                 QtGui.QMessageBox.information(self, "Information", "Please select at least 4 points.")
                 return
        #except AttributeError:
             #QtGui.QMessageBox.information(self, "Information", "Please select at least 4 points.")
             #return
        
        
        
        
    

    @QtCore.pyqtSlot()
    def backToSelection(self):
        self.layoutPipeline.setCurrentIndex(0)
        

    @QtCore.pyqtSlot()
    def selectArea(self):
        self.selectAreaMT = RectangleMapTool(self.canvasRaster)
        self.canvasRaster.setMapTool(self.selectAreaMT)

    @QtCore.pyqtSlot()
    def end(self):
        pass
    
    def loadResultRasterImage(self, canvas):
        #fileName = QFileDialog.getOpenFileName(None, "historical map", ".", "Image Files (*.png *.jpg *.bmp *.tiff)")
        fileName='C:/Users/Freddy/HiBo-plugin/hibo/map.jpg'
        fileInfo = QFileInfo(fileName)
        #baseName = fileInfo.baseName()
        baseName = 'map'
        im = Image.open(fileName)
        im.show()
        box=self.selectAreaMT.getArea()
        fileNameOut='C:/Users/Freddy/HiBo-plugin/hibo/map2.bmp'
        baseNameOut = 'map2'
        box=(0,0,100,100)
        im.crop(box)
        im.save(fileNameOut,"BMP")
        self.rlayer_temp = QgsRasterLayer(fileNameOut, baseNameOut)
        if not self.rlayer_temp.isValid():
            print "Layer failed to load!"
            return  
        self.rlayer = self.rlayer_temp
        self.rlayer.extent()
        #self.rlayer.setRenderer(QgsRasterRenderer().setOpacity(0.5))
        self.rlayer.renderer().setOpacity(0.5)
        self.layerlistr = []
        self.layerlistr.append(self.rlayer)
        QgsMapLayerRegistry.instance().addMapLayers(self.layerlistr, False) 
        canvas.setExtent(self.rlayer.extent())
        canvas.setLayerSet( [ QgsMapCanvasLayer(self.rlayer) ] )
        canvas.setCurrentLayer(self.rlayer)
        canvas.setVisible(True)
        canvas.refresh()

