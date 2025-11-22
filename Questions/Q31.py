#Write a Python program to count the number of elements in a list within a specified range

''''def cou(num,s,e):
    count=0
    for i in num:
        if(s<i<e):
            count+=1
    print(count)

cou([1,2,3,4,5,6,7,8,9],2,8)'''

'''ls=[1,2,3,4,5,6,7,8,9]
s=2
e=9

count=len([i for i in ls if s<i<e])
print(count)'''

ls=[1,2,3,4,5,6,7,8,9]
s=2
e=9
count=sum(s<i<e for i in ls)
print(count)