
def show(value):
    print("hi", end=" ")
    print(value)
    return value

result = show(1) or show(2) and show(3)
print(f"{result = }") #<-1

#since in a or/and expression, or takes the first truthy value
# the line ends on the first execution of show()

print("************")
result = (show(1) or show(2)) and show(3) 
#show(2) is not executed but show(3) now is due to the parenthesis

print(f"{result = }") #<-3