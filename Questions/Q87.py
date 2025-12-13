"""
 Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user.
	Input rows: 2
	Input columns: 2
	Input number of elements in a row (1, 2, 3):
	1 2
	3 4
	sum for each column:
	4 6

"""

row=int(input("Enter number of rows : "))
col=int(input("Enter number of columns : "))

c=0
matrix=[]

for i in range(row):
    rowmat=[]
    for j in range(col):
        c+=1
        rowmat.append(c)
    matrix.append(rowmat)

print(matrix)

col_sum=[0] * col

for i in range(row):
    for j in range(col):
        col_sum[j]+=matrix[i][j]

print(col_sum)