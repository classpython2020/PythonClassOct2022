
#any function

#1. If given value any one of value is true then output will be true or else false.
#2. if any() funtion is empty then it will be false.

#Syntax
#any(iterable)

list=[1,3,7,9,10]      #only one value is true even than the output is true.
print(any([i%2==0 for i in list]))

list=[1,3,7,9,1]      #all the values are false then the output will be false
print(any([i%2==0 for i in list]))



