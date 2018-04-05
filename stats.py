#!/usr/bin/env python
import sys
import re
convertor = {
    'ms' : 1/1000,
    's' : 1,
    'min' : 60
}

T = 0

for line in sys.stdin:
    try :
        line = line.split(' ')
        time1 = line[-6]
        time2 = line[-5]
        time2 = convertor[time2]
        time = float(time1) * float(time2)
        T = T + float(time)

    except (AttributeError,KeyError,IndexError) as ss :
        print line


print T