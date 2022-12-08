#its unorder collection
#dic has key word
#all keys are immutable
#all value are mutable
#dic is mutable object

dic1={'key':'value','key2':'value','key3':'value3'}

dic_={2:2,'name':'version',1:[1,2,3,4,5]}
print(type(dic_))

my_dictionary=dict({2:2,'name':'version',1:[1,2,3,4,5]})
print(type(my_dictionary))

my_dictionary12=dict([(1,'apple'),(2,'eat')])
print(my_dictionary12)

#acess element and upadte the value add dictionary

dic_={2:2,'name':'version',1:[1,2,3,4,5]}
print(dic_['name'])
print(dic_[2]) #retun key error it is not there in dictionary
print(dic_.get) #retune none is key is not there in dictionary

dic_['name']='version100'
print(dic_)

