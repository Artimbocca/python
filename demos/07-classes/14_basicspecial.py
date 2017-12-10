class Basic:
    def __init__(self, name): 
        self.name = name
    def show(self): 
        print ('Basic -- name: %s' % self.name)
class Special(Basic):
    def __init__(self, name, edible):
        Basic.__init__(self, name)
        self.upper = name.upper()
        self.edible = edible
    def show(self):
        Basic.show(self)
        print ('Special -- upper name: %s.' % self.upper,)
        if self.edible:
            print ("It's edible.")
        else:
            print ("It's not edible.")
    def edible(self):
        return self.edible

s = Special("pipo", 0)
s.show()

obj1 = Basic('Apricot')
obj1.show()
print ('=' * 30)
obj2 = Special('Peach', 1)
obj2.show()