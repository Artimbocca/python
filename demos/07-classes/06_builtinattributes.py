class A :
    x = 1
    s = 'a'
    def f(self):
        pass
     
a = A()
print(A.__dict__)
print(A.__doc__)
print(A.__name__)
print(A.__module__)
print(A.__bases__)


