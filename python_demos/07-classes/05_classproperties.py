class A(object):
    count = 0
    def __init__(self, name):
        self.name = name
    def set_name(self, name):
        print('setting name: %s' % name)
        self.name = name
    def get_name(self):
        print('getting name: %s' % self.name)
        return self.name
    objname = property(get_name, set_name)

def test():
    a = A('apple')
    print('name: %s' % a.objname)
    a.objname = 'banana'
    print('name: %s' % a.objname)

test()

