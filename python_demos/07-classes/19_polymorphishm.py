class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ('(Initialized SchoolMember: {0})'.format(self.name))
 
    def tell(self):
        '''Tell my details.'''
        print ('Name:"{0}" Age:"{1}"'.format(self.name, self.age))
 
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print ('(Initialized Teacher: {0})'.format(self.name))
 
    def tell(self):
        SchoolMember.tell(self)
        print ('Salary: "{0:d}"'.format(self.salary))
 
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ('(Initialized Student: {0})'.format(self.name))
 
    def tell(self):
        SchoolMember.tell(self)
        print ('Marks: "{0:d}"'.format(self.marks))
 
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
 
print() # prints a blank line
 
members = [t, s]
for member in members:
    member.tell() # works for both Teachers and Students

class A(object):
    def show(self, msg):
        print ('class A -- msg: "%s"' % (msg, ))
class B(object):
    def show(self, msg):
        print ('class B -- msg: "%s"' % (msg, ))
class C(object):
    def show(self, msg):
        print ('class C -- msg: "%s"' % (msg, ))
def test():
    objs = [A(), B(), C(), A(), ]
    for idx, obj in enumerate(objs):
        msg = ('message # %d' % (idx + 1, ))
        obj.show(msg)
if __name__ == '__main__':
    test()

