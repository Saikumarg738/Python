"""Write a Python program to insert a given string at the beginning of all items in a list.
	Sample list : [1,2,3,4], string : emp
	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""

def insertstr(ls,val):
    ls=[val+str(i) for i in ls]
    return ls

print(insertstr([1,2,3,4],"emp"))