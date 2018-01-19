total = 0; # This is a global variable
#Function definition :

def sum( arg1, arg2 ):
    # Add both the parameters and return them."
    total = arg1 + arg2; # Here total is local variable.
    print ("Inside the function local total : ", total)
    return total;

#Function call :

sum( 10, 20 );
print ("Outside the function global total : ", total) 

#Result :

#Inside the function local total :  30
#Outside the function global total :  0

