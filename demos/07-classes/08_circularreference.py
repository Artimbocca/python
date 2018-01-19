class A:
    def __init__(self, x):
        print ("A: Hi")
        self.x = x
    def __del__(self):
        print ("A: bye")
 
class B:
    def __init__(self):
        print ("B: Hi")
        self.a = A(self) # x = this instance
 
    def __del__(self):
        print ("B: Bye")
 
b = B()
# del b # This doesn't work either
