
#callable() Function

#1. it will check if we can callable the function or not.
#2. if we can callalbe that function it will be true.
#3. if we can not callalbe that function it will be False.

#syntex
callable(object)

#if we can callalbe that function it will be true.

def function():
    x=5
    print(x)

print(callable(function))  #output is true

#if we can not callalbe that function it will be False.

x=5
print(x)

print(callable(x))  #output id False
