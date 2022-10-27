#logical operataros

#And

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


#Or

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


#not

a=55
print(not(a>65 and a>75))

a=75
print(not(a==75 or a==77))

a=66""
print(not(a<=75 or a<=66))
