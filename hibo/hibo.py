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
from georef_hibo import georef
from marking_hibo import marking
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
