#!/usr/local/bin/python

import markten
import locatie
import cgitb

# set the errors to visible
cgitb.enable(display=1)

# set the general settings
google_api_key = "AIzaSyCg219BZX5-sVkO5423wOAIwRF_OxW7F8E"
userlocation = [51.90923, 4.486283]

# build the json string to use in html
pythondata = "["

# add the python data for the markets
pythondata = pythondata + "{\"name\": \"Markten\", \"data\": ["
week = (1,1,1,1,1,1,1)      
marktadres = markten.GetMarkten(week)

# add the data for each individual market
for x in range(0,len(marktadres)):
	marktnaam = marktadres[x][1].replace("\xa0", "").replace("&nbsp;", "") # this is added in the CSV file for some reason
	marktlocatie = locatie.GetLatLong(marktnaam, google_api_key)
	marktafstand = locatie.GetDistanceMeters(userlocation[0], userlocation[1], marktlocatie[0], marktlocatie[1], google_api_key)
	pythondata = pythondata + "{ \"name\": \""+str(marktnaam)+"\", \"dist\": \""+str(marktafstand)+"\", \"walk\": \"300\", \"transport\": \"100\", \"lat\": \""+str(marktlocatie[0])+"\", \"lng\": \""+str(marktlocatie[1]) + "\" },"

pythondata = pythondata[:-1]
pythondata = pythondata + "]}"
pythondata = pythondata + "]";

# print the html to the screen
print "Content-type: text/plain\n"
print pythondata,