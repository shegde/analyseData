import urllib
import xml.etree.ElementTree as ET
import re

url = 'http://www.cpsc.gov/en/Newsroom/CPSC-RSS-Feed/Recalls-RSS/'
urlData = urllib.urlopen(url)
xmlData = urlData.read()
rss = ET.fromstring(xmlData)

recallData = {}
companies = []
regex = r'(.*?)[rR]ecall{1}.*'

count = 0

for channel in rss:
	for item in channel.iter('item'):
		title = item.find('title').text
		pubDate = item.find('pubDate').text
		desc = item.find('description').text
		guide = item.find('guid').text
		link = item.find('link').text
		recallData[count] = {'title': title, 'pubDate': pubDate, 'description': desc, 'guide': guide, 'link': link}
		count = count + 1
		
for id in recallData.keys():
	title = recallData[id]['title']
	m = re.search(regex, title)
	companies.append(m.group(1))

setList = set(companies)

# duplicates
morethanone = set([x for x in companies if companies.count(x) > 1])

# number of companies that have recalled
print len(setList)

# companies that have recalled more than one product
print morethanone


	

		
