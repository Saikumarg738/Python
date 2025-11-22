"""Write a Python program to flatten a given nested list structure.
		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
		Flatten list:
		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""
ols=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

newls=[]

for i in ols:
    if(isinstance(i,list)):
        newls.extend(i)
    else:
        newls.append(i)

print(newls)