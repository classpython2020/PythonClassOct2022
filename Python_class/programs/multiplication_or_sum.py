#Exercise 1: Calculate the multiplication and sum of two numbers.
#Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.

def multiplication_or_sum(a,b):
    product=(a*b)
    if product > 1000:
        print("the product value is :",product)
    else:
        print(a+b)

print("Enter the product1 number:")
product1=int(input())
print("Enter the product2 number:")
product2=int(input())
print(multiplication_or_sum(product1,product2))