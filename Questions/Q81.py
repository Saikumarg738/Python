"""
Write a Python program to extract a given number of randomly selected elements from a given list.
	Original list:
	[1, 1, 2, 3, 4, 4, 5, 1]
	Selected 3 random numbers of the above list:
	[4, 4, 1]
"""

import random

def sel_random(ls,num):
    return random.sample(ls,num)

print(sel_random([1,2,3,4,5,6,7],3))