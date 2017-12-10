list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd to 4th
print (list * 2)      # Prints list two times

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list1 = ['physics', 'chemistry', 1997, 2000]

print ("Value available at index 2 : ")
print (list1[2])
list1[2] = 2001
print ("New value available at index 2 : ")
print (list1[2])

list1 = ['physics', 'chemistry', 1997, 2000]
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)

list1.remove('physics')
print (list1)

list3 = []
print (list3)

multilist = [['a', 'b', 'c'], [1, 2, 3, 4]]

# first dimension
print (multilist[0][0])
print (multilist[0][1])
print (multilist[0][2])

# second dimension
print (multilist[1][0])
print (multilist[1][1])
print (multilist[1][2])
print (multilist[1][3])

# print (multilist[1][4]) # IndexError: list index out of range

del multilist[0][2]
print (multilist)
multilist.remove(['a', 'b'])
print (multilist)