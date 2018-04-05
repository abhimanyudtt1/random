

class abc(object):
    def __init__(self,x):
        if x == 1 :
            self.x = 1
        else:
            self.x = abc(x-1).x*x
m = abc(5)
print m.x


import