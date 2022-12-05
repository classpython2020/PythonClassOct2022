#bool function

#1. bool will return output as True or False
#2. bool function always returns true unless;
  # the object is empty. like () {} []
  # the object is False
  # the abject is 0
  # the object is None

#Syntex

#bool(object)

x= bool(1)
print(x)

# the object is empty. like () {} []

print(bool(()))
print(bool([]))
print(bool({}))
print(bool())

# the object is False

print(bool(False))

# the abject is 0

print(bool(0))

# the object is None

print(bool(None))
