#1.capitalize ---we can convet the first letter of string from lower case to upper case
str1="this is raja yanamala"
str2=str1.capitalize()
print(str2)

#2.upper ---- we can convert the lower case strings to upper case
str1="this is raja yanamala"
str2=str1.upper()
print(str2)

#3.lower---- we can convert the upper case to lower case
str1="THIS IS RAJA YAnamALA"
str2=str1.lower()
print(str2)

#4.casefold-- this methode is same as like lower case but it is stronger than lower case method
str1="THIS IS RAJA YANAMALA"
str2=str1.casefold()
print(str2)

#5.swapcase--- this will convert the lower case to upper case and upper case to lower case
str1="THIS is RAJA yanamala"
str2=str1.swapcase()
print(str2)

#6.title--- it will conver all the strings starting letter to upper case
str1="this is raja yanamala"
str2=str1.title()
print(str2)

#7.center--- we can use this methode to give space before and after the string
str1="pythone"
str2=str1.center(20,"0")
print(str2)

#8.expandtabs--- it can give space between elements is string, but we have to give \t betwen
str1="p\ty\tt\th\to\tn"
str2=str1.expandtabs(5)
print(str2)

#9. endswith-- this will give result as true or false like that and it will check the end of the string correct or not
str1="this is raja yanamala"
str2=str1.endswith("ala")
print(str2)

#10.count---we can count how many elements are there in strings
str1="this is raja is yanamala raja"
count1=str1.count("is")
print(count1)
count2=str1.count("raja")
print(count2)
count3=str1.count("a")
print(count3)

#11.index--- it will give a specific letter index to us
str1="this is raja yanamala"
str2=str1.index("a")
print(str2)

str1="this is raja yanamala"
str2=str1.index("a",5, 10)
print(str2)

#12.find---- it will find the specific string index
str1="this is raja yanamala"
str2=str1.find("raja")
print(str2)

#13. replace--- it will replace the old string with new string
str1="this is raja yanamala"
str2=str1.replace("a", "y")
print(str2)

str1="this is raja yanamala"
str2=str1.replace("a", "y",2)
print(str2)

#14.split---it will break the string
str1="this is raja yanamala"
str2=str1.split(" ")
print(str2)

#15. join---- it will join the strings into one string

str1="this is raja yanamala"
str2=str1.split(" ") # we are breaking the string with split
str3=' '.join(str2)#join then with join
print(str3)

#16. format--- we can add the missing strings to the string
str1="this {name} raja {name1} from srm {name2}"
str2=str1.format(name="is",name1="yanamala",name2="univercity")
print(str2)

str1="this {a} raja {b} from srm {c}"
str2=str1.format(b="is",c="yanamala",a="univercity")
print(str2)

#17.using % operators in format
str1="this is raja %s" "from srm %s" "and got %d" %("yanamala", "university",70)
print(str1)

#18.floating precedance-- we can give how many digits should be after dot
str1=10/3
str2=("%5.4f" %(str1))
print(str2)

#19.f-string format
str1="this is raja yanamala"
print(f"{str1}")

#20.isainum-- if given string is isnumeric it will be true or false
str1="this is" #numeric means it should be 0-9 or alpabatice and should'nt be any space or any special characters
str2=str1.isalnum()
print(str2)

#21.isalpha---if the given string is alphabits then it will be true or false and should'nt be any space or any special characters
str1="thisisrajayanamala"
str2=str1.isalpha()
print(str2)

#22.islower--if given string is all in lower case then it will be true or flase
str1="this is raja yanamala"
str2=str1.islower()
print(str2)

#23.isupper--if given string is all in upper case then it will be true or flase
str1="THIS IS RAJA YANAMALA"
str2=str1.isupper()
print(str2)

#24.isspace--if given string[empty string] as space than it will be true or false
str1="    "
str2=str1.isspace()
print(str2)

#25.istital--if in string the first letter is capital it is true or flase
str1="This Is Raja Yanamala"
str2=str1.istitle()
print(str2)

#26.strip---if string has any special charecters in the middle then we can use this method to remove them
str1="this is &&&&raja  yanamala"
str2=str1.strip("&")
print(str2)