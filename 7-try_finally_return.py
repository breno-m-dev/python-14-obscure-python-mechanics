def fun():
    try:
        return "A"
    finally:
        return "B" ### <- returns this, gives a warning though

print(fun()) # <- B