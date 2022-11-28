#Globle Non Local Variable

#1. Non local variable will be create when we write code by using function inside of another function.
#2. By using that non local variable inside of another function we need to menion it as non local variable.



#1. Non local variable will be create when we write code by using function inside of another function.

x=15               #globle variable
def my_function():
    y=20           #Non local variable
    def my_function1():
        z=25       #Local variable
        return


#2. By using that non local variable inside of another function we need to menion it as non local variable.

x=15
def my_function2():
    global x     #globle variable
    y=20         # here y is local veriable for my_function2(), non local variable for my_function3
    y=y+x
    def my_function3():
        nonlocal y
        z=20     #local variable
        z=x+y+z
        my_function3()
        return z

print(my_function2())




def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


