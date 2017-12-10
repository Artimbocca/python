class Secretive:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)
    def __inaccessible(self):
        print ("Bet you can't see me...")
    def accessible(self):
        print ("The secret message is:")
        self.__inaccessible()

s = Secretive()
s.accessible()
s._Secretive__inaccessible()
#s.__inaccessible()

s.count()
s.count()

print (s._Secretive__secretCount)
print (s.__secretCount)