#Write a Python program to sum all the items in a list.

ls=[1,2,3,4,5,6]
print(sum(ls))
a=0
for i in ls:
    a+=i
print("Sum is",a)