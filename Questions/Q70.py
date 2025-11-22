"""Write a Python program to find the items starts with specific character from a given list.
		Expected Output:
		Original list:
		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
		Items start with a from the said list:
		['abcd', 'abc', 'acjd']
		Items start with d from the said list:
		['dagfa']
		Items start with w from the said list:
		[]
"""

ols=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

res={'a':[],'d':[],'w':[]}

for i in ols:
    if(i.startswith("a")):
        res['a'].append(i)
    elif(i.startswith("d")):
        res['d'].append(i)
    elif(i.startswith("w")):
        res['d'].append(i)

for i,j in res.items():
    print(f"Words that start with {i} are {j}")


