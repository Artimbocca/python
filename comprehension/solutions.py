#1
def even(n):
    return n % 2 == 0

print([x for x in range(12) if even(x)])

#2
def perfect(n):
    return int(n**0.5)== n**0.5

print([x for x in range(100) if perfect(x)])

#3
def eg1_for(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat


matrix = [list(r) for r in [range(0,5), range(5,10), range(10,15)]]
print("Original Matrix: " + str(matrix))
print("FOR-loop result: " + str(eg1_for(matrix)))

print([x for sublist in matrix for x in sublist])

#4
print({k:v for k,v in zip(range(10),range(10))})

#5

import random
from string import ascii_lowercase
d = {k:v for k in random.sample(ascii_lowercase, 10) for v in random.sample(range(10,200), 10)}
print(d)
items = d.items()
print(items)
for k in d:
    d[k] += 1
# updating d is reflected in the items view !!!
print(items)
ordered = sorted([(v, k) for k, v in items], reverse=True)
for v, k in ordered:
    print("{}: {}".format(k, v))
print([k for v, k in ordered])
