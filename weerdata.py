import urllib2
import json
import cgitb

cgitb.enable(display=1)

def GetWeerdata():
	urldata = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Rotterdam&APPID=9c6c775e33798582cec99cb843fedf3a").read()
	parsed_json = json.loads(urldata)
	return parsed_json["weather"][0]["main"];

print "Content-type: text/plain\n"
print GetWeerdata()