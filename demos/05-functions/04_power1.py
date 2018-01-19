def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

print (power(2,3))
print (power(3,2))
print (power(5,0))
print (power(3))