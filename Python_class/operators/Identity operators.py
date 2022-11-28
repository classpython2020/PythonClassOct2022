#identity operators

#is
#is not


#**************************************Example************************************


#is :-Returns True if both variables are the same object
a=5
b=10
print(a is b)

a=15
b=15
print(a is b)

a=20
b=15
print(a is b)

a=20
b=20
print(a is b)

#is not :-Returns True if both variables are not the same object

a=20
b=20
print(a is not b)

a=20
b=21
print(a is not b)

a=21
b=55
print(a is not b)

a=29
b=29
print(a is not b)
