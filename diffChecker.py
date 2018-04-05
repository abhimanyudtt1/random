import sys

hash1 = {}
for line in open(sys.argv[1],'r') :
    line = line.replace('\n','').replace('(','')
    key,value = line.split(')')
    hash1[key] = value

hash2 = {}
for line in open(sys.argv[2],'r') :
    line = line.replace('\n','').replace('(','')
    key,value = line.split(')')
    hash2[key] = value



print "Keys in %s and not in %s " % (sys.argv[1],sys.argv[2] )
print set(hash1.keys()) - set(hash2.keys())


print "Keys in %s and not in %s " % (sys.argv[2],sys.argv[1] )
print set(hash2.keys()) - set(hash1.keys())


for key in set(hash1.keys()).intersection(set(hash2.keys())):
    if hash1[key] != hash2[key]:
        print key,hash1[key],hash2[key]

