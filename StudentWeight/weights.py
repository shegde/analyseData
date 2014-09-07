"""

Statistics on student body weights in NY schools.
Gives total students per category - elementary/middle/
Gives top 5 cities

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
	

orderdCityWise = collections.OrderedDict(sorted(cityWise.items()))
for s in orderdCityWise:
    print "City: %s, Total: %s" % (s, orderdCityWise[s])
    

print "Total students overweight or obese: %d" % sum(overList)

# top 5 cities with
top = []
for k in cityWise.keys():
    top.append((cityWise[k], k))
    
print sorted(top, reverse=True)[:5]
		




