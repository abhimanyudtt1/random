import sys
import re
import SubnetTree
import ipaddress
import socket
import time
if len(sys.argv) < 2:
	print "Usage: "+sys.argv[0]+" <Input file with list of Prefixes> <Input file with list of IP addresses>"
	print "Example: "+sys.argv[0]+"prefix_file ipaddress_file"
	sys.exit()
prefix_file = sys.argv[1]
ip_file = sys.argv[2]

prefixList = []
ts = time.time()

from multiprocessing import Pool


def f(filename,breakup):
    fileList = []
    counter = 0
    temp = []
    for line in open(filename):
        ip = ipaddress.ip_address(unicode(line.rstrip('\n').lstrip(' '), "utf-8"))
        if counter < breakup :
            temp.append(ip)
        else:
            fileList.append(tuple(temp))
            counter = 0
            temp = []
            continue
        counter += 1

    return fileList


def comparison(ipList):
    longestPrefixMatch = {}
    for ip in ipList :
        for prefix in prefixList:
            if ip in prefix:
                if not ip in longestPrefixMatch :
                    longestPrefixMatch[ip] = prefix
                else:
                    if int(str(longestPrefixMatch[ip]).split('/')[-1]) < int(str(prefix).split('/')[-1]) :
                        longestPrefixMatch[ip] = prefix
    #from pprint import pprint
    print longestPrefixMatch


ipList = f(ip_file,breakup=2)

for line in open(prefix_file):
    line = unicode(line.rstrip('\n').rstrip(' '), "utf-8")
    try :
        prefixList.append(ipaddress.ip_network(line))
    except ipaddress.AddressValueError as e :
        print e.message

#ipaddress.ip_network(u'138.121.244.0/27').broadcast_address


p = Pool(5)
p.map(comparison,ipList)
print time.time() - ts
exit(1)

ipList = []

for i in open(ip_file):
    try :
        ipList.append(ipaddress.ip_address(unicode(i.rstrip('\n').lstrip(' '),'utf-8')))
    except ipaddress.AddressValueError as e :
        print e.message

for ip in ipList :
    for prefix in prefixList :
        if ip in prefix :
            print "%s : %s " % (prefix,ip)


print time.time() - ts
exit(1)








st = SubnetTree.SubnetTree()
for prefix in open(prefix_file).readlines():
	prefix = prefix.strip('\n')
	if prefix:
		st[prefix] = prefix
st.set_binary_lookup_mode(False)
def pass_ipfile(ip_file):
	for ip in open(ip_file).readlines():
		st.set_binary_lookup_mode(False)
		ip = ip.strip('\n')
		if ip:
			if ip in st:
				st.set_binary_lookup_mode(True)
				print ip,':',st[socket.inet_aton(ip)]
			else:
				print ip,':','No matching prefix found'
def pass_ip (ip ):
	if ip in st:
		st.set_binary_lookup_mode(True)
		print ip,':',st[socket.inet_aton(ip)]
	else:
		print ip,':','No matching prefix found'

pass_ipfile(ip_file)