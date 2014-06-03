#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from PyQt4 import QtCore, QtGui

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

        self.setWindowTitle(self.tr("HiBo"))

    def setupUi(self):
	"""setup for toolbar"""
	self.toolbarVector 	= QtGui.QToolBar('vector', self)
	self.toolbarRaster 	= QtGui.QToolBar('raster', self)

	self.zoominVector 	= QtGui.QAction(QtGui.QIcon("zoomin.png"), 'zoominVector', self)
	self.zoomoutVector 	= QtGui.QAction(QtGui.QIcon("zoomout.png"), 'zoomoutVector', self)
	self.moveVector 	= QtGui.QAction(QtGui.QIcon("move.png"), 'moveVector', self)
	self.loadVector 	= QtGui.QAction(QtGui.QIcon("load.png"), 'loadVector', self)
	self.zoominRaster 	= QtGui.QAction(QtGui.QIcon("zoomin.png"), 'zoominRaster', self)
	self.zoomoutRaster 	= QtGui.QAction(QtGui.QIcon("zoomout.png"), 'zoomoutRaster', self)
	self.moveRaster 	= QtGui.QAction(QtGui.QIcon("move.png"), 'moveRaster', self)
	self.loadRaster 	= QtGui.QAction(QtGui.QIcon("load.png"), 'loadRaster', self)
	self.selectRaster	= QtGui.QAction(QtGui.QIcon("select.png"), 'selectRaster', self)	

	self.toolbarVector.addAction(self.loadVector)
	self.toolbarVector.addAction(self.zoominVector)
	self.toolbarVector.addAction(self.zoomoutVector)
	self.toolbarVector.addAction(self.moveVector)
	
	self.toolbarRaster.addAction(self.loadRaster)	
	self.toolbarRaster.addAction(self.zoominRaster)
	self.toolbarRaster.addAction(self.zoomoutRaster)
	self.toolbarRaster.addAction(self.moveRaster)
	self.toolbarRaster.addAction(self.selectRaster)
	#self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

	
	"""layout"""
	vectorarea 	= QtGui.QWidget()
	rasterarea 	= QtGui.QWidget()

	layoutVector 	= QtGui.QHBoxLayout()
	layoutRaster 	= QtGui.QVBoxLayout()

	vectorarea.setLayout(layoutVector)
	rasterarea.setLayout(layoutRaster)

	layoutVector.addWidget(self.toolbarVector)
	layoutRaster.addWidget(self.toolbarRaster)

	layoutCentral = QtGui.QHBoxLayout(self)
	layoutCentral.addWidget(vectorarea)
	layoutCentral.addWidget(rasterarea)	
	
    def retranslateUi(self):
        self.setWindowTitle(_translate("hibo", "hibo", None))

