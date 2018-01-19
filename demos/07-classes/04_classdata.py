class C:
    count = 0   # number of times C.__init__ called
    def __init__(self):
        C.count = C.count + 1
    def getcount(self):
        return C.count  # or return self.count

c1 = C()
print('Current count:', c1.getcount())
c2 = C()
#print  'Current count:', C.getcount()
print('Current count:', c1.getcount())
