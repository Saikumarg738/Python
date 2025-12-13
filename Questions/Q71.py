"""Write a Python program to check whether all dictionaries in a list are empty or not.
	Sample list : [{},{},{}]
	Return value : True
	Sample list : [{1,2},{},{}]
	Return value : False
"""


def checkemp(ls):
    return all(len(i)==0 for i in ls)


print(checkemp([{2:3},{},{}]))