#methods in list
#append
#extend
#insert
#count
#pop
#remove
#sort
#copy
#clear
#index

#append--- it can add the number or string at the last of the list

# Syntax
# list.append(elmnt)

list1=[1,2,444,443,3,2,45,3]
list1.append(32)
print(list1)

#extend--- it can be add any ittarable data types at the end of the current list

#Syntax
#list.extend(iterable)

list1=[1,2,444,443,3,2,45,3]
list1.extend(('raja','rajesh'))
print(list1)

#insert---- it can adds an element at the specified position.

# Syntax
# list.insert(pos, elmnt)


list1=[1,2,444,443,3,2,45,3]
list1.insert(7,9000)
print(list1)

#count-- it can count the value how many times are there in list

# Syntax
# list.count(value)


list1=[1,2,444,443,3,2,45,3]
result=list1.count(3)
print(result)

#pop--- it will delete the value baised on index count.

# Syntax
# list.pop(pos)

list1=[1,2,444,443,3,2,45,3]
list1.pop(2)
print(list1)

#remove---it will delete the specipic value in the list.

# Syntax
# list.remove(elmnt)

list1=[1,2,444,443,3,2,45,3]
list1.remove(444)
print(list1)

#sort--- it will sort the value in the list from top to bottom and bottom to top.

# Syntax
# list.sort(reverse=True|False, key=myFunc)

list1=[1,2,444,443,3,2,45,3]
list1.sort()
print(list1)

list1=[1,2,444,443,3,2,45,3]
list1.sort(reverse=False)  # by defualt reverse=false will be there
print(list1)

list1=[1,2,444,443,3,2,45,3]
list1.sort(reverse=True)  #if we need to get descending order we need to give true
print(list1)

#copy--- it will copy

# Syntax
# list.copy()

list1=[1,2,444,443,3,2,45,3]
list2=list1.copy()
print(list1)
print(list2)

#clear--- it will clear everything in the list.

# Syntax
# list.clear()

list1=[1,2,444,443,3,2,45,3]
list1.clear()
print(list1)

#index:-Returns the index of the first element with the specified value.

# Syntax
# list.index(elmnt)

list1=[1,2,444,443,3,2,45,3]
result=list1.index(444)
print(result)

list1=[1,2,444,443,3,2,45,3]
result=list1.index(3,3,7)
print(result)
