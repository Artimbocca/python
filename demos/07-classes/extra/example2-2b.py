class A(object):
    def __init__(self):
        print "A",
        super(A, self).__init__()

class B(object):
    def __init__(self):
        print "B",
        super(B, self).__init__()

class N:
    def __init__(self):
        print "N",
class M:
    def __init__(self):
        print "M",


class F1(A,B,N):
    def __init__(self):
        print "F1",
        super(F1, self).__init__()

class F2(A,N,B):
    def __init__(self):
        print "F2",
        super(F2, self).__init__()

class F3(N,A,B):
    def __init__(self):
        print "F3",
        super(F3, self).__init__()

class F4(A,B,N,M):
    def __init__(self):
        print "F3",
        super(F4, self).__init__()

        
def test(cl):
    print "MRO:", [x.__name__ for x in cl.__mro__]
    print "Calls:",
    cl()
    print

test(F1)
test(F2)
test(F3)
test(F4)
