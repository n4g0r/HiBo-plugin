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
from PyQt4 import QtCore, QtGui 
from Ui_hibo import Ui_hibo
# create the dialog for hibo
class hiboDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_hibo ()
    self.ui.setupUi(self)
