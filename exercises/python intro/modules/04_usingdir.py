import sys # get list of attributes, in this case, for the sys module

print("dir for sys")
print(dir(sys))
a = 1
print("dir for current module")
print(dir())

import math
content = dir(math)
print(content)