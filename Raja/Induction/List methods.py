#methods in list

#append--- it can add the number or string at the last of the list
list1=[1,2,444,443,3,2,45,3]
list1.append(32)
print(list1)

#extend--- it can add the number or string at the starting of the list
list1=[1,2,444,443,3,2,45,3]
list1.extend([32,43])
print(list1)

#insert---- it can add the number or string at the specipic index  of the list
list1=[1,2,444,443,3,2,45,3]
list1.insert(7,9000)
print(list1)

#count-- it can count the value how many times are there in list
list1=[1,2,444,443,3,2,45,3]
result=list1.count(3)
print(result)

#pop--- it will delete the value baised on index count
list1=[1,2,444,443,3,2,45,3]
list1.pop(2)
print(list1)

#remove---it will delete the specipic value in the list
list1=[1,2,444,443,3,2,45,3]
list1.remove(444)
print(list1)

#sort--- it will sort the value in the list from top to bottom and bottom to top
list1=[1,2,444,443,3,2,45,3]
list1.sort()
print(list1)

list1=[1,2,444,443,3,2,45,3]
list1.sort(reverse=False)
print(list1)

list1=[1,2,444,443,3,2,45,3]
list1.sort(reverse=True)
print(list1)

#copy--- it will copy
list1=[1,2,444,443,3,2,45,3]
list2=list1.copy()
print(list1)
print(list2)

#clear--- it will clear everything in the list
list1=[1,2,444,443,3,2,45,3]
list1.clear()
print(list1)

#index
list1=[1,2,444,443,3,2,45,3]
result=list1.index(444)
print(result)

list1=[1,2,444,443,3,2,45,3]
result=list1.index(3,3,7)
print(result)


#tuple

#index
list1=(1,2,444,443,3,2,45,3)
result=list1.index(45)
print(result)

list1=(1,2,444,443,3,2,45,3)
result=list1.index(2,3,7)
print(result)

#count
list1=(1,2,444,443,3,2,45,3)
result=list1.count(2)
print(result)
