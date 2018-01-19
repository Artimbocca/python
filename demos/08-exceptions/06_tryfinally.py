import traceback

def ExceptionDoNotCatch():
    try:
        print ("In ExceptionDoNotCatch")
        i = 10
        j = 0
        z = i/j
        print (z)
    finally:
        print ("Finally executed in ExceptionDoNotCatch")
    print ("Will never reach this point")

print ("\nCalling ExceptionDoNotCatch")

try:
    ExceptionDoNotCatch()
except Exception as e:
    print ("Caught exception from ExceptionDoNotCatch in main program.")
    print (e.args)
    traceback.print_exc()