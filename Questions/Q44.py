""" Write a Python program to generate groups of five consecutive numbers in a list.
numbers = list(range(1, 21))"""

numbers = list(range(1, 21))

"""fin=[]
newls=[]
for i in numbers:
    newls.append(i)
    if(len(newls)==5):
        fin.append(newls)
        newls=[]

print(fin)"""

group=[]
for i in range(0,len(numbers),5):
    group.append(numbers[i:i+5])

print(group)
