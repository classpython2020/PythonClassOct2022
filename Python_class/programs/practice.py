#capitalize method

str1="His is raja yanamala"
str2=str1.capitalize()
print(str2)

#casefold-- this method is just like lower method but casefold is stronger then lower it will convert all lower case to upper case

str1="THIS IS RAJA YANAMALA"
str2=str.casefold()
print(str2)

#center--- this will center the string by giving whitespaces in front and back of the string

str1="python"
str2=str1.center(20)
print(str2)


str1="python"
str2=str1.center(20,"0")
print(str2)

#count-- it will count thw specific value how many time is there in string and we can take counts how many time we need
#just we need to increase the syntex

str1="th is is raja yanamala is"
count1=str1.count("is")
print(count1)
count2=str1.count("a")
print(count2)
count3=str1.count("Raja")
print(count3)

#Endswith---- we can check the end of the string word is correct or not

str1="this is raja yanamala"
str2=str1.endswith("ala")
print(str2)

#expendtabs--- we can give tabs between letter in string and we can mention the size as well

str1="p\ty\tt\th\to\tn"
str2=str1.expandtabs(10)
print(str2)

#find--- this is find the potion of specific letter in the string

str1="this is raja yanamala"
str2=str1.find("a", 1,15)
print(str2)

#format-- we can use this to add the elements to string at a specifie position

str1="this {name} raja {name2} from srm {name3}"
str2=str1.format(name="is", name3="univercity", name2="yanamala")
print(str2)

#index--we can know the specific element index by using this method
str1="this is raja yanamala"
str2=str1.index("y")
print(str2)

#isalnum--- isalnum will represent given string is true or false,
#if given string is alpanumaric then it is true or it will be false
str1="raja yanamala222"
str2=str1.isalnum()
print(str2)

str1="rajayanamala222"
str2=str1.isalnum()
print(str2)

#isalpha ----isalpha will represent given string is true or false,
#if we give any special charecter or digits will be false or true
str1="thisisRAJA"
str2=str1.isalpha()
print(str2)

list=[1,2,3,4,5,6]
j=0
for i in list:
    i=i+ list
    print(i, end=(' '))

i=15
while  i>00:
    i=i-1
    print(i,end=(' '))


# Decide the row count. (above pattern contains 5 rows)
row = 6
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1,5 + 1, 1):
    print(i)
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")