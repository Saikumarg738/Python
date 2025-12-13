"""
Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
	Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
	Result:
	243
"""

ls=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

total=0
for i in ls:
    num=round(i)
    total+=num

print(total*len(ls))