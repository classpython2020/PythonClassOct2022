#logical operataros

#and
#Or
#not

#*****************************************Example************************************

#And :-Returns True if both statements are true

a=55
if a>=105 and a>=56:
    print("true")
else:
    print("false")

a=67
if a>66 and a>77:
    print("number between 66 to 77")
else:
    print("number not between 66 to 77")

a=78
if a<108 and a<666:
    print("true")
else:
    print("false")


#Or :-Returns True if one of the statements is true

a=77
if a>55 or a>105:
    print("true")
else:
    print("false")

a=98
if a==97 or a==98:
    print("yes a equal to 98")
else:
    print("yes a is not equal to 98")

a=67
if a!=67 or a!=66:
    print("yes a is not equal to 67")
else:
    print("yes a is equal to 67")


#not :-Reverse the result, returns False if the result is true

a=55
print(not(a>65 and a>75))

a=75
print(not(a==75 or a==77))

a=66
print(not(a<=75 or a<=66))


#Logical operetor
#it will always returns boolean value.

#and, or, not
#
#   a     b    a and b   a or b   not a   not b
# TRUE	TRUE	TRUE	  TRUE	  FALSE	  FALSE
# FALSE	TRUE	FALSE	  TRUE	  TRUE	  FALSE
# TRUE	FALSE	FALSE	  TRUE	  FALSE   TRUE
# FALSE	FALSE	FALSE	  FALSE	  TRUE	  TRUE

a=True
b= False

print(a and b)
print(a or b)
print(not a)
print(not b)
