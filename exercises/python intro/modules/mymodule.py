# Filename: mymodule.py
__version__ = '0.1'

def say_hi():
    print('Hi, this is mymodule. Name: {}, version: {}.'.format(__name__, __version__))

say_hi()
# End of mymodule.py

