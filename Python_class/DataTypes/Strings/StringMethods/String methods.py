#strings methods

#1.upper()
#2.lower()
#3.casefold()
#4.swapcase()
#5.capitalize()
#6.title()
#7.startswith()
#8.endswith()
#9.find()
#10.count()
#11.index()
#12.center()
#13.expandtabs()
#14.split()
#15.splitline
#15.join()
#16.replace()
#17.strip()
#18.rstrip
#19.lstrip
#21.marketrans
#22.translate
#23.partition
#24.format()
#25.format_map()
#26.encode
#27.isalnum()
#28.isalpha()
#29.isascii
#30.isdecimal
#31.isdigit
#32.isidentifier
#33.islower()
#34.isnumeric
#35.isprintable
#36.isspace()
#37.istitle()
#38.isupper()
#39.ljust
#40.rfind
#41.rindex
#42.rjust
#43.rpartition
#44.zfill


#*******************************************examples*************************************************
#1.upper ---- we can convert the lower case strings to upper case

#syntex
#string.upper(self)

str1="this is raja yanamala"
str2=str1.upper()
print(str2)

#2.lower---- we can convert the upper case to lower case

#syntex
#string.lower(self)

str1="THIS IS RAJA YAnamALA"
str2=str1.lower()
print(str2)

#3.casefold-- this methode is same as like lower case but it is stronger and more aggrasive than lower case method,
#it will convert the other languages upper case alphabets also in lower case

#syntex
#string.casefold(self)

str1="THIS IS RAJA YANAMALA"
str2=str1.casefold()
print(str2)

#4.swapcase--- this will convert the lower case to upper case and upper case to lower case

#syntex
#string.swapcase(self)

str1="THIS is RAJA yanamala"
str2=str1.swapcase()
print(str2)

#5.capitalize ---we can convet the first letter of string from lower case to upper case

#syntex
#string.capitalize(self)

str1="this is raja yanamala"
str2=str1.capitalize()
print(str2)


#6.title--- it will conver all the strings starting letter to upper case

#syntex
#string.title(self)

str1="this is raja yanamala"
str2=str1.title()
print(str2)


#7. startswith-- this will give result as true or false like that and it will check the strating of the string correct or not

#syntex
#string.starswith(self,prefix,start,end)

str1="this is raja yanamala"
str2=str1.startswith('this')
print(str2)


str1="this is raja yanamala"
str2=str1.startswith("this",0,7)
print(str2)


#8. endswith-- this will give result as true or false like that and it will check the end of the string correct or not
str1="this is raja yanamala"
str2=str1.endswith("ala")
print(str2)


#9.find---- it will find the specific string index

#syntex
#string.find(sub,start,end)

str1="this is raja yanamala"
str2=str1.find("a")
print(str2)

#10.count---we can count how many times that string is there in the line.

#syntex
#string.count(sub,start,end)

str1="this is raja is yanamala raja"
count1=str1.count("is")
print(count1)
count2=str1.count("raja")
print(count2)
count3=str1.count("a")
print(count3)

#11.index--- it will give a specific letter index to us

#Syntax
#string.index(value, start, end)

#Parameter Values
#Parameter	Description
#value	Required. The value to search for
#start	Optional. Where to start the search. Default is 0
#end	Optional. Where to end the search. Default is to the end of the string

str1="this is raja yanamala"
str2=str1.index("raja")
print(str2)

str1="this is raja yanamala"
str2=str1.index("a",5, 10)
print(str2)

#12.center--- we can use this methode to give space before and after the string

#Syntax
#string.center(length, character)
#Parameter Values
#Parameter	Description
#length	Required. The length of the returned string
#character	Optional. The character to fill the missing space on each side. Default is " " (space)

str1="pythone"
str2=str1.center(20,"0")
print(str2)

#13.expandtabs--- it can give space between string, but we have to give \t between where we want to give space for it.

#Syntax
#string.expandtabs(tabsize)
#Parameter Values
#Parameter	Description
#tabsize	Optional. A number specifying the tabsize. Default tabsize is 8

str1="p\ty\tt\th\to\tn"
str2=str1.expandtabs(5)
print(str2)


#14.split---it will break the string and give the output in list

#Syntax
#string.split(separator, maxsplit)
#Parameter Values
#Parameter	Description
#separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

str1="this is raja yanamala"
str2=str1.split("a")
print(str2)   #it will split by alphabets and space as well

str1="this is raja yanamala"
str2=str1.split(" ")
print(str2)

str1="this is raja yanamala"  #by using of maxsplit
str2=str1.split("a", 3)
print(str2)



#15.splitline:- splitline is just like split method but it is stonger than split method.
#it will spilt and give output in list

