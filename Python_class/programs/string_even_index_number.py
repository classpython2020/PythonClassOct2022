#Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.

#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

def stringEvenIndexNumber(string):
    word=list((string))
    for i in word[1::2]:
        print(i)
    return print


string=input("enter the word")
print(stringEvenIndexNumber(string))

