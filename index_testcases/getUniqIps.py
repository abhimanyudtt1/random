from utils.uniqueValueGetter import getUniqValue
from pprint import pprint

log = 'adfcuk-2018.03.14'

ipList = list(getUniqValue('192.168.133.216:6775',log,'sourceNetworkAddress'))

subnets = ['/8', '/24', '/29' ,'/20' ,'/16', '/32']


prefix = []
for i in subnets:
    for j in range(6):
        prefix.append(ipList[j]+ i)



for i in subnets:
    for j in range(6):
        prefix.append(filter(lambda x : ':' in x , ipList)[j]+ i)

if True :
    fh = open('/tmp/prefixMix','w' )
    for i in prefix :
        fh.write('%s\n' % i)
    fh.close()
