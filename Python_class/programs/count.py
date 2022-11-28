#Return the count of a given substring from a string
#Write a program to find how many times substring “Emma” appears in the given string.

#Given:
#str_x = "Emma is good developer. Emma is a writer"

def count_string(string):
    string1=string.count("Emma")
    return string1

str = "Emma is good developer. Emma is a writer"
print("this string has repeated ",count_string(str),"times")