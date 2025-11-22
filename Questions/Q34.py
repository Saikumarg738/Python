"""Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
	Sample list : ['p', 'q']
	n =5
	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

sl=['p','q']
n=6
newsl=[]
for i in range(1,n):
    for j in sl:
        newsl.append(j+str(i))


print(newsl)