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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "HiBo" 
def description():
  return "Quantum GIS plugin for semiautomated processing of historical maps"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "2.0"
def classFactory(iface): 
  # load hibo class from file hibo
  from hibo import hibo 
  return hibo(iface)
