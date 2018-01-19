import sys
import sys as s
 
print('The command line arguments are:')
for i in sys.argv:
    print(i)
 
print('\n\nThe PYTHONPATH is', sys.path, '\n')

print('The command line arguments are:')
for i in s.argv:
    print(i)
 
print('\n\nThe PYTHONPATH is', s.path, '\n')