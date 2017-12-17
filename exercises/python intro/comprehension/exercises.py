# 1:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write a list comprehension that takes this list and makes a new list with only the even elements in this list.


# 2: Find all x where   x is a natural number less than or equal to 100 and x is a perfect square.
# This can be solved using a for-loop as:

for i in range(1,101):         # the iterator
    if int(i**0.5) == i**0.5:  # conditional filtering
        print(i)               # output-expression

# Create a list comprehension doing the same


# 3: Matrix Flattening
# Take a 2-D matrix as input and return a list with each row placed on after the other.
# The Python code with a FOR-loop could look as follows:


def flatten(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat


# Create a matrix (using list comprehension!) and test flatten.
# Create a list comprehension version that achieves the same result.
# Other options to pursue:
# •	Extend to n-dimensional matrices
# •	Or to trees


# 4: Dictionary Comprehension
# Take two lists of the same length as input and return a dictionary
# with the first list as keys and the second as values.
# The Python code with a FOR-loop could look like this:

    def makedict(keys, values):
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = values[i]
        return dic

# Create a solution using dictionary comprehension, using e.g.:
# country = ['Germany', 'France', 'Belgium', 'England', 'Spain', 'Italy']
# capital = ['Berlin', 'Paris', 'Brussels', 'London', 'Madrid', 'Rome']
# Hint: look at the zip generator.
# Dictionary comprehension is just one way to achieve this.
# Look up the dict type and see what other (built-in) options there are.


#5

import random
from string import ascii_lowercase
# use these imports to create a dictionary with 10 random characters as key
# and their frequency (a random number) as their value
# sort these by decreasing frequency and return
# check that the dict.values(), dict.items() etc. return views on a single dict