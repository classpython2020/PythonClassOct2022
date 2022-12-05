#else

#it will caught anything which is'nt cought by the preceding conditions

#Example:

a=55
b=77

if a>b:
    print("a is grater than b")
elif a>=b:
    print("a is grater than b")
else:
    print("b is grater than a")

#short hand else

#if we have any one condition to exucute, one for if and one for else, then we can put them on same line.

#Example

a=23
b=77
print("a is grater than b") if a>b else print("b is grater than a")

#we can write multipul statments in single line as well for that we need to use {}

a=15
{print("this is"),print("even number")} if a%2==0 else {print('i am '),print("odd number")}



