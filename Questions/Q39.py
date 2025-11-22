"""Write a Python program to convert a list of multiple integers into a single integer.
		Sample list: [11, 33, 50]
		Expected Output: 113350"""

ls=[11,33,50]

val=''.join(str(i) for i in ls)

print(int(val))