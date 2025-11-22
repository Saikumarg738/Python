"""Write a Python program to change the position of every n-th value with the (n+1)th in a list.
	Sample list: [0,1,2,3,4,5]
	Expected Output: [1, 0, 3, 2, 5, 4]"""

ls=[0,1,2,3,4,5]

def swaplist(lst):
    for i in range(0,len(lst),2):
        ls[i],ls[i+1]=ls[i+1],ls[i]
    return ls

print(swaplist(ls))