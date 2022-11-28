
#set is a mutable
#set should has immutable values (list,set,dictionary)
#set is a unordering collection
#set does  not allow indexing
#set does not allow duplicate values
#set allows hetrogenous elements
#set allow for loop
#set allow membership operators


#Creating a empty set with set fuction

set1=set()
print(set1)

  #we can create set with values

set1=set({1,2,3,4,5})
print(set1)

  #let's see how we can write set directly

set1={1,2,33,4}
print(set1)

#set should has immutable values
#set values can be only immutables like strings,tuple,numbers,floats
# in set we can not use list,set,dictionary

set={'python',1,2,3,(1,2,3,4),2.22}
print(set)

#set does not allow duplicate values
# we can not have duplicates in set

set={1,2,3,4,5,2,3,4}
print(set)
  #output will be {1, 2, 3, 4, 5} because it wont allow duplicates

#set allows hetrogenous elements
#hetrogenous elements means mixed data types we can use

set={'python',1,2,3,(1,2,3,4),2.22}   #we can only use immutable values here, if we use mutable values wee will get error
print(set)

#set allow for loop

set={1,2,3,4,5}
for i  in set:
    print(i)

#type casting:- By using type casting we can convert one data type to another data type
 #for example we can convert list to tuple and tuple to set like that

set={1,2,3,4,5}
print(list(set))  #output will be in list like this [1, 2, 3, 4, 5]

 #like this we can convert from one data type to another data type
 #we can know the type of that data type by using type function
set1=set()
print(type(set1))






