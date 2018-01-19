sum1 = lambda arg1, arg2: arg1 + arg2;
def plus (a,b):
    return a+b

print (sum1(3,7))

l = map(sum, [(2,3),(9,4)])

l = map(plus, range(10),range(20,30))

for r in l:
    print(r)


squared =  [x**2 for x in range(10)]
sq = lambda x: x**2
squared =  [(lambda x: x**2)(x) for x in range(10)]

print (squared)

print((lambda x: x**2))
print(lambda x: x**2)