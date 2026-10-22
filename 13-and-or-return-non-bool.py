# TRUTHY AND FALSY VALUES

# Falsy values:
# False, None, numeric zeros (0, 0.0, 0j),
# and empty collections/strings ([], (), {}, set(), "").
#
# Most other values are Truthy, including negative numbers,
# non-empty strings, and non-empty collections.
#
# NON empty collections filled with falsy values, are still considered
# Truthy.
#
# Use bool(value) to check a value's truthiness.


# OR AND AND OPERATORS

# OR returns the first Truthy value, or the last value
# if all operands are Falsy.

x = "" or "Python" or None or True
y = [None, False] or "Hello" or 42 or True or False 
# [None, false] Is truthy, since its a non empty Collection!
w = True or 42 or True or 1
z = None or 0 or []

print("OR:")
print(x)  # Python
print(y)  # 1
print(w)  # Hello
print(z)  # []


# AND returns the first Falsy value, or the last value
# if all operands are Truthy.

a = 56 and "Hello" and 42
b = 56 and 0 and "Python"
c = "Hello" and None and 42
print("********************")
print("AND:")
print(a)  # 42
print(b)  # 0
print(c)  # None


# TRUTHINESS TESTS
print("********************")
print("TRUTHINESS:")

print(f"0 -> {bool(0)}")              # 0 -> False
print(f"None -> {bool(None)}")        # None -> False
print(f'"" -> {bool("")}')            # "" -> False
print(f"[] -> {bool([])}")            # [] -> False
print(f'"0" -> {bool("0")}')         # "0" -> True
print(f'"False" -> {bool("False")}')  # "False" -> True
print(f"[0] -> {bool([0])}")          # [0] -> True
print(f"-1 -> {bool(-1)}")            # -1 -> True