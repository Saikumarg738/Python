"""
Write a Python program to decode a run-length encoded given list.
	Original encoded list:
	[[2, 1], 2, 3, [2, 4], 5, 1]
	Decode a run-length encoded said list:
	[1, 1, 2, 3, 4, 4, 5, 1]

"""

ls=[[2, 1], 2, 3, [2, 4], 5, 1]
newls=[]
for i in ls:
    if(isinstance(i,list)):
        for j in range(i[0]):
            newls.append(i[1])
    else:
        newls.append(i)

print(newls)
