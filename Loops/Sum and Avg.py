#Take dynamic numbers and find sum avg

n=int(input("Enter number of values : "))
sum=0
i=1
ls=[]
for i in range(i,n+1):
    a=int(input("Enter numbers : "))
    ls.append(a)
else:
    for s in ls:
        sum+=s
    else:
        avg=sum/len(ls)
print("Sum is {}".format(sum))
print("Sum is {}".format(avg))