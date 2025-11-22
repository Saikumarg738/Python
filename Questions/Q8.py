#Write a Python program to check a list is empty or not.

a=[1,2,3,4]
b=[]
c=[]
d=["a","b"]

ls=[a,b,c,d]

for i in ls:
    if(len(i)>0):
        print(f"{i} is not empty")