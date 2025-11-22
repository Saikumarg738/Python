#Write a Python program to get unique values from a list.


ls=[1,2,3,4,5,6,7,6,5,4,3,2,1]

uls=[]

for i in ls:
    if i not in uls:
        uls.append(i)

print(uls)