d = {True: "A", 1: "B", 1.0: "C"}
print(len(d)) ## <- 1
print(d[True]) ## <- "C"
print(d) # <- {True : "C"}

# all keys have same value(True is 1!!) even though they are different
# types, so only the last element will be saved, since it overwrites the
# others. same would happen for:
d = {False: "A", 0: "B", 0.0: "C"}
print(len(d)) ## <- 1
print(d[False]) ## <- "C"

# But not for
d = {True: "A", 1: "B", "1": "C"}
print(len(d)) ## <- 2
print(d) ## <- "B"

# since its using the string of 1 on the last element, not the value 1.
# the string 1 in unicode is U+0031

# this would still create 2 values, because python will take into 
# account the difference of types, and do not consider a string as a 
# integer for the comparison.
d = {31: "B", "1": "C"}
print(len(d)) # <- 2
print(d) # <- {31: "B", "1": "C"}