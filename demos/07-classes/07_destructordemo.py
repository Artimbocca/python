class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3)) # prints the ids of the objects
print(pt1, pt2, pt3) # prints the ids of the objects
print(hex(id(pt1)), hex(id(pt2)), hex(id(pt3))) # prints the ids of the objects
del pt1
del pt2
#del pt3
str = eval(input("Enter your input: "));
print(("Received input is : ", str))