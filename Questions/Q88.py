"""
Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
	Input the size of the matrix: 3
	2 3 4
	4 5 6
	3 4 7
	Sum of matrix primary diagonal:
	14

"""

n=int(int(input("Enter size of matrix : ")))

matrix=[]

for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)

for i in matrix:
    print(i)

sum_col=0

for i in range(3):
    sum_col+=matrix[i][i]

print(sum_col)