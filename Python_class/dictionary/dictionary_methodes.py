#items

dic1_={'name':'teja','name1':'anil','name3':'mani','name4':'mani4'}
for i,j in dic1_.items():
    print(i,j)


#keys

dic1_={'name':'teja','name1':'anil','name3':'mani','name4':'mani4'}
for i in dic1_.keys():
    print(i)


#values

dic1_={'name':'teja','name1':'anil','name3':'mani','name4':'mani4'}
for i in dic1_.values():
    print(i)


#setdefault

dic1_={'name':'teja','name1':'anil','name3':'mani','name4':'mani4'}
dic1_.setdefault('name5',"lkddijg")
print(dic1_)

#fromkeys

list1=[1,2,3,4,543]
value="this is python"

dic1={}
dic1=dic1_.fromkeys(list1) #if we dont give value default to none
print(dic1)

#remove elements  LIFO(last in first out)

#by using clear
dic_={2:2,'name':'version',1:[1,2,3,4,5],3:[12345]}
dic_.clear()
print(dic_)

#by using popitem
dic_={2:2,'name':'version',1:[1,2,3,4,5]}
dic_.popitem()
print(dic_)


#by using pop
dic_={2:2,'name':'version',1:[1,2,3,4,5]}
dic_.pop(2)
print(dic_)

#copy
dic_={2:2,'name':'version',1:[1,2,3,4,5]}
dic2=dic_.copy()
print(dic2)

#update
dic1_={'name':'teja','name1':'anil','name3':'mani','name4':'mani4'}
dic_.update(new='i am leela')
print(dic_)


#nested dictionary #my self its wrong to be corrected

nest_dict={'dict1':234,'dict2':{'name':'bob','age':25}}
print(nest_dict['dict2']['name'])
print(nest_dict)

nest_dict['dict3']={'name':'bob','age':25}
nest_dict['dict1']['salary']=3453
nest_dict['dict1'].update(adress='pathuru',area='kpta')
print(nest_dict)

#dictionary comprehesion        both are error

dict1={'a':'1','b':'2','c':'3','d':'4','e':'5'}
my_dictionary={k:v*v for (k,v)in dict1.items()}
print(my_dictionary)





