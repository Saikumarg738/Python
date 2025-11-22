# Write a Python program to split a list based on first character of word.

words = ['apple', 'ant', 'ball', 'bat', 'cat', 'cool', 'dog', 'doll']

newdc={}
for word in words:
    fw=word[0]
    if(fw not in newdc):
        newdc[fw]=[]
    newdc[fw].append(word)


print(newdc)