#Syntax
#string.splitlines(keeplinebreaks)
#Parameter Values
#Parameter	Description
#keeplinebreaks	Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False

str1="th\nis is\nraja\nyanamala"
str2=str1.splitlines( )
print(str2)

str1="this\nis\nraja\nyanamala"
str2=str1.splitlines(False)     #when we use true it will split along with \n
print(str2)                     #by defalut false will be there
str2=str1.splitlines(True)
print(str2)


str1="this\nis\nraja\ryanamala"
str2=str1.splitlines( )     #even if we give some of alphabite also it will split
print(str2)

#16. join---- it will join the strings into one string

#Syntax
#string.join(iterable)
#Parameter Values
#Parameter	Description
#iterable	Required. Any iterable object where all the returned values are strings

str1="this is raja yanamala"
str2=str1.split(" ") # we are breaking the string with split
str3=' '.join(str2)#join then with join
print(str3)


#17. replace--- it will replace the old string with new string

#Syntax
#string.replace(oldvalue, newvalue, count)
#Parameter Values
#Parameter	Description
#oldvalue	Required. The string to search for
#newvalue	Required. The string to replace the old value with
#count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences


str1="this is raja yanamala"
str2=str1.replace("a", "y")
print(str2)

str1="this is raja yanamala"
str2=str1.replace("a", "y",2)
print(str2)


#18.strip---by using this method we can remove special characters and alphabets from the left and right side
#we can't remove the meddile of the strings

#Syntax
#string.strip(characters)
#Parameter Values
#Parameter	Description
#characters	Optional. A set of characters to remove as leading/trailing characters


str1='@@@@@@raja@@@@@'
str2=str1.strip("@")
print(str2)

str1='aaaaaarajaAAAAAAA'
str2=str1.strip("a,A")
print(str2)

   #we can't remove the meddile characters

str1='aaaarajaaarajaaaa'
str2=str1.strip("a")
print(str2)

#19.lstrip:- by using this method we can remove the left side of characters

#Syntax
#string.lstrip(characters)
#Parameter Values
#Parameter	Description
#characters	Optional. A set of characters to remove as leading characters

str1='aaaarajaaaaaaa'
str2=str1.lstrip("a")
print(str2)

#20.rstrip:-  by using this method we can remove the right side of characters

#Syntax
#string.rstrip(characters)
#Parameter Values
#Parameter	Description
#characters	Optional. A set of characters to remove as trailing characters

str1='aaaarajaaaaaaa'
str2=str1.lstrip("a")
print(str2)

#21.marketrans:- # it will create a table which is in form of dictionary.
#it contains old value and new value to replace
#this table will tell which value need to be deleted (none) and which value need to be replaced
#after we get the output, that we will call as table and with that we can use translate method and convert them into string.

#22.traslate:- after we get the table from the marketrans then only we can use the translate method and replace and delete the characters

string="this is raja yanamala"
dict1={'a':1,'b':2,'r':'r','i':None,}
table=string.maketrans(dict1)
print(table)
string=string.translate(table)  #after we get the table we can use that with translate method to replace the values and delete them by using none
print(string)
   # we have created a table here and we can keep the variable whatever we want .

#23.partition:-#The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
#The first element contains the part before the specified string.
#The second element contains the specified string.
#The third element contains the part after the string.


#syntex
#string.partition(value)

string="this is raja yanamala from ap"
str1=string.partition("yanamala")
print(str1)

#If the specified value is not found, the partition() method returns a tuple
# containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)


#24. format--- we can add the missing strings to the string
str1="this {name} raja {name1} from srm {name2}"
str2=str1.format(name="is",name1="yanamala",name2="univercity")
print(str2)

str1="this {a} raja {b} from srm {c}"
str2=str1.format(b="is",c="yanamala",a="univercity")
print(str2)

#25.using % operators in format
str1="this is raja %s" "from srm %s" "and got %d" %("yanamala", "university",70)
print(str1)

#26.floating precedance-- we can give how many digits should be after dot
str1=10/3
str2=("%5.4f" %(str1))
print(str2)

#27.f-string format
str1="this is raja yanamala"
print(f"{str1}")

#28.isainum-- if given string is isnumeric it will be true or false

#Syntax
string.isalnum()

str1="this is" #numeric means it should be 0-9 or alpabatice and should'nt be any space or any special characters
str2=str1.isalnum()
print(str2)

#29.isalpha---if the given string is alphabits then it will be true or false and should'nt be any space or any special characters

#Syntax
string.isalpha()

str1="thisisrajayanamala"
str2=str1.isalpha()
print(str2)


