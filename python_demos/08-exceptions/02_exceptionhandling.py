try :
    x = 1
    y = 0
    z = x/y                   # ZeroDivisionError
except :
    print ('Cannot divide by zero')
    
try :
    tup = (1,2,3)
    tup[0] = 2                 # TypeError
except :
    print ('Cannot change tuple contents')

try :
    fh = open("somefile", "r")  # IOError
except :
    print ('Cannot open file')