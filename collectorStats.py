from node import node
import time
import threading
nd = {'ip':'192.168.113.93',
      'user':'root',
      'password':'root@123'
      }

collectorNode = node(nd)

adaptors = ['netflow','netflowV10']

type = '''average-bin-size
dropped-flow-invalid-field-count
dropped-future-binning-flow
max-flow
total-flow
average-flow-rate
dropped-flow-invalid-field-format
dropped-header
num-files-dropped
dropped-binning-flow
dropped-flow-invalid-field-value
expired-data-flow
num-files-processed
dropped-expired-binning-flow
dropped-flow-length-mismatch
last-freezed-bin
num-files-with-errors
dropped-flow
dropped-flow-missing-header
last-freezed-bin-size
prorated-flow'''
collectorNode.login()

tt = time.strftime("%y-%m-%d_%H:%M")


# cli -m config -t "pm process collector terminate" ;
# nnShellRunAll "date -s \"2017/05/24 10:20\" " ;
# sleep 5; hadoop fs -rmr /data/collector_p7_test;
# cli -m config -t "pm process collector restart" ;

#collectorNode.cliCmd('pm process collector terminate')
#print 'pm process collector terminated'
#collectorNode.shellCmd('nnShellRunAll \"date -s \\"2017/05/24 10:20\\" \"')
#print "Time Changed waiting for 5 secs "
#time.sleep(5)
#collectorNode.shellCmd('/opt/hadoop/bin/hadoop fs -rmr /data/collector_p7_test')
#print "/data/collector_p7_test removed"
#collectorNode.cliCmd('pm process collector restart')
#print "Collector restarted"
#time.sleep(5)

#collectorNode.shellCmd()
#collectorNode.shellCmd()

#threading.Thread(target=collectorNode.shellCmd,args=[
#    'python /var/home/root/replay_pcap/replay_pcap.py -l -r /var/home/root/replay_pcap/autoconfig.cfgx -f /data/217.149.32.12_Netflow.pcap'
#])

#threading.Thread(target=collectorNode.shellCmd,args=[
#    'python /var/home/root/replay_pcap/replay_pcap.py -l -r /var/home/root/replay_pcap/autoconfig.cfgx -f /data/144.228.243.98_Ipfix.pcap'
#])


#print "Replaying traffic on collector done"
#time.sleep(5)
type = type.split('\n')

FH = open('./stats/log_%s' % tt ,'w')
for adaptor in adaptors:
    for ty in type:
        print 'collector stats instance-id 200 adaptor-stats %s %s' % (adaptor,ty)
        stdout,stderr = collectorNode.cliCmd('collector stats instance-id 200 adaptor-stats %s %s' % (adaptor, ty))
        print stdout[0].rstrip('\n')
        FH.write('collector stats instance-id 200 adaptor-stats %s %s\n' % (adaptor,ty))
        FH.write(stdout[0])

collectorNode.cliCmd('pm process collector terminate')
FI = open('./data/log_%s' % tt ,'w')
stdout,stderr = collectorNode.shellCmd('/opt/hadoop/bin/hadoop fs -ls -R /data/collector_p7_test/ ')

for line in stdout:
    FI.write(line)

collectorNode.ssh.close()