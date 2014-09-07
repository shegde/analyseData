"""
	Find top 5 streets with most potholes in Chicago
"""


import csv
import pprint
import operator

openCases = {}
f = open('potholes.csv')
rows = csv.DictReader(f)

for row in rows:
	if row['STATUS'] == 'Open':
		fulladdr = row['STREET ADDRESS']
		splitaddr = fulladdr.split()
		addr = ' '.join(splitaddr[2:])	
		# '7617 W EVERELL AVE' becomes 'EVERELL AVE'
		if addr not in openCases:
			openCases[addr] = 1
		else:
			openCases[addr] += 1


# get max value item in one line
k_max = max(openCases.iteritems(), key=operator.itemgetter(1))[0]
print "Max potholes on %s, Number: %s" % (k_max, openCases[k_max])

# Top 5 number of potholes
top = []
for k in openCases.keys():
    top.append((openCases[k], k))

print sorted(top, reverse=True)[:5]




	


