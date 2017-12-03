# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:24:56 2017

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
        table[k] = start.append(v)
add("x", 2)
add("y", 5)
add("x", 5)
add("z",3,[2])
add("z",4)
print("Last added to table {}: {}", table, last_added)


