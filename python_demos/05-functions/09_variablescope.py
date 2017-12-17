# def func1(x):
#     print ('x is', x)
#     x = 2
#     print ('Changed local x to', x)
# x = 50
# func1(x)
# print ('x is still', x)
#
# def func2():
#     global y
#     print ('y is', y)
#     y = 2
#     print ('Changed global y to', y)
# y = 50
# func2()
# print ('Value of y is', y)


x = 1


def g(x):
    print(x)
    x = 2


def f(x):
    x = 3
    g(x)


f(x)

print(x)

import this