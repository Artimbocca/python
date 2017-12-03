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

# So, let's quickly get rid of this eval and make our own much more specific eval that only excepts
# some basic mathematical expressions

# For this, you need to distinguish between operators and operands, write your own evaluator
# and keep track of the result: in a simple calculator you basically keep a running total as left operand.

# One option is to build a dictionary in which you store functions (lambda's?) under whatever symbols you want to use
# for different operators.

# Extensions: building expression trees for composite expressions, an undo option etc.