#set methods.

#1. Add
#2. Update
#3. Remove
#4. Discard
#5. Clear
#6. Del
#7. Union
#8. pop
#9. copy




# Add:- it will add one element to the set

# Syntex
#set.add(Self, element)

myset={1,23,342,52,"Raja",(45,23)}
myset.add(55)
print(myset)

  # we can'nt add more than one element with ADD methode.

#update:- By using this methode we can update multipul elements to set.

#Syntex
#set.update(self, kwarg,arg)

myset={1,23,342,52,"Raja",(45,23)}
myset.update([1,2,3,4],{2,33,45},(5,2,3))
print(myset)

#remove:- it will remove the selected element from the set

#syntex
#set.remove(self, element)


myset={1,23,342,52,"Raja",(45,23)}   #it can'nt remove the values which or inside of tuples.
myset.remove((342))
print(myset)

#discard :- it is just like remove but if given element is there in set it will not give any error.

#syntex
#set.discard(self, element)

myset={1,23,342,52,"Raja",(45,23)}
myset.discard(54)           # i had given 54 which is not there in set but it did'nt raise any error
print(myset)

#clear :- it will remove all the data from set and print empty set in output.

#syntex
#set.clear(self)

myset={1,23,342,52,"Raja",(45,23)}
myset.clear()
print(myset)

    #if we want to delete empty set also we can use the del key
del myset
print(myset)

#copy:- it will copy the set

#syntex
#set.copy(self)


myset={1,23,342,52,"Raja",(45,23)}
myset1=myset.copy()
print(myset)
print(myset1)

#Union:- it eill add the data from different variable data to one variable.

#Syntex
#set.union()

myset={1,23,342,52,"Raja",(45,23)}
myset1={2,33,23,"raj",(25,13,24)}
print(myset|myset1)
print(myset.union(myset1))  #secound way


#**************Intersection ***********
# Intersection:- it will return common values from both variables

#Syntex
# set.intersection(self,set)

A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(A & B)  # intersection
print(A.intersection(B))

#**************** differnce ************
A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(A-B)
print(A.difference(B))

A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(B-A)
print(B.difference(A))

#******************* Symmetric differnce ***********
A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(A^B)
print(A.symmetric_difference(B))

#************************** differnce update ################3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
print(y)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.difference_update(x)
print(x)
print(y)
