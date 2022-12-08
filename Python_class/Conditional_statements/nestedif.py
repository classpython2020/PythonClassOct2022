#nested if

#we can have if statement inside if statement, this is called nestedif.

a=55
b=99
if a>b:
    print("a grater than b")
    if b>a:
        print("b grater than a")
else:
    print("both are equal")