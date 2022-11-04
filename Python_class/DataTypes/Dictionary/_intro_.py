#unordered collection
#dic has key value
#all keys are immutable
#all values are mutable
#dic mutable object

#Syntex

dic={'key1':'value','key2':'value','key3':'value'}

#we can write syntex in different way also

dic=dict({'key1':'value','key2':'value','key3':'value'})
print(dic)

# we can use this dict fuction to write multipul data types also

dic=dict([(1,2,3,4),(6,7,8,9)])  #like this we can use multi data types in one list
print(dic)                       #we can'nt use multipul data types without dict function

#let's see how we can print value  by using key

#Both will give the key value in output but the differance is

dic={'key1':'value','key2':'value1','key3':'value2'}
print(dic['key2'])  #returns key error if key is not present in dicstionary

dic={'key1':'value','key2':'value1','key3':'value2'}
print(dic.get('key2'))   #returns none if key is not present in dicstionary


#let's give how can we add new keys to dictionary

dic={'key1':'value','key2':'value1','key3':'value2'}
dic['key4']='value4'
print(dic)








