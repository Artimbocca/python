class BreakException1(Exception):
    pass
    
def test():
    a = [11, 22, 33, 44, 55, 66, ]
    b = [111, 222, 333, 444, 555, 666, ]
    try:
        for x in a:
            print ('outer -- x: %d' % x)
            for y in b:
                if x > 22 and y > 444:
                    raise BreakException1('leaving inner loop')
                print ('inner -- y: %d' % y)
            print ('outer -- after')
            print ('-' * 40)
    except BreakException1 as exp:
        print ('out of loop -- exp: %s' % exp)

test()
