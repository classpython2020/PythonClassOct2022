# Id function

#1. by using the if function we can know the memory loction where we have stored the variable in python,
# we will get the id of it.
#2. If variable memory loction changes it called immutable data type.
#3. if variable memory loction is not changed it is called mutable data type.
#4. We can find out that which data type is a mutable and which is not by using the ID function.

#how to use Id function

str="raja"
print(id(str))  #2030290158704 we will get the id of that loction like this.

#2. If variable memory loction changes it called immutable data type.

str=str+"Raja" #concertination will happen here
print(id(str))   #2030290078128  id has changed becuase string is a immutable data type.

#3. if variable memory loction is not changed it is called mutable data type.

list=[1,2,3,45]
print(id(list))  #2030290231808
list.append(5)
print(id(list))  #2030292866944 after adding value also list Id did not change because list is mutable data type.


