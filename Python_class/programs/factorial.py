
#Python Program for factorial of a number

def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while n>1:
            fact=fact*n
            n=n-1
        return fact


num=int(input("please enter the factorial number:"))
print("factorial number of",num,'is', factorial(num))