print ("Separate except clauses")
for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "-->",)
        print (float(value))
    except(TypeError):
        print ("TypeError : Only a string or a number can be converted!")
    except(ValueError):
        print ("ValueError : Only a string of digits can be converted!")
       
print ("Combined except clauses")
for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "-->",)
        print (float(value))
    except(TypeError, ValueError):
        print ("Something went wrong!") 