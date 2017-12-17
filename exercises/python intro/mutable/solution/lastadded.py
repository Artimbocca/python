# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:26:43 2017

@author: Jos
"""


table = {}
last_added = ()
def add(k, v, start=[]):
    last_added = (k,v)
    print("Adding: ", last_added)
    if k in table:
        table[k].append(v)
    else:
        # table[k] = start.append(v)
        # the append method returns None, so we can not use its value if we want to assign the list to a key
        # we should do this in two steps 
        start.append(v)
        table[k] = start
add("x", 2)
add("y", 5)
add("x", 5)
add("z",3,[2])
add("z",4)
# the format method was not called
print("Last added to table {}: {}".format(table, last_added))

# The above version returns:
#    Last added to table {'x': [2, 5, 5], 'y': [2, 5, 5], 'z': [2, 3, 4]}: ()
# By using a mutable value as a default, we have made x and y point to the same object
# print(id(table['x']) == id(table['y']))
# default values are evaluated at definition time, i.e. only once !!!
# one way to resolve this is by replacing
#        start.append(v)
#        table[k] = start 
# with:
#       table[k] = start + [v]
# or use None as default and do: table[k] = start + [v] if start else [v]
# Finally: updating last_added inside the add function has no effect on the global last_added; 
# return that tuple and use last_added = add(....) or use list as global, thereby allowing add to directly (re)set its items
