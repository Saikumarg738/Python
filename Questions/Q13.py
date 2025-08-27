#Write a Python program to generate a 3*4*6 3D array whose each element is *.
ls2=[]
for i in range(3):
    ls1 = []
    for j in range(4):
        ls = []
        for k in range(6):
            ls.append("*")
        ls1.append(ls)
    print(ls1)
    ls2.append(ls1)


