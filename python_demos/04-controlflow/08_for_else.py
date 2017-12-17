from math import sqrt
for n in range(99, 80, -1):
    root = sqrt(n)
    print (root)
    print (int(root))
    if root == int(root):
        print (n)
        break
else:
    print( "Didn't find it!")
