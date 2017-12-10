def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    print (vartuple)
    for var in vartuple:
        print (var)
    return;

#printinfo( 10 );
printinfo( 70, 60 , "a", 'b', "d");

