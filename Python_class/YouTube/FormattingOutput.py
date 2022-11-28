#Formatting output

#1. we can print the output in diffrent ways.
#2. we can print the output in single line or multipule lines as well.

#Approch 1

# we can write like the variable like in multilines.
name="Raja"
age=27
salary=35000.50

print(name)
print(age)
print(salary)

#Approch 2
#we can write the output in single line also.
name,age,salary="Raja",27,35000.50
print(name,age,salary)

#Approch 3
# we can write the data along with some other meaningful information.

name="Raja"
age=27
salary=35000.50

print("my name is:",name)
print("My age is:",age)
print("My salary is:",salary)

#approch 4
#let's see how we can write in single line also.

name="Raja"
age=27
salary=35000.50
print("my name is:",name,"my age is:",age,"my salary is:",salary)

#approch 5
#let's see we can write in diffrent way by using %.
#We have to give the variables in order or else the data will be mismatch.

name="Raja"
age=27
salary=35000.50

print("my name is:%s my age is:%d my salary is:%g" %(name,age,salary))

#Approch 6
# Let's see how we can write with format method by usig {}.
#We have to give the variables in order or else the data will be mismatch.


name="Raja"
age=27
salary=35000.50

print("my name is:{} my age is:{} my salary is:{}".format(name,age,salary))

#Approch 7
# If we can'nt give the data in order then we have to use this method

nam="Raja"
age=27
salary=35000.50
print("My name is {name} yanamala, i am {name1} old \nand i work at home and get {name2} of salary".format(name=nam,name1=age,name2=salary ))
  #let's see if we want to change the data how to use
print("My name is {name1} yanamala, i am {name} old \nand i work at home and get {name2} of salary".format(name=nam,name1=age,name2=salary ))
  # we just need to change the keys  in {}

