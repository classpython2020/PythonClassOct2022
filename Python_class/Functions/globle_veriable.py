#Globle veriable

#1. it will be outside of the function
#2. it can be usuful for all functions in entair module
#3. we can not modify the globle variable but if we want to modify then we need to mention
#    the globle veriable indside function




#1. it will be outside of the function.

x=10  # this is globle variable.
def my_veriable():
    return

#2. it can be usuful for all functions in entair module

x=10
def my_function1():
    print(x)

print(my_function1())

def my_function2():
    print(x)

print(my_function2())


#3. we can not modify the globle variable but if we want to modify then we need to mention
#    the globle veriable indside function

def my_function3():
    x=x+1     # we can not modify the globle variable with out mention inside of the function
    print(x)

def my_function4():
    global x   # we have to mention the globle variable like this
    x=x+1
    print(x)

my_function4()