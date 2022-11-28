
#Exercise 6: Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5


def divisible(n,d):
    for i in n:
        if i%d==0:
            print(i)
    return i

number=[10, 20, 33, 46, 55]
print(divisible(number,5))