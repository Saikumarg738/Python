#Program for accepting Numerical Values and display separate List of +Ve and -Ve
n=int(input("Enter number of value you want to enter : "))
i=0
ls=[]
while(i<n):
    a=int(input("Enter {} value".format(i)))
    ls.append(a)
    i+=1
ps=[]
ng=[]
for ch in ls:
    if(ch<0):
        ng.append(ch)
    else:
        ps.append(ch)

print("Positive list is \n {}".format(ps))
print("Negative list is \n {}".format(ng))
