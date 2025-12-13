"""
Write a Python program to create a multidimensional list (lists of lists) with zeros.
Multidimensional list: [[0, 0], [0, 0], [0, 0]]

"""

rows=3
cols=2

matrix=[[0 for _ in range(cols)] for _ in range(rows)]

print(matrix)