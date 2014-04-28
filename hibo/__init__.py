# -*- coding: utf-8 -*-
"""
/***************************************************************************
 hibo
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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load hibo class from file hibo
    from hibo import hibo
    return hibo(iface)
