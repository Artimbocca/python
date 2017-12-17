Money = 2000

def AddMoney():
    # Uncomment the following line to fix the code:
    global Money
    Money = 0
    Money = Money + 1

print (Money)
AddMoney()
print (Money)



# 'nonlocal' keyword is only in Python 3
def outer():
    x = 1
    def inner():
        #nonlocal x
        x = 2
        y = x
        print("inner:", x, y)
    inner()
    print("outer:", x)

outer()