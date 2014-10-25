#!/usr/bin/python
print "Content-Type: text/plain\n\n"
import urllib, re, sys
import cgi

url = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MGRAI1"

url_1 = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MAR795"

# Create the regex and use multiline

webpage = urllib.urlopen(url).read()

webpage1 = urllib.urlopen(url_1).read()

match = re.search("<city>([^<]*)</city>", webpage)
loc = match.group(1)

match = re.search("<observation_time>([^<]*)</observation_time>", webpage)
time = match.group(1)

match = re.search("<windchill_string>([^<]*)</windchill_string>", webpage)
wind_chill = match.group(1)

match = re.search("<state>([^<]*)</state>", webpage)
state = match.group(1)

match = re.search("<temperature_string>([^<]*)</temperature_string>", webpage)
temp = match.group(1)

match = re.search("<wind_string>([^<]*)</wind_string>", webpage)
wind = match.group(1)

match = re.search("<relative_humidity>([^<]*)</relative_humidity>", webpage)
rh = match.group(1)

match = re.search("<elevation>([^<]*)</elevation>", webpage)
ele = match.group(1)

match = re.search("<precip_today_string>([^<]*)</precip_today_string>", webpage)
precip = match.group(1)

print "         Black Canyon Weather Report"
print "         Elevation", ele 
print "         Temperature", temp
print "         Wind",wind
print "         Precipitation Today", precip
print "         RH",rh,"%"
print "        ",time
