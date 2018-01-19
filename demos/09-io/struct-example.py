import struct

nr1 = 1
# native byteorder
buffer = struct.pack("i", nr1)
#print (repr(buffer))
print (struct.unpack("i", buffer))

# data from a sequence, network byteorder
#data = [1, 2, 3]
#
#buffer = struct.pack("!ihb", *data)
#
## in Python 1.5.2 and earlier, use this instead:
## buffer = apply(struct.pack, ("!ihb",) + tuple(data))
#
#print (repr(buffer))
#print (struct.unpack("!ihb", buffer))
