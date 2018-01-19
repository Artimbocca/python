class MyClass:
    def __init__(self):             # "base" constructor.
        pass
    @classmethod
    def one_constructor(cls, foo): # Special constructor.
        self = cls()
        self.foo = foo
        return self
    @classmethod
    def another_constructor(cls, bar): # Constructor.
        pass
class MySubclass(MyClass):   # Does necessary customizations.
        pass
obj = MySubclass.one_constructor('foo')
print (obj)
