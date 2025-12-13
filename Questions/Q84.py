"""
Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
	Minimum value: 4
	Maximum value: 22
	Result:
	20 25 45 55 60 70 80 90 110

"""

ls=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

print(round(min(ls)))
print(round(max(ls)))

for i,j in enumerate(ls):
    r=round(j)*5
    ls.pop(i)
    ls.insert(i,r)

print(sorted(ls))
