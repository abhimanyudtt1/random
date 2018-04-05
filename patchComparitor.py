import sys
import subprocess

#patch1 = sys.argv[2]
#path2 = sys.argv[3]


FH = open('./aa.csv','w')

FH.write('delete from IngressProspectSearchTable where INGRESS_PROSPECT_ENTITY_ID not in (')
for i in range(5578,6578):
    FH.write('%s,' % i)
