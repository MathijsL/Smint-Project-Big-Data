#!/usr/local/bin/python

import markten
import supermarkten
import ret
import locatie
import cgitb
import weerdata
import datetime

# set the errors to visible
cgitb.enable(display=1)

# set the general settings
google_api_key = "AIzaSyCg219BZX5-sVkO5423wOAIwRF_OxW7F8E"
userlocation = [51.90923, 4.486283]

# get the weather data
huidigweer = weerdata.GetWeerdata()

# build the json string to use in html
pythondata = "["

##### MARTKET DATA #####

# add the python data for the markets
pythondata = pythondata + "{\"name\": \"Markten\", \"weather\" : \""+huidigweer+"\", \"data\": ["

week = [0,0,0,0,0,0,0]
def dow(date):
    days=["3","1","2","3","4","5","6"]   #maandag wordt als donderdag doorgegeven
    dayNumber=date.weekday()
    return days[dayNumber]

today = datetime.date.today()
print "vandaag is: ", today
vandaag=int(dow(today))
#print vandaag
week[vandaag]=1
marktadres = markten.GetMarkten(week)
#print marktadres


# add the data for each individual market
for x in range(0,len(marktadres)):
	marktnaam = marktadres[x][1].replace("\xa0", "").replace("&nbsp;", "") # this is added in the CSV file for some reason
	marktlocatie = locatie.GetLatLong(marktnaam, google_api_key)
	marktafstand = locatie.GetDistanceMeters(userlocation[0], userlocation[1], marktlocatie[0], marktlocatie[1], google_api_key)
	pythondata = pythondata + "{ \"directions\": \""+marktafstand[1]+"\", \"image\" : \"marketicon.jpg\", \"name\": \""+str(marktnaam)+"\", \"dist\": \""+str(marktafstand[0])+"\", \"lat\": \""+str(marktlocatie[0])+"\", \"lng\": \""+str(marktlocatie[1]) + "\" },"

pythondata = pythondata[:-1]
pythondata = pythondata + "]},"

##### SUPERMARKET DATA #####

# add the data for the supermarkets
pythondata = pythondata + "{\"name\": \"Supermarkten\", \"weather\" : \""+huidigweer+"\", \"data\": ["      
supermarktenadres = supermarkten.GetSupermarkten()

# add the data for each individual market
for x in range(0,len(supermarktenadres)):
	supermarktnaam = supermarktenadres[x][0].replace("\xa0", "").replace("&nbsp;", "") # this is added in the CSV file for some reason
	supermarktafstand = locatie.GetDistanceMeters(userlocation[0], userlocation[1], supermarktenadres[x][3], supermarktenadres[x][4], google_api_key)
	pythondata = pythondata + "{ \"directions\": \""+supermarktafstand[1]+"\", \"image\" : \"supermarkticon.jpg\", \"name\": \""+str(supermarktnaam)+"\", \"dist\": \""+str(supermarktafstand[0])+"\", \"lat\": \""+str(supermarktenadres[x][3])+"\", \"lng\": \""+str(supermarktenadres[x][4]) + "\" },"

pythondata = pythondata[:-1]
pythondata = pythondata + "]},"

##### RET DATA #####
###kunnen we verschillende vinkjes voor verschillende type vervoer toevoegen?
pythondata = pythondata + "{\"name\": \"Haltes\", \"weather\" : \""+huidigweer+"\", \"data\": ["
retadres = ret.GetHalte("M")

for x in range(0,len(retadres)):   #dit stukje werkt nog niet, afgesterd
    ##print retadres[x][3], retadres[x][4]
    retafstand = locatie.GetDistanceMeters(userlocation[0], userlocation[1], retadres[x][3], retadres[x][4], google_api_key)
    pythondata = pythondata + "{ \"directions\": \""+supermarktafstand[1]+"\", \"image\" : \"metro.jpg\", \"name\": \""+str(retadres[x][0])+"\", \"dist\": \""+str(retafstand[0])+"\", \"walk\": \"300\", \"transport\": \"100\", \"lat\": \""+str(retadres[x][3])+"\", \"lng\": \""+str(retadres[x][4]) + "\" },"

pythondata = pythondata[:-1]
pythondata = pythondata + "]}"

pythondata = pythondata + "]";

# print the html to the screen
print "Content-type: text/plain\n"
print pythondata.encode('utf-8'),