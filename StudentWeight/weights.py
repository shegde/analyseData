"""

Statistics on student body weights in NY schools.
Gives total students per category - elementary/middle/
Plots on map based on color

"""

import xml.etree.ElementTree as ET
import collections


tree = ET.parse('data.xml')

response = tree.getroot()

overList = []
cityWise = {}

for row in response.iter('row'):
	area_name = category = city = state = 'n/a'
	zip = '00000'
	over = 0
	
	if row.find('area_name') is not None:
		area_name = row.find('area_name').text
	if row.find('grade_category') is not None:
		category = row.find('grade_category').text
	if row.find('city') is not None:
		city = row.find('city').text
	if row.find('state') is not None:
		state = row.find('state').text
	if row.find('zip_code') is not None:
		zip = row.find('zip_code').text
	if state is not 'n/a' and row.find('overweight_or_obese_1') is not None:
		over = int(row.find('overweight_or_obese_1').text)
		overList.append(over)
	if city and over:
	    if city not in cityWise:
	        cityWise[city] =  over
	    else:
	        cityWise[city] = cityWise[city] + over
	
	#print "%40s %40s %20s %2s %5d %5d" % (area_name, category, city, state, int(zip), over)
	


orderdCityWise = collections.OrderedDict(sorted(cityWise.items()))
for s in orderdCityWise:
    print "State: %s, Total: %s" % (s, orderdCityWise[s])
    
    
print "Total students overweight or obese: %d" % sum(overList)
		




