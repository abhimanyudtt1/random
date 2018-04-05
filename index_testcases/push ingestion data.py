import requests
from pprint import pprint

api = 'http://192.168.133.215:6774/metadatamanagementservice/v1/namespaces/default/ingest/'
prefix = 'spider'


from getUniqIps import subnets
header = {'Content-Type' : 'application/json'}
jsonData = '{"tempflag": "false", "inputconffile": "/opt/guavus/security/conf/Parser_blacklist.conf", "inputlogspath": "/tmp/logs_new/prefix_ib.csv" , "type" : "catalogue"}'
import json

jsonData = json.loads(jsonData)
print jsonData
print type(jsonData)
for i in subnets :
    api1 = api + 'prefix%s%s' % (prefix,i.split('/')[-1])
    jsonData['inputlogspath'] = "/tmp/prefix_%s" %  i.split('/')[-1]
    jsonData1 = json.dumps(jsonData)
    print header, api, jsonData1
    response = requests.post(api1,data=jsonData1,headers=header)
    pprint (response)