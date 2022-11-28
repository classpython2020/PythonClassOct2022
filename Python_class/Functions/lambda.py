#1.lambda functions are nothing but, the fuctions which are defined without a name
#2.lambda function also called as anonymous functions
#we will define a function by giving def before of it, but in lambda we don't use def

#lambda syntex

#lambda arguments:exprestion

#multipling  the elements by using lambda fuction.

multi= lambda a,b,c,d,e,f:[a*a,b*b,c*c,d*d,e*e,f*f]
print(multi(1,2,3,4,5,6))




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

#All function

#1. if given values all are true then it will return output as true.
#2. if even one value is false then it will be flase.
#3. if all()  is empty then it will reture True.

#Syntex

#all(ittarable)

list=[2,4,6,8,10]
print(all([i%2==0 for i in list]))

list=[2,4,7,8,10]   #even one value is false, the out[ut will be false
print(all([i%2==0 for i in list]))


#any function

#1. If given value any one of value is true then output will be true or else false.
#2. if any() funtion is empty then it will be false.

#Syntax
#any(iterable)

list=[1,3,7,9,10]      #only one value is true even than the output is true.
print(any([i%2==0 for i in list]))

list=[1,3,7,9,1]      #all the values are false then the output will be false
print(any([i%2==0 for i in list]))



#bin function

#1. it will return binary of an integer.
#2. the count will start after the 0b

#syntex
#bin(n)

x=bin(160)
print(x)

#bool function

#1. bool will return output as True or False
#2. bool function always returns true unless;
  # the object is empty. like () {} []
  # the object is False
  # the abject is 0
  # the object is None

#Syntex

#bool(object)

x= bool(1)
print(x)

# the object is empty. like () {} []

print(bool(()))
print(bool([]))
print(bool({}))
print(bool())

# the object is False

print(bool(False))

# the abject is 0

print(bool(0))

# the object is None

print(bool(None))

#callable() Function

#1. it will check if we can callable the function or not.
#2. if we can callalbe that function it will be true.
#3. if we can not callalbe that function it will be False.

#syntex
callable(object)

#if we can callalbe that function it will be true.

def function():
    x=5
    print(x)

print(callable(function))  #output is true

#if we can not callalbe that function it will be False.

x=5
print(x)

print(callable(x))  #output id False

#chr() Function

#1. it will return the spicified character in unicode

#Syntex
#chr(number)

print(chr(97))
print(chr(98))
print(chr(99))
print(chr(100))