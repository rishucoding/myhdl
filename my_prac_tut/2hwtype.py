from myhdl import intbv
from myhdl import modbv
from myhdl import bin
# hardware modelling requires elegant modelling of wrap - around behavior
# 2**8  = 256 .. ** is exponential operator	
# to support operations like: 
# shifter <<= 4
# count_var +=1
# intbv and modbv have identical interface, but they handle the bounds differently
# out of bound values result in an error with intbv, and 
# in wrap-around with modbv
# wrap around behavior is : 
# val = (val - min) % (max - min) + min
a  = intbv(12,min = 0, max = 2**4)
#a = intbv(12)
print bin(a) # bin function behaves differently if you dont' 
# import bin from myhdl. The default bin will print 0b1100
# while after importing this will print 1100

b = a.signed() # now the msb bit acts as sign bit
# which changes 1100 = 12 to 1100 = -4
print type(b)
print int(b)
print bin(b)

print bin(b, width = 5) # we can use this parameter to 
# adjust the total number of bits. 


# let's take a 8bit  wide data bus
data_bus = intbv(0)[8:]
'''
have to resolve the erroor: 
NameError: name 'real' is not defined
'''
real.next = data_bus[8:4].signed()
imag.next = data_bus[4:0].signed()


