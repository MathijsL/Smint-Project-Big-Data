import urllib2
urldata = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Amsterdam  ").read()
print urldata

