i = 2+2
print (i)

i = (50-5*6)/4
print (i)

i =  8/5 # Fractions aren't lost when dividing integers
print (i)

i = 7//3 # Discarding any fractional result 
print (i)

z = 1j * 1J
print (z) # (-1+0j)

z = 1j * complex(0, 1)
print (z)  # (-1+0j)

z = 3+1j*3
print (z)  # (3+3j)

z = (3+1j)*3
print (z) # (9+3j)


print (z.real)
print (z.imag)