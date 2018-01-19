t = ()
print (t)

print (tuple())

zoo = ('wolf', 'elephant', 'penguin')
print ('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'dolphin', zoo)
print ('Number of animals in the new zoo is', len(new_zoo))
print ('All animals in new zoo are', new_zoo)
print ('Animals brought from old zoo are', new_zoo[2])
print ('Last animal brought from old zoo is', new_zoo[2][2])

tup1 = "a", "b", "c", "d"
print (tup1)

age = 22; name = 'pipo'
print ('%s is %d years old' % (name, age))
print ('Why is %s playing with that python?' % name)

singleton = 'hello',    # <-- note trailing comma

print (len(singleton))  # 1
print (singleton)       #('hello',)

list1 = ["x", 1, "y", 2]
list1[0] = "a"
list1[2] = "b"
print (list1)

tupfromlist = tuple(list1)
print (tupfromlist)
#tupfromlist[0] = "x"
#tupfromlist[2] = "y"


list3 = ['a' ,'b', 'c']
list4 = ['c' ,'d', 'e']
tup12 = list3, list4
print (tup12[0])
print (tup12[1])












