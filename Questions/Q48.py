# Write a Python program to print a nested lists (each list on a new line) using the print() function.

ls=[1,2,3,[4,5,6],7,8,[9,10,11,12]]

for i in ls:
    if(isinstance(i,list)):
        print(i)