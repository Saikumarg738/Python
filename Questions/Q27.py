# Write a Python program to find the second smallest number in a list.

def second_smallest(num):
    small=second=float('inf')

    for i in num:
        if(i<small):
            second=small
            small=i
        elif(i<second):
            second=i
    return second

print(second_smallest([5,9,7,8,7,1,2]))