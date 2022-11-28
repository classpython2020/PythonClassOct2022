#Local Variable

#1. we will use local variable inside of the function
#2. After mention that we can modify that


#1. we will use local variable inside of the function.


x=15   #globle variable
def my_function():
    y=10    #Local variable
    y=y+2
    print(y)

print(my_function())

# To use globle variable with local variable we have to mention globle variable inside of the function.


x=15   #globle variable
def my_function():
    global x
    y=10    #Local variable
    y=y+2+x #globle variable with local variable
    print(y)

print(my_function())