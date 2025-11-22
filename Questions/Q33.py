#Write a Python program to generate all sublists of a list.

ls=[1,2,3,4,5,6,7]

for i in range(len(ls)):
    for j in range(i+1,len(ls)+1):
        print(ls[i:j])
