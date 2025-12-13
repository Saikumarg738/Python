"""
Write a Python program to rotate a given list by specified number of items to the right or left direction.
original List:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Rotate the said list in left direction by 4:
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
Rotate the said list in left direction by 2:
[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
Rotate the said list in Right direction by 4:
[8, 9, 10, 1, 2, 3, 4, 5, 6]
Rotate the said list in Right direction by 2:
[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

"""
LS=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n=int(input("Enter Number : "))

for i in range(n):
    a=LS[-1]
    LS.pop(-1)
    LS.insert(0,a)

print(LS)