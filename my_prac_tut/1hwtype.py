from myhdl import intbv
from myhdl import bin
#intbv class

# provides support for indexing and slicing
# mutable type.. value can be changed after object creation

# unconstrained intbv
a = intbv(24)
print a.min
print a.max
print len(a)

# constrained intbv
a = intbv(24, min = 0, max = 25)
print a.min
print a.max
print len(a)

# the bound values allow fine grained control and error checking
# of the value range

# common requirement in the hardware design is access to the individual 
# bits

# bit indexing
print a
print bin(a)
for i in a:
	print int(i) # need to typecast as it prints bool

print a[0]
print int(a)
print type(a)
print "///////////////// b = intbv(-10) ////////////"
b = intbv(31)
print int(b)
print bin(b)
print bin(b[20:]) 
print "b is 31 = 11111"
print "b[4:]" + bin(b[4:])
print "b[4:0]" + bin(b[4:0])
print "b[4:1]" + bin(b[4:1])
print "b[4:2]" + bin(b[4:2])
print "b[4:3]" + bin(b[4:3])
print "b[2:0]" + bin(b[2:0])

# remember .. when an intbv object is sliced.. a new intbv object is return
# this new intbv object is always positive. 
# slicing returns a positive object
