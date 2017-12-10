
n = eval(input("Give an integer :"))

if n == 0:
    print ("You typed zero.\n")
elif n== 1 or n == 9 or n == 4:
    print ("n is a perfect square\n")
elif n == 2:
    print ("n is an even number\n")
elif  n== 3 or n == 5 or n == 7:
    print ("n is a prime number\n")

def zero():
    print ("You typed zero.\n")
def sqr():
    print ("n is a perfect square\n")
def even():
    print ("n is an even number\n")
def prime():
    print ("n is a prime number\n")
       
  
options = {0 : zero, 1 : sqr, 4 : sqr, 9 : sqr,
           2 : even, 3 : prime, 5 : prime, 7 : prime,
}

options[n]()


