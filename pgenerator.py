x = ''
while (True):
    x = raw_input('Enter the place value after decimal for pi(Enter \'Quit\' to exit) : ')
    try :
        x = int(x)
        break
    except ValueError:
        if x != 'quit':
            print "Please enter a digit only!"
        else:
            exit(0)

n = 10
for i in range(x):
    q = n/7
    r = n%7
    n = int(str(r)+'0')

print q



if __name__ == '__main__':
    global q
    print q
    print x
