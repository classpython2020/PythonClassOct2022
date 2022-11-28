# to prove it is palindrome or not
#firth we need to reverse the string
#then we need to check string is equal or not equal by using equal(==)
#then we need to use if statement to check it is a palindrome or not

def palindrome(string):
    rev_string=string[::-1]
    if string==rev_string:
         print("this is palindrome:",string)
    else:
        print("this is not palindrome:",string)

palindrome('madam')

