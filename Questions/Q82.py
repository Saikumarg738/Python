"""
82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
HINT
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
"""

ls=[1, 2, 3, 4, 5, 6, 7, 8, 9]

newls=[]

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        tml=[ls[i],ls[j]]
        newls.append(tml)

print(newls)