class SquareGetterSetter(object):
    def __init__(self, length):
        self._length = length
    def get_length(self):  # Java-style
        return self._length
    def set_length(self, length):  # Java-style
        self._length = length

r = SquareGetterSetter(5)
print (r.get_length())
r.set_length(6)
print (r.get_length())


class SquarePropertySyntax(object):
    def __init__(self, length):
        self._length = length
    def get_length(self):  
        return self._length
    def set_length(self, length): 
        self._length = length
    def del_length(self): 
        del self._length
    length = property(get_length, set_length, del_length)   

r = SquarePropertySyntax(15)
print (r.length)  # automatically calls getter
r.length = 16  # automatically calls setter
print (r.length)


class SquarePropertyDecorator(object):
    def __init__(self, length):
        self._length = length
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @length.deleter
    def length(self):
        del self._length

r = SquarePropertyDecorator(115)
print (r.length)  # automatically calls getter
r.length = 116  # automatically calls setter
print (r.length)