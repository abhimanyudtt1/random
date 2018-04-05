import requests
import re
from pprint import pprint




def getUniqValue(url,index,field) :
    values = set()
    data = requests.get('http://%s/%s/_search?size=10000' % (url,index)).json()
    #pprint(data)
    for v in data['hits']['hits'] :
        values.add(v['_source'][field])

    return values




#pprint (getUniqValue('192.168.133.216:6775','firewallbuild55-2018.03.06','dstIp'))