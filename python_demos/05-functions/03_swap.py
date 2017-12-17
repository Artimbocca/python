def swap1( i, j ):
    tmp = j
    j = i
    i = tmp
    print (i, j)
    return 

def swap2( i, j ):
    tmp = j
    j = i
    i = tmp
    print (i, j)
    return i, j

print ('swap1')
x = 10
y = 11
print (x, y)
swap1(x, y)
print (x, y)

print ('swap2')
x = 10
y = 11
print (x, y)
x, y = swap2(x, y)
print (x, y)