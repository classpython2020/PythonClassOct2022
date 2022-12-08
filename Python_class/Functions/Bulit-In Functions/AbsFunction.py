
#Abs function

#1.Abs function will be used for absolute value for a number.
#2.If number in nagitive also it will convert into positive value.

#Syntex
#abs(x)

a=abs(15)
print(a)

a=abs(-15)    #it will convert into positive value.
print(a)


list=[1,2,3,-1,-2,-3]    #it will convert all the nagitive numbers to positive numbers.
mylist=[abs(i) for i in list]
print(mylist)
