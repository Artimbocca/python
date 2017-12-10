def changeme1( mylist ):
    "This changes a passed list into this function"
    mylist.append([1,2,3,4])
    print ("Values inside the function changeme1: ", mylist)
    return

mylistouter = [10,20,30]
changeme1( mylistouter )
print ("Values outside the function: ", mylistouter)

mylistouter = [10,20,30]
changeme1( mylistouter )
print ("Values outside the function: ", mylistouter)

def changeme2( mylist ):
    "This changes a passed list into this function"
    mylist = [1,2,3,4]; # This would assign new reference
    print ("Values inside the function changeme2: ", mylist)
    return
mylistouter = [10,20,30]
changeme2( mylistouter )
print ("Values outside the function: ", mylistouter)

def changeme3( mystr ):
    mystr = "data inside"
    print ("Values inside the function changeme3: ", mystr)
    return

mystrouter = "data outside"
changeme3( mystrouter )
print ("Values outside the function: ", mystrouter)
