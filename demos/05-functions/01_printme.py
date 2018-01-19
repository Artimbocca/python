def printme( s ):
    "This prints a passed parameter into this function"
    print (s)
    return 

printme("I'm first call to user defined function!");
printme("Again second call to the same function");
printme(100)
printme()  # gives an error, printme takes exactly 1 argument, 0 given