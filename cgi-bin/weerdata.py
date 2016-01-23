#!/usr/local/bin/python

import urllib2
import json
import cgitb

# set the errors to visible
cgitb.enable(display=1)

def GetWeerdata():
	# Get JSON data from openweathermap
	urldata = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Rotterdam&APPID=9c6c775e33798582cec99cb843fedf3a").read()
	parsed_json = json.loads(urldata)
	return parsed_json["weather"][0]["main"];