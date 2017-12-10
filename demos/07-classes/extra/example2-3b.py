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

class F1(A,N):
    def __init__(self):
        print "G1",
        super(F1, self).__init__()
class F2(B,M):
    def __init__(self):
        print "G2",
        super(F2, self).__init__()
        
class G(F1,F2):
    def __init__(self):
        print "G",
        super(G, self).__init__()


def test(cl):
    print "MRO:", [x.__name__ for x in cl.__mro__]
    print "Calls:",
    cl()
    print

test(G)
