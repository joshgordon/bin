#!/usr/bin/env python
# Simple python scrypt for calling weather undergournd API for collecting
# some simple weather info. Currently inculudes temp, weather ("clear", etc), 
# and a URL to an icon. 

# API key is stored in a file in the user's home directory. (Accessed through
# os, so it *SHOULD* be cross platform... 
# It will warn you if you don't already have a file there. Use -a to create one.

# Please report bugs (I know there's probably some...) to github@joshgordon.net

# I did cacheing in the tempdir to help cut down on API calls. Use -flushcache 
# to clear this cache. 

# Import some stuff. 
import json
import urllib
import sys
import string
import os
import tempfile
import time

# weather API key
try: 
    home = os.getenv("HOME") 
    keyFile = open(home + "/.wunderground.apikey", "r")
    key = keyFile.read().strip()
    
    keyFile.close() 

except: 

    print "API Key not found. Create one at wunderground.com/weather.api." 
    print "Then use '" + thisFile, "-a' to add the API key."  


def getNewKey(): 
    keyFile = open(home + "/.wunderground.apikey", "w")
    getNewKey(keyFile)
    newKey = raw_input("Enter your new API key: ")
    keyFile.write(newKey)

def getTemp(json): 
    print json["current_observation"]["temp_f"]

def getWeather(json): 
    print json["current_observation"]["weather"]

def getIcon(json): 
    print json["current_observation"]["icon_url"]
def flushCache(file): 
    os.remove(file)


def printUsage(): 
    print "Not implemented yet." 


################################################################################
# Get some stuff set up: 
newKey=False
temp=False
weather=False
thisFile=sys.argv[0]
stateCity="MD/Severna_Park" 

#URL of json to get. 
url="http://api.wunderground.com/api/" + key + "/conditions/q/" + stateCity + ".json"

jsonDump=""

# get the weather json and put it into json. 
timeNow = time.mktime(time.gmtime())
jsonFile = tempfile.gettempdir() + "/weather.json"
if (os.path.exists(jsonFile) and os.path.getmtime(jsonFile) < timeNow - 250): 
    sys.stderr.write("Using cache.\n") 
    try: 
        jsonDump = json.load(open(jsonFile))
    except: 
        print "No cache file found. Removing existing file to eliminate errors. " 
        os.remove(jsonFile)

else: 
    jsonDump = json.load(urllib.urlopen(url)) 
    outFile = open(jsonFile, "w" )
    outFile.write(json.dumps(jsonDump))


if len(sys.argv) == 1: 
    printUsage()
    sys.exit(1) 

    

for arg in sys.argv[1:]: 
    if (arg == "-a"): 
        getNewKey()
    elif (arg == "-t"): 
        getTemp(jsonDump) 
    elif (arg == "-w"): 
        getWeather(jsonDump) 
    elif (arg == "-i"): 
        getIcon(jsonDump)
    elif (arg == "-flushcache"): 
        flushCache(jsonFile)
