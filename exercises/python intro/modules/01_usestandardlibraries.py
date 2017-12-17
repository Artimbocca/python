import sys
import sys as s
from sys import argv

 
print('The command line arguments are: {}'.format(argv))
for i in sys.argv:
    print(i)
 
print('\nThe PYTHONPATH is', s.path)

import test as t
t.print_func("Joop")