
#bitwise operator

#and (&)
#or  (|)
#Xor (^)
#right shift  (>>)
#left shift   (<<)


#********************************************examples*************************************************


# and & :-Sets each bit to 1 if both bits are 1

a=70
b=80
print(a&b)

a=90
b=74
print(a&b)

a=102
b=155
print(a&b)

# Or |:-Sets each bit to 1 if one of two bits is 1

a=20
b=60
print(a|b)

a=61
b=74
print(a|b)

a=251
b=174
print(a|b)

a=77
b=66
print(a|b)

# Xor ^:-Sets each bit to 1 if only one of two bits is 1

a=17
b=15
print(a^b)

a=15
b=22
print(a^b)

a=19
b=120
print(a^b)

a=27
b=5
print(a^b)

# not ~ :-Inverts all the bits

a=15
x=~a
print(x)

a=17
x=~a
print(x)

a=20
x=~a
print(x)

a=22
x=~a
print(x)

# right shift >> :Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

a=15
print(a>>4)

a=17
print(a>>3)

a=25
print(a>>2)

a=27
print(a>>6)

