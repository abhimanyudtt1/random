from node import node
import time
nd = {'ip':'192.168.113.93',
      'user':'root',
      'password':'root@123'
      }

collectorNode = node(nd)
path ='/data/collector/BR_sprint_2hrs_data'
doneFile = '/data/collector/BR_sprint_2hrs_data/2017/07/17/00/00/br.1500249600._DONE'

output = collectorNode.shellCmd('hadoop fs -ls -R %s | grep DONE' % path)[0]


dataMatrix = {}
for line in output :
    if line.startswith('d'):
        continue
    else:
        file = str(line.rstrip('\n'))
        file = file.split(' ')[-1]
        file = file.split('/')
        #print line
        try :
            dataMatrix['/'.join(file[:-2])].add(file[-2])
        except KeyError:
            dataMatrix['/'.join(file[:-2])] =  set(file[-2])

from pprint import pprint
pprint(dataMatrix)

for k,v in dataMatrix.items():
    for bin in map(lambda x : str(x).zfill(2),range(0,60,5)) :
        collectorNode.shellCmd('hadoop fs -mkdir -p %s/%s ' % (k, bin))
        t = '%s/%s' % (k, bin)
        t = t.split('/')[-5:]
        t = str(int(int(time.mktime(time.strptime('/'.join(t), "%Y/%m/%d/%H/%M"))) + 5.5 * 3600)) + '_DONE'
        collectorNode.shellCmd('hadoop fs -cp %s %s/%s/%s' % (doneFile, k, bin, t))


#for line in open('aa','rb'):
