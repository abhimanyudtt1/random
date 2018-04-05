
import re

mainDict = {}
values = []
key = ''
firstFlag = True
for line in open('./sample','r'):
    line = line.rstrip('\n')
    line = line.split(' ')[-1].replace('"','')
    if re.search('adid_msisdn_mapping_[0-9A-Z]{8}-[0-9A-Z]{4}-[0-9A-Z]{4}-[0-9A-Z]{4}-[0-9A-Z]{12}',line) \
            or re.search('[0-9A-Z]{32}',line)\
            or re.search('[0-9A-Z]{8}-[0-9A-Z]{4}-[0-9A-Z]{4}-[0-9A-Z]{4}-[0-9A-Z]{12}',line) :
        if not firstFlag :
            mainDict[key] = values
        else:
            firstFlag = False
        if 'adid_msisdn_mapping' in line :
            key = re.search('adid_msisdn_mapping_(.*)',line).group(1)
            values = []
        else:
            key = line
            values = []
    elif re.search('[0-9]{10}',line):
        for each in line.split('_'):
            values.append(each)

from pprint import pprint
pprint(mainDict)


countDict = dict(map(lambda (x,y) : (x,len(y)),mainDict.items()))
print
print
pprint (countDict)

measuresSet = set()
for (k,v) in mainDict.items():
    for each in v :
        measuresSet.add(each)


print
print
pprint(measuresSet)