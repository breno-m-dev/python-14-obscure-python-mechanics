#any() checks if there is a Truthy value on the collection

def check(value):
    print(value, end=" ")
    return value


result = any([
    check(False),
    check(True),
    check(False)
]) # -> False True False
# this shows python needs to evaluate all values before doing the check
# with the Any value
# It is known that Any stops after finding the first truthy value
# but it is told that with generators it is different!!

print("->", result) # -> True

# List argument: the list elements are evaluated before any() starts.

# Generator expression: values are evaluated as any() requests them,
# allowing short-circuiting to prevent later evaluations.