import requests
import re
from pprint import pprint




def getAllIndex(url) :
    indexList = []
    index = requests.get('http://%s/_cat/indices' % url).text
    for line in index.split('\n'):
        if len(line.split()) > 1 :
            if not line.split()[2].startswith('.') and not 'temp' in line:
                if re.search('[A-Za-z0-9]+-[0-9]{4}.[0-9]{2}.[0-9]{2}',line.split()[2]):
                    indexList.append(line.split()[2])
    return indexList




# pprint(getAllIndex('192.168.133.216:6775'))
