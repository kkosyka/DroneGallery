#Allow user to manually add a new drone image's information

import os, sys

layerName = raw_input("Layer name? ")
description = raw_input("Description? ")
date = raw_input("Date? ")
xcoor = raw_input("X-Coordinate? ")
ycoor = raw_input("Y-Coordinate? ")

readFile = open("droneGalleryJSON.json")
lines = readFile.readlines()
readFile.close()
w = open("droneGalleryJSON.json",'w')

w.writelines([item for item in lines[:-1]])
w.writelines(',{"layer": "' + layerName +'", "description": "'+description+'", "date": "' +date+ '", "xcoor": "'+ xcoor+'", "ycoor": "' + ycoor + '"}')
w.writelines("\n]")
w.close()



# {
# 	"layer": "northbeach",
# 	"description": "from our recent trip to Georgia.",
# 	"date": "3/12/17",
# 	"xcoor": "31.684522",
# 	"ycoor": "-81.132717"
# }