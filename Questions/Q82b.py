"""
82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
HINT
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
"""

from itertools import combinations

ls=[1,2,3,4,5,6,7,8,9]

n=3

newls=list(combinations(ls,n))

print(newls)
