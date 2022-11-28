#input and type

#1. we can take the input from the console window by using input funcion.
#2. What even we give thought console window it will be consedier as string by defalut.
#3. To change the data type from string to anther data type we need to use that data type infront of the input.


#1. we can take the input from the console window by using input funcion.

num=input("please enter the number")  # we can add some of masssage to input.
num1=input ("please enter the number")


#2. What even we give thought console window it will be consedier as string by defalut.

num=input("please enter the number")
num1=input ("please enter the number")


   #to know the type of that value we can use type function.
print(type(num))
print(type(num1))


print(num+num1)   # here we can do concertenation becuase that value are in string

#output
# please enter the number>? 29
# please enter the number>? 29
# <class 'str'>
# <class 'str'>
# 2929

#3. To change the data type from string to anther data type we need to use that data type infront of the input.


num=int(input("please enter the number"))
num1=int(input ("please enter the number"))
              # to convert into int we need to mention the int for float we need to mention float.

  #to know the type of that value we can use type function.
print(type(num))
print(type(num1))

print(num+num1)

#output
# please enter the number>? 29
# please enter the number>? 29
# <class 'int'>
# <class 'int'>
# 58


