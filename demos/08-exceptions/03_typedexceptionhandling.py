try :
    x = 1
    y = 0
    #z = x/y                   # ZeroDivisionError
  
    tup = (1,2,3)
    #tup[0] = 2                 # TypeError
    
    fh = open("somefile", "r")  # IOError
except ZeroDivisionError :
    print ('Division by zero')
except TypeError :
    print ('Cannot change tuple contents')
except IOError :
    print ('Cannot open file') 