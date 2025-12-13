"""
Write a Python program to sort a given list of lists by length and value.
	Original list:
	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
	Sort the list of lists by length and value:
	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

"""

ls=[[2], [0], [1, 3], [0, 7],[13, 15, 17], [9, 11]]

newls=list(sorted(list(sorted(ls,key=lambda a:a[0])),key=lambda a:len(a)))

print(newls)