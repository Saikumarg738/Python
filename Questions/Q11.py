#Write a Python function that takes two lists and returns True if they have at least one common member.

a=[1,2,3,4,5,6,7]
b=[9,8,5]
d="n"
for i in a:
    for j in b:
        if(i==j):
            print("Common value found")
            d="y"
            break
    if(d=="y"):
        break
    print(i)

