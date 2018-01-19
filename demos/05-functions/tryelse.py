def print_object(some_object):
    # Check if the object is printable...
    try:
        printable = str(some_object)
        print(printable)
    except TypeError:
        print("unprintable object")


def print_object(some_object):
    # Check if the object is printable...
    try:
        printable = str(some_object)
    except TypeError:
        print("unprintable object")
    else:
        print(printable)
