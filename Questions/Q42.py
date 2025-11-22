"""Write a Python program to find missing and additional values in two lists.
	Sample data : Missing values in second list: b,a,c
	Additional values in second list: g,h

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']"""

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']

set1=set(list1)
set2=set(list2)

print("Missing values in second list are",set1.difference(set2))
print("Additional values in second list are",set2.difference(set1))