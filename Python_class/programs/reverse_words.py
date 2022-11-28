#Exercise 1: Reverse each word of a string
#Given:
#str = 'My Name is Jessa'
#Expected Output
#yM emaN si asseJ

def reversewords(string):
    words=string.split()
    new_string=[word[::-1] for word in words]
    reversed_words=''.join(new_string)
    return reversed_words


str = 'My Name is Jessa'
print(reversewords(str))

