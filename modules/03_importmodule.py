import mymodule
mymodule.say_hi()
print ('Version', mymodule.__version__)

#Alternatively from .. import can be used :

from mymodule import say_hi, __version__
say_hi()
print('Version', __version__)
