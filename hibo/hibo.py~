"""
/***************************************************************************
Name			 	 : HiBo
Description          : Quantum GIS plugin for semiautomated processing of historical maps
Date                 : 06/May/14 
copyright            : (C) 2014 by Chair of Computer Vision in Engineer
email                : marcus.kossatz@uni-weimar.de, volker.rodehorst@uni-weimar.de, suvratha.narayan.bejai@uni-weimar.de, frederic.gaillard@uni-weimar.de, felix.schmidt@uni-weimar.de 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
import sys
import os
# Import the code for the dialog
from Ui_hibo import Ui_hibo

class hibo: 

    def __init__(self, iface):
        self.iface = iface
        self.gui = Ui_hibo ()

    def initGui(self):  
        self.action = QAction(QIcon("icon.png"), "HiBo", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("activated()"), self.run) 

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&HiBo", self.action)

    def unload(self):
        self.iface.removePluginMenu("&HiBo",self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self): 
	#self.gui.showMaximized()
        self.gui.show()
        result = self.gui.exec_() 
