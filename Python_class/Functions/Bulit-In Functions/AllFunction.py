
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
