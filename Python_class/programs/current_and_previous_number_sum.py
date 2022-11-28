#Exercise 2: Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

def currentandpreviousnumbersum():
    previous_num=0
    for i in range(1,11):
        sum=i+previous_num
        print("Current Number",i, "Previous Number", previous_num, " Sum:", sum)
        previous_num=i
    return print

print(currentandpreviousnumbersum())