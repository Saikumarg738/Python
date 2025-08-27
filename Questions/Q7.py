#Write a Python program to remove duplicates from a list.

ls=[1,2,2,5,83,94,27,2,94,47,2,38,49,20,49]

for i in ls:
    if(ls.count(i)>1):
        ls.remove(i)
print(ls)