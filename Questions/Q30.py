#Write a Python program to get the frequency of the elements in a list.

ls=[1,2,3,4,5,6,7,6,5,4,3,2,1]

'''uls=list(set(ls))

for i in uls:
    print(i,ls.count(i))'''

'''uls=[]
for i in ls:
    if i not in uls:
        print(i,ls.count(i))
        uls.append(i)'''

dc={}

for i in ls:
    dc[i]=dc.get(i,0)+1

for k,v in dc.items():
    print(k,v)

