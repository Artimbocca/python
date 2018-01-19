try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

#class SizeError(Exception):
#    pass
#    
#def test_exception(size):
#     try:
#        if size <= 0:
#           raise SizeError, 'size must be greater than zero'
#           # Produce a different error to show that it will not be caught.
#        #x = y
#     except SizeError, exp:
#        print '%s' % (exp, )
#        print 'goodbye'
#    
#def test():
#    test_exception(-1)
#    print '-' * 40
#    test_exception(1)
#    
#test()

