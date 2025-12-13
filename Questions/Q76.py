"""Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
	Original list:
	[1, 1, 2, 3, 4, 4, 5, 1]
	List reflecting the modified run-length encoding from the said list:
	[[2, 1], 2, 3, [2, 4], 5, 1]
	Original String:
	aabcddddadnss
	List reflecting the modified run-length encoding from the said string:
	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

"""

ls=[1, 1, 2, 3, 4, 4, 5, 1]
#ls="automatically"

mainls=[]
subls=[]
prev=ls[0]
count=1
for i in ls[1:]:
    if(i==prev):
        count+=1
    else:
        if(count>1):
            subls=[count,prev]
        else:
            subls = prev
        mainls.append(subls)
        count=1
    prev=i

if(count>1):
    mainls.append([count,prev])
else:
    mainls.append(prev)

print(mainls)
