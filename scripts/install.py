import os
import json
from subprocess import call
from os.path import dirname, realpath

print "\n\n\n"

print "Updating CKAN"
call("ckan.exe update")

print "Cleaning the cache..."
call("ckan.exe clean")

print "Scanning for manually added mods.."
call("ckan.exe scan")

print "Initializing KSP Directory..."
path = dirname(realpath(dirname(__file__)))
call("ckan.exe ksp add KerbalSpaceCamp " + path)
call("ckan.exe ksp default KerbalSpaceCamp")

print "\n Installing Mods...\n"
json_data = open('mods.json')
mods = json.load(json_data)
for mod in mods:
    print 'Installing ' + mod['name']
    call("ckan.exe install " + mod['identifier'])
