def test():
    infilename = 'nothing_noplace.txt'
    try:
        infile = open(infilename, 'r')
        for line in infile:
            print (line)
    except IOError as exp:
        print ('cannot open file "%s"' % infilename)

test()