#30.isdigit:-The isdigit() method returns True if all the characters are digits, otherwise False.
#Exponents, like ², are also considered to be a digit.

#Syntax
string.isdigit()

str1="12346542"
str2=str1.isdigit()
print(str2)

#31.isidentifier:-
#The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#A string is considered a valid identifier if it only contains alphanumeric letters
# (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

#Syntax
string.isidentifier()

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


#32.islower--if given string is all in lower case then it will be true or flase

#Syntax
string.islower()

str1="this is raja yanamala"
str2=str1.islower()
print(str2)

#33.isnumeric:-
#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
#Exponents, like ² and ¾ are also considered to be numeric values.
#"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

#Syntax
string.isnumeric()

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

#34.isprintable:-
# The isprintable() method returns True if all the characters are printable, otherwise False.
#Example of none printable character can be carriage return and line feed.

#Syntax
string.isprintable()

txt = "Hello this is r@j@ Yanamala "
x = txt.isprintable()
print(x)

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

#35.isspace--if given string[empty string] as space than it will be true or false

#Syntax
string.isspace()

str1=" "
str2=str1.isspace()
print(str2)

#36.istital--if in string the first letter is capital it is true or flase

#Syntax
string.istitle()

str1="This Is Raja Yanamala"
str2=str1.istitle()
print(str2)

#37.isupper--if given string is all in upper case then it will be true or flase

#Syntax
string.isupper()

str1="THIS IS RAJA YANAMALA"
str2=str1.isupper()
print(str2)

#38.ljust:-
#The ljust() method will left align the string, using a specified character (space is default)
# as the fill character.

#Syntax
#string.ljust(length, character)

#Parameter Values
#Parameter	Description
#length	Required. The length of the returned string
#character	Optional. A character to fill the missing space (to the right of the string).
# Default is " " (space).

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#Using the letter "O" as the padding character:

txt = "banana"
x = txt.ljust(20, "O")
print(x)

#39.rfind:-
#The rfind() method finds the last occurrence of the specified value.
#The rfind() method returns -1 if the value is not found.
#The rfind() method is almost the same as the rindex() method. See example below.

#Syntax
#string.rfind(value, start, end)

#Parameter Values
#Parameter	Description
#value	Required. The value to search for
#start	Optional. Where to start the search. Default is 0
#end	Optional. Where to end the search. Default is to the end of the string

#Where in the text is the last occurrence of the string "casa"?:

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)


#Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)

#If the value is not found, the rfind() method returns -1,
# but the rindex() method will raise an exception:

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q"))


#40.rindex:-
#The rindex() method finds the last occurrence of the specified value.
#the rindex() method raises an exception if the value is not found.
#The rindex() method is almost the same as the rfind() method. See example below.

#Syntax
#string.rindex(value, start, end)

# Parameter Values
#Parameter	Description
#value	Required. The value to search for
#start	Optional. Where to start the search. Default is 0
#end	Optional. Where to end the search. Default is to the end of the string

#Where in the text is the last occurrence of the string "casa"?:

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#Where in the text is the last occurrence of the letter "e"?:

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

#Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

#If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q"))


#41.rjust:-
#The rjust() method will right align the string, using a specified character (space is default) as the fill character.

#Syntax
#string.rjust(length, character)

#Parameter Values
#Parameter	Description
#length	Required. The length of the returned string
#character	Optional. A character to fill the missing space (to the left of the string). Default is " " (space).

#Return a 20 characters long, right justified version of the word "banana":

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")


txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
#Using the letter "O" as the padding character:

txt = "banana"
x = txt.rjust(20, "O")
print(x)

#42.rpartition

#The rpartition() method searches for the last occurrence of a specified string,
# and splits the string into a tuple containing three elements.
#The first element contains the part before the specified string.

#The second element contains the specified string.

#The third element contains the part after the string.

#Syntax
#string.rpartition(value)

#Parameter Values
#Parameter	Description
#value	Required. The string to search for

#Search for the last occurrence of the word "bananas", and return a tuple with three elements:

#1 - everything before the "match"
#2 - the "match"
#3 - everything after the "match"

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#If the specified value is not found, the rpartition() method returns a tuple containing:
# 1 - an empty string, 2 - an empty string, 3 - the whole string:

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

#43.zfill:-
 #The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

 #If the value of the len parameter is less than the length of the string, no filling is done.

 #Syntax
string.zfill(len)

 #Parameter Values
 #Parameter	Description
 #len	Required. A number specifying the desired length of the string

 #Fill the string with zeros until it is 10 characters long:

txt = "50"
x = txt.zfill(10)
print(x)

 #Fill the strings with zeros until they are 10 characters long:

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))










