# Range function
#1. Range can be use to print the values between given range.
#2. We can not use range alone, we have to store that values in some variable or function.
#3. There are there paramaters i range
    # 1.starting point
    # 2. Ending point -1
    # 3. Incremante
#Syntex
#range(starting point,ending point-1,incremante)


#2. We can not use range alone, we have to store that values in some variable or function.

print(range(10))  #if we print this we will get output like,Range 10, Because we have'nt store range value in anothing.

# 2. Ending point -1
print(list(range(10))) #it will print from 0 to till 9, Because by defualt 0 will be taken as starting point
                    # and 9 will print because ending point will be -1

# 1.starting point

print(list(range(1,10))) # it will start from 1 because we have mention the starting point

# 3. Incremante

print(list(range(1,10,2))) #[1, 3, 5, 7, 9] it will increase the starting point with given incremanet number
    # 1+2=3, 3+2=5, 5+2=7  like this it will be increase with increament number.

# We can do decending order also with range function

print(list(range(10,1,-1)))  #[10, 9, 8, 7, 6, 5, 4, 3, 2] it will decrease because we have mention -1





