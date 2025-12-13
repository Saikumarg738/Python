"""
 Write a Python program to Zip two given lists of lists.
	Original lists:
	[[1, 3], [5, 7], [9, 11]]
	[[2, 4], [6, 8], [10, 12, 14]]
	Zipped list:
	[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]

"""

newls=[]

LS1=[[1, 3], [5, 7], [9, 11]]
LS2=[[2, 4], [6, 8], [10, 12, 14]]

for i,j in zip(LS1,LS2):
    i.extend(j)
    newls.append(i)

print(newls)


