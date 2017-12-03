# You can use the input() function to ask for input:
# n = input("Enter number: ")
# print(n)

# To build a simple calculator we could just rely on the eval function of Python:
# print(eval(input("Expression: ")))   # e.g. 21 + 12

# Store result in variable and it can be used in expression:
while True:
    exp = input("Expression: ")  # e.g. 21 + 12, or m - 7
    m = eval(exp)
    print(m)

# HOWEVER, using eval is a very bad, as in dangerous, idea. If someone were to enter: os.system(‘rm -rf /’): disaster.

# So, let's quickly get rid of this eval and make our own much more specific eval that only excepts some basic mathematical expressions


