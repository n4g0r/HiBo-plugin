#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from rdp import rdp

begin = "{\n\"type\": \"FeatureCollection\",\n\"crs\": { \"type\": \"name\", \"properties\": { \"name\": \"urn:ogc:def:crs:OGC:1.3:CRS84\" } },\n\n\"features\": [\n{ \"type\": \"Feature\", \"properties\": { \"id\": 0001 }, \"geometry\": { \"type\": \"LineString\", \"coordinates\": "

end = "} }\n]\n}"

def execute(reduce_map,path):

   print "number before reducing: " + str(len(reduce_map))
   print "number after  reducing: " + str(len(rdp(reduce_map, epsilon=0.0001)))
   write(rdp(reduce_map, epsilon=0.0001),path)

def write(reduced_map,path):

   fobj = open(path, "w") 
   fobj.write(begin + str(reduced_map) + end ) 
   fobj.close()
