#-------------------------------------------------------------------------------
# Name:        Blacks
# Purpose:
#
# Author:      casey.jenkins
#
# Created:     26/10/2012
# Copyright:   (c) casey.jenkins 2012
# Licence:     
#-------------------------------------------------------------------------------


#!/usr/bin/python
#print "Content-Type: text/plain\n\n"
import urllib, re, sys
import cgi

#LOCO = sys.argv[1].upper()

url = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MGRAI1"

url_1 = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MAR795"

url_2 = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=KIDGRACE5"

# Create the regex and use multiline

webpage = urllib.urlopen(url).read()

webpage1 = urllib.urlopen(url_1).read()

webpage2 = urllib.urlopen(url_2).read()

match = re.search("<full>([^<]*)</full>", webpage2)
loc = match.group(1)

match = re.search("<observation_time>([^<]*)</observation_time>", webpage2)
time = match.group(1)

match = re.search("<windchill_string>([^<]*)</windchill_string>", webpage2)
wind_chill = match.group(1)

match = re.search("<state>([^<]*)</state>", webpage2)
state = match.group(1)

match = re.search("<temperature_string>([^<]*)</temperature_string>", webpage2)
temp = match.group(1)

match = re.search("<wind_string>([^<]*)</wind_string>", webpage2)
wind = match.group(1)

match = re.search("<relative_humidity>([^<]*)</relative_humidity>", webpage2)
rh = match.group(1)

match = re.search("<pressure_string>([^<]*)</pressure_string>", webpage2)
press = match.group(1)

print "         "
print "         Black Canyon Weather Report"
print "         Location", loc
print "         Temperature", temp
print "         Wind",wind
print "         RH",rh,"%"
print "         Pressure", press
print "        ",time
print "        "

#end
