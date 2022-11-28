
#key:- By using this methiod we can print the only keys from the Dictionary.

#Syntex
#dict.key(self)

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.keys()
print(result)
   #if we don't need the output in dictionary we can use the for loop to print one by one

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.keys()
for i in result:
    print(i)

#value:- By using this method we can print only values in output from Dictionary

#Syntex
#dic.value(self)

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.values()
print(result)

 # if we don't need the output in dictionary we can use the for loop to print one by one.

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.values()
for i in result:
    print(i)

#items:- By using this method we can print keys and values in output from Dictionary.

#Syntex
#dict.items(self)

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.items()
print(type(result))

 # if we don't need the output in dictionary we can use the for loop to print one by one.


dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.items()
for i,j in result:
    print(i,j)
 #Another way to get output

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.items()
for i in result:    #type of this dictionary will convert into tuple so by using index medthod in tuple we can take 0 and 1
    print(i[0],i[1])

#update:- By using this method we can update the new items into Dictionary

#syntex
#dict.update(self,kwarg)

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.update(name='raja')
print(dic)

 #Another way to update items into Dictionary

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic['key4']='value4'
print(dic)

#get:- we can get the value from Dictionary by using key

#Syntex
#dict.get(self,key)

dic={'key1':'value1','key2':'value2','key3':'value3'}
result=dic.get('key2')
print(result)

#setdefult:- it can be used in 3 different ways

#syntex
#dict.setdefault(self,key,defualt)

 #we can add the items by using this method

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.setdefault('keys4','value4')
print(dic)

 #if we give only key the bydefault it will add None

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.setdefault('keys4')
print(dic)

 #if we give already existing key then it won't change anything

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.setdefault('key2','value333')
print(dic)

#fromkey:- By using this method we can convert any ittarable Data types into dictionary

#Syntex
#dict.fromkeys(class,ittarables,values)

str="python"
dic_={}
dic_=dic_.fromkeys(str) #it wil add None as value by default
print(dic_)

 #let's see how we can add value also

list=[1,2,3,4,5]
value='python'
dic_={}
dic_=dic_.fromkeys(list,value)
print(dic_)

#clear:- By using this method we can remove all the keys from the Dictionary.

#Syntex
#dict.clear(self)

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.clear()
print(dic)

#popitem:- By using this method we can remove the last key from the dictionary.

#syntex
#dict.popitem(self)

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.popitem()
print(dic) # it will remove every time the last item of dictionary.

#pop:- it will remove the item by using the key in the dictionary.

#syntex
#dict.pop(self,key)

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic.pop('key2')
print(dic)

#copy:- it will copy the dictionary.

#Syntex
#dict.copy(self)

dic={'key1':'value1','key2':'value2','key3':'value3'}
dic1=dic.copy()
print(dic1)








