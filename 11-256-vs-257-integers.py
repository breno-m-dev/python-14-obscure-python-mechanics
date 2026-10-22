a = 256
b = 256
print( a is b) # <- true

c = 257
d = 257
print (c is d) # <- COULd be false or true

# usually in python integers from -5  up to 256 will usually be cached
# so to save memory they names with same values on this range will
# refence the same imutable(int) object. Values outside this range
# might not have same id. 
# 
# If you run this directly on terminal it works better
# type
# Python
# line per line of code

a = -5
b = -5
print( a is b) # <- true

c = -6
d = -6
print (c is d) # <- false