from pprint import pprint
def aTotallyWeirdFuction(file):
    total2 = {}
    for line in open(file, 'r'):
        # -rw-r--r--   2 admin supergroup        217 2017-05-24 10:21 /data/collector_p7_test/ipfix/2017/05/24/10/05/br.1495620300._DONE
        line = line.replace('\s+', ' ')
        line = line.split(' ')
        line = filter(lambda x: x != '', line)
        bytes = int(line[4])
        key = line[-1].split('/')[-2]
        try:
            total2[key] += bytes
        except KeyError:
            total2[key] = bytes

    pprint(total2)

aTotallyWeirdFuction('./data/1')
aTotallyWeirdFuction('./data/2')
aTotallyWeirdFuction('./data/3')