def testArgLists(arg, *argtuple, **kwargs):
    """ Function referencing argument, argument list and keyword arguments"""
    print ('arg:', arg)
    print ('args:', argtuple)
    print ('kwargs:', kwargs)


testArgLists(1, 2, 3, 4, 5, x=1 , y=2)
testArgLists(33, x=8 , y=9)
testArgLists(44)

def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
 
total(10, 1, 2, 3, extra_number=50)
total(10, extra_number=50)
