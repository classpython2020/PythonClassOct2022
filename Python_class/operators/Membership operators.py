
#membership operators

#In
#not in

#*****************************************Example**********************************************

#in  :-Returns True if a sequence with the specified value is present in the object

fruits=["apple,pine apple,orange,mango"]
if "apple" in fruits:
    print("yes apple in fruits")
else:
    print("no apple is not in fruits")

list=[1,2,3,4,5,6]
if 3 in list:
    print("3 in list")
else:
    print("3 is not in list")

names=["raji,venky,rakesh,malli"]
if "raji" in names:
    print("raji in names")
else:
    print("raji is not in names")

#not in :-Returns True if a sequence with the specified value is not present in the object

list=[1,2,3,4,5]
if 6 not in list:
    print("6 is not in list")
else:
    print("6 is in list")


fruits=["apple,pine apple,orange,mango"]
if "banana" not in fruits:
    print("banana is not in fruits")
else:
    print("banana is a fruit")


names=["raja,venky,rakehs,malli"]
if "venky" not in names:
    print("raja is in list")
else:
    print("raja is not in list")

