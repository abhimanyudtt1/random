import requests

from index_testcases.utils.getAllValidIndex import getAllIndex

log = 'firewallbuild55-2018.03.06'

for log in getAllIndex('192.168.133.216:6775') :
    print "Log Index : %s" % log
    responseRecord = requests.get('http://192.168.133.216:6775/%s/_search?size=1' % log).json()
    responseMeta = requests.get('http://192.168.133.216:6775/%s' % log).json()
    try :
        responseMeta = responseMeta['%s' % log]['mappings']['log']['properties']
    except KeyError:
        print "Error : Incorrect Format Log found : %s .Please check " % log
        continue
    mappings = {}
    for (x,y) in responseMeta.items():
        if not x == 'beat':
            try :
                mappings[x] = y['type']
            except KeyError:
                print "Error : No Key type found for key,v : %s,%s " % (x,y)
    for k,v in responseRecord['hits']['hits'][0]['_source'].items():
        if not k == 'beat':
            try :
                int(v)
                if not mappings[k] == 'long':
                    print "Error : ",k, v, mappings[k]
                else:
                    pass
            except (TypeError,ValueError):
                if mappings[k] == 'text' and isinstance(v,list):
                    print "Error : ", k, v, mappings[k]
                elif mappings[k] == 'text' and isinstance(v,str):
                    pass
