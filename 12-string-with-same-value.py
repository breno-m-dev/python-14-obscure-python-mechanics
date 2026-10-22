a = "python"
b = "py" + "thon"
c = "".join(["py", "thon"])

print(a == b)  # True
print(a is b)  # normalmente True no CPython
print(a == c)  # True
print(a is c)  # normalmente False