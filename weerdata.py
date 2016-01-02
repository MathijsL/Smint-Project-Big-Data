import urllib2

def GetWeerdata():
	urldata = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Rotterdam").read()
	return urldata

