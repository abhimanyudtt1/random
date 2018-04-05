import sys

FH = open(sys.argv[1],'r')
popId = open(sys.argv[2],'r')
cust = open(sys.argv[3],'r')
nonPop = open(sys.argv[4],'r')

finalDataIngress = {}
finalDataEgress = {}

popMap = {}
custMap = {}

nonPop = nonPop.readlines()
nonPop = map(lambda x : x.rstrip('\n'),nonPop)

for line in popId :
    line = line.split('|')
    popMap[line[0]] = line[1]

for line in cust :
    line = line.split('\t')
    custMap[line[0]] = line[1]

for line in FH :
    line = line.split('^')
    try :
        customer = custMap[line[3]]
    except KeyError :
        customer = line[3]
    try :
        popIngress = popMap[line[4]].rstrip('\n')
    except KeyError:
        popIngress = line[4]
    try :
        popEgress = popMap[line[7]].rstrip('\n')
    except KeyError:
        popEgress = line[7]
    # noinspection PyRedeclaration
    data = line[-1]
    data = data.replace('\n','').replace(']','').replace(',','',1)
    data = reduce(lambda x,y : int(x)+int(y),data.split(','))
    direction = line[0]
    if direction == '102':
        try:
            finalDataIngress['%s,%s' % ( popIngress,popEgress)] += data*8/3600
        except KeyError:
            finalDataIngress['%s,%s' % ( popIngress,popEgress)] = data*8/3600
    else:
        try:
            finalDataEgress['%s,%s' % ( popIngress,popEgress)] += data*8/3600
        except KeyError:
            finalDataEgress['%s,%s' % ( popIngress,popEgress)] = data*8/3600




FH.close()

FOIngressAll = open('%s_report_ingress_all' % sys.argv[1],'w')
FOEgressAll = open('%s_report_egress_all' % sys.argv[1],'w')
FOIngressNonUS = open('%s_report_ingress_nonUs' % sys.argv[1],'w')
FOEgressNonUS = open('%s_report_egress_nonUs' % sys.argv[1],'w')
FOIngressUS = open('%s_report_ingress_us' % sys.argv[1],'w')
FOEgressUS = open('%s_report_egress_us' % sys.argv[1],'w')

for k,v in finalDataIngress.items():
    popIngress = k.split(',')[0]
    popEgress = k.split(',')[1]
    if popIngress in nonPop:
        FOIngressUS.write('%s -> %s \n' % (k,v))

for k,v in finalDataEgress.items():
    popIngress = k.split(',')[0]
    popEgress = k.split(',')[1]
    if popEgress in nonPop :
        FOEgressUS.write('%s -> %s \n' % (k,v))

for k,v in finalDataIngress.items():
    popIngress = k.split(',')[0]
    popEgress = k.split(',')[1]
    if not ( popEgress in nonPop and popIngress in nonPop):
        FOIngressNonUS.write('%s -> %s \n' % (k,v))

for k,v in finalDataEgress.items():
    popIngress = k.split(',')[0]
    popEgress = k.split(',')[1]
    if not (popEgress in nonPop and popIngress in nonPop):
        FOEgressNonUS.write('%s -> %s \n' % (k,v))

for k,v in finalDataIngress.items():
    popIngress = k.split(',')[0]
    popEgress = k.split(',')[1]
    if True:
        FOIngressAll.write('%s -> %s \n' % (k,v))

for k,v in finalDataEgress.items():
    popIngress = k.split(',')[0]
    popEgress = k.split(',')[1]
    if True:
        FOEgressAll.write('%s -> %s \n' % (k,v))