fo = open("textfile3.txt", "wb")
fo.write( bytes("Python is a great language.\nYeah its great!!\n", 'UTF-8'));
fo.write(bytes(10, "UTF-8"))
#fo.write(bytes(11, "UTF-8"))
#fo.write(bytes(15, "UTF-8"))
#fo.write(bytes(17, "UTF-8"))
#fo.write(bytes(18, "UTF-8"))
#fo.write(bytes(19, "UTF-8"))
fo.close()
#now reading just 5 characters
fo = open("textfile3.txt", "rb")
str = fo.read();
print ("Read String is : ")
print (str.decode("UTF-8"))
fo.close()