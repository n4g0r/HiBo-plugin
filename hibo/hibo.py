from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
import resources
import sys
import os
from Ui_hibo import Ui_hibo
from georef_hibo import georef

class hibo: 
    def __init__(self, iface):
        self.iface = iface
        self.gui = Ui_hibo ()

    def initGui(self):  
        self.action = QAction(QIcon(":/icons/hibo.png"), "HiBo", self.iface.mainWindow())
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
