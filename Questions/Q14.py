# Write a Python program to print the numbers of a specified list after removing even numbers from it.

ls=[1,2,3,4,5,6,7,8,9]

newls=[i for i in ls if i%2!=0]

print(newls)