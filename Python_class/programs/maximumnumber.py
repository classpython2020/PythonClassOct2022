#Maximum of two numbers in Python

#Given two numbers, write a Python code to find the Maximum of these two numbers.

def maximum(a,b):
    if a>b:
        return a
    else:
        b>a
        return b


max1=int(input("please enter the number"))
max2=int(input("please enter the number:"))
print(maximum(max1,max2))



#another way to write program
def maximum1(a,b):
    result=max(a,b)
    return result


max1=int(input("please enter the number"))
max2=int(input("please enter the number:"))
print(maximum1(max1,max2))

#by using lambdha function

def maximum2(a,b):
    result=(a if a>b else b)
    return result


max1=int(input("please enter the number"))
max2=int(input("please enter the number:"))
print(maximum1(max1,max2))




