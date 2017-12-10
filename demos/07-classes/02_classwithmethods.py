# Filename: classwithmethod.py

class Person:
    def sayHi(self):
        print('Hello, how are you?')
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello, world! I'm %s." % self.name)

p1 = Person()
p1.sayHi()
 
# This short example can also be written as Person().sayHi()
Person().sayHi()

p2 = Person()
p2.setName('pipo')
print (p2.getName())
p2.greet()
print(p2.name)

#Person().setName('mamaloe')
#print (Person().getName())
#Person().greet()
#print (Person().name)