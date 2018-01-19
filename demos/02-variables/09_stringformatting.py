print ("My name is %s and weight is %d kg!" % ('Pipo', 66)) 

i = 111
print ("Integer %d Hexadecimal %x exponential %e floating point %.3f" % (i, i, i, i))

print ('{0}, {1}, {2}'.format('a', 'b', 'c')) # 'a, b, c'

print ('{}, {}, {}'.format('a', 'b', 'c'))    # 3.1+ only : 'a, b, c'

print ('{2}, {1}, {0}'.format('a', 'b', 'c')) # 'c, b, a'

print ('{2}, {1}, {0}'.format(*'abc'))        # unpacking argument sequence : 'c, b, a'

print ('{0}{1}{0}'.format('abra', 'cad'))     # arguments' indices can be repeated : 'abracadabra'

s = '{0}, {1}, {2}'.format('a', 'b', 'c')
print (s)
s = '{}, {}, {}'.format('a', 'b', 'c')
print (s)
s = '{2}, {1}, {0}'.format('a', 'b', 'c')
print (s)
