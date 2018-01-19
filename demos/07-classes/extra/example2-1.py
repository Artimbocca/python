class A(object):
    def __init__(self):
        print ("A",)
        super(A, self).__init__()
    pass
    
class B(object):
    def __init__(self):
        print ("B",)
        super(B, self).__init__()
    pass

# some other module defines this class, not knowing about super()

class C(A,B):
    def __init__(self):
        print ("C",)
        A.__init__(self)
        B.__init__(self)
#        super(D, self).__init__()
    pass

print ("MRO:", [x.__name__ for x in C.__mro__])
print ("Calls:",)
C()
print 
