import os

fo = open("datafile1.txt", "w")
fo.close()
os.rename( "datafile1.txt", "renamedfile.txt" )
os.remove("renamedfile.txt")