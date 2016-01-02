import urllib2
import urllib
import json

def GetLatLong(address, api_key):
	# Get JSON data from google
	urldata = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address="+urllib.quote_plus(address)+",Rotterdam&key=" + api_key).read()
	# parse the JSON data
	parsed_json = json.loads(urldata)
	# find the correct items in the JSON data
	return [parsed_json["results"][0]["geometry"]["location"]["lat"], parsed_json["results"][0]["geometry"]["location"]["lng"]]
	
def GetDistanceMeters(x1, y1, x2, y2, api_key):
	# Get JSON data from google
	urldata = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin="+str(x1)+","+str(y1)+"&destination="+str(x2)+","+str(y2)+"&key=" + api_key).read()
	# parse the JSON data
	parsed_json = json.loads(urldata)
	# find the correct item in the JSON data
	return parsed_json["routes"][0]["legs"][0]["distance"]["text"];