# -*- coding: utf-8 -*-
"""
/***************************************************************************
 hiboDialog
                                 A QGIS plugin
 Quantum GIS plugin for semiautomated processing of historical maps
                             -------------------
        begin                : 2014-04-28
        copyright            : (C) 2014 by Chair of Computer Vision in Engineering at Bauhaus-University Weimar
        email                : marcus.kossatz@uni-weimar.de, suvratha.narayan.bejai@uni-weimar.de, frederilgaillard@googlemail.com, felix.schmidt@uni-weimar.de
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
from ui_hibo import Ui_hibo
# create the dialog for zoom to point


class hiboDialog(QtGui.QDialog, Ui_hibo):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
