#we are using slice method here to reversed the string
#slice rule is [start,end,step]
#if we don't give start and end it will directly go to step
# if we give -1 then it will start from backwards

string=(input("please enter the string value:"))
result=string[::-1]
print(result)

# 0  1  2  3 4 5 6 7 8 9 10 11
# r  a  j  a y a n a m a l  a
#-12-11-10-9-8-7-6-5-4-3-2-1