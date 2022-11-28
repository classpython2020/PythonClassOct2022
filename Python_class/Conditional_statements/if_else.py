#if and else

var="orange"
if var=="apple":
    print("i am orange")
else:
    print("i not orange")

#if and else and nestedif

marks=57
if marks==90:
    print("i am passes with A grade")
elif marks<=89 and marks>=80:
    print("i am passed with B grade")
elif marks<=79 and marks>=60:
    print("i am passed with C grade")
elif marks<=59 and marks>=35:
    print("i am passed")
else:
    print("i am failed")


#example----1

#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.


print("enter salary")
salary=int(input())
print(salary)
print("years of salary")
yos=int(input())
if yos>=5:
    print("you are allgiable for 5* of bonus" )
else:
    print("you are not allgiable for bonus")


#example----2

#Take values of length and breadth of a rectangle from user and check if it is square or not.

print("enter the lenth")
lenth=int(input())
print("enter the breadth")
breadth=int(input())
if lenth==breadth:
    print("yes, it is a square")
else:
    print("no it is not a square")



#example----3

#Take two int values from user and print greatest among them.

print("enter A value")
a=int(input())
print("enter B value")
b=int(input())
if a>b:
    print("the greatest numner is:",a)
else:
    print("the greatest numner is:",b)

#example----4

#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#suppose, one unit will cost 100.
#Judge and print total cost for user.


print("quantity of perchase")
quantity=int(input())
print("price of one quantity")
price=int(input())
price=quantity*price
print("cost of purchased")
cost=price
print(cost)
if cost>1000:
    print("congrats, you are alligiable for 10% discount ")
else:
    print("sorry, you are not alligiable for 10% discount")


#example----5

#A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.

print("Enter the marks")
marks=int(input())
if marks<=25:
    print("You have got F grade")
elif marks<=25 and marks<=45:
    print("You have got E grade")
elif marks<=45 and marks<=50:
    print("You have got D grade")
elif marks<=50 and marks<=60:
    print("You have got C grade")
elif marks<=60 and marks<=80:
    print("You have got B grade")
else:
    print("you have passes with A grade")


#example---6

#Take input of age of 3 people by user and determine oldest and youngest among them.

print("first person age")
first_person=int(input())
print("second person age")
second_person=int(input())
print("third person age")
third_person=int(input())

if first_person>second_person and first_person>third_person:
    print(first_person,"is oldest person")
elif second_person>first_person and second_person>third_person:
    print(second_person, "is oldest person")
elif third_person>first_person and third_person>second_person:
    print(third_person, "is oldest person")
else:
    print("all are equal")

#example----7

#Write a program to print absolute vlaue of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1

print("Enter the number")
number=int(input())
if number<0:
    print(number*-1)  #how - is covecting into +
else:
    print(number)


#example---8

#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.


print("number of classes held")
noh=int(input())
print("number od classes attanded")
noa=int(input())
percentage=(noh/100 and (noa/100))*100
print("percentage is:",percentage)
if percentage>75:
    print("this student is allowed to sit in exam")
else:
    print("this student is not allowed to sit in exam")

#example---9

#Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.


print("number of classes held")
noh=int(input())
print("number od classes attanded")
noa=int(input())
percentage=(noh/100 and (noa/100))*100
print("percentage is:",percentage)
print("he/she has medical cause")
medical=input()
a="yes"
if medical=="yes":
    print("this student is allowed to sit in exam")
else:
    if percentage>75:
        print("this student is allowed to sit in exam")
    else:
        print("this student is not allowed to sit in exam")


#example---10
#Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then
# it must be divisible by 400.

print("enter the year:")
year=int(input())
if year%4==0:
    print("true")
elif year%100==0:
    print("false")
elif year%400==0:
    print("true")
else:
    print("false")

#example---11
#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"

print("please enter age:")
age=int(input())
print("please enter sex:")
sex=input()
a="female"
b="male"
print("enter marital status:")
marital_status=input()
if sex==a:
    print("she will work only in urban areas")
elif sex==b and age>=20 and age<=40:
    print("he may work in anywhere")
elif sex==b and age>=40 and age<=60:
    print("he will work in urban areas only")
else:
    print("Error")


