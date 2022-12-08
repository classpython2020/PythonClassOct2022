# 1.Take 10 integers from keyboard using loop and print their average value on the screen.


def average(list1):
    sum=0
    for i in list1:
        sum=sum+i
        sum=sum/10.0
        print("average of this",sum)


list=[272,333,122,31]
print(average(list))

# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
#
# Given 1:
#
# number1 = 20
# number2 = 30
# Expected Output:
#
# The result is 600
# Given 2:
#
# number1 = 40
# number2 = 30
# Expected Output:
#
# The result is 70
#



def discount(num1,num2):
    sum=num1*num2
    if sum>=1000:
        return ("i am algible for discount")
    else:
        return (num1+num2)


a=int(input("please enter the first number:"))
b=int(input("please enter the secound number:"))
print(discount(a,b))
