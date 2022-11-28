# for loop

#we will use for loop for iteration over a seqence.[Either a list, a set, a string, a tuple, distonary]
#for loop is not like in other programming languages, it is used for iteration in python
#with for loop we can execute a set of statements.

#basic syntex
for x in var:
    print(x)

#example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#looping through a string

#even strings are iterable and they contain a seqence of characters

#example

fruits = "banana"
for x in fruits:
  print(x)


#break statement

#with break statement we can stop the looping before it has looped through other iteams.

#example

list=[1,2,3,4,5]
for i in list:
    if i==3:
        break
    print(i)

#continue

# with continue statement we can stop looping and continue with next one

#example

list=[1,2,3,4,5]
for i in list:
    if i==3:
        continue
    print(i)

#range function

#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.

#Example

for i in range(6):
    print(i)

#using start parameters

for x in range(2, 6):
  print(x)

#using increment parameters

#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#else in for loop

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#Example
#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nested Loops
#A nested loop is a loop inside a loop.

#The "inner loop" will be executed one time for each iteration of the "outer loop":

#Example
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y, end=(' ,'))


#Example 1: Print the first 10 natural numbers using for loop.

for i in range(0,10+1):
    print(i)

#Example 2: Python program to print all the even numbers within the given range.

print("enter the number:")
number=int(input())
for i in range(1,number+1):
    if i % 2==0:
        print(i)

#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

print("enter the number:")
number=int(input())
sum=0
for i in range(1,number+1):
    sum+=i
print(sum)

#example 4:  Python program to calculate the sum of all the odd numbers within the given range.

print("Enter the number:")
number=int(input())
for i in range(0,number+1):
    if i % 2==1:
        print(i)

#Example 5: Python program to print a multiplication table of a given number

print("Enter the table number:")
table=int(input())
for i in range(10):
    print(table,"x",i,"=",table*i)


#Example 6: Python program to display numbers from a list using a for loop.

list=[1,2,3,44,5,56,6,7]
for  i in list:
    print(i)

#Example 7: Python program to count the total number of digits in a number.

print("Enter the number:")
number=int(input())
string_number=str(number)
count=0
for i in string_number:
    count=count+1
print(count)

#Example 9: Python program that accepts a word from the user and reverses it.

print("Enter the word:")
word=input()
rev_string=""
for i in word:
    rev_string=i+rev_string
print(rev_string)

#Example 8: Python program to check if the given string is a palindrome.

print("enter the value:")
str=input()
rev_string=""
for i in str:
    rev_string=i+rev_string
if str==rev_string:
    print(str,"this is palindrome")
else:
    print(str,"this is not palindrome")

#Example 10: Python program to check if a given number is an Armstrong number
print("enter the number")
given_number=int(input())
given_number=str(given_number)
string_lengh=len(given_number)
sum=0
for i in given_number:
    sum+=int(i)**string_lengh
print(sum)

#Example 11: Python program to count the number of even and odd numbers from a series of numbers.

print("Enter the number:")
number=int(input())
for i in range(0,number+1):
    if i%2==0:
        print(i,"is a even number")
    else:
        print(i,"is a odd number")


