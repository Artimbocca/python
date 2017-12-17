class Employee:        # define parent class
    def __init__(self, name):
        print ("Inside Employee constructor")
        self.name = name
    def calcSalary(self):
        print ('Inside calcSalary of Employee')
        self.salary = 0
        return self.salary
    def setName(self, name): self.name = name
    def getName(self): return self.name

class WageEmployee(Employee): # define child class
    def __init__(self, name, wage, hours):
        print ("Inside WageEmployee constructor")
        super().__init__(name)
        # Employee.__init__(self, name)     # alternative
        self.wage = wage
        self.hours = hours
    def setWage(self, wage): self.wage = wage
    def getWage(self): return self.wage
    def setHours(self, hours): self.hours = hours
    def getHours(self): return self.hours

e = Employee("Employee 1")
w = WageEmployee("WageEmployee 1", 10, 10)

print (e.getName())
print (e.calcSalary())

print (w.getName())
print (w.calcSalary())
print (w.getWage())
print (w.getHours())