
#Given an array, find the largest element in it.

#Input : arr[] = {10, 20, 4}
#Output : 20

#Input : arr[] = {100, 10, 20, 4, 101}
#Output : 100

def largestelelement(list1):
    max=list1[0]
    size=len(list1)
    for i in range(1,size) :
        if list1[i]>max:
            print(list[i])
            max=list1[i]
    return max


list=[100, 10, 1002, 4, 1001]
print(largestelelement(list))