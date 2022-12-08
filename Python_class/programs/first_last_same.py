#Exercise 5: Check if the first and last number of a list is the same

#Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

def firstlastsame(list):
    print("given number:",list)
    first_number= list[0]
    last_number= list[-1]
    if first_number == last_number:
        return True
    else:
        return False

list1=[10, 20, 30, 40, 10]
print(firstlastsame(list1))

list2=[75, 65, 35, 75, 30]
print(firstlastsame(list2))
