number=int(input())
for i in range(0,number):
    print(i)

#Example 2: Python program to print all the even numbers within the given range.

print("Eenter the number:")
number=int(input())
for i in range(0,number):
    if i%2==0:
        print(i, end=(',')

#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

print("enter the number")
number=int(input())
sum=0
for i in range(1,number+1):
    sum=sum+i
print(sum)


#example 4:  Python program to calculate the sum of all the odd numbers within the given range.

print("Enter the number ")
number=int(input())
for i in range(1,number):
    if i%2==1:
        print(i)

#Example 5: Python program to print a multiplication table of a given number

print("enter the table number")
number=int(input())
for i in range(10+1):
    print(number,"x",i,"=",number*1)

#Example 6: Python program to display numbers from a list using a for loop.


list=[1,2,3,4,5,6,7]
for i in list:
    print(i)

#Example 7: Python program to count the total number of digits in a number.

print("enter the number")
given_number=int(input())

given_number=str(given_number)
count=0
for i in given_number:
    count+=1
print(count)


#Example 8: Python program to check if the given string is a palindrome.

print("please enter the string")
string=str(input())
rev_string=string [: : -1]
if string== rev_string:
    print("the given value is palindome")
else:
    print("the given value is not palindome")

#Example 9: Python program that accepts a word from the user and reverses it.

given_string=input()
rev_string=""
for i in given_string:
    rev_string=i+rev_string
print(rev_string)

#Example 10: Python program to check if a given number is an Armstrong number

given_number=int(input())
given_number=str(given_number)
string_lengh=len(given_number)
sum=0
for i in given_number:
    sum+=int(i)**string_lengh
 print(sum)

#Example 11: Python program to count the number of even and odd numbers from a series of numbers.

list=[1,2,3,4,5,5,6,7,8,9]
for i in list:
    if i%2==0:
        print(i,"is a even numner")
    else:

        print(i,"is a odd number")



#example 1:Take 10 integers from keyboard using loop and print their average value on the screen.

sum=0
i=10
while i >0:
    num=int(input("please enter the number:"))
    sum=sum+num
    i=i-1
print("average is ",sum/10.0)

#example  2: Print multiplication table of 24, 50 and 29 using loop.

i=1
table=int(input("please enter the table:"))
while i<=10:
    print(table,"x",i,"=",table*i)
    i=i+1

#example  3:Write an infinite loop.
#A inifinte loop never ends. Condition is always true.

while True:
    print("i love you")


#example  4: Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
#4! = 1*2*3*4 = 24
#3! = 3*2*1 = 6
#2! = 2*1 = 2
#Also,
#1! = 1
#0! = 1
#Write a program to calculate factorial of a number.

number=int(input("please enter the number:"))
fac=2
if number==0:
    print(1)
else:
    while number>=1:
        fac=fac*number
        number=number-1
    print(fac)


dic={2:"raja","string":[1,2,3,4,5],[1,2,3]:"string"}
print(dic)

