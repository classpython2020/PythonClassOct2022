
#when we are writing a code we can store that enteir code in one package and we need to give a name to that code.
#then whenever we want to use that code with different inputs we can call that code by given name and modify the inputs
#let's see how this will work out

#syntex of function

#def programname():

    #we have to start with def and give a space and should give the name to that program which we write after
    #we should write the program below of the given program name,
    #or else if we write the program from starting of the line then that will not come under of that program,
    #and will not show when we call that program with name.

#let's see how we write the program under of given name

def sumoftwonumbers():
    a=20
    b=50
    c=a+b
    print(c)

    #like this we need to write the program under of give program name
    # we are giving the values here but if another person want to give inputs then we have to do in nather way
def sumoftwonumbers():
    a = 20
#sumoftwonumbers()
   #like this we can call with program name

#let's see what if another person what to give different input and how we need to modify the code

def sumoftwonumbers(a,b):
    c=a+b
   #print(c)

sumoftwonumbers(20,10)

#let's see if we want to keep some of the fixed value

def sumoftwonumbers(a,b=10):
    c=a+b
    print(c)

sumoftwonumbers(25) # in parameters we can not give the value to strating paramater but we can give to the last one

#if we give one fixed parameter and two input values it will replace the fixed value with new value

def sumoftwonumbers(a,b=10):
    c=a+b
    print(c)

sumoftwonumbers(20,20) #like this it will replace with new given value

#if we want to use the code from another page we can import the code from that page.
#for that we need to use some code

import Defining_a_function

Defining_a_function.sumoftwonumbers()

   #we can use that is another page or same page as well

#when we are running some code and we will get the output but if user ask that he want to print output
#then we have to return the output to user like this

def sumofthenumbers():
    list=[1,2,3,4,5,6]
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
    #this is the actual program but if user ask he wants to print

def sumofthenumbers(list1):
    sum=0
    for i in list1:
        sum=sum+i
    return sum

result=sumofthenumbers([1,2,3,4,5,6])
print(result)
     #like this we can return the output to user

#some times we don't know how many values user can give that time we need to use this method
#this is called *arguments

def sumofnumbers(*list):
    sum = 0
    for i in list:
        sum = sum + i
    return (sum)



result=sumofnumbers(20,24,56)
print(result)
    #like this we need to use *argument in functions

#*********************************more examples******************************************


#there are two types in functions

#1.function creation

def sumoftwonumbers():
    a=20
    b=50
    c=a+b
    print(c)

#2. function calling

#type of functions

#1.without parameters, without result value

def welcome_msg():
    print('hello welcome to online classes')
    print('welcome to classes')


welcome_msg()


#2.without parameters, with return value

def sumofnumbers():
    sum=0
    for i in range(0,11):
        sum=sum+i
    return sum

print(sumofnumbers())


#3. with parameters, without return value
def welcome_user(name,gender):
    if gender == 'M':
        print('welcome mr.',name)
    else:
        print('welcome mrs.',name)


name = input('enter the name:')
gender = input('please enter the gender(M/F):')

print(welcome_user(name,gender))

#4. with paramaters, with return type

def count_numbers(array,size,number_count):
    count=0
    for i in range(0,size):
        if array[i]==number_count:
            count=count+1
    return count

list=[1,2,2,2,2,2,1,1,1,1,1,11,1,3,3,3,33,3]
print(count_numbers(list,len(list),2))




