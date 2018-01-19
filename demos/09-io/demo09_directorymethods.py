import os

print (os.getcwd())
os.mkdir("justtesting")
os.chdir("justtesting")
print (os.getcwd())
os.chdir("..\\")
print (os.getcwd())
os.rmdir("justtesting")
