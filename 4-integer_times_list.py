a = 3 * [1, 3]
# print(3.2*[1,2]) # <- TypeError: can't multiply sequence by non-int of
# type 'float'

print(a) # <- [1, 3, 1, 3, 1, 3]
print(f"id(a[0]):{id(a[0])}")
print(f"id(a[1]):{id(a[1])}")
print(f"id(a[2]):{id(a[2])}") ## <- same id as a[0]
print(f"id(a[3]):{id(a[3])}") ## <- same id as a[1]

# this shows multipling a list, increase its size if
# a reference to the original list, not a copy!!
a[1] = 2 #this rebounds a[1] but the original a[1] stillexists on a[3]
print(a) # <- [1, 2, 1, 3, 1, 3]
print("----------------")

b = [[]] * 3
b[0].append(7) ## mutates object, doesnt rebound, since all list
## positiosn reference the same object, it changes them all
print(b) ## <- [[7], [7], [7]] 

