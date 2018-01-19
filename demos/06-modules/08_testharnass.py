"""
This simple module contains definitions of a class and several 
functions.
"""

LABEL = '===== Testing a simple module ====='

class Person:
    """Sample of a simple class definition.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def show(self):
        print ('Person -- name: %s  description: %s' % (self.name, self.description))

def tes(msg, count):
    """A sample of a simple function.
    """
    for idx in range(count):
        print ('%s %d' % (msg, idx))

def tesDefaultArgs(arg1='default1', arg2='default2'):
    """A function with default arguments.
    """
    print ('arg1:', arg1)
    print ('arg2:', arg2)

def tesArgLists(*args, **kwargs):
    """
    A function which references the argument list and keyword arguments.
    """
    print ('args:', args)
    print ('kwargs:', kwargs)

def main():
    """
    A test harness for this module.
    """
    print (LABEL)
    person = Person('Herman', 'A cute guy')
    person.show()
    print ('=' * 30)
    tes('Test #', 4)
    print ('=' * 30)
    tesDefaultArgs('Explicit value')
    print ('=' * 30)
    tesArgLists('aaa', 'bbb', arg1='ccc', arg2='ddd')

if __name__ == '__main__':
    import sys
    print(sys.path)


