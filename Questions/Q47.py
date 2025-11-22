# Write a Python program to insert an element before each element of a list.

ls=[1,2,3,4,5]
newls=[]
for i in range(0,len(ls)*2,2):
    ls.insert(i,10)

print(ls)