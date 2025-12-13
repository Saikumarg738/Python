"""Write a Python program to pack consecutive duplicates of a given list elements into sublists.
	Original list:
	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
	After packing consecutive duplicates of the said list elements into sublists:
	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

"""

def checkdup(ls):
    mainls=[]
    subls=[ls[0]]
    prev=ls[0]
    for i in ls[1:]:
        if(i!=prev):
            mainls.append(subls)
            subls=[i]
        else:
            subls.append(i)
        prev=i
    mainls.append(subls)
    print(mainls)

checkdup([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])