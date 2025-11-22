#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

inls=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

otls=[]

for i in inls:
    if(inls.index(i) not in [0,4,5]):
        otls.append(i)

print(otls)
