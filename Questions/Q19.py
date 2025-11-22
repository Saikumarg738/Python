# Write a Python program to get the difference between the two lists.

ls1=[1,2,3,4]
ls2=[4,5,6,7]

ls3=ls1+ls2
ls4=[]
for i in ls3:
    if(ls3.count(i)==1):
        ls4.append(i)

print(ls4)