# Write a Python program to flatten a shallow list.

ls=[[1, 2, 3], [4, 5], [6, 7, 8]]
nls=[]
for i in ls:
    for j in i:
        nls.append(j)

print(nls)