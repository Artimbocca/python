class Account :
    interestRate = 10
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def getInterestRate1():
        return Account.interestRate
    getInterestRate1 = staticmethod(getInterestRate1)
    @staticmethod
    def getInterestRate2():
        return Account.interestRate
   
print (Account.getInterestRate1())
print (Account.getInterestRate2())

account1 = Account('pipo')
account2 = Account('mamaloe')

print (account1.name)
print (account1.getInterestRate1())

Account.interestRate = 11

print (account2.name)
print (account2.getInterestRate1())
print (account2.getInterestRate2())
print (account1.getInterestRate2())
