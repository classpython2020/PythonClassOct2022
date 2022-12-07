#1.string is an immutable data type.
#2.string has order collection.
#3.string supports index.
#4.string supports itterating.
#5.string allows hetrogenous elements.
#6.string can allow duplicates.
#7. string can be used in loops.



#how to create a empty string
  #there are four ways to create a string by using quotes

string=''
print(type(string))


string=""
print(type(string))

string=''' '''
print(type(string))

string=""" """
print(type(string))

#'',"",''',""" """ quotes use
# how to use string dirctly.

list='this is raja yanamala'
print(list)

list="this is raja yanamala"
print(list)

list='''this is raja yanamala'''
print(list)

list="""this is raja yanamala"""
print(list)

#how to use '''
list='''this is 
raja yanamala'''  #we use the triple quotes to write the sentance in the next line
print(list)

#we can use \n also to make different lines in string

list='''this is \nraja yanamala'''
print(list)

#how to use quotes in strings

list='this is "raja" yanamala'
print(list)

list="this is 'raja' yanamala"
print(list)

list='''this is raja "yana'mala"'''
print(list)

#slice

list="this is raja yanamala"
result=list[0:16]
print(result)

# if and else

list="this is raja yanamala"
if "suresh" in list:
    print("true")
else:
    print("false")

#for loop

list="this is raja yanamala"
for x in list:
    print(x,end="")

#comparation operators

list1="this is raja yanamala"
list2="this is raja yanamala"
print(list1==list2)

list1="this is  yanamala"
list2="this is raja yanamala"
print(list1==list2)


#!=
list1="this is raja yanamala"
list2="this is raja yanamala"
print(list1!=list2)

list1="this is  yanamala"
list2="this is raja yanamala"
print(list1!=list2)

#<
list1="this is raja yanamala"
list2="this is  yanamala"
print(list1<list2)

list1="this is  yanamala"
list2="this is raja yanamala"
print(list1<list2)

#>
list1="this is raja yanamala"
list2="this is  yanamala"
print(list1>list2)

list1="this is  yanamala"
list2="this is raja yanamala"
print(list1>list2)

#<=
list1="this is raja yanamala"
list2="this is  yanamala"
print(list1<=list2)

list1="this is  yanamala"
list2="this is raja yanamala"
print(list1<=list2)

#>=
list1="this is raja yanamala"
list2="this is  yanamala"
print(list1>=list2)

list1="this is  yanamala"
list2="this is raja yanamala"
print(list1>=list2)


















