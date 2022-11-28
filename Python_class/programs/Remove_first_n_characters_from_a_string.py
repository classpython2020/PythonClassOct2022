#Exercise 4: Remove first n characters from a string
#Write a program to remove characters from a string starting from zero up to n and return a new string.

def slicingastring(string,n):
    x=string[n:]
    return x


word=input("enter the word:")
n=int(input("please enter the number:"))
print(slicingastring(word,n))
