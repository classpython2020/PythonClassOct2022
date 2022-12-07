# Slicing Function

#1. Slicing will be use with string to cut the string from a paticelar index position
#2. Slicing also can be used to reverse the string
#3. There are three paramaters in slicing
    #1. Starting point---- from index of 0
    #2. Ending point _____from index of 1
    #3. -1, We can use - index to cut the string from the backfowords and revese  a string.

str="welcome"
print(str[:5]) #If we dont give any starting point by defalut it will take as 0.
print(str[1:5]) #it will start from index of one.
print(str[1::]) #if we give only starting point then it will take last index as defalut value .

print(str[::-1]) #with out any paramaters if we give -1 then it will reverse the string.




