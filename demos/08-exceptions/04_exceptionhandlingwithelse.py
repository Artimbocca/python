while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops! That was not valid number")
    else:
        print ("Yeah! That was a really good number")