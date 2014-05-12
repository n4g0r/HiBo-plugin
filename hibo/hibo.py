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
# Import the code for the dialog
from hiboDialog import hiboDialog

class hibo: 

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    @QtCore.pyqtSlot()
    def loadImage(self):
        print "test"
        #self.labelHalloWelt.setText(self.editText.text()) 

    def connects(self):
        self.iface.mainWindow.load_button.clicked.connect(self.loadImage)

    def initGui(self):  
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/hibo/icon.png"), "HiBo", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("activated()"), self.run) 

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&HiBo", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&HiBo",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self): 
        # create and show the dialog
        dlg = hiboDialog() 
        # show the dialog
        dlg.show()
        #bis hierher programm nach start
        result = dlg.exec_() 
        # See if OK was pressed
        if result == 1: 
            # do something useful (delete the line containing pass and
            # substitute with your code
            print "test1"

