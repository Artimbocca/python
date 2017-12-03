
def say_hi():
    print('Hi, this is {} speaking.'.format(__name__))

__version__ = '0.1'

if __name__ == '__main__':
    say_hi()
