fr = open('trilobyte.jpg', mode='rb')
print (fr.mode)
print (fr.name)
#print (fr.encoding)  # => not available in binary mode

print (fr.tell())

data = fr.read(3)
print (type(data))

print (fr.tell())
fr.seek(0)
#
data = fr.read()
print (len(data))
print (data)
#
#fw = open('trilobyte2.jpg', mode='wb')
#fw.write(data)
#fw.close()