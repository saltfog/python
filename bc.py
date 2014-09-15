#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      casey.jenkins
#
# Created:     26/10/2012
# Copyright:   (c) casey.jenkins 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#!/usr/bin/python
#print "Content-Type: text/plain\n\n"
import urllib, re, sys
import cgi

#LOCO = sys.argv[1].upper()

url = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MGRAI1"

url_1 = "http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=MAR795"

url_2 = "http://www.pacificorp.com/es/hydro/hl/wr/br/bgd.html"

# Create the regex and use multiline

webpage = urllib.urlopen(url).read()

webpage1 = urllib.urlopen(url_1).read()

webpage2 = urllib.urlopen(url_2).read()

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

match = re.search("<precip_1hr_in>([^<]*)</precip_1hr_in>", webpage1)
precip = match.group(1)

#Water Level
match = re.search("</td><td>([^<]*)</td><td></td></tr></table>", webpage2)
level = match.group(1)

print "         Temperature", temp
print "         Wind",wind
print "         RH",rh,"%"
print "         Precipitation", precip, "in"
print "         Water Level", level, "CFS"
print "        ",time